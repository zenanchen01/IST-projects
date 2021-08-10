#Nome: Zenan Chen
#Numero: 95688

#####################
# 2.1.1 TAD posicao #
#####################


### Funcoes auxiliares ###

def numero(n):
    #a funcao numero ve se o valor eh um inteiro positivo   
    return isinstance(n, int) and n >= 0 


### construtores ###

def cria_posicao(x,y):
    '''
    A funcao cria_posicao recebe os valores correspondentes as coordenadas de uma posicao\
    e devolve a posicao correspondente. O construtor verifica a validade dos seus argumentos, \
    gerando um ValueError com a mensagem 'cria_posicao: argumentos invalidos' \
    caso os seus argumentos nao sejam validos
     
    cria_posciao: N x N -> posicao
    ''' 
    if numero(x) and numero(y):
        return (x,y)
    else: 
        raise ValueError('cria_posicao: argumentos invalidos')
    

def cria_copia_posicao(p):
    '''
    A funcao cria_copia_posicao recebe uma posicao e devolve uma copia nova da posicao
    
    cria_copia_posicao: posicao -> posicao
    '''
    return (p[0], p[1])
   

### seletores ###

def obter_pos_x(p):
    '''
    A funcao obter_pos_x devolve a componente x da posicao p
    
    obter_pos_x: posicao -> N 
    '''
    return p[0]


def obter_pos_y(p):
    '''
    A funcao obter_pos_y devolve a componente y da posicao p
    
    obter_pos_y: posicao -> N 
    '''    
    return p[1]


### reconhecedor ###

def eh_posicao(arg):
    '''
    A funcao eh_posicao devolve True caso o seu argumento seja um TAD posicao e False caso contrario
    
    eh_posicao universal -> booleano 
    '''
    return isinstance(arg,tuple) and len(arg) == 2 and numero(arg[0]) and numero(arg[1])
    # ve se argumento eh um tuplo contendo 2 numeros inteiros positivos

### teste ###
    
def posicoes_iguais(p1, p2):
    '''
    A posicoes_iguais devolve True apenas se p1 e p2 sao posicoes iguais
    
    posicoes_iguais: posicao x posicao 7 -> booleano 
    '''
    return p1 == p2


### transformador ###

def posicao_para_str(p):
    '''
    A funcao posicao_para_srt devolve a cadeia de caracteres '(x, y)' que representa o seu argumento,\
    sendo os valores x e y as coordenadas de p
    posicao_para_srt: posicao -> str 
    '''
    return str(p)


### funcoes de alto nivel ###  

def obter_posicoes_adjacentes(p):
    '''
    A funcao obter_poscioes_adjacentes devolve um tuplo com as posicoes \
    adjacentes a posicao p de acordo com a ordem de leitura de um labirinto
    
    obter_posicoes adjacentes: posicao -> tuplo de posicoes
    '''
    if not eh_posicao(p):
        raise ValueError('posicoes_adjacentes: argumento invalido') # ver se a posicao eh valida
    else:
        p_adj = ((obter_pos_x(p), obter_pos_y(p) - 1),\
                (obter_pos_x(p) - 1, obter_pos_y(p)), (obter_pos_x(p) + 1,obter_pos_y(p)),\
                (obter_pos_x(p),obter_pos_y(p)+1)) # obter todas as posicoes adjacentes
        p_validas = () 
        for e in p_adj:
            if eh_posicao(e):
                p_validas = p_validas + (e,) # obter apenas as posicoes sao validas
        return p_validas


#####################
# 2.1.2 TAD unidade #
#####################

### Funcoes auxiliares ###

def natural(n):
    #a funcao natural ve se o valor eh um numero natural
    return isinstance(n, int) and n > 0


### construtores ###

def cria_unidade(p, v, f, exercito):
    '''
    A funcao cria_unidade recebe uma posicao p, dois valores inteiros maiores que 0 \
    correspondentes a vida e forca da unidade, e uma cadeia de caracteres nao vazia \
    correspondente ao exercito da unidade; e devolve a unidade correspondente. \
    O construtor verfica a validade dos seus argumentos, gerando um ValueError com a mensagem \
    'cria unidade: argumentos invalidos' caso os seus argumentos nao sejam validos
    
    cria_unidade: posicao x N x N x str -> unidade
    '''
    if not eh_posicao(p) or not natural(v) or not natural(f) or not isinstance(exercito,str) or exercito == '':
        raise ValueError('cria_unidade: argumentos invalidos')
    else:
        return {'posicao':p, 'vida':v, 'forca':f, 'exercito':exercito} 

    
def cria_copia_unidade(u):
    '''
    A funcao cria_copia_unidade recebe uma unidade u e devolve uma nova copia da unidade
    
    cria_copia_unidade: unidade -> unidade
    '''
    copia = {}
    for i in u:
        copia[i] = u[i]
    return copia


### seletores ###

def obter_posicao(u):
    '''
    A funcao obter_posicao devolve a posicao da unidade u
    
    obter_posicao: unidade -> posicao
    '''
    return u['posicao']


def obter_exercito(u):
    '''
    A funcao obter_posicao devolve a cadeia de carateres correspondente ao exercito da unidade
    
    obter_exercito: unidade -> str
    '''    
    return u['exercito']


def obter_vida(u):
    '''
    A funcao obter_posicao devolve o valor corresponde aos pontos de vida da unidade
    
    obter_exercito: unidade -> N
    '''    
    return u['vida']


def obter_forca(u):
    '''
    A funcao obter_posicao  devolve o valor corresponde a forca de ataque da unidade
    
    obter_exercito: unidade -> N
    '''       
    return u['forca']


### modificadores ###

def muda_posicao(u, p):
    '''
    A funcao muda_posicao modifica destrutivamente a unidade u \
    alterando a sua posicao com o novo valor p, e devolve a propria unidade
    
    muda_posicao: unidade x N -> unidade
    ''' 
    u['posicao'] = p
    return u


def remove_vida(u, v):
    ''' 
    A funcao remove_vida modifica destrutivamente a unidade u\
    alterando os seus pontos de vida subtraindo o valor v, e devolve a propria unidade
    
    remove_vida: unidade x N -> unidade
    '''
    u['vida'] = u['vida'] - v 
    return u


### reconhecedor ###

def eh_unidade(arg):
    '''
    A funcao eh_unidade devolve True caso o seu argumento seja um TAD unidade e False caso contrario
    
    eh_unidade: universal -> booleano
    '''
    # verifica se eh um dicionario com 4 elementos validos associados a TAD unidade
    if isinstance(arg, dict) and len(arg) == 4\
    and 'posicao' in arg and 'forca' in arg and 'vida' in arg and 'exercito' in arg:
        if eh_posicao(arg['posicao']) and numero(arg['vida'])\
        and numero(arg['forca']) and isinstance(arg['exercito'],str):
            return True
        else:
            return False
    else:
        return False


def unidades_iguais(u1, u2):
    '''
    A funcao unidades_iguais devolve True apenas se u1 e u2 sao unidades iguais
    
    unidades_iguais: unidade x unidade -> booleano 
    '''   
    return u1 == u2


### transformadores ###

def unidade_para_char(u):
    '''
    A funcao unidade_para_char devolve a cadeia de caracteres dum unico elemento,\
    correspondente ao primeiro caracter em maiuscula do exercito da unidade passada por argumento
    
    unidade_para_char: unidade -> str 
    '''
    #trasnformar todos os caracteres de cadeia em maiusculas
    nome_maiusculas = obter_exercito(u).upper() 
    
    return nome_maiusculas[0] #retornar o primeiro caracter

def unidade_para_str(u):
    '''
    A funcao unidade_para_str devolve a cadeia de caracteres que\
    representa a unidade como pedido pelo enunciado
    
    unidade_para_str: unidade -> srt
    '''
    nome_unidade = str(unidade_para_char(u))\
        + str([obter_vida(u),obter_forca(u)]) + '@' + str(obter_posicao(u))
    return nome_unidade


### funcoes de alto nivel ###

def unidade_ataca(u1, u2):
    '''
    A funcao unidade_ataca modifica destrutivamente a unidade u2 retirando\
    o valor de pontos de vida correspondente a forca de ataque da unidade u1.\
    A funcao devolve True se a unidade u2 for destruida ou False caso contrario
    
    unidade_ataca: unidade x unidade -> booleano 
    '''
    forca = obter_forca(u1)
    vida = obter_vida(u2)

    if vida - forca > 0:
        u2['vida'] = vida - forca
        return False
    else: 
        # se diferenca entre a vida e a forca for negaiva, a vida passa a zero 0
        u2['vida'] = 0
        return True


def ordenar_unidades(t):
    '''
    A funcao ordenar_unidade devolve um tuplo contendo as mesmas unidades do tuplo\
    fornecido como argumento, ordenadas de acordo com a ordem de leitura do labirinto
    
    ordenar_unidade: tuplo unidades -> tuplo unidades 
    '''
    posicoes = {}
    ordenado = ()
    
    # criar um dicionario do tipo {(x,y): unidade}, associando cada unidade a sua posicao
    for i in t:  
        posicoes[obter_posicao(i)] = i 
    
    #ordenar o dicionario com as posicoes de acordo com a ordem de leitura do mapa e retirar as unidades
    for i in sorted(posicoes, key = lambda k: [k[1], k[0]]): 
        ordenado = ordenado + (posicoes[i],)
    
    return ordenado

##################    
# 2.1.3 TAD mapa #
##################

### Funcoes auxiliares ###

def eh_posicao_valida(d, p):
    '''
    A funcao recebe um tuplo contendo as dimensoes de um mapa e uma posicao\
    e retorna verdadeiro caso a posicao esteja dentro das dimensoes
    '''
    return isinstance(p[0], int) and isinstance(p[1], int) and 0 < p[0] < d[0]-1 and 0 < p[1] < d[1] - 1


def eh_dimensao(arg):
    '''
    A funcao ve se o argumento eh um tuplo com valores validos para a dimensao\
    de um mapa (inteiro e maior que 2)  
    '''
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int)\
           and arg[0] > 2 and isinstance(arg[1], int) and arg[1] > 2
 
    
def eh_parede_valido(t, d):
    '''
    A funcao devolve True se t for um tuplo contendo 0 ou mais posicoes dentro do mapa
    '''   
    if isinstance(t, tuple):
        # se o tuplo nao conter elementos, devolve True
        if t == ():
            return True 
          
        # para cada elemento do tuplo, ver se eh uma posicao valida do mapa    
        for i in t:
            if isinstance(i, tuple) and eh_dimensao(d):
                if not eh_posicao_valida(d, i): 
                    return False
            else: 
                return False   
        return True
    else:
        return False
                
            
def eh_exercito_valido(e):
    '''
    A funcao ve se o argumento eh um tuplo contendo unidades validas de acordo\
    com a TAD unidade
    '''
    flag = True
    # ver se arggumento eh tuplo
    if isinstance(e, tuple) and len(e) > 0:
        # ver se os elementos do tuplo sao unidades
        for i in e:
            if not isinstance(i, dict) or not eh_unidade(i):
                flag = False
        return flag
    else:
        return False


def obter_todas_paredes(m):
    # a funcao devolve um tuplo contendo todas a posicoes das paredes do mapa m
    paredes = ()
    for i in m['paredes']:
        paredes = paredes + (i,)
    return paredes
 
    
def obter_todas_posicoes(m):
    # a funcao devolve um tuplo contendo todas a posicoes do mapa m
    posicoes = ()
    for i in obter_todas_unidades(m):
        posicoes = posicoes + (i['posicao'],)
    return posicoes


### Construtor ### 

def  cria_mapa(d, w, e1, e2):
    '''
    A funcao cria_mapa recebe um tuplo d de 2 valores inteiros correspondentes\
    as dimensoes Nx e Ny do labirinto seguindo as restricoes do primeiro projecto,\
    um tuplo w de 0 ou mais posicoes correspondentes as paredes que nao sao dos\
    limites exteriores do labirinto, um tuplo e1 de 1 ou mais unidades do mesmo\
    exercito, e um tuplo e2 de um ou mais unidades de um outro exercito;\
    e devolve o mapa que representa internamente o labirinto e as unidades presentes.\
    O construtor verifica a validade dos seus argumentos, gerando um ValueError com 
    a mensagem 'cria mapa: argumentos invalidos' caso os seus argumentos nao sejam validos
    
    cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa
    '''
    if not eh_dimensao(d) or not eh_parede_valido(w, d) or\
       not eh_exercito_valido(e1) or not eh_exercito_valido(e2):
        return ValueError('cria_mapa: argumentos invalidos')
    else:
        return {'dimensao':d, 'paredes':w, 'e1':list(e1), 'e2':list(e2)}


def cria_copia_mapa(m):
    '''
    A funcao cria_copia_mapa recebe um mapa e devolve uma nova copia do mapa
    
    cria_copia_mapa: mapa -> mapa
    '''
    copia = {}
    e1 = []
    e2 = []
    # copiar a dimensao e as paredes
    copia['dimensao'] = m['dimensao']
    copia['paredes'] = m['paredes']
    
    # percorrer os dois exercitos e copiar cada unidade individualmente
    for i in m['e1']:
        e1 = e1 + [cria_copia_unidade(i)]
    for i in m['e2']:
        e2 = e2 + [cria_copia_unidade(i)] 
    copia['e1'] = e1
    copia['e2'] = e2
    
    return copia

        
### seletores ###
    
def obter_tamanho(m):
    '''
    A funcao obter_tamanho devolve um tuplo de dois valores inteiros correspondendo\
    o primeiro deles a dimensao Nx e o segundo a dimensao Ny do mapa
    
    obter_tamanho: mapa -> tuplo
    '''
    return m['dimesao']


def obter_nome_exercitos(m):
    '''
    A funcao obter_nome_exercitos devolve um tuplo ordenado com duas cadeias de\
    caracteres correspondendo aos nomes dos exercitos do mapa
    
    obter_nome_exercitos: mapa -> tuplo
    '''
    return (obter_exercito(m['e1'][0]), obter_exercito(m['e2'][0]))

            
def obter_unidades_exercito(m, e):
    '''
    A funcao obter_unidade_exercito devolve um tuplo contendo as unidades\
    do mapa pertencentes ao exercito indicado pela cadeia de caracteres e,\
    ordenadas em ordem de leitura do labirinto
    
    obter_unidades_exercito: mapa x str -> tuplo de unidades 
    '''
    u = ()
    # para o caso de e ser o nome do exercito
    if e != 'e1' and e != 'e2':
        if e == obter_nome_exercitos(m)[0]:
            e = 'e1'
        else:
            e = 'e2'
    #obter as unidades do exercito correspondente
    for i in m[e]:
        u = u + (i,)
    #devolver o tuplo orndenado   
    return ordenar_unidades(u)


def obter_todas_unidades(m):
    '''
    A funcao obter_todas_unidades devolve um tuplo contendo todas as unidades do mapa,\
    ordenadas em ordem de leitura do labirinto
    
    obter_todas_unidades: mapa -> tuplo de unidades
    '''
    # por num tuplo todas as unidades dos 2 exercitos
    unidades = obter_unidades_exercito(m, 'e1') + obter_unidades_exercito(m, 'e2')
    # ordenar tuplo
    return ordenar_unidades(unidades)


def obter_unidade(m, p):
    '''
    A funcao_unidade devolve a unidade do mapa que se encontra na posicao p
    
    obter_unidade: mapa x posicao -> unidade
    '''
    # percorrer todas as unidades e devolver a unidade se a sua posicao for igual a p
    for u in obter_todas_unidades(m):
        if posicoes_iguais(p, obter_posicao(u)):
            return u


### modificadores ###
        
def eliminar_unidade(m, u):
    '''
    A funcao eliminar_unidade modifica destrutivamente o mapa m eliminando a unidade u\
    do mapa e deixando livre a posicao onde se encontrava a unidade. Devolve o proprio mapa
    
    eliminar_unidade: mapa x unidade -> mapa
    '''
    # ver a qual exercito pertence a unidade u
    if u in obter_unidades_exercito(m, 'e1'):
        e = 'e1'
    if u in obter_unidades_exercito(m, 'e2'):
        e = 'e2'    
    # eliminar a unidade do exercito    
    for i in range(len(m[e])):
        if unidades_iguais(m[e][i], u):
            del(m[e][i])
            break
        
    return m

    
def mover_unidade(m, u, p):
    '''
    A funcao mover_ unidade modifica destrutivamente o mapa m e a unidade u\
    alterando a posicao da unidade no mapa para a nova posicao p e deixando\
    livre a posicao onde se encontrava. Devolve o proprio mapa
    
    mover_unidade: mapa x unidade x posicao -> mapa
    '''
    for i in obter_todas_unidades(m):
        if unidades_iguais(i, u):
            muda_posicao(i, p)
    
    return m     


### reconhecedores ###

def eh_posicao_unidade(m, p):
    '''
    A funcao eh_posicao_unidade devolve True apenas no caso da\
    posicao p do mapa estar ocupada por uma unidade
    
    eh_posicao_unidade: mapa x posicao -> booleano
    '''
    return p in obter_todas_posicoes(m)     

        
def eh_posicao_corredor(m, p):
    '''
    A funcao eh_posicao_corredor devolve True apenas\
    no caso da posicao p do mapa corresponder a um corredor\
    no labirinto (independentemente de estar ou nao ocupado por uma unidade)
    
    eh_posicao_corredor: mapa x posicao -> booleano
    '''
    return eh_posicao_valida(m['dimensao'], p) and not eh_posicao_parede(m, p)


def eh_posicao_parede(m, p):
    '''
    A funcao eh_posicao_parede devolve True apenas no caso da posicao p\
    do mapa corresponder a uma parede do labirinto
    
    eh_posicao_parede: mapa x posicao -> booleano
    '''
    return p in obter_todas_paredes(m) or obter_pos_x(p) == 0 or obter_pos_y(p) == 0 \
           or obter_pos_x(p) == m['dimensao'][0]-1 or obter_pos_y(p) == m['dimensao'][1]-1


def mapas_iguais(m1, m2):
    '''
    A funcao mapas_iguais devolve True apenas se m1 e m2 forem mapas iguais
    
    mapas_iguais: mapa x mapa -> booleano
    '''
    return m1 == m2


### trasformador ###

def mapa_para_str(m):
    '''
    A funcao mapa_para_strdevolve uma cadeia de caracteres\
    que representa o mapa como descrito no primeiro projeto, neste caso,\
    com as unidades representadas pela sua representacao externa
    
    mapa_para_str: mapa -> str
    '''
    mapa = '' # comecar a defenir o mapa como uma string vazia
    l = []
    ''' criar uma lista contendo todas as posicoes do mapa m, incluindo as paredes externas\
    e separados por '\n' a cada linha'''    
    for y in range(m['dimensao'][1]):
        for x in range(m['dimensao'][0]):
            l = l + [(x,y)]
        if y != m['dimensao'][1] - 1:
            l = l + ['\n']
     
    # percorrer por todas as posicoes           
    for i in l:
        # se for uma posicao interna do mapa
        if eh_posicao_corredor(m, i):
        # se for uma unidade, adiciona-se a string primeiro caracter do nome do seu exercito
            if eh_posicao_unidade(m, i): 
                mapa = mapa + str(unidade_para_char(obter_unidade(m, i)))
            # se for parede, adiciona-se o simbolo correspondente
            elif eh_posicao_parede(m, i):
                mapa = mapa + '#'
            # se for uma posicao vazia, adiciona-se um simbolo correspondente
            else:
                mapa = mapa + '.'
        # se for o simbolo '\n', passa-se para a proxima linha
        elif i == '\n':
            mapa = mapa + '\n'
        # se nao eh uma parede externa
        else:
            mapa = mapa + '#'
            
    return mapa


### Funcoes de alto nivel ###

def obter_inimigos_adjacentes(m, u):
    '''
    A funcao obter_inimigos_adjacentes devolve um tuplo contendo as unidades\
    inimigas adjacentes a unidade u de acordo com a ordem de leitura do labirinto
    
    obter_inimigos_adjacentes: mapa x unidade -> tuplo de unidades
    '''
    inimigos = ()
    # obter todas as posicoes adjacentes dentro do mapa
    for i in obter_posicoes_adjacentes(obter_posicao(u)):
        # ver as posicoes correspondem a unidades
        if eh_posicao_unidade(m, i):
            # ver se eh uma unidade inimiga
            if obter_exercito(u) != obter_exercito(obter_unidade(m, i)):
                inimigos = inimigos + (obter_unidade(m, i),)
    
    return inimigos


def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1])

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)


# Funcoes adicionais #
def calcula_pontos(m, e):
    '''
    A funcao recebe um mapa e uma cadeia de caracteres correspondente\
    ao nome de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao \
    dum exercito e o total dos pontos de vida de todas as unidades do exercito
    
    calcula_pontos: mapa x exercito -> int
    '''
    pontos = 0
    # percorrer todas as unidades e somar as vidas
    for i in obter_unidades_exercito(m, e):
        pontos = pontos + i['vida']
        
    return pontos

    
def simula_turno(m):
    '''
    A funcao simula_turno modifica o mapa fornecido como argumento de acordo\
    com a simulacao de um turno de batalha completo, e devolve o proprio mapa.\
    Isto eh, seguindo a ordem de leitura do labirinto, cada unidade (viva) realiza\
    um unico movimento e (eventualmente) um ataque de acordo com as regras descritas
    
    simula_turno: mapa -> mapa
    '''
    # para todas as unidades do mapa seguindo a ordem de leitura
    for u in obter_todas_unidades(m):
        # ver se a unidade ainda esta no mapa (pode ter sido eliminada)
        if u in obter_todas_unidades(m):
            # obter a posicao de movimento pretendido
            nova_posicao = obter_movimento(m, u)
            # mover a unidade para a nova posicao
            mover_unidade(m, u, nova_posicao)
            # obter unidade apos ela ser movida
            u_movida = obter_unidade(m, nova_posicao)
            # ver se a unidade movida tem inimigos nas posicoes adjacentes
            if obter_inimigos_adjacentes(m, u_movida) != ():
                # ataca primeira unidade inimiga seguindo a ordem de leitura do labirinto
                unidade_inimiga = obter_inimigos_adjacentes(m, u_movida)[0]
                unidade_ataca(u_movida, unidade_inimiga)
                # eliminar a unidade atacada do mapa se a vida chegar a 0
                if obter_vida(unidade_inimiga) == 0:
                    eliminar_unidade(m, unidade_inimiga)   
    # devolver o mapa modificado                
    return m


def simula_batalha(file, boolean): 
    '''
    A funcao simula_batalha eh a funcao principa que permite simular uma\
    batalha completa. A batalha termina quando um dos exercitos vence ou,\
    se apos completar um turno de batalha, nao ocorreu nenhuma alteracao\
    ao mapa e as unidades. A funcao simula batalha recebe uma cadeia de\
    caracteres e um valor booleano e devolve o nome do exercito ganhador.\
    Em caso de empate, a funcao deve devolver a cadeia de caracteres 'EMPATE'.\
    A cadeia de caracteres passada por argumento corresponde ao ficheiro de\
    configuracao do simulador. O argumento booleano ativa o modo verboso (True)\
    ou o modo quiet (False). No modo quiet mostra-se pela saida standard o mapa\
    e a pontuacao no inicio da simulacao e apos do ultimo turno de batalha.\
    No modo verboso, mostra-se tambem o mapa e a pontuacao apos de cada turno de batalha 
    
    simula_batalha: str x booleano -> str
    '''
    # abrir o ficheiro
    f = open(file, 'r')
    # ler cada linha do ficheiro e obter os elementos pretendidos
    dim = eval(f.readline())
    exercito1 = eval(f.readline())
    exercito2 = eval(f.readline())
    paredes = eval(f.readline())
    posicoes_e1 = eval(f.readline())
    posicoes_e2 = eval(f.readline())
    # fechar o ficheiro
    f.close()
    # atribuir a ordem dos exercitos de acordo com a ordem alfabetica dos nomes 
    if exercito1[0][0] > exercito2[0][0]:
        exercito1, exercito2 = exercito2, exercito1
        posicoes_e1, posicoes_e2 = posicoes_e2, posicoes_e1
        
    e1 = ()
    e2 = ()
    
    # criar as unidades de acordo com as indicacoes do ficheiro
    for i in posicoes_e1:
        e1 = e1 + (cria_unidade(i, exercito1[1], exercito1[2], exercito1[0]),) 
    for i in posicoes_e2:
        e2 = e2 + (cria_unidade(i, exercito2[1], exercito2[2], exercito2[0]),)
    
    # criar o mapa de acordo com as indicacoes do ficheiro    
    m = cria_mapa(dim, paredes, e1, e2)
    nome_e1 = exercito1[0]
    nome_e2 = exercito2[0]
    
    # mostrar o mapa no display
    print(mapa_para_str(m))
    
    resultado = '[ ' + nome_e1 + ':' + str(calcula_pontos(m, 'e1')) + ' '\
        + nome_e2 + ':' + str(calcula_pontos(m, 'e2')) + ' ]'
    # mostrar os pontos de vida nno display
    print(resultado) 
    
    # criar uma variavel para armazenar o mapa anteriror ao simula turno
    # tem que ser diferente do mapa para comecar o ciclo while
    m_anterior = ()
    
    # no caso de ser modo verboso
    if boolean == True:
        # repetir o ciclo enquanto nenhum dos exercitos for derrotado ou nao haver empate
        while calcula_pontos(m, 'e1') != 0 and calcula_pontos(m, 'e2') != 0 \
              and not mapas_iguais(m_anterior, m):
            # copiar o mapa antes do simula turno
            m_anterior = cria_copia_mapa(m)
            # mostrar o mapa apos uma ronda
            print(mapa_para_str(simula_turno(m)))
            resultado = '[ ' + nome_e1 + ':' + str(calcula_pontos(m, 'e1')) + ' '\
                + nome_e2 + ':' + str(calcula_pontos(m, 'e2')) + ' ]'
            # mostrar a pontuacao apos uma ronda
            print(resultado) 
            
    # no caso de ser modo quiet       
    else:
        # repetir o ciclo enquanto nenhum dos exercitos for derrotado ou nao haver empate
        while calcula_pontos(m, 'e1') != 0 and calcula_pontos(m, 'e2') != 0 and not mapas_iguais(m_anterior, m):
            # copiar o mapa antes do simula turno
            m_anterior = cria_copia_mapa(m)
            # simular os turnos
            mapa_para_str(simula_turno(m))
        
        # mostar o mapa apos o fim da simulacao
        print(mapa_para_str(m))
        resultado = '[ ' + nome_e1 + ':' + str(calcula_pontos(m, 'e1')) + ' '\
            + nome_e2 + ':' + str(calcula_pontos(m, 'e2')) + ' ]'
        #mostar as pontuacoes apos o fim da simulacao
        print(resultado)  
        
    # no caso de ter havido empate, escrever empate
    if mapas_iguais(m_anterior, m):
        return('EMPATE')
    # no caso de ter havido vitoria de um exercito, escrever o nome do exercito vitorioso
    else:
        return(obter_exercito(obter_todas_unidades(m)[0]))