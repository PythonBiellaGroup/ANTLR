grammar Condizioni;

//Partiamo con una sequenza non nulla di action (comandi)
root: action+ EOF; 

//('else' action) è opzionale
action: 'if' expr action ('else' action)? # Condition
    | 'print' expr                        # Print
    ;


expr: expr GT expr # Gt
    | expr LT expr # Lt
    | NUM          # Value
    ;

GT: '>';
LT: '<';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;
