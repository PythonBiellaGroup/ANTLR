from CondizioniVisitor import CondizioniVisitor
    
    
class InterpreteVisitor(CondizioniVisitor):
    
    def visitRoot(self,ctx):
        for i in list(ctx.getChildren()):
            self.visit(i)
     
    def visitCondition(self,ctx):
        l = list(ctx.getChildren())
        if self.visit(l[1]) == 1:
            self.visit(ctx.action(0))
        elif len(l) > 3:
            if ctx.getChild(3).getText() == 'else':
                self.visit(ctx.action(1))
        
    
    def visitPrint(self,ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[1]))
        
    def visitGt(self,ctx):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) > self.visit(l[2]))
    
    
    def visitLt(self,ctx):
        l = list(ctx.getChildren())
        return int(self.visit(l[0]) < self.visit(l[2]))
    
    def visitValue(self,ctx):
        return int(ctx.NUM().getText())
