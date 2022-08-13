grammar Expr;

root: expr EOF;

expr: expr PLUS expr
    | NUM
    ;

// i tokens sono espressi come espressioni regolari
NUM: [0-9]+;
PLUS: '+';
WS: [ \n\t\r] -> skip;
