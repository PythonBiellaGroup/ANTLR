grammar Expr;

root: expr EOF;

expr: expr PLUS expr
    | NUM
    ;

NUM: [0-9]+;
PLUS: '+';
WS: [ \n] -> skip;
