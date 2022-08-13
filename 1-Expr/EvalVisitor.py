if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
    from .ExprVisitor import ExprVisitor
else:
    from ExprParser import ExprParser
    from ExprVisitor import ExprVisitor
    
    
    
class EvalVisitor(ExprVisitor):
    '''
    Sottoclasse di ExprVisitor, che implementa la somma tra interi
    ctx è il contesto della regola e permette l'accesso a tutti gli elementi della regola
    '''
    
    def visitRoot(self,ctx): # regola root
        l = list(ctx.getChildren()) # lista di nodi
        # Visit expr e lo mostro come risultato finale
        return int(self.visit(l[0]))
        
    def visitExpr(self,ctx): # regola expr
        l = list(ctx.getChildren())
        if len(l) == 1: #caso: expr
            # Converto a int il testo del nodo
            # print("Trovato il numero: ", l[0].getText())
            return int(l[0].getText())
        else: # len(l) == 3; caso: expr PLUS expr
            # print("Trovato il segno: ", l[1].getText())
            # Applico la somma
            return self.visit(l[0]) + self.visit(l[2])
            
    
    
    
    
