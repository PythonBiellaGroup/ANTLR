from PBGLangParser import PBGLangParser
from PBGLangListener import PBGLangListener

# Implementazione custom del listener
class PBGImplListener(PBGLangListener):

    def __init__(self):
        # Creo il dizionario dove inserisco le variabili definite 
        # dallo script da interpretare
        self.var_dict = dict()
        super(PBGLangListener, self).__init__()

    # Mette la variabile nel dizionario
    def exitLet(self, ctx:PBGLangParser.LetContext):
        self.var_dict[ctx.VAR().getText()] = int(ctx.INT().getText())

    def exitShow(self, ctx:PBGLangParser.ShowContext):
        # Se intero, mostro
        if (ctx.INT()):
            print(ctx.INT().getText())
        # Se variabile, prende valore dal dizionario
        elif (ctx.VAR()):
            print(self.var_dict[ctx.VAR().getText()])