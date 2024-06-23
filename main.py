
from antlr4 import *
from antlr.VBasicLexer import VBasicLexer
from antlr.VBasicParser import VBasicParser
from antlr.VBasicVisitor import VBasicVisitor

class VBasicInterpreter(VBasicVisitor):
    def __init__(self):
        self.runmode = 0    # 0=token/parse but don't execute, 1=execute
        self.program_linenumbers = []
        self.program_lines = {}
        self.program_text = {}
        self.currentLine = 0

    def processLine(self, input_text):
        lexer = VBasicLexer(InputStream(input_text))
        stream = CommonTokenStream(lexer)
        parser = VBasicParser(stream)
        tree = parser.typedline()
        line_number = self.visit(tree)
        if line_number != 0:
            if line_number in self.program_linenumbers:
                self.program_text[line_number] = input_text
            elif line_number in self.program_text:
                del self.program_text[line_number]

    def visitTypedline(self, ctx):
        c = ctx.getChild(0)
        if type(c) is VBasicParser.LinenumberContext:
            # Not Immediate mode, store the parsed line
            line_number = int(c.getText())
            if ctx.getChildCount() == 1:
                if line_number in self.program_lines:
                    print(f'Deleting Line {line_number}')
                    self.program_linenumbers.remove(line_number)
                    del self.program_lines[line_number]
            else:
                print(f'Storing Line {line_number}')
                self.program_linenumbers.append(line_number)
                self.program_linenumbers = sorted(set(self.program_linenumbers))
                self.program_lines[line_number] = ctx
            return line_number
        else:
            # Immediate mode
            print(f'Executing Immediate Mode Line')
            self.visitChildren(ctx)
            return 0
    
    def visitStatement(self, ctx):
        if ctx.getText().upper() == 'NEW':   # Probably Wrong
            self.program_linenumbers = []
            self.program_lines = {}
            self.program_text = {}
            return False    # ???
        else:
            return self.visitChildren(ctx)

    def printProgramState(self):
        print(self.program_linenumbers)
        print(self.program_lines)
        print(self.program_text)
    
class VBasicShell:
    def __init__(self) -> None:
        self.interp = VBasicInterpreter()

    def Start(self):
        print("VBASIC 1.0 - based on jvmBasic by Tom Everett")
        while True:
            input_text = input(">")
            self.interp.processLine(input_text)
            #self.interp.printProgramState()

shell = VBasicShell()
shell.Start()

"""
print("VBASIC 1.0 - based on jvmBasic by Tom Everett")
input_text = input(">")
lexer = VBasicLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = VBasicParser(stream)

tree = parser.typedline()
visitor = VBasicVisitor()

#print(stream.tokens)
print(tree.toStringTree(recog=parser))
visitor.visit(tree)


Need to lex, parse, and maybe store line
Need to interpret parsed line

"""
