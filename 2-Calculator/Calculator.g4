grammar Calculator;

// le labels per ciascun caso sono usati nel visitor
// se si usano le labels occorre specificarle per tutti i casi
expr:	left=expr op=('*'|'/') right=expr  # OpExpr
    |	left=expr op=('+'|'-') right=expr  # OpExpr
    |	atom=NUM                           # AtomExpr
    |	'(' expr ')'                       # ParenExpr
    ;

// i tokens sono espressi come espressioni regolari
NUM : [0-9]+ ;
WS  :   [ \n\r\t]+ -> skip ;
