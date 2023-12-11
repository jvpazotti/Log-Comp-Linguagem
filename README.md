# FoodLang 

A linguagem FoodLang é uma linguagem de comida fortemente baseada em Golang que foi
elaborada com base no compilador feito nas aulas de Lógica de Computação.

## EBNF da Linguagem Proposta

```
PROGRAM = { STATEMENT };

BLOCK = { "{", STATEMENT, "}"};

STATEMENT = ( λ | ASSIGNMENT | PRINT | CONDITONAL | LOOP | VAR | DECLARATION | RETURN_DEC ), "\n" ;

ASSIGMENT = IDENTIFIER, "=", BOOLEXPRESSION;

PRINT = "refeicao", "(", BOOLEXPRESSION, ")";

EXPRESSION = TERM, {("+" | "-" | "."), TERM};

TERM = FACTOR, {("*" | "/"), FACTOR };

FACTOR = (("+" | "-" | "!"), FACTOR | NUMBER | STRING | "(", EXPRESSION, ")" | IDENTIFIER, [ "(", ( { BOOLEXPRESSION, ( ",", BOOLEXPRESSION| λ ) } | λ ), ")" ] | 
SCAN, "(", ")");

RELEXPRESSION = EXPRESSION, {("==" | "<" | ">"), EXPRESSION};

BOOLEXPRESSION = BOOLTERM, {("||"), BOOLTERM};

BOOLTERM = RELEXPRESSION, {("&&"), RELEXPRESSION};

VAR = "comida", IDENTIFIER, { "doce" | "salgado" | "=", EXPRESSION};

LOOP = "degustando", ASSIGMENT, ";", EXPRESSION, ";", ASSIGMENT, BLOCK;

DECLARATION = "banquete", IDENTIFIER, "(", ( { IDENTIFIER, TYPE, (",", λ) } | λ ), ")", TYPE, BLOCK;

RETURN_DEC = "satisfeito", BOOLEXPRESSION; 

CONDITIONAL = "experimentar", EXPRESSION, {"bagre", BLOCK|BLOCK};

IDENTIFIER = LETTER, { LETTER | DIGIT | "_"};

NUMBER = DIGIT, { DIGIT };

STRING = ( a | ... | z | A | .. | Z);

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 );
```
## Para testar

```s
python main.py <nome do arquivo>.food
```
No root do repositório tem 3 testes prontos para ver a linguagem em uso, teste.food (um teste mais robusto) , teste2.food e teste3.food (testes mais simples)
