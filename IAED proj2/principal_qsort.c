/*
 * Ficheiro: principal.c
 * Ficheiros complementares: gestao_jogos.h  gestao_jogos.c  hashtable.h  hashtable.c  item.h  item.c  
 * Linguagem do programa: C
 * Autor:  Zenan Chen 
 * N aluno: 95688
 * Descricao: Um programa que funciona como um sistema de gestao de uma base de dados de jogos de futebol amigaveis.
              O utilizador introduz os dados relativos a um jogo, a qual esta' associado um nome para o jogo, 
              dois nomes correspondentes as duas equipas e a pontuacao obtida por cada uma destas no jogo.
              Para um jogo ser valido, e' necessario adicionar previamente o nome das equipas ao sistema.
              Os comandos existentes e os standard input respetivos sao seguintes:

            |  a  Adiciona um novo jogo: 'a nome:equipa1:equipa2:score1:score2'               |
            |  A  Adiciona uma nova equipa: 'A nome'                                          |
            |  l  Lista todos os jogos pela ordem em que foram introduzidos: 'l'              |
            |  p  Procura um jogo dado um nome: 'p nome'                                      |
            |  P  Procura uma equipa dado um nome: 'P nome'                                   |
            |  r  Apaga um jogo dado um nome: 'r nome'                                        |
            |  s  Altera a pontuacao (score) de um jogo dado um nome: 's nome:score1:score2'  |
            |  g  Encontra as equipas que venceram mais jogos: 'g'                            |
            |  x  Termina o programa: 'x'                                                     |
*/

#include "hashtable.h"
#include "item.h"
#include "gestao_jogos_qsort.h"


int main(){
    int comando, contador = 0, n_equipas = 0;
    /* reserva espaco na memoria para a lista de jogos */
    lista_jogo * lst_jogo = (lista_jogo*) malloc(sizeof(lista_jogo));
    /* inicializa a cabeca para a lista de equipas e reserva memoria para a hashtable de jogos e para a hashtable de equipas */
    Item * head_equipa = NULL, * head_anterior, * hashtable_jogo[TAMANHO_TAB], * hashtable_equipa[TAMANHO_TAB];

    /* inicializa as posicoes das hashtables com valor NULL */
    init_hashtable(hashtable_jogo);
    init_hashtable(hashtable_equipa);

    lst_jogo->head = NULL;
    lst_jogo->last = NULL;

    /* deteta o comando inserido pelo utilizador, termina o programa caso input seja o caracter 'x' */
    while((comando = getchar()) != 'x'){
        if (comando != '\n'){
            contador++; /* conta o numero de linhas do input*/

            switch(comando){
                case 'a':
                    a_adicionaNovoJogo(lst_jogo, hashtable_jogo, hashtable_equipa, contador);
                    break;
                
                case 'A':
                    head_anterior = head_equipa;
                    head_equipa = A_adicionaNovaEquipa(head_equipa, hashtable_equipa, contador);
                    if (head_anterior != head_equipa){
                        n_equipas++;
                    }
                    break;

                case 'l':
                    l_listaTodosJogosPorOrdem(lst_jogo, contador);
                    break;
                
                case 'p':
                    p_procuraJogo(hashtable_jogo, contador);
                    break;

                case 'P':
                    P_procuraEquipa(hashtable_equipa, contador);
                    break;

                case 'r':
                    r_apagaJogo(lst_jogo, hashtable_jogo, hashtable_equipa, contador);
                    break;
                
                case 's':
                    s_alteraPontuacao(hashtable_jogo, hashtable_equipa, contador);
                    break;

                case 'g':
                    head_equipa = g_encontraEquipasMaisVitorias(head_equipa, contador, n_equipas);
                    break;
                
                default:
                    printf("Input invalido\n");
                    break;
            }
        }
    }    

    /* liberta na memoria os dados associados aos jogos e 'as equipas*/
    apaga_equipas(head_equipa);
    apaga_jogos(lst_jogo);
    
    return 0;
}

