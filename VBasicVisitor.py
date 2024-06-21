# Generated from VBasic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VBasicParser import VBasicParser
else:
    from VBasicParser import VBasicParser

# This class defines a complete generic visitor for a parse tree produced by VBasicParser.

class VBasicVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VBasicParser#prog.
    def visitProg(self, ctx:VBasicParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#line.
    def visitLine(self, ctx:VBasicParser.LineContext):
        print("visitLine")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#amperoper.
    def visitAmperoper(self, ctx:VBasicParser.AmperoperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#linenumber.
    def visitLinenumber(self, ctx:VBasicParser.LinenumberContext):
        print("visitLinenumber")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#amprstmt.
    def visitAmprstmt(self, ctx:VBasicParser.AmprstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#statement.
    def visitStatement(self, ctx:VBasicParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#vardecl.
    def visitVardecl(self, ctx:VBasicParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#printstmt1.
    def visitPrintstmt1(self, ctx:VBasicParser.Printstmt1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#printlist.
    def visitPrintlist(self, ctx:VBasicParser.PrintlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#getstmt.
    def visitGetstmt(self, ctx:VBasicParser.GetstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#letstmt.
    def visitLetstmt(self, ctx:VBasicParser.LetstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#variableassignment.
    def visitVariableassignment(self, ctx:VBasicParser.VariableassignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#relop.
    def visitRelop(self, ctx:VBasicParser.RelopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#neq.
    def visitNeq(self, ctx:VBasicParser.NeqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#ifstmt.
    def visitIfstmt(self, ctx:VBasicParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#forstmt1.
    def visitForstmt1(self, ctx:VBasicParser.Forstmt1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#forstmt2.
    def visitForstmt2(self, ctx:VBasicParser.Forstmt2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#nextstmt.
    def visitNextstmt(self, ctx:VBasicParser.NextstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#inputstmt.
    def visitInputstmt(self, ctx:VBasicParser.InputstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#readstmt.
    def visitReadstmt(self, ctx:VBasicParser.ReadstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#dimstmt.
    def visitDimstmt(self, ctx:VBasicParser.DimstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#gotostmt.
    def visitGotostmt(self, ctx:VBasicParser.GotostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#gosubstmt.
    def visitGosubstmt(self, ctx:VBasicParser.GosubstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#pokestmt.
    def visitPokestmt(self, ctx:VBasicParser.PokestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#callstmt.
    def visitCallstmt(self, ctx:VBasicParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#hplotstmt.
    def visitHplotstmt(self, ctx:VBasicParser.HplotstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#vplotstmt.
    def visitVplotstmt(self, ctx:VBasicParser.VplotstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#plotstmt.
    def visitPlotstmt(self, ctx:VBasicParser.PlotstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#ongotostmt.
    def visitOngotostmt(self, ctx:VBasicParser.OngotostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#ongosubstmt.
    def visitOngosubstmt(self, ctx:VBasicParser.OngosubstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#vtabstmnt.
    def visitVtabstmnt(self, ctx:VBasicParser.VtabstmntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#htabstmnt.
    def visitHtabstmnt(self, ctx:VBasicParser.HtabstmntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#himemstmt.
    def visitHimemstmt(self, ctx:VBasicParser.HimemstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#lomemstmt.
    def visitLomemstmt(self, ctx:VBasicParser.LomemstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#datastmt.
    def visitDatastmt(self, ctx:VBasicParser.DatastmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#datum.
    def visitDatum(self, ctx:VBasicParser.DatumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#waitstmt.
    def visitWaitstmt(self, ctx:VBasicParser.WaitstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#xdrawstmt.
    def visitXdrawstmt(self, ctx:VBasicParser.XdrawstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#drawstmt.
    def visitDrawstmt(self, ctx:VBasicParser.DrawstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#defstmt.
    def visitDefstmt(self, ctx:VBasicParser.DefstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#tabstmt.
    def visitTabstmt(self, ctx:VBasicParser.TabstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#speedstmt.
    def visitSpeedstmt(self, ctx:VBasicParser.SpeedstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#rotstmt.
    def visitRotstmt(self, ctx:VBasicParser.RotstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#scalestmt.
    def visitScalestmt(self, ctx:VBasicParser.ScalestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#colorstmt.
    def visitColorstmt(self, ctx:VBasicParser.ColorstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#hcolorstmt.
    def visitHcolorstmt(self, ctx:VBasicParser.HcolorstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#hlinstmt.
    def visitHlinstmt(self, ctx:VBasicParser.HlinstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#vlinstmt.
    def visitVlinstmt(self, ctx:VBasicParser.VlinstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#onerrstmt.
    def visitOnerrstmt(self, ctx:VBasicParser.OnerrstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#prstmt.
    def visitPrstmt(self, ctx:VBasicParser.PrstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#instmt.
    def visitInstmt(self, ctx:VBasicParser.InstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#storestmt.
    def visitStorestmt(self, ctx:VBasicParser.StorestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#recallstmt.
    def visitRecallstmt(self, ctx:VBasicParser.RecallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#liststmt.
    def visitListstmt(self, ctx:VBasicParser.ListstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#popstmt.
    def visitPopstmt(self, ctx:VBasicParser.PopstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#amptstmt.
    def visitAmptstmt(self, ctx:VBasicParser.AmptstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#includestmt.
    def visitIncludestmt(self, ctx:VBasicParser.IncludestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#endstmt.
    def visitEndstmt(self, ctx:VBasicParser.EndstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#returnstmt.
    def visitReturnstmt(self, ctx:VBasicParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#restorestmt.
    def visitRestorestmt(self, ctx:VBasicParser.RestorestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#number.
    def visitNumber(self, ctx:VBasicParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#func_.
    def visitFunc_(self, ctx:VBasicParser.Func_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#signExpression.
    def visitSignExpression(self, ctx:VBasicParser.SignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#exponentExpression.
    def visitExponentExpression(self, ctx:VBasicParser.ExponentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#multiplyingExpression.
    def visitMultiplyingExpression(self, ctx:VBasicParser.MultiplyingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#addingExpression.
    def visitAddingExpression(self, ctx:VBasicParser.AddingExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#relationalExpression.
    def visitRelationalExpression(self, ctx:VBasicParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#expression.
    def visitExpression(self, ctx:VBasicParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#var_.
    def visitVar_(self, ctx:VBasicParser.Var_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#varname.
    def visitVarname(self, ctx:VBasicParser.VarnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#varsuffix.
    def visitVarsuffix(self, ctx:VBasicParser.VarsuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#varlist.
    def visitVarlist(self, ctx:VBasicParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#exprlist.
    def visitExprlist(self, ctx:VBasicParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#sqrfunc.
    def visitSqrfunc(self, ctx:VBasicParser.SqrfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#chrfunc.
    def visitChrfunc(self, ctx:VBasicParser.ChrfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#lenfunc.
    def visitLenfunc(self, ctx:VBasicParser.LenfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#ascfunc.
    def visitAscfunc(self, ctx:VBasicParser.AscfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#midfunc.
    def visitMidfunc(self, ctx:VBasicParser.MidfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#pdlfunc.
    def visitPdlfunc(self, ctx:VBasicParser.PdlfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#peekfunc.
    def visitPeekfunc(self, ctx:VBasicParser.PeekfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#intfunc.
    def visitIntfunc(self, ctx:VBasicParser.IntfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#spcfunc.
    def visitSpcfunc(self, ctx:VBasicParser.SpcfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#frefunc.
    def visitFrefunc(self, ctx:VBasicParser.FrefuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#posfunc.
    def visitPosfunc(self, ctx:VBasicParser.PosfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#usrfunc.
    def visitUsrfunc(self, ctx:VBasicParser.UsrfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#leftfunc.
    def visitLeftfunc(self, ctx:VBasicParser.LeftfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#rightfunc.
    def visitRightfunc(self, ctx:VBasicParser.RightfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#strfunc.
    def visitStrfunc(self, ctx:VBasicParser.StrfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#fnfunc.
    def visitFnfunc(self, ctx:VBasicParser.FnfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#valfunc.
    def visitValfunc(self, ctx:VBasicParser.ValfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#scrnfunc.
    def visitScrnfunc(self, ctx:VBasicParser.ScrnfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#sinfunc.
    def visitSinfunc(self, ctx:VBasicParser.SinfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#cosfunc.
    def visitCosfunc(self, ctx:VBasicParser.CosfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#tanfunc.
    def visitTanfunc(self, ctx:VBasicParser.TanfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#atnfunc.
    def visitAtnfunc(self, ctx:VBasicParser.AtnfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#rndfunc.
    def visitRndfunc(self, ctx:VBasicParser.RndfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#sgnfunc.
    def visitSgnfunc(self, ctx:VBasicParser.SgnfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#expfunc.
    def visitExpfunc(self, ctx:VBasicParser.ExpfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#logfunc.
    def visitLogfunc(self, ctx:VBasicParser.LogfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#absfunc.
    def visitAbsfunc(self, ctx:VBasicParser.AbsfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VBasicParser#tabfunc.
    def visitTabfunc(self, ctx:VBasicParser.TabfuncContext):
        return self.visitChildren(ctx)



del VBasicParser