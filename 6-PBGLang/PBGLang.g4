grammar PBGLang;

program     : statement+;
statement   : let | show ;
let         : VAR '=' INT;
show        : 'mustra' (INT | VAR) ;

VAR         : [a-z]+ ;
INT         : [0-9]+ ;
WS          : [ \n\r\t]+ -> skip ;
