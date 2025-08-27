parser grammar Action;

options { tokenVocab=CommonLexer; }

import Part; 

action
    : ACTION ID (COLON ID)? LBRACE
        (attribute | part | param | flowStatement | action)*
      RBRACE
    ;
param
    : IN REDEFINES? ID EQUAL expr SEMI
    | OUT ID SEMI
    ;
attribute
    : ATTRIBUTE ID COLON ID (LBRACE attributeInit* RBRACE)? SEMI
    ;
attributeInit
    : REDEFINES ID EQUAL expr SEMI
    ;
flowStatement
    : firstStep
    | thenStep
    ;

firstStep
    : FIRST ID SEMI
    ;

thenStep
    : THEN DONE SEMI
    | THEN PERFORM ID SEMI
    ;
    
expr
    : ID
    | ID DOT ID
    | STRING
    | NUMBER
    ;
