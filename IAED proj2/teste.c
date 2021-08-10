#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TRUE 1
#define FALSE 0
#define MAX_STR 1023

typedef struct str_jogo{
    struct str_jogo* next;
    char* nome;
    char* equipa1;
    char* equipa2;
    int score1;
    int score2;
} jogo;

typedef struct  
{
    struct str_jogo * head, * last;
} lista_jogo;


typedef struct str_equipa{
    struct str_equipa* next;
    char* nome;
    int vitorias;
} equipa;


void a_adicionaNovoJogo(lista_jogo * lst_jogo){
    char nome[MAX_STR], equipa1[MAX_STR], equipa2[MAX_STR];
    jogo* novo_jogo = (jogo*) malloc(sizeof(jogo));

    scanf(" %[^:]%[^:]%[^:]%d:%d",nome,equipa1,equipa2,&novo_jogo->score1,&novo_jogo->score2);

    novo_jogo->nome = (char*) malloc((strlen(nome)+1)*sizeof(char));
    novo_jogo->equipa1 = (char*) malloc((strlen(equipa1)+1)*sizeof(char));
    novo_jogo->equipa2 = (char*) malloc((strlen(equipa2)+1)*sizeof(char));
    novo_jogo->next = NULL;

    printf("")
}



int main(){
    int c;
    lista_jogo * lst_jogo = NULL;
    equipa * head_equipa = NULL;

    while((c=getchar())!='x'){
        /* deteta o comando inserido pelo utilizador */
        if (c == 'a'){
            a_adicionaNovoJogo(lst_jogo);
        }

    }    

    return 0;
}