parser grammar Model;

options { tokenVocab=CommonLexer; }

import Action, Part;

model
    : packageDecl? importDecl* (action | part)* EOF
    ;

packageDecl
    : PACKAGE qualifiedName LBRACE (importDecl | action | part)* RBRACE
    ;

importDecl
    : PRIVATE? IMPORT qualifiedName COLONCOLON STAR SEMI
    ;

qualifiedName
    : ID (COLONCOLON ID)*
    ;