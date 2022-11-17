parser grammar AntlrScriptParser;

options {
    tokenVocab=AntlrScriptLexer; // Riferimento al lexer
}

script:
    STATEMENT*
    EOF
    ;

statement:
    ;


type_spec  // Regola definita per casi
    : INTEGER   #integer_type
    | BOOLEAN   #boolean_type
    | STRING    #string_type
    | target=ID #entity_type
    ;