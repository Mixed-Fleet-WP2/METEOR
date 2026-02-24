lexer grammar CommonLexer;

PACKAGE     : 'package';
IMPORT      : 'import';
PRIVATE     : 'private';
ACTION      : 'action';
PART        : 'part';
IN          : 'in';
OUT         : 'out';
PERFORM     : 'perform';
ATTRIBUTE   : 'attribute';  
REDEFINES   : ':>>';

FIRST       : 'first';
THEN        : 'then';
DONE        : 'done';
IF          : 'if';
ELSE        : 'else';

// Logical operators
AND         : 'and';
OR          : 'or';
NOT         : 'not';

// Comparison operators
EQUAL_EQ    : '==';
NOT_EQ      : '!=';
GREATER_EQ  : '>=';
LESS_EQ     : '<=';
GREATER     : '>';
LESS        : '<';

// Delimiters
COLONCOLON  : '::';
COLON       : ':';
SEMI        : ';';
EQUAL       : '=';
DOT         : '.';
STAR        : '*';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';
LPAREN      : '(';
RPAREN      : ')';  

ID      : [a-zA-Z_][a-zA-Z0-9_]* ;
STRING  : '"' (~["\\] | '\\' .)* '"' ;
NUMBER  : [0-9]+ ('.' [0-9]+)? ;
WS      : [ \t\r\n]+ -> skip ;
