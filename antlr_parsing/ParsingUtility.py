import sys
from antlr4 import *
from BooleanExprLexer import BooleanExprLexer
from BooleanExprParser import BooleanExprParser
from BooleanExprVisitor import BooleanExprVisitor
from EvaluationVisitor import EvaluationVisitor

class ParsingUtility:

    def __init__(self, variables=None):
        self.variables = variables

    def read_from_file(self, path):
        pass

    def parse(self, input):
        lexer = BooleanExprLexer(input)
        stream = CommonTokenStream(lexer)
        parser = BooleanExprParser(stream)
        tree = parser.compileUnit()
        ast = BooleanExprVisitor().visitCompileUnit(tree)
        value = EvaluationVisitor(self.variables).visit(ast)
        return value

def main(argv):
    while True:
        text = InputStream(input(">"))
        p = ParsingUtility()
        print('=', p.parse(text))

if __name__ == '__main__':
    main(sys.argv)