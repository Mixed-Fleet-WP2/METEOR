parser grammar Part;

options { tokenVocab=CommonLexer; }

part
    : PART ID COLON ID LBRACE partBody* RBRACE
    ;

partBody
    : ATTRIBUTE REDEFINES ID EQUAL expr unit? SEMI
    | PERFORM ID SEMI
    ;

expr
    : ID
    | STRING
    | NUMBER
    ;

unit
    : LBRACK ID RBRACK
    ;
