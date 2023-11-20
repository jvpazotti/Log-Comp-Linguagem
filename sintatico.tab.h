/* A Bison parser, made by GNU Bison 2.3.  */

/* Skeleton interface for Bison's Yacc-like parsers in C

   Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.

   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program; if not, write to the Free Software
   Foundation, Inc., 51 Franklin Street, Fifth Floor,
   Boston, MA 02110-1301, USA.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     ADICIONE = 258,
     REFOGAR = 259,
     SE = 260,
     ENTAO = 261,
     PROVAR = 262,
     IGUAL = 263,
     PONTOVIRGULA = 264,
     NOVALINHA = 265,
     VIRGULA = 266,
     INGREDIENTE = 267,
     PORCAO = 268,
     SOMA = 269,
     SUBTRACAO = 270,
     MULTIPLICACAO = 271,
     DIVISAO = 272,
     ABRECHAVES = 273,
     FECHACHAVES = 274,
     ABREPARENTESES = 275,
     FECHAPARENTESES = 276,
     IGUALIGUAL = 277,
     MENOR = 278,
     MAIOR = 279,
     OU = 280,
     E = 281,
     NOT = 282
   };
#endif
/* Tokens.  */
#define ADICIONE 258
#define REFOGAR 259
#define SE 260
#define ENTAO 261
#define PROVAR 262
#define IGUAL 263
#define PONTOVIRGULA 264
#define NOVALINHA 265
#define VIRGULA 266
#define INGREDIENTE 267
#define PORCAO 268
#define SOMA 269
#define SUBTRACAO 270
#define MULTIPLICACAO 271
#define DIVISAO 272
#define ABRECHAVES 273
#define FECHACHAVES 274
#define ABREPARENTESES 275
#define FECHAPARENTESES 276
#define IGUALIGUAL 277
#define MENOR 278
#define MAIOR 279
#define OU 280
#define E 281
#define NOT 282




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef union YYSTYPE
#line 14 "sintatico.y"
{
    char *str;
    int num;
}
/* Line 1529 of yacc.c.  */
#line 108 "sintatico.tab.h"
	YYSTYPE;
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
# define YYSTYPE_IS_TRIVIAL 1
#endif

extern YYSTYPE yylval;

