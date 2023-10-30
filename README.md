# Log-Comp-Linguagem
```
PRATO      ::= { RECEITA };

FORMA      ::= "{", RECEITA, "}";

RECEITA    ::= ( λ | TEMPERO | DEGUSTAR | CONDICIONAR | COZINHAR | INGREDIENTE ), "\n";

TEMPERO    ::= INGREDIENTE, "=", SABOR;

DEGUSTAR   ::= "provar", "#", SABOR, "#";

SABOR      ::= GOSTO, {("+" | "-" | "."), GOSTO};

GOSTO      ::= TOQUE, {("*" | "/"), TOQUE};

TOQUE      ::= (("+" | "-" | "!"), TOQUE | PORÇÃO | CONDIMENTO | "(", SABOR, ")" | INGREDIENTE | DEGUSTAR, "(", ")");

COMPARAR   ::= (SABOR, ("==" | "<" | ">" | "<=" | ">="), SABOR);

TEMPERAR   ::= (SABOR, ("e" | "ou"), SABOR);

INGREDIENTE::= "adicione", INGREDIENTE, { "picado" | "ralado" | "=", SABOR};

COZINHAR   ::= "refogar", TEMPERO, ";", SABOR, ";", TEMPERO, FORMA;

CONDICIONAR::= "se", SABOR, {"então", FORMA | FORMA};

INGREDIENTE::= CONDIMENTO, { CONDIMENTO | PORÇÃO | "_"};

PORÇÃO     ::= UNIDADE, { UNIDADE };

CONDIMENTO ::= (a | ... | z | A | .. | Z);

UNIDADE    ::= (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);
```
Algumas adaptações feitas:

PROGRAM virou PRATO – Pense nisso como um prato que você está preparando.
STATEMENT é agora RECEITA.
ASSIGNMENT se transformou em TEMPERO - Você está temperando um ingrediente com algum sabor.
PRINT virou DEGUSTAR – Para provar o sabor de uma expressão.
EXPRESSION é agora SABOR - Representa os diferentes sabores que você pode criar combinando ingredientes.
VAR se transformou em INGREDIENTE.
LOOP se tornou COZINHAR.
CONDITIONAL é agora CONDICIONAR.
IDENTIFIER se transformou em INGREDIENTE.
NUMBER é PORÇÃO – Quantidades de um ingrediente.
LETTER virou CONDIMENTO - Ingredientes básicos que você pode usar
