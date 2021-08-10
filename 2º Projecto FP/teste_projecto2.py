#construtores
def numero(n):
    return n
        
def cria_posicao(x,y):
    return (x,y)
    
def cria_copia_posicao(p):
    return p
   
#seletores
def obter_pos_x(p):
    return p

def obter_pos_y(p):
    return p

#recochecedor
def eh_posicao(arg):
    return arg

def posicoes_iguais(p1, p2):
    return (p1, p2)

def posicao_para_str(p):
    return p

#alto nivel    
def obter_posicoes_adjacentes(p):
    return p

#2.1.2
#construtor
def cria_unidade(p, v, f, exercito):
    return (p, v, f , exercito)
    
def cria_copia_unidade(u):
    return u

#seletores
def obter_posicao(u):
    return u

def obter_exercito(u):
    return u

def obter_vida(u):
    return u

def obter_forca(u):
    return u

#modificadores
def muda_posicao(u, p):
    return (u, p)

def remove_vida(u, v):
    return (u, v)

#reconhecerdor
def eh_unidade(u):
    return u

def unidades_iguais(u1, u2):
    return (u1, u2)

#transformadores
def unidade_para_char(u):
    return u

def unidade_para_str(u):
    return u

#alto nivel
def unidade_ataca(u1, u2):
    return (u1, u2)
    
def ordenar_unidades(t):
    return t
    
#2.1.3
# Construtor 
#auxiliar, recebe um tuplo conentendo as dimensoes de um mapa e uma posicao\
#e retorna verdadeiro caso a posicao esteja dentro das dimensoes
def eh_posicao_valida(d, p):
    return (d, p)

def dimensao(n):
    return n
    
def eh_parede_valido(t, d):
    return (t, d)
                
            
def eh_exercito_valido(e):
    return e
    
def  cria_mapa(d, w, e1, e2):
    return (d, w, e1, e2)
    
def cria_copia_mapa(m):
    return m
        
#seletores
#funacao auxiliar, recebe mapa e unidade e indica a que exercito pertence
def qual_exercito(m, u):
    return (m, u)
    
def obter_tamanho(m):
    return m

def obter_nome_exercitos(m):
    return m
            
def obter_unidades_exercito(m, e):
    return (m, e)

def obter_todas_unidades(m):
    return m

def obter_unidade(m, p):
    return (m, p)

def obter_todas_paredes(m):
    return m
    
def obter_todas_posicoes(m):
    return m

#modificadores
def eliminar_unidade(m, u):
    return (m, u)
    
def mover_unidade(m, u, p):
    return m     


#reconhecedores
def eh_posicao_unidade(m, p):
    return (m, p)    
        
def eh_posicao_corredor(m, p):
    return (m, p)

def eh_posicao_parede(m, p):
    return (m, p)

def mapa_para_str(m):
    return m
                
def obter_inimigos_adjacentes(m, u):
    return (m, u)

def obter_movimento(mapa, unit):
    return (mapa, unit)

def calcula_pontos(m, e):
    return (m, e)
    
def simula_turno(m):
    return m

unidades = obter_todas_unidades(m)
for e in unidades:
    atacou = False
    for i in obter_posicoes_adjacentes(obter_posicao(e)):
        if eh_posicao_unidade(m, i) and obter_exercito(obter_unidade(m, i)) != obter_exercito(e):
            unidade_inimiga = obter_unidade(m, i)
            unidade_ataca(e, unidade_inimiga)
            if obter_vida(unidade_inimiga) == 0:
                eliminar_unidade(m, unidade_inimiga)
                atacou = True
                break
    if not atacou : 
        mover_unidade(m, e, obter_movimento(m, e))
        unidade_movida = obter_unidade(m, obter_movimento(m, e))
        
        for i in obter_posicoes_adjacentes(obter_posicao(unidade_movida)):
            if eh_posicao_unidade(m, i) and obter_exercito(obter_unidade(m, i)) != obter_exercito(unidade_movida):
                unidade_inimiga = obter_unidade(m, i)
                unidade_ataca(unidade_movida, unidade_inimiga)
                if obter_vida(unidade_inimiga) == 0:
                    eliminar_unidade(m, unidade_inimiga)
                    break          
                
                
                d = (7, 6)  
                w = (cria_posicao(2,3), cria_posicao(4,4)) 
                e1 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 30, 5, 'elfos') for p in ((4, 2), (5, 4))) 
                e2 = tuple(cria_unidade(cria_posicao(p[0], p[1]), 20, 5, 'orcos') for p in ((2, 1), (3, 4), (5, 2), (5, 3)))
                m1 = cria_mapa(d, w, e1, e2) 
                print(mapa_para_str(m1))
                
                
                for i in obter_posicoes_adjacentes(nova_posicao):
                    if eh_posicao_unidade(m, i):
                        if obter_exercito(obter_unidade(m, i)) != obter_exercito(u_movida):
                            unidade_inimiga = obter_unidade(m, i)
                            unidade_ataca(u_movida, unidade_inimiga)
                            if obter_vida(unidade_inimiga) == 0:
                                eliminar_unidade(m, unidade_inimiga)
                            break     
        return m
    
    
    '''exercito1 = eval(t.readline())
    exercito2 = eval(t.readline())
    paredes = eval(t.readline())
    posicoes_e1 = eval(t.readline())
    posicoes_e2 = eval(t.readline())
    exercito1[0], exercito1[1], exercito1[2] = exercito1[1], exercito1[2], exercito1[0]
    exercito2[0], exercito2[1], exercito2[2] = exercito2[1], exercito2[2], exercito2[0]
    e1 = ()
    e2 = ()
    for i in posicoes_e1:
        e1 = e1 + (i,) + (exercito1,)'''    