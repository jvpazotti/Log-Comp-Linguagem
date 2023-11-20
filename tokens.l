%{
#include "sintatico.tab.h"
%}

%%

"adicione"                  { return ADICIONE; }
"refogar"                   { return REFOGAR; }
"se"                        { return SE; }
"então"                     { return ENTAO; }
"provar"                    { return PROVAR; }
[a-zA-Z_][a-zA-Z0-9_]*      { yylval.str = strdup(yytext); return INGREDIENTE; }
[0-9]+                      { yylval.num = atoi(yytext); return PORCAO; }
"+"                         { return SOMA; }
"-"                         { return SUBTRACAO; }
"*"                         { return MULTIPLICACAO; }
"/"                         { return DIVISAO; }
"="                         { return IGUAL; }
"=="                        { return IGUALIGUAL; }
"<"                         { return MENOR; }
">"                         { return MAIOR; }
"||"                        { return OU; }
"&&"                        { return E; }
"!"                         { return NOT; }
"{"                         { return ABRECHAVES; }
"}"                         { return FECHACHAVES; }
";"                         { return PONTOVIRGULA; }
"("                         { return ABREPARENTESES; }
")"                         { return FECHAPARENTESES; }
","                         { return VIRGULA; }
"\n"                        { return NOVALINHA; }
.                           { /* caracteres não reconhecidos */ }

%%
