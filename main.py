
from antlr4 import *
from VBasicLexer import VBasicLexer
from VBasicParser import VBasicParser
from VBasicVisitor import VBasicVisitor

print("VBASIC 1.0 - based on jvmBasic by Tom Everett")
input_text = input(">")
lexer = VBasicLexer(InputStream(input_text))
stream = CommonTokenStream(lexer)
parser = VBasicParser(stream)

tree = parser.line()
visitor = VBasicVisitor()

#print(stream.tokens)
print(tree.toStringTree(recog=parser))
visitor.visit(tree)
