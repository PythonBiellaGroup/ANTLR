from CalculatorParser import CalculatorParser
from CalculatorVisitor import CalculatorVisitor
    
# Usiamo le labels della grammatica
class EvalVisitor(CalculatorVisitor):
    '''
    Sottoclasse di CalculatorVisitor
    Vengono utilizzate le label della grammatica per gestire i casi
    ctx è il contesto della regola e permette l'accesso a tutti gli elementi della regola
    '''
    def visitAtomExpr(self, ctx:CalculatorParser.AtomExprContext):
        return int(ctx.getText())

    def visitParenExpr(self, ctx:CalculatorParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitOpExpr(self, ctx:CalculatorParser.OpExprContext):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        op = ctx.op.text
        if op == '+':
            return l + r
        elif op == '-':
            return l - r
        elif op == '*':
            return l * r
        elif op == '/':
            # Gestione particolare della divisione per zero
            if r == 0:
                print('divide by zero!')
                return 0
            return l / r

