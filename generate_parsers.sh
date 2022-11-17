alias antlr4="java -jar `pwd`/antlr/antlr-4.11.1-complete.jar"
pushd grammar;
antlr4 -Dlanguage=Python3 AntlrEntityLexer.g4 -o ../entity_parser;
antlr4 -Dlanguage=Python3 AntlrEntityParser.g4 -o ../entity_parser;
antlr4 -Dlanguage=Python3 AntlrScriptLexer.g4 -o ../script_parser;
antlr4 -Dlanguage=Python3 AntlrScriptParser.g4 -o ../script_parser;
popd