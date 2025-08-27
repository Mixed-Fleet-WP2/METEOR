lexer grammar CommonLexer;

ACTION      : 'action';
PART        : 'part';
IN          : 'in';
OUT         : 'out';
PERFORM     : 'perform';
ATTRIBUTE   : 'attribute';  
REDEFINES : ':>>';

FIRST       : 'first';
THEN        : 'then';
DONE        : 'done';

COLON       : ':';
SEMI        : ';';
EQUAL       : '=';
DOT         : '.';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING  : '"' (~["\\] | '\\' .)* '"' ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
