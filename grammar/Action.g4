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
    : ATTRIBUTE ID COLON ID (EQUAL expr)? (LBRACE attributeInit* RBRACE)? SEMI
    ;
attributeInit
    : REDEFINES ID EQUAL expr SEMI
    ;
flowStatement
    : firstStep
    | thenStep
    | ifStatement
    ;

firstStep
    : FIRST ID SEMI
    ;

thenStep
    : THEN DONE SEMI
    | THEN PERFORM ID SEMI
    ;

ifStatement
    : IF LPAREN condition RPAREN LBRACE flowBody* RBRACE (ELSE LBRACE flowBody* RBRACE)?
    ;

flowBody
    : PERFORM ID SEMI
    ;

condition
    : condition AND condition
    | condition OR condition
    | NOT LPAREN condition RPAREN
    | LPAREN condition RPAREN
    | comparison
    ;

comparison
    : expr compareOp expr
    ;

compareOp
    : EQUAL_EQ
    | NOT_EQ
    | GREATER_EQ
    | LESS_EQ
    | GREATER
    | LESS
    ;
    
expr
    : ID DOT ID DOT ID  // e.g., defaultLocation.X.value
    | ID DOT ID          // e.g., defaultLocation.X
    | ID                 // e.g., variable
    | STRING             // e.g., "value"
    | NUMBER             // e.g., 50.0
    ;
