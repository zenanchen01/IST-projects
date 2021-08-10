%===============================================================================
% Programa: projectoLP1920.pl
%
% Descricao: Solucionador de Palavras Cruzadas
%
% Autor: Zenan Chen - 95688
%
% Data realizacao: 17/03/2020 - 05/03/2020
%===============================================================================

:- use_module(library(clpfd)).
%===============================================================================
% mat_transposta(Matriz, Transp) significa que Transp e a transposta de Matriz
%===============================================================================

mat_transposta(Matriz, Transp) :-
    transpose(Matriz, Transp).

%===============================================================================
% escreve_Grelha(Grelha)
%===============================================================================

escreve_Grelha(Grelha) :-
    maplist(escreve_Linha, Grelha).

escreve_Linha([]) :- nl, !.

escreve_Linha([P | R]) :-
    (var(P) -> write('- ')
            ;
     write(P), write(' ')),
     escreve_Linha(R).

%===============================================================================
% obtem_letras_palavras/2
% obtem_letras_palavras(Lst_Pals, Letras): Lst_Pals e' uma lista de palavras, 
% significa que Letras e' a lista ordenada cujos elementos sao listas com as 
% letras de cada palavra de Lst_Pals 
%===============================================================================

obtem_letras_palavras(Lst_Pals, Letras):-
    maplist(atom_chars,Lst_Pals,Letras_desord),
    sort(Letras_desord,Letras).

%===============================================================================
% espaco_fila/2
% espaco_fila(Fila, Esp): Fila e' uma fila (linha ou coluna) de uma grelha,
% significa que Esp e' um espaco de Fila, sendo espaco uma lista com pelo menos 
% 3 posicoes que podem ser substituidas por letras

% espaco_fila_aux/3
% espaco_fila_aux(Fila, Acum, Esp): percorre a lista Fila e vai acumulando em
% Acum as posicoes validas para um espaco. Esp e' um espaco de Fila
%===============================================================================

espaco_fila(Fila,Esp) :-
    espaco_fila_aux(Fila,[],Esp).

espaco_fila_aux([], Esp, Esp) :-
    length(Esp,Comp),
    Comp >= 3.

espaco_fila_aux([H|_], Esp, Esp) :-
    H == '#',
    length(Esp,Comp),
    Comp >= 3. 

espaco_fila_aux([H|T],_,Esp) :-
    H == '#',
    espaco_fila_aux(T,[],Esp).

espaco_fila_aux([H|T], Acum ,Esp):-
    H \== '#',
    append(Acum,[H],L), 
    espaco_fila_aux(T, L, Esp).

%===============================================================================
% espacos_fila/2
% espacos_fila(Fila, Espacos): Fila e' uma fila (linha ou coluna) de uma grelha, 
% significa que Espacos e' a lista de todos os espacos de Fila, da esquerda para 
% a direita
%===============================================================================

espacos_fila(Fila,Espacos):-
    bagof(Espaco,espaco_fila(Fila,Espaco),Espacos).

%===============================================================================
% espacos_puzzle/2
% espacos_puzzle(Grelha, Espacos): Grelha e' uma grelha, significa que Espacos e'
% a lista de todos os espacos de Grelha, na horizontal e na vertical

% espacos_puzzle_aux/3
% espacos_puzzle_aux(Grelha, Acum, Espacos): percorre todas as filas de Grelha e
% de Grelha transposta e obtem todos os espacos, acumulando em Acum. Espacos e'
% a lista com todos os espacos possiveis de Grelha
%===============================================================================

espacos_puzzle(Grelha, Esp):-
    mat_transposta(Grelha,Grelha_Trans),
    append(Grelha,Grelha_Trans,Tudo),
    espacos_puzzle_aux(Tudo,[],Esp).

espacos_puzzle_aux([],Espacos,Espacos).

espacos_puzzle_aux([H|T],Acum,Espacos):-
    \+ espacos_fila(H,_),
    espacos_puzzle_aux(T,Acum,Espacos).

espacos_puzzle_aux([H|T],Acum,Espacos):-
    espacos_fila(H,Lst_espacos),
    append(Acum,Lst_espacos,Tudo),
    espacos_puzzle_aux(T,Tudo,Espacos).

%===============================================================================
% espacos_com_posicoes_comuns/3
% espacos_com_posicoes_comuns(Espacos, Esp, Esps_com): Espacos e' uma lista de 
% espacos e Esp e' um espaco, significa que Esps_com e' a lista de espacos com 
% variaveis em comum com Esp, exceptuando Esp

% espacos_com_posicoes_comuns_aux/4
% espacos_com_posicoes_comuns_aux(L,Esp,El,Res): Res e' a lista que contem dos 
% os espacos da lista L com o elemento El, exceptuando o espaco Esp

% espacos_comuns/2
% espacos_comuns(El,Lista): verifica se a lista Lista contem o elemeno El
%===============================================================================

espacos_com_posicoes_comuns(Espacos,Esp,Esps_com):-
    maplist(espacos_com_posicoes_comuns_aux(Espacos,Esp),Esp,L),
    exclude(==([]),L,Esps_com).

espacos_com_posicoes_comuns_aux(L,Esp,El,Res):-
    include(espacos_comuns(El),L,Espacos), 
	exclude(==(Esp),Espacos,R),
    flatten(R,Res).

espacos_comuns(El,Lista):- % verifica se elemento X esta na lista Y
    include(==(El),Lista,Iguais),
    length(Iguais,Comp),
    Comp \== 0.

%===============================================================================
% palavra_possivel_esp/4
% palavra_possivel_esp(Pal, Esp, Espacos, Letras): e Pal e' uma lista de letras 
% de uma palavra, Esp e' um espaco, Espacos e' uma lista de espacos, e Letras e'
% uma lista de listas de letras de palavras, significa que Pal e' uma palavra 
% possivel para o espaco Esp 

% palavra_possivel_esp_aux/2
% palavra_possivel_esp_aux(Letras,Esp): verifica se existe uma lista de letras 
% que pode substituir o espaco Esp

% palavra_possivel/2
% palavra_possivel(Esp, Pal): verifica se e' possivel substituir o espaco Esp 
% pela lista de letras Pal

% substitui/3
% substitui(Pal,Esp,Espacos): substitui o espaco Esp da lista de espacos Espacos
% pela lista de letras de uma palavra Pal
%===============================================================================

palavra_possivel_esp(Pal, Esp, Espacos, Letras):-
    palavra_possivel(Esp, Pal),
    espacos_com_posicoes_comuns(Espacos,Esp,Esps_com),
    substitui(Pal,Esp,Espacos),
    maplist(palavra_possivel_esp_aux(Letras),Esps_com).

palavra_possivel_esp_aux(Letras,Esp):-
    include(palavra_possivel(Esp),Letras,Res),
    length(Res,C),
    C \== 0.

palavra_possivel(Esp, Pal):-
    length(Pal,C1),
    length(Esp,C2),
    C1 == C2,
	subsumes_term(Esp,Pal).

substitui(Pal,Esp,[H|T]):-
    H \== Esp,
    substitui(Pal,Esp,T).

substitui(Pal,Esp,[H|_]):-
    H == Esp,
    H = Pal.

%===============================================================================
% palavras_possiveis_esp/4
% palavras_possiveis_esp(Letras, Espacos, Esp, Pals_Possiveis): Letras e' uma
% lista de listas de letras de palavras, Espacos e' uma lista de espacos, Esp 
% e' um espaco, significa que Pals_Possiveis e' a lista ordenada de palavras 
% possiveis para o espaco Esp

% palavras_possiveis_esp_aux/4
% palavras_possiveis_esp_aux(Esp, Espacos, Letras, Pal): verifica que a lista de 
% letras Pal nao e' possivel para o Espaco esp
%===============================================================================

palavras_possiveis_esp(Letras, Espacos, Esp, Pals_Possiveis):-
    exclude(palavras_possiveis_esp_aux(Esp,Espacos,Letras),Letras,Pals_Possiveis).
    
palavras_possiveis_esp_aux(Esp, Espacos, Letras, Pal):-
    \+ palavra_possivel_esp(Pal, Esp, Espacos, Letras).    

%===============================================================================
% palavras_possiveis/3
% palavras_possiveis(Letras, Espacos, Pals_Possiveis): Letras e' uma lista de 
% listas de letras de palavras e Espacos e' uma lista de espacos, significa que
% Pals_Possiveis e' a lista de palavras possiveis

% palavras_possiveis_aux/4
% palavras_possiveis_aux(Letras, Espacos, Esp, Pals_Possiveis): Pals_Possiveis e'
% uma lista de dois elementos, sendo o primeiro o espaco Esp da lista de espacos 
% Espacos e o segundo uma lista de palavras possiveis para o espaco Esp, da lista
% de palavras Letras
%===============================================================================

palavras_possiveis(Letras, Espacos, Pals_Possiveis):-
    maplist(palavras_possiveis_aux(Letras, Espacos),Espacos,Pals_Possiveis).

palavras_possiveis_aux(Letras, Espacos, Esp, Pals_Possiveis):-
    palavras_possiveis_esp(Letras, Espacos, Esp, Palavras),
    append([Esp],[Palavras],Pals_Possiveis).

%===============================================================================
% letras_comuns/2
% letras_comuns(Lst_Pals, Letras_comuns): Lst_Pals e' uma lista de listas de 
% letras, significa que Letras_comuns e' uma lista de pares (pos, letra),
% significando que todas as listas de Lst_Pals conteem a letra letra na posicao pos.
% Fazendo a matriz transposta de Lst_Pals, se uma lista tiver todos os elementos 
% iguais significa que o elemento dessa lista e' uma letra comum

% todos_iguais/1
% todos_iguais(Lista): verifica se a lista Lista tem todos os elementos iguais

% adiciona_numero/2
% adiciona_numero(Lista, Lista_res): modifica o primeiro elemento da lista Lista 
% de acordo com o processo descrito no predicado adiciona_numero_aux/4 e devolve
% a lista Lista_res igual a Lista exeptuando o primeiro elemento modificado

% adiciona_numero_aux/4
% adiciona_numero_aux(Lista,N,Acum,Lista_res): percorre os elementos da lista
% Lista e associa a cada um a sua posicao, acumulando na lista Acum; Lista_res 
% e' a lista resultante da acumulacao
%===============================================================================
    
letras_comuns(Lst_Pals, Letras_comuns):-
    adiciona_numero(Lst_Pals,Pals_mod),
    mat_transposta(Pals_mod,Letras),
    include(todos_iguais,Letras,Letras_iguais),
    maplist(nth1(1),Letras_iguais,Letras_comuns).
    
todos_iguais([(_,H)|T]):-
    include(==(H),[H|T],Iguais),
    Iguais == [H|T].
    
adiciona_numero([H|T],[L|T]):-
    adiciona_numero_aux(H,1,[],L).
 
adiciona_numero_aux([],_,Y,L):-
    flatten(Y,L).

adiciona_numero_aux([H|T],N,Acum,L):-
    append([Acum],[(N,H)],Y),
    N1 is N + 1,
    adiciona_numero_aux(T,N1,Y,L).
    
%===============================================================================
% atribui_comuns/1
% atribui_comuns(Pals_Possiveis): Pals_Possiveis e' uma lista de palavras possiveis,
% actualiza esta lista atribuindo a cada espaco as letras comuns a todas as palavras
% possiveis para esse espaco

% atribui_comuns_aux/1
% atribui_comuns_aux(Pal_Possivel): a lista Pal_Possivel e' uma palavra possivel
% e e' atualizada atribuindo seu espaco as letras comuns a todas as palavras 
% possiveis para esse espaco

% substitui_letra/2
% substitui_letra(Esp,(Pos,Letra)): Atribui ah posicao Pos do espaco Esp a letra Letra 
%===============================================================================

atribui_comuns(Pals_Possiveis):-
    maplist(atribui_comuns_aux,Pals_Possiveis).
    
atribui_comuns_aux([H|T]):-
    length(T,Comp),
    Comp == 1, 
    flatten(T,Pal),
    H = Pal.

atribui_comuns_aux([H|T]):-
    nth1(1,T,Pals),
    length(Pals,Comp),
    Comp \== 1, 
    letras_comuns(Pals, Letras_comuns),
    maplist(substitui_letra(H),Letras_comuns).

substitui_letra(Esp,(Pos,Letra)):-
    nth1(Pos,Esp,X),
    X = Letra.

%===============================================================================
% retira_impossiveis/2
% retira_impossiveis(Pals_Possiveis, Novas_Pals_Possiveis): Pals_Possiveis e' uma
% lista de palavras possiveis, significa que Novas_Pals_Possiveis e' o resultado 
% de tirar todas as palavras impossiveis de Pals_Possiveis

% retira_impossiveis_aux/2
% retira_impossiveis_aux(Palavra,Nova_Pal): Nova_Pal e' a lista resultante de 
% retirar todas as palavras impossiveis da lista Palavra
%===============================================================================

retira_impossiveis(Pals_Possiveis, Novas_Pals_Possiveis):-
	maplist(retira_impossiveis_aux,Pals_Possiveis,Novas_Pals_Possiveis).

retira_impossiveis_aux([Esp,Pals],[Esp|[Pals_poss]]):-
    include(subsumes_term(Esp),Pals,Pals_poss).
    
%===============================================================================
% obtem_unicas/2 
% obtem_unicas(Pals_Possiveis, Unicas): Pals_Possiveis e' uma lista de palavras 
% possiveis, significa que Unicas e' a lista de palavras unicas de Pals_Possiveis

% pal_unica/1
% pal_unica(Pal_Possivel): verifica se a lista Pal_Possivel tem apenas uma palavra
% possivel para o respetivo espaco

% obtem_palavra/2
% obtem_palavra(Pal_Possivel,Pal): Pal e' unica palavra possivel da lista 
% Pal_Possivel para o respetivo espaco
%===============================================================================

obtem_unicas(Pals_Possiveis, Unicas):-
    include(pal_unica,Pals_Possiveis,Pals),
    maplist(obtem_palavra,Pals,Unicas).
    
pal_unica([_,Pals]):-
    length(Pals,C),
    C == 1.

obtem_palavra([_,[Pal]],Pal).
    
%===============================================================================
% retira_unicas/2
% retira_unicas(Pals_Possiveis, Novas_Pals_Possiveis): encontra as palavras unicas
% da lista de palavras possiveis Pals_Possiveis e aplica a cada elemento desta o
% predicado retira_pal/3

% retira_pal/3
% retira_pal(Unicas,Pals_Possiveis, Novas_Pals_Possiveis): Pals_Possiveis e' uma 
% lista de palavras possiveis, significa que Novas_Pals_Possiveis e' o resultado 
% de retirar de Pals_Possiveis as palavras da lista Unica

% membro/2
% membro(L,El): verifica o elemento El e' membro da lista L
%===============================================================================

retira_unicas(Pals_Possiveis, Novas_Pals_Possiveis):-
    obtem_unicas(Pals_Possiveis,Unicas),
    maplist(retira_pal(Unicas),Pals_Possiveis,Novas_Pals_Possiveis).

retira_pal(_,[Esp,Pals],[Esp,Pals]):-
    length(Pals,C),
    C == 1.
    
retira_pal(Unicas,[Esp,Pals],[Esp|[Res]]):-
    length(Pals,C),
    C \== 1,
    exclude(membro(Unicas),Pals,Res).
    
membro(L,El):-
    member(El,L).

%===============================================================================
% simplifica/2
% simplifica(Pals_Possiveis, Novas_Pals_Possiveis): Pals_Possiveis e' uma lista 
% de palavras possiveis, significa que Novas_Pals_Possiveis e' o resultado de 
% simplificar Pals_Possiveis, aplicado-lhe os predicados atribui_comuns, 
% retira_impossiveis e retira_unicas ate' nao haver mais alteracoes
%===============================================================================

simplifica(Pals_Possiveis, Novas_Pals_Possiveis):-
    atribui_comuns(Pals_Possiveis),
    retira_impossiveis(Pals_Possiveis, X),
    retira_unicas(X, Novas_Pals_Possiveis), 
    Pals_Possiveis == Novas_Pals_Possiveis.
    
simplifica(Pals_Possiveis, Novas_Pals_Possiveis):-
    atribui_comuns(Pals_Possiveis),
    retira_impossiveis(Pals_Possiveis, X),
    retira_unicas(X, Novas_Pals),
    Pals_Possiveis \== Novas_Pals,
    simplifica(Novas_Pals,Novas_Pals_Possiveis).

%===============================================================================
% inicializa/2
% inicializa(Puz, Pals_Possiveis): e Puz e' um puzzle, significa que Pals_Possiveis
% e' a lista de palavras possiveis simplificada para Puz
%===============================================================================

inicializa(Puz, Pals_Possiveis):-
    nth1(1,Puz,Lst_Pals),
    nth1(2,Puz,Grelha),
    obtem_letras_palavras(Lst_Pals, Letras),
    espacos_puzzle(Grelha, Espacos),
    palavras_possiveis(Letras, Espacos, Pals),
    simplifica(Pals, Pals_Possiveis).

%===============================================================================
% escolhe_menos_alternativas/2
% escolhe_menos_alternativas(Pals_Possiveis, Escolha): Pals_Possiveis e' uma lista
% de palavras possiveis, significa que Escolha e' o elemento de Pals_Possiveis com
% o menor numero de palavras possiveis, a partir de 2. Devolve falso se todos os
% espacos em Pals_Possiveis tiverem associadas listas de palavras unitarias

% menos_alternativas/4
% menos_alternativas(Pals_Possiveis, Comp, Maior_comp, Escolha): Escolha e' o 
% elemento da lista de palavras possiveis Pals_Possiveis com o menor numero de
% palavaras possiveis, a partir de 2. Comp e' o numero de palavras possiveis e 
% Maior_comp e' numero de palavras que o espaco com mais palavras de Pals_Possiveis 
% tem. Este predicado repete-se ate encontrar a Escolha ou ate o numero de repeticoes 
% atingir Maior_comp vezes

% comprimento/2
% comprimento(Comp,Pals_Possiveis): Comp e' o numero de palavras possiveis que 
% existe na lista de palavras possiveis Pals_Possiveis
%===============================================================================

escolhe_menos_alternativas(Pals_Possiveis, Escolha):-
    length(Pals_Possiveis,Maior_comp),
    menos_alternativas(Pals_Possiveis,2,Maior_comp,Escolha).

menos_alternativas(Pals_Possiveis,Comp,Maior_comp,Escolha):-
    Maior_comp >= Comp,
    include(comprimento(Comp),Pals_Possiveis,Escolhidos),
    Escolhidos == [],
    Novo_comp is Comp + 1,
    menos_alternativas(Pals_Possiveis,Novo_comp,Maior_comp,Escolha).
    
menos_alternativas(Pals_Possiveis,Comp,_,Escolha):-
    include(comprimento(Comp),Pals_Possiveis,Escolhidos),
    Escolhidos \== [],
    nth1(1,Escolhidos,Escolha).

comprimento(Comp,Pals_Possiveis):-
    nth1(2,Pals_Possiveis,Pals),
    length(Pals,Comp).
    
%===============================================================================
% experimenta_pal/3
% experimenta_pal(Escolha, Pals_Possiveis, Novas_Pals_Possiveis): Novas_Pals_Possiveis
% e' o resultante de substituir uma palavra da lista de palaras Escolha pelo respetivo
% espaco na lista de palavras possiveis Pals_Possiveis 

% muda/4
% muda(El_ant,El_novo,Lista,Nova_Lista): Nova_Lista e' a lista resultante de 
% substituir o elemento El_ant pelo elemento El_novo na lista Lista
%===============================================================================
    
experimenta_pal(Escolha, Pals_Possiveis, Novas_Pals_Possiveis):-
    nth1(1,Escolha,Esp),
    nth1(2,Escolha,Lst_Pals),
    member(Pal,Lst_Pals),
    Esp = Pal,
    retira_impossiveis_aux(Escolha,Novo),
    muda(Escolha,Novo,Pals_Possiveis,Novas_Pals_Possiveis).

muda(El_ant,El_novo,[H|L],[El_novo|L]):-
    H == El_ant.

muda(El_ant,El_novo,[H|L1],[H|L2]):-
    H \== El_ant,
    muda(El_ant,El_novo,L1,L2).

%===============================================================================
% resolve_aux/2
% resolve_aux(Pals_Possiveis, Novas_Pals_Possiveis): Pals_Possiveis e' uma lista 
% de palavras possiveis, significa que Novas_Pals_Possiveis e' o resultado de 
% aplicar os predicados escolhe_menos_alternativas, experimenta_pal e simplifica
% ate resolver o puzzle
%===============================================================================

resolve_aux(Pals_Possiveis, Novas_Pals_Possiveis):-
    escolhe_menos_alternativas(Pals_Possiveis, Escolha),
    experimenta_pal(Escolha, Pals_Possiveis, X),
    simplifica(X,Y),
    Pals_Possiveis \== Y,
    resolve_aux(Y, Novas_Pals_Possiveis).

resolve_aux(Pals_Possiveis, Pals_Possiveis):-
    \+ escolhe_menos_alternativas(Pals_Possiveis, _).
       
%===============================================================================
% resolve/1
% resolve(Puz): resolve o puzzle Puz, , isto e', apos a invocacao deste predicado
% a grelha de Puz tem todas as variaveis substituidas por letras que constituem 
% as palavras da lista de palavras de Puz
%===============================================================================

resolve(Puz):-
    inicializa(Puz,Pals_Possiveis),
    resolve_aux(Pals_Possiveis,_).