#construtores
def numero(n):
    return isinstance(n, int) and n >= 0

def natural(n):
    return isinstance(n, int) and n > 0
        
def cria_posicao(x,y):
    if numero(x) and numero(y):
        return (x,y)
    else: 
        raise ValueError('cria_posicao: argumentos invalidos')
    
def cria_copia_posicao(p):
    return (p[0], p[1])
   
#seletores
def obter_pos_x(p):
    return p[0]

def obter_pos_y(p):
    return p[1]

#recochecedor
def eh_posicao(arg):
    return isinstance(arg,tuple) and len(arg) == 2 and numero(arg[0]) and numero(arg[1])

def posicoes_iguais(p1, p2):
    return p1 == p2

def posicao_para_str(p):
    return str(p)

#alto nivel    
def obter_posicoes_adjacentes(p):
    if not eh_posicao(p):
        raise ValueError('posicoes_adjacentes: argumento invalido') # ver se a posicao eh valida
    else:
        p_adj = ((obter_pos_x(p),obter_pos_y(p)-1),\
                (obter_pos_x(p)-1,obter_pos_y(p)),(obter_pos_x(p)+1,obter_pos_y(p)),\
                (obter_pos_x(p),obter_pos_y(p)+1)) # ver todas as posicoes adjacentes
        p_validas = () 
        for e in p_adj:
            if eh_posicao(e):
                p_validas = p_validas + (e,) # ver as posicoes sao validas
        return p_validas

#2.1.2
#construtor
def cria_unidade(p, v, f, exercito):
    if not eh_posicao(p) or not natural(v) or not natural(f) or not isinstance(exercito,str) or exercito == '':
        raise ValueError('cria_unidade: argumentos invalidos')
    else:
        return {'posicao':p, 'vida':v, 'forca':f, 'exercito':exercito} #!!!!vida (e forca)? nao pode ser 0
    
def cria_copia_unidade(u):
    copia = {}
    for i in u:
        copia[i] = u[i]
    return copia

#seletores
def obter_posicao(u):
    return u['posicao']

def obter_exercito(u):
    return u['exercito']

def obter_vida(u):
    return u['vida']

def obter_forca(u):
    return u['forca']

#modificadores
def muda_posicao(u, p):
    u['posicao'] = p
    return u

def remove_vida(u, v):
    u['vida'] = u['vida'] - v
    return u

#reconhecerdor
def eh_unidade(u):
    if isinstance(u, dict) and len(u) == 4 and 'posicao' in u and 'forca' in u and 'vida' in u and 'exercito' in u:
        if eh_posicao(u['posicao']) and numero(u['vida']) and numero(u['forca']) and isinstance(u['exercito'],str):
            return True
        else:
            return False
    else:
        return False

def unidades_iguais(u1, u2):
    return u1 == u2

#transformadores
def unidade_para_char(u):
    nome_maiusculas = obter_exercito(u).upper()
    return nome_maiusculas[0]

def unidade_para_str(u):
    nome_unidade = str(unidade_para_char(u)) + str([obter_vida(u),obter_forca(u)]) + '@' + str(obter_posicao(u))
    return nome_unidade

#alto nivel
def unidade_ataca(u1, u2):
    forca = obter_forca(u1)
    vida = obter_vida(u2)
    if vida - forca > 0:
        u2['vida'] = vida - forca
        return False
    else:
        u2['vida'] = 0 
        return True
    
def ordenar_unidades(t):
    posicoes = {}
    ordenado = ()
    for i in t:    
        posicoes[obter_posicao(i)] = i #{(x,y): un}
    for i in sorted(posicoes, key = lambda k: [k[1], k[0]]): #(x , y) sorted , sort un correspondente
        ordenado = ordenado + (posicoes[i],)
    return ordenado
    
#2.1.3
# Construtor 
#auxiliar, recebe um tuplo conentendo as dimensoes de um mapa e uma posicao\
#e retorna verdadeiro caso a posicao esteja dentro das dimensoes
def eh_posicao_valida(d, p):
    return isinstance(p[0], int) and isinstance(p[1], int) and 0 < p[0] < d[0]-1 and 0 < p[1] < d[1] - 1

def dimensao(n):
    return isinstance(n, int) and n > 2
    
def eh_parede_valido(t, d):
    if isinstance(t, tuple):
        if t == ():
            return True
        elif len(t) == 1:
            return eh_posicao(d, t)
        else:
            for i in t:
                if isinstance(i, tuple) and dimensao(d[0]) and dimensao(d[1]):
                    if not eh_posicao_valida(d, i):
                        return False
                else: 
                    return False                
            return True
                
            
def eh_exercito_valido(e):
    flag = True
    if len(e) > 0:
        for i in e:
            if not isinstance(i, dict) or not eh_unidade(i):
                flag = False
        return flag
    else:
        return False
    
def  cria_mapa(d, w, e1, e2):
    if not isinstance(d ,tuple) or not isinstance(w, tuple) or not isinstance(e1, tuple) or not isinstance(e2, tuple):
        return ValueError('cria_mapa: argumentos invalidos')
    elif len(d) != 2 or not dimensao(d[0]) or not dimensao(d[1]) or not eh_parede_valido(w, d):
        return ValueError('cria_mapa: argumentos invalidos')
    elif not eh_exercito_valido(e1) or not eh_exercito_valido(e2):
        return ValueError('cria_mapa: argumentos invalidos')
    else:
        return {'dimensao':d, 'paredes':w, 'e1':list(e1), 'e2':list(e2)}
    
def cria_copia_mapa(m):
    copia = {}
    e1 = []
    e2 = []
    copia['dimensao'] = m['dimensao']
    copia['paredes'] = m['paredes']
    for i in m['e1']:
        e1 = e1 + [cria_copia_unidade(i)]
    for i in m['e2']:
        e2 = e2 + [cria_copia_unidade(i)] 
    copia['e1'] = e1
    copia['e2'] = e2
    return copia
        
#seletores
#funacao auxiliar, recebe mapa e unidade e indica a que exercito pertence
def qual_exercito(m, u):
    if u in obter_unidades_exercito(m1, 'e1'):
        return 'e1'
    if u in obter_unidades_exercito(m1, 'e2'):
        return 'e2'
    
def obter_tamanho(m):
    return m['dimesao']

def obter_nome_exercitos(m):
    return (obter_exercito(m['e1'][0]), obter_exercito(m['e2'][0]))
            
def obter_unidades_exercito(m, e):
    u = ()
    if e != 'e1' and e != 'e2':
        if e == obter_nome_exercitos(m)[0]:
            e = 'e1'
        else:
            e = 'e2'
    for i in m[e]:
        u = u + (i,)
    return ordenar_unidades(u)

def obter_todas_unidades(m):
    unidades = obter_unidades_exercito(m, 'e1') + obter_unidades_exercito(m, 'e2')
    return ordenar_unidades(unidades)

def obter_unidade(m, p):
    for u in obter_todas_unidades(m):
        if posicoes_iguais(p, obter_posicao(u)):
            return u

def obter_todas_paredes(m):
    paredes = ()
    for i in m['paredes']:
        paredes = paredes + (i,)
    return paredes
    
def obter_todas_posicoes(m):
    posicoes = ()
    for i in obter_todas_unidades(m):
        posicoes = posicoes + (i['posicao'],)
    return posicoes

#modificadores
def eliminar_unidade(m, u):
    if u in obter_unidades_exercito(m, 'e1'):
        e = 'e1'
    if u in obter_unidades_exercito(m, 'e2'):
        e = 'e2'    
    for i in range(len(m[e])):
        if unidades_iguais(m[e][i], u):
            del(m[e][i])
            break
    return m
    
def mover_unidade(m, u, p):
    for i in obter_todas_unidades(m):
        if unidades_iguais(i, u):
            muda_posicao(i, p)
        
    
    return m     


#reconhecedores
def eh_posicao_unidade(m, p):
    return p in obter_todas_posicoes(m)     
        
def eh_posicao_corredor(m, p):
    return eh_posicao_valida(m['dimensao'], p) and not eh_posicao_parede(m, p)#!!!!!nao pode ser parede

def eh_posicao_parede(m, p):
    return p in obter_todas_paredes(m) or obter_pos_x(p) == 0 or obter_pos_y(p) == 0 \
           or obter_pos_x(p) == m['dimensao'][0]-1 or obter_pos_y(p) == m['dimensao'][1]-1

def mapas_iguais(m1, m2):
    return m1 == m2

#trasformador
def mapa_para_str(m):
    mapa = ''
    l = []
    for y in range(m['dimensao'][1]):
        for x in range(m['dimensao'][0]):
            l = l + [(x,y)]
        if y != m['dimensao'][1] - 1:
            l = l + ['\n']
               
    for i in l:
        if eh_posicao_corredor(m, i):
            if eh_posicao_unidade(m, i):
                mapa = mapa + str(unidade_para_char(obter_unidade(m, i)))
            elif eh_posicao_parede(m, i):
                mapa = mapa + '#'
            else:
                mapa = mapa + '.'
        elif i == '\n':
            mapa = mapa + '\n'
        else:
            mapa = mapa + '#'
            
    return mapa
                
def obter_inimigos_adjacentes(m, u):
    inimigos = ()
    for i in obter_posicoes_adjacentes(obter_posicao(u)):
        if eh_posicao_unidade(m, i):
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

def calcula_pontos(m, e):
    pontos = 0
    for i in obter_unidades_exercito(m, e):
        pontos = pontos + i['vida']
    return pontos
    
def simula_turno(m):
    for u in obter_todas_unidades(m):
        if u in obter_todas_unidades(m):
            nova_posicao = obter_movimento(m, u)
            mover_unidade(m, u, nova_posicao)
            u_movida = obter_unidade(m, nova_posicao)
            if obter_inimigos_adjacentes(m, u_movida) != ():
                unidade_inimiga = obter_inimigos_adjacentes(m, u_movida)[0]
                unidade_ataca(u_movida, unidade_inimiga)
                if obter_vida(unidade_inimiga) == 0:
                    eliminar_unidade(m, unidade_inimiga)                 
    return m

def simula_batalha(text, boolean):           
    t = open(text, 'r')
    dim = eval(t.readline())
    exercito1 = eval(t.readline())
    exercito2 = eval(t.readline())
    paredes = eval(t.readline())
    posicoes_e1 = eval(t.readline())
    posicoes_e2 = eval(t.readline())
    e1 = ()
    e2 = ()
    
    for i in posicoes_e1:
        e1 = e1 + (cria_unidade(i, exercito1[1], exercito1[2], exercito1[0]),) 
    for i in posicoes_e2:
        e2 = e2 + (cria_unidade(i, exercito2[1], exercito2[2], exercito2[0]),)
    m = cria_mapa(dim, paredes, e1, e2)
    nome_e1 = exercito1[0]
    nome_e2 = exercito2[0]
    
    print(mapa_para_str(m))
    resultado = '[ ' + nome_e1 + ':' + str(calcula_pontos(m, 'e1')) + ' '\
        + nome_e2 + ':' + str(calcula_pontos(m, 'e2')) + ' ]'
    print(resultado) 
    m_anterior = ()
    
    if boolean == True:
        while calcula_pontos(m, 'e1') != 0 and calcula_pontos(m, 'e2') != 0 and not mapas_iguais(m_anterior, m):
            m_anterior = cria_copia_mapa(m)
            print(mapa_para_str(simula_turno(m)))
            resultado = '[ ' + nome_e1 + ':' + str(calcula_pontos(m, 'e1')) + ' '\
                + nome_e2 + ':' + str(calcula_pontos(m, 'e2')) + ' ]'
            print(resultado) 
            
    else:
        while calcula_pontos(m, 'e1') != 0 and calcula_pontos(m, 'e2') != 0 and not mapas_iguais(m_anterior, m):
            m_anterior = cria_copia_mapa(m)
            mapa_para_str(simula_turno(m))
        
        print(mapa_para_str(m))
        resultado = '[ ' + nome_e1 + ':' + str(calcula_pontos(m, 'e1')) + ' '\
            + nome_e2 + ':' + str(calcula_pontos(m, 'e2')) + ' ]'
        print(resultado)  
        
        
    if mapas_iguais(m_anterior, m):
        print('EMPATE')
    else:
        return(obter_exercito(obter_todas_unidades(m)[0]))
    
    