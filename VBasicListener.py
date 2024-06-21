# Generated from VBasic.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .VBasicParser import VBasicParser
else:
    from VBasicParser import VBasicParser

# This class defines a complete listener for a parse tree produced by VBasicParser.
class VBasicListener(ParseTreeListener):

    # Enter a parse tree produced by VBasicParser#prog.
    def enterProg(self, ctx:VBasicParser.ProgContext):
        pass

    # Exit a parse tree produced by VBasicParser#prog.
    def exitProg(self, ctx:VBasicParser.ProgContext):
        pass


    # Enter a parse tree produced by VBasicParser#line.
    def enterLine(self, ctx:VBasicParser.LineContext):
        pass

    # Exit a parse tree produced by VBasicParser#line.
    def exitLine(self, ctx:VBasicParser.LineContext):
        pass


    # Enter a parse tree produced by VBasicParser#amperoper.
    def enterAmperoper(self, ctx:VBasicParser.AmperoperContext):
        pass

    # Exit a parse tree produced by VBasicParser#amperoper.
    def exitAmperoper(self, ctx:VBasicParser.AmperoperContext):
        pass


    # Enter a parse tree produced by VBasicParser#linenumber.
    def enterLinenumber(self, ctx:VBasicParser.LinenumberContext):
        pass

    # Exit a parse tree produced by VBasicParser#linenumber.
    def exitLinenumber(self, ctx:VBasicParser.LinenumberContext):
        pass


    # Enter a parse tree produced by VBasicParser#amprstmt.
    def enterAmprstmt(self, ctx:VBasicParser.AmprstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#amprstmt.
    def exitAmprstmt(self, ctx:VBasicParser.AmprstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#statement.
    def enterStatement(self, ctx:VBasicParser.StatementContext):
        pass

    # Exit a parse tree produced by VBasicParser#statement.
    def exitStatement(self, ctx:VBasicParser.StatementContext):
        pass


    # Enter a parse tree produced by VBasicParser#vardecl.
    def enterVardecl(self, ctx:VBasicParser.VardeclContext):
        pass

    # Exit a parse tree produced by VBasicParser#vardecl.
    def exitVardecl(self, ctx:VBasicParser.VardeclContext):
        pass


    # Enter a parse tree produced by VBasicParser#printstmt1.
    def enterPrintstmt1(self, ctx:VBasicParser.Printstmt1Context):
        pass

    # Exit a parse tree produced by VBasicParser#printstmt1.
    def exitPrintstmt1(self, ctx:VBasicParser.Printstmt1Context):
        pass


    # Enter a parse tree produced by VBasicParser#printlist.
    def enterPrintlist(self, ctx:VBasicParser.PrintlistContext):
        pass

    # Exit a parse tree produced by VBasicParser#printlist.
    def exitPrintlist(self, ctx:VBasicParser.PrintlistContext):
        pass


    # Enter a parse tree produced by VBasicParser#getstmt.
    def enterGetstmt(self, ctx:VBasicParser.GetstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#getstmt.
    def exitGetstmt(self, ctx:VBasicParser.GetstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#letstmt.
    def enterLetstmt(self, ctx:VBasicParser.LetstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#letstmt.
    def exitLetstmt(self, ctx:VBasicParser.LetstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#variableassignment.
    def enterVariableassignment(self, ctx:VBasicParser.VariableassignmentContext):
        pass

    # Exit a parse tree produced by VBasicParser#variableassignment.
    def exitVariableassignment(self, ctx:VBasicParser.VariableassignmentContext):
        pass


    # Enter a parse tree produced by VBasicParser#relop.
    def enterRelop(self, ctx:VBasicParser.RelopContext):
        pass

    # Exit a parse tree produced by VBasicParser#relop.
    def exitRelop(self, ctx:VBasicParser.RelopContext):
        pass


    # Enter a parse tree produced by VBasicParser#neq.
    def enterNeq(self, ctx:VBasicParser.NeqContext):
        pass

    # Exit a parse tree produced by VBasicParser#neq.
    def exitNeq(self, ctx:VBasicParser.NeqContext):
        pass


    # Enter a parse tree produced by VBasicParser#ifstmt.
    def enterIfstmt(self, ctx:VBasicParser.IfstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#ifstmt.
    def exitIfstmt(self, ctx:VBasicParser.IfstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#forstmt1.
    def enterForstmt1(self, ctx:VBasicParser.Forstmt1Context):
        pass

    # Exit a parse tree produced by VBasicParser#forstmt1.
    def exitForstmt1(self, ctx:VBasicParser.Forstmt1Context):
        pass


    # Enter a parse tree produced by VBasicParser#forstmt2.
    def enterForstmt2(self, ctx:VBasicParser.Forstmt2Context):
        pass

    # Exit a parse tree produced by VBasicParser#forstmt2.
    def exitForstmt2(self, ctx:VBasicParser.Forstmt2Context):
        pass


    # Enter a parse tree produced by VBasicParser#nextstmt.
    def enterNextstmt(self, ctx:VBasicParser.NextstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#nextstmt.
    def exitNextstmt(self, ctx:VBasicParser.NextstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#inputstmt.
    def enterInputstmt(self, ctx:VBasicParser.InputstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#inputstmt.
    def exitInputstmt(self, ctx:VBasicParser.InputstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#readstmt.
    def enterReadstmt(self, ctx:VBasicParser.ReadstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#readstmt.
    def exitReadstmt(self, ctx:VBasicParser.ReadstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#dimstmt.
    def enterDimstmt(self, ctx:VBasicParser.DimstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#dimstmt.
    def exitDimstmt(self, ctx:VBasicParser.DimstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#gotostmt.
    def enterGotostmt(self, ctx:VBasicParser.GotostmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#gotostmt.
    def exitGotostmt(self, ctx:VBasicParser.GotostmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#gosubstmt.
    def enterGosubstmt(self, ctx:VBasicParser.GosubstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#gosubstmt.
    def exitGosubstmt(self, ctx:VBasicParser.GosubstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#pokestmt.
    def enterPokestmt(self, ctx:VBasicParser.PokestmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#pokestmt.
    def exitPokestmt(self, ctx:VBasicParser.PokestmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#callstmt.
    def enterCallstmt(self, ctx:VBasicParser.CallstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#callstmt.
    def exitCallstmt(self, ctx:VBasicParser.CallstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#hplotstmt.
    def enterHplotstmt(self, ctx:VBasicParser.HplotstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#hplotstmt.
    def exitHplotstmt(self, ctx:VBasicParser.HplotstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#vplotstmt.
    def enterVplotstmt(self, ctx:VBasicParser.VplotstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#vplotstmt.
    def exitVplotstmt(self, ctx:VBasicParser.VplotstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#plotstmt.
    def enterPlotstmt(self, ctx:VBasicParser.PlotstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#plotstmt.
    def exitPlotstmt(self, ctx:VBasicParser.PlotstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#ongotostmt.
    def enterOngotostmt(self, ctx:VBasicParser.OngotostmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#ongotostmt.
    def exitOngotostmt(self, ctx:VBasicParser.OngotostmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#ongosubstmt.
    def enterOngosubstmt(self, ctx:VBasicParser.OngosubstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#ongosubstmt.
    def exitOngosubstmt(self, ctx:VBasicParser.OngosubstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#vtabstmnt.
    def enterVtabstmnt(self, ctx:VBasicParser.VtabstmntContext):
        pass

    # Exit a parse tree produced by VBasicParser#vtabstmnt.
    def exitVtabstmnt(self, ctx:VBasicParser.VtabstmntContext):
        pass


    # Enter a parse tree produced by VBasicParser#htabstmnt.
    def enterHtabstmnt(self, ctx:VBasicParser.HtabstmntContext):
        pass

    # Exit a parse tree produced by VBasicParser#htabstmnt.
    def exitHtabstmnt(self, ctx:VBasicParser.HtabstmntContext):
        pass


    # Enter a parse tree produced by VBasicParser#himemstmt.
    def enterHimemstmt(self, ctx:VBasicParser.HimemstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#himemstmt.
    def exitHimemstmt(self, ctx:VBasicParser.HimemstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#lomemstmt.
    def enterLomemstmt(self, ctx:VBasicParser.LomemstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#lomemstmt.
    def exitLomemstmt(self, ctx:VBasicParser.LomemstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#datastmt.
    def enterDatastmt(self, ctx:VBasicParser.DatastmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#datastmt.
    def exitDatastmt(self, ctx:VBasicParser.DatastmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#datum.
    def enterDatum(self, ctx:VBasicParser.DatumContext):
        pass

    # Exit a parse tree produced by VBasicParser#datum.
    def exitDatum(self, ctx:VBasicParser.DatumContext):
        pass


    # Enter a parse tree produced by VBasicParser#waitstmt.
    def enterWaitstmt(self, ctx:VBasicParser.WaitstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#waitstmt.
    def exitWaitstmt(self, ctx:VBasicParser.WaitstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#xdrawstmt.
    def enterXdrawstmt(self, ctx:VBasicParser.XdrawstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#xdrawstmt.
    def exitXdrawstmt(self, ctx:VBasicParser.XdrawstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#drawstmt.
    def enterDrawstmt(self, ctx:VBasicParser.DrawstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#drawstmt.
    def exitDrawstmt(self, ctx:VBasicParser.DrawstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#defstmt.
    def enterDefstmt(self, ctx:VBasicParser.DefstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#defstmt.
    def exitDefstmt(self, ctx:VBasicParser.DefstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#tabstmt.
    def enterTabstmt(self, ctx:VBasicParser.TabstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#tabstmt.
    def exitTabstmt(self, ctx:VBasicParser.TabstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#speedstmt.
    def enterSpeedstmt(self, ctx:VBasicParser.SpeedstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#speedstmt.
    def exitSpeedstmt(self, ctx:VBasicParser.SpeedstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#rotstmt.
    def enterRotstmt(self, ctx:VBasicParser.RotstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#rotstmt.
    def exitRotstmt(self, ctx:VBasicParser.RotstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#scalestmt.
    def enterScalestmt(self, ctx:VBasicParser.ScalestmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#scalestmt.
    def exitScalestmt(self, ctx:VBasicParser.ScalestmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#colorstmt.
    def enterColorstmt(self, ctx:VBasicParser.ColorstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#colorstmt.
    def exitColorstmt(self, ctx:VBasicParser.ColorstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#hcolorstmt.
    def enterHcolorstmt(self, ctx:VBasicParser.HcolorstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#hcolorstmt.
    def exitHcolorstmt(self, ctx:VBasicParser.HcolorstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#hlinstmt.
    def enterHlinstmt(self, ctx:VBasicParser.HlinstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#hlinstmt.
    def exitHlinstmt(self, ctx:VBasicParser.HlinstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#vlinstmt.
    def enterVlinstmt(self, ctx:VBasicParser.VlinstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#vlinstmt.
    def exitVlinstmt(self, ctx:VBasicParser.VlinstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#onerrstmt.
    def enterOnerrstmt(self, ctx:VBasicParser.OnerrstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#onerrstmt.
    def exitOnerrstmt(self, ctx:VBasicParser.OnerrstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#prstmt.
    def enterPrstmt(self, ctx:VBasicParser.PrstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#prstmt.
    def exitPrstmt(self, ctx:VBasicParser.PrstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#instmt.
    def enterInstmt(self, ctx:VBasicParser.InstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#instmt.
    def exitInstmt(self, ctx:VBasicParser.InstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#storestmt.
    def enterStorestmt(self, ctx:VBasicParser.StorestmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#storestmt.
    def exitStorestmt(self, ctx:VBasicParser.StorestmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#recallstmt.
    def enterRecallstmt(self, ctx:VBasicParser.RecallstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#recallstmt.
    def exitRecallstmt(self, ctx:VBasicParser.RecallstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#liststmt.
    def enterListstmt(self, ctx:VBasicParser.ListstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#liststmt.
    def exitListstmt(self, ctx:VBasicParser.ListstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#popstmt.
    def enterPopstmt(self, ctx:VBasicParser.PopstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#popstmt.
    def exitPopstmt(self, ctx:VBasicParser.PopstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#amptstmt.
    def enterAmptstmt(self, ctx:VBasicParser.AmptstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#amptstmt.
    def exitAmptstmt(self, ctx:VBasicParser.AmptstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#includestmt.
    def enterIncludestmt(self, ctx:VBasicParser.IncludestmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#includestmt.
    def exitIncludestmt(self, ctx:VBasicParser.IncludestmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#endstmt.
    def enterEndstmt(self, ctx:VBasicParser.EndstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#endstmt.
    def exitEndstmt(self, ctx:VBasicParser.EndstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#returnstmt.
    def enterReturnstmt(self, ctx:VBasicParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#returnstmt.
    def exitReturnstmt(self, ctx:VBasicParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#restorestmt.
    def enterRestorestmt(self, ctx:VBasicParser.RestorestmtContext):
        pass

    # Exit a parse tree produced by VBasicParser#restorestmt.
    def exitRestorestmt(self, ctx:VBasicParser.RestorestmtContext):
        pass


    # Enter a parse tree produced by VBasicParser#number.
    def enterNumber(self, ctx:VBasicParser.NumberContext):
        pass

    # Exit a parse tree produced by VBasicParser#number.
    def exitNumber(self, ctx:VBasicParser.NumberContext):
        pass


    # Enter a parse tree produced by VBasicParser#func_.
    def enterFunc_(self, ctx:VBasicParser.Func_Context):
        pass

    # Exit a parse tree produced by VBasicParser#func_.
    def exitFunc_(self, ctx:VBasicParser.Func_Context):
        pass


    # Enter a parse tree produced by VBasicParser#signExpression.
    def enterSignExpression(self, ctx:VBasicParser.SignExpressionContext):
        pass

    # Exit a parse tree produced by VBasicParser#signExpression.
    def exitSignExpression(self, ctx:VBasicParser.SignExpressionContext):
        pass


    # Enter a parse tree produced by VBasicParser#exponentExpression.
    def enterExponentExpression(self, ctx:VBasicParser.ExponentExpressionContext):
        pass

    # Exit a parse tree produced by VBasicParser#exponentExpression.
    def exitExponentExpression(self, ctx:VBasicParser.ExponentExpressionContext):
        pass


    # Enter a parse tree produced by VBasicParser#multiplyingExpression.
    def enterMultiplyingExpression(self, ctx:VBasicParser.MultiplyingExpressionContext):
        pass

    # Exit a parse tree produced by VBasicParser#multiplyingExpression.
    def exitMultiplyingExpression(self, ctx:VBasicParser.MultiplyingExpressionContext):
        pass


    # Enter a parse tree produced by VBasicParser#addingExpression.
    def enterAddingExpression(self, ctx:VBasicParser.AddingExpressionContext):
        pass

    # Exit a parse tree produced by VBasicParser#addingExpression.
    def exitAddingExpression(self, ctx:VBasicParser.AddingExpressionContext):
        pass


    # Enter a parse tree produced by VBasicParser#relationalExpression.
    def enterRelationalExpression(self, ctx:VBasicParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by VBasicParser#relationalExpression.
    def exitRelationalExpression(self, ctx:VBasicParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by VBasicParser#expression.
    def enterExpression(self, ctx:VBasicParser.ExpressionContext):
        pass

    # Exit a parse tree produced by VBasicParser#expression.
    def exitExpression(self, ctx:VBasicParser.ExpressionContext):
        pass


    # Enter a parse tree produced by VBasicParser#var_.
    def enterVar_(self, ctx:VBasicParser.Var_Context):
        pass

    # Exit a parse tree produced by VBasicParser#var_.
    def exitVar_(self, ctx:VBasicParser.Var_Context):
        pass


    # Enter a parse tree produced by VBasicParser#varname.
    def enterVarname(self, ctx:VBasicParser.VarnameContext):
        pass

    # Exit a parse tree produced by VBasicParser#varname.
    def exitVarname(self, ctx:VBasicParser.VarnameContext):
        pass


    # Enter a parse tree produced by VBasicParser#varsuffix.
    def enterVarsuffix(self, ctx:VBasicParser.VarsuffixContext):
        pass

    # Exit a parse tree produced by VBasicParser#varsuffix.
    def exitVarsuffix(self, ctx:VBasicParser.VarsuffixContext):
        pass


    # Enter a parse tree produced by VBasicParser#varlist.
    def enterVarlist(self, ctx:VBasicParser.VarlistContext):
        pass

    # Exit a parse tree produced by VBasicParser#varlist.
    def exitVarlist(self, ctx:VBasicParser.VarlistContext):
        pass


    # Enter a parse tree produced by VBasicParser#exprlist.
    def enterExprlist(self, ctx:VBasicParser.ExprlistContext):
        pass

    # Exit a parse tree produced by VBasicParser#exprlist.
    def exitExprlist(self, ctx:VBasicParser.ExprlistContext):
        pass


    # Enter a parse tree produced by VBasicParser#sqrfunc.
    def enterSqrfunc(self, ctx:VBasicParser.SqrfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#sqrfunc.
    def exitSqrfunc(self, ctx:VBasicParser.SqrfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#chrfunc.
    def enterChrfunc(self, ctx:VBasicParser.ChrfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#chrfunc.
    def exitChrfunc(self, ctx:VBasicParser.ChrfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#lenfunc.
    def enterLenfunc(self, ctx:VBasicParser.LenfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#lenfunc.
    def exitLenfunc(self, ctx:VBasicParser.LenfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#ascfunc.
    def enterAscfunc(self, ctx:VBasicParser.AscfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#ascfunc.
    def exitAscfunc(self, ctx:VBasicParser.AscfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#midfunc.
    def enterMidfunc(self, ctx:VBasicParser.MidfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#midfunc.
    def exitMidfunc(self, ctx:VBasicParser.MidfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#pdlfunc.
    def enterPdlfunc(self, ctx:VBasicParser.PdlfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#pdlfunc.
    def exitPdlfunc(self, ctx:VBasicParser.PdlfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#peekfunc.
    def enterPeekfunc(self, ctx:VBasicParser.PeekfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#peekfunc.
    def exitPeekfunc(self, ctx:VBasicParser.PeekfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#intfunc.
    def enterIntfunc(self, ctx:VBasicParser.IntfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#intfunc.
    def exitIntfunc(self, ctx:VBasicParser.IntfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#spcfunc.
    def enterSpcfunc(self, ctx:VBasicParser.SpcfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#spcfunc.
    def exitSpcfunc(self, ctx:VBasicParser.SpcfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#frefunc.
    def enterFrefunc(self, ctx:VBasicParser.FrefuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#frefunc.
    def exitFrefunc(self, ctx:VBasicParser.FrefuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#posfunc.
    def enterPosfunc(self, ctx:VBasicParser.PosfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#posfunc.
    def exitPosfunc(self, ctx:VBasicParser.PosfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#usrfunc.
    def enterUsrfunc(self, ctx:VBasicParser.UsrfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#usrfunc.
    def exitUsrfunc(self, ctx:VBasicParser.UsrfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#leftfunc.
    def enterLeftfunc(self, ctx:VBasicParser.LeftfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#leftfunc.
    def exitLeftfunc(self, ctx:VBasicParser.LeftfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#rightfunc.
    def enterRightfunc(self, ctx:VBasicParser.RightfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#rightfunc.
    def exitRightfunc(self, ctx:VBasicParser.RightfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#strfunc.
    def enterStrfunc(self, ctx:VBasicParser.StrfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#strfunc.
    def exitStrfunc(self, ctx:VBasicParser.StrfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#fnfunc.
    def enterFnfunc(self, ctx:VBasicParser.FnfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#fnfunc.
    def exitFnfunc(self, ctx:VBasicParser.FnfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#valfunc.
    def enterValfunc(self, ctx:VBasicParser.ValfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#valfunc.
    def exitValfunc(self, ctx:VBasicParser.ValfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#scrnfunc.
    def enterScrnfunc(self, ctx:VBasicParser.ScrnfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#scrnfunc.
    def exitScrnfunc(self, ctx:VBasicParser.ScrnfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#sinfunc.
    def enterSinfunc(self, ctx:VBasicParser.SinfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#sinfunc.
    def exitSinfunc(self, ctx:VBasicParser.SinfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#cosfunc.
    def enterCosfunc(self, ctx:VBasicParser.CosfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#cosfunc.
    def exitCosfunc(self, ctx:VBasicParser.CosfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#tanfunc.
    def enterTanfunc(self, ctx:VBasicParser.TanfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#tanfunc.
    def exitTanfunc(self, ctx:VBasicParser.TanfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#atnfunc.
    def enterAtnfunc(self, ctx:VBasicParser.AtnfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#atnfunc.
    def exitAtnfunc(self, ctx:VBasicParser.AtnfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#rndfunc.
    def enterRndfunc(self, ctx:VBasicParser.RndfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#rndfunc.
    def exitRndfunc(self, ctx:VBasicParser.RndfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#sgnfunc.
    def enterSgnfunc(self, ctx:VBasicParser.SgnfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#sgnfunc.
    def exitSgnfunc(self, ctx:VBasicParser.SgnfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#expfunc.
    def enterExpfunc(self, ctx:VBasicParser.ExpfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#expfunc.
    def exitExpfunc(self, ctx:VBasicParser.ExpfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#logfunc.
    def enterLogfunc(self, ctx:VBasicParser.LogfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#logfunc.
    def exitLogfunc(self, ctx:VBasicParser.LogfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#absfunc.
    def enterAbsfunc(self, ctx:VBasicParser.AbsfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#absfunc.
    def exitAbsfunc(self, ctx:VBasicParser.AbsfuncContext):
        pass


    # Enter a parse tree produced by VBasicParser#tabfunc.
    def enterTabfunc(self, ctx:VBasicParser.TabfuncContext):
        pass

    # Exit a parse tree produced by VBasicParser#tabfunc.
    def exitTabfunc(self, ctx:VBasicParser.TabfuncContext):
        pass



del VBasicParser