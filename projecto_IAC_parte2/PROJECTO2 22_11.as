;===============================================================================
;
;       Projecto IAC Parte 2
;
;       Zenan Chen 95688
;
;       Francisco Goncalves
;       
;       Grupo 69 Turno pratica terca-feira 9h30
;
;===============================================================================

TERM_READ       EQU     FFFFh
TERM_WRITE      EQU     FFFEh
TERM_STATE      EQU     FFFDh
TERM_CURSOR     EQU     FFFCh
TERM_COLOR      EQU     FFFBh
INT_MASK        EQU     FFFAh
SWITCHES        EQU     FFF9h
LEDS            EQU     FFF8h
TIMER_CONTROL   EQU     FFF7h
TIMER_VALUE     EQU     FFF6h
LCD_WRITE       EQU     FFF5h
LCD_CONTROL     EQU     FFF4h
DISP7SEG_3      EQU     FFF3h
DISP7SEG_2      EQU     FFF2h
DISP7SEG_1      EQU     FFF1h
DISP7SEG_0      EQU     FFF0h
DISP7SEG_5      EQU     FFEFh
DISP7SEG_4      EQU     FFEEh
GSENSOR_Z       EQU     FFEDh
GSENSOR_Y       EQU     FFECh
GSENSOR_X       EQU     FFEBh

; Other constants
STR_END         EQU     0000h
SP_ADDRESS      EQU     fdffh
INT_MASK_VALUE  EQU     FFFFh

;============== Data Region (starting at address 8000h) ========================

                ORIG    8000h
                ; allocate variables and data here (WORD, STR and TAB)
                
TEMPO_ACTUALIZACAO      EQU     1D ;tempo de interrupcao que se pretende 

TEMPO           WORD    3 ;valor arrendontado de uma decima de segundo, multiplicado por 2^5

CAS_DEC         EQU     5 ;numero de casas decimais para a vírgula fixa               
VELOCIDADE      WORD    0 
POSICAO         WORD    0 
ACELERACAO      WORD    0  
POSICAO_FINAL   WORD    0  

;estes valores são iniciados com valor 0 e actualizados e guardados em memória quando chamadas as respectivas funções

POSICAO_OBJECTO WORD    101h
;============== Code Region (starting at address 0000h) ========================

                ORIG    0000h
                JMP     Main                    ; jump to main

;-------------- Routines -------------------------------------------------------

;conversao da aceleracao obtida no acelerometro
FUNC_ACELER:    MVI     R6, 8000h ; 
                DEC     R6
                STOR    M[R6], R7
                
                MVI     R1, GSENSOR_X
                LOAD    R2, M[R1]
                MVI     R1, 10
                JAL     Produto
                
                SHRA    R3
                SHRA    R3
                SHRA    R3
                
                MVI     R1, ACELERACAO
                STOR    M[R1], R3
                
                LOAD    R7, M[R6]
                INC     R6
                JMP     R7

; funcao que calcula a velocidade com o valor a aceleracao obtida no acelerometro
FUNC_VELOC:     MVI     R6, 8000h  
                DEC     R6
                STOR    M[R6], R7 
                
                MVI     R1, ACELERACAO
                LOAD    R1, M[R1]
                
                MVI     R2, TEMPO 
                LOAD    R2, M[R2]
                
                JAL     Produto; 
                JAL     DIV   
                   
                MVI     R1, VELOCIDADE
                LOAD    R1, M[R1] 
                          
                ADD     R3, R1, R3 
                
                MVI     R1, VELOCIDADE
                STOR    M[R1], R3 
                
                LOAD    R7, M[R6]
                INC     R6 

                JMP     R7 
                               
; função que calcula o valor da posição do objecto recebendo como parâmetros a posição inicial e a velocidade calculado pela função velocidade
FUNC_POS:       MVI     R6, 8000h  
                DEC     R6
                STOR    M[R6], R7 
                
                MVI     R1, VELOCIDADE
                LOAD    R1, M[R1]
                
                MVI     R2, TEMPO 
                LOAD    R2, M[R2]
                
                JAL     Produto
                JAL     DIV
                
                DEC     R6
                STOR    M[R6], R3
                
                MVI     R1, POSICAO
                LOAD    R1, M[R1]
                ADD     R3, R1, R3
                             
                JAL     DIV

;verificar se a posicao ultrapassa a parede do lado direito
                MVI     R4, 78
                CMP     R4, R3
                BR.P    menorzero

;muda o sentido de delocamento na bola quando bate numa barede
resalto:        MVI     R5, VELOCIDADE
                LOAD    R4, M[R5]
                NEG     R4
                STOR    M[R5], R4
                        
                JMP     ACTUALIZA_RESSALTO

;verificar se a posicao ultrapassa a parede do lado esquerdo
menorzero:      MVI     R4, 0
                CMP     R3, R4
                BR.N    resalto
                
;limpa a posicao anterior da bola e coloca-a bola na nova posicao obtida                
normal:         MVI     R1, POSICAO
                LOAD    R1, M[R1] 
                
                LOAD    R3, M[R6]
                INC     R6
            
                ADD     R3, R1, R3 
                
                MVI     R1, POSICAO
                STOR    M[R1], R3 
                
                JAL     DIV 
     
                MVI     R1, POSICAO_FINAL
                STOR    M[R1], R3 
                
                MVI 	R1, TERM_WRITE
                MVI 	R2, TERM_CURSOR
                        
                MVI     R4, POSICAO_OBJECTO
                LOAD    R4, M[R4]
                STOR    M[R2], R4
                MVI     R4, ' '
                STOR    M[R1], R4
                                        
                MVI     R4, 101h
                ADD     R3, R3, R4
                MVI     R4, POSICAO_OBJECTO
                STOR    M[R4], R3
                STOR    M[R2], R3
                MVI     R4, 'o'
                STOR    M[R1], R4
                                
                LOAD    R7, M[R6]
                INC     R6 
                JMP     R7 

;função que divide o valor em R3 por 2^(numero de casas decimais defenida pelo utilizador)               
DIV:            MVI     R4, CAS_DEC 
                MVI     R5,0
                
DLOOP:          SHRA    R3; 
                INC     R5
                CMP     R4, R5
                BR.NZ   DLOOP                
                JMP     R7
                
;função que faz o produto entre os valores contidos no R1 e R2
Produto:        MVI     R3, 0
                CMP     R2, R0
                BR.Z    .Fim
                
.Loop:          ADD     R3, R3, R1
                DEC     R2
                BR.NZ   .Loop
                
.Fim:           JMP     R7

;desenhar as paredes no display
paredes:        MVI     R4, '*'
                MVI     R6, 80     
                MOV     R3, R0
loop1:          STOR    M[R1], R4     
                INC     R3
                CMP     R6, R3
                BR.P    loop1     
                JMP     R7              


;-------------- Main Program ---------------------------------------------------

Main:
                MVI     R6, SP_ADDRESS          ; set stack pointer
                MVI     R1, INT_MASK
                MVI     R2, INT_MASK_VALUE
                STOR    M[R1], R2               ; set interrupt mask
                ENI                             ; enable interrupts
                
                MVI 	R1, TERM_WRITE
                MVI 	R2, TERM_CURSOR


;-------------- desenhar paredes e bola na posicao inicial ---------------------
                
                MVI 	R4, 000h
                STOR 	M[R2], R4
                JAL     paredes
                
                MVI 	R4, 200h
                STOR 	M[R2], R4
                JAL     paredes
                
                MVI     R4, 100h
                STOR    M[R2], R4
                MVI     R4, '*'
                STOR    M[R1], R4
                                        
                MVI     R4, 14Fh
                STOR    M[R2], R4
                MVI     R4, '*'
                STOR    M[R1], R4
                
                MVI     R4, POSICAO_OBJECTO
                LOAD    R4, M[R4]
                STOR    M[R2], R4
                MVI     R4, 'o'
                STOR    M[R1], R4 
                
;obter o valor do tempo para utilizar no calculo da posicao de acordo com o tempo de actualizacao inserida pelo utilizador               
                MVI     R1, TEMPO_ACTUALIZACAO
                MVI     R2, TEMPO
                LOAD    R2, M[R2]
                JAL     Produto
                MVI     R1, TEMPO
                STOR    M[R1], R3
                
                ;defenir o tempo das interrupcoes do timer
                MVI     R1, TIMER_VALUE
                MVI     R2, TEMPO_ACTUALIZACAO
                STOR    M[R1], R2
                
                ;iniciar o timer
                MVI     R1, TIMER_CONTROL
                MVI     R2, 1
                STOR    M[R1], R2
                

;ciclo que atualiza a posicao da bola no display, a cada interrupcao               
ACTUALIZA:      JAL     FUNC_ACELER
                JAL     FUNC_VELOC 
ACTUALIZA_RESSALTO:     JAL     FUNC_POS 
                
                MVI     R1, TIMER_CONTROL
                MVI     R2, 1
                STOR    M[R1], R2
               
                RTI     
                
Stop:           BR      Stop



;-------------- Interrupts -----------------------------------------------------

                ; Button 0
                ORIG    7F00h
                RTI

                ; Button 1
                ORIG    7F10h
                RTI

                ; Button Right
                ORIG    7F20h
                RTI

                ; Button Up
                ORIG    7F30h
                RTI

                ; Button Down
                ORIG    7F40h
                RTI

                ; Button Left
                ORIG    7F50h
                RTI

                ; Button Select
                ORIG    7F60h
                RTI

                ; Keyboard
                ORIG    7F70h
                RTI

                ; Timer
                ORIG    7FF0h
                JMP     ACTUALIZA
                
;===============================================================================
