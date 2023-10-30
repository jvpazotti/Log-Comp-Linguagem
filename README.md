# Log-Comp-Linguagem

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
