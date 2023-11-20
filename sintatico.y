%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
void yyerror(const char *s) { fprintf(stderr, "Erro: %s\n", s); }
%}

%token ADICIONE REFOGAR SE ENTAO PROVAR IGUAL PONTOVIRGULA NOVALINHA VIRGULA
%token INGREDIENTE PORCAO
%token SOMA SUBTRACAO MULTIPLICACAO DIVISAO
%token ABRECHAVES FECHACHAVES ABREPARENTESES FECHAPARENTESES
%token IGUALIGUAL MENOR MAIOR OU E NOT

%union {
    char *str;
    int num;
}

%%

prato: /* vazio */
      | prato receita NOVALINHA
      ;

forma: ABRECHAVES receita FECHACHAVES ;

receita: tempero
       | degustar
       | condicionar
       | cozinhar
       | ingrediente
       ;

tempero: INGREDIENTE IGUAL sabor;

degustar: PROVAR ABREPARENTESES sabor FECHAPARENTESES;

sabor: gosto
      | gosto SOMA gosto
      | gosto SUBTRACAO gosto
      ;

gosto: toque
      | toque MULTIPLICACAO toque
      | toque DIVISAO toque
      ;

toque: SOMA toque
      | SUBTRACAO toque
      | NOT toque
      | ABREPARENTESES sabor FECHAPARENTESES
      | INGREDIENTE
      | PORCAO
      ;

condicionar: SE sabor ENTAO forma
            | SE sabor forma
            ;

cozinhar: REFOGAR tempero PONTOVIRGULA sabor PONTOVIRGULA tempero forma;

ingrediente: ADICIONE INGREDIENTE
           ;

%%

int main(void) {
    return yyparse();
}


