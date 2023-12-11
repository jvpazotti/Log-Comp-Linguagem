# Log-Comp-Linguagem

## EBNF do Golang Original

```
PROGRAM         ::= { STATEMENT };

BLOCK           ::= "{", { STATEMENT }, "}";

STATEMENT       ::= ( λ | ASSIGNMENT | PRINT | CONDITIONAL | LOOP | VARIABLE ), "\n";

ASSIGNMENT      ::= IDENTIFIER, "=", EXPRESSION;

PRINT           ::= "print", "#", EXPRESSION, "#";

EXPRESSION      ::= TERM, {("+" | "-" | "."), TERM};

TERM            ::= FACTOR, {("*" | "/"), FACTOR};

FACTOR          ::= (("+" | "-" | "!"), FACTOR | NUMBER | LETTER | "(", EXPRESSION, ")" | IDENTIFIER | PRINT, "(", ")");

COMPARISON      ::= (EXPRESSION, ("==" | "<" | ">" | "<=" | ">="), EXPRESSION);

LOGICAL_OPERATOR::= (EXPRESSION, ("and" | "or"), EXPRESSION);

VARIABLE        ::= "var", IDENTIFIER, { "int" | "string" | "=", EXPRESSION};

LOOP            ::= "loop", ASSIGNMENT, ";", EXPRESSION, ";", ASSIGNMENT, BLOCK;

CONDITIONAL     ::= "if", EXPRESSION, {"then", BLOCK | BLOCK};

IDENTIFIER      ::= LETTER, { LETTER | DIGIT | "_" };

NUMBER          ::= DIGIT, { DIGIT };

LETTER          ::= (a | ... | z | A | ... | Z);

DIGIT           ::= (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);

```

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


