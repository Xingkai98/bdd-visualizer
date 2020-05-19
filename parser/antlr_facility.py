import sys
from antlr4 import *
from BooleanExprLexer import BooleanExprLexer
from BooleanExprParser import BooleanExprParser
from BooleanExprVisitor import BooleanExprVisitor
from evaluation_visitor import EvaluationVisitor

# 对Antlr生成的代码进行封装

class AntlrFacility:
    # 返回 True 或 False (bool type)
    def get_parse_result(self, text, variables):
        antlr_input = InputStream(text)
        lexer = BooleanExprLexer(antlr_input)
        stream = CommonTokenStream(lexer)
        parser = BooleanExprParser(stream)
        tree = parser.compileUnit()
        ast = BooleanExprVisitor().visitCompileUnit(tree)
        value = EvaluationVisitor().visit(node=ast, variables=variables)
        return value

    # 返回变量列表
    def get_variable_list(self, text):
        antlr_input = InputStream(text)
        lexer = BooleanExprLexer(antlr_input)
        stream = CommonTokenStream(lexer)
        parser = BooleanExprParser(stream)
        tree = parser.compileUnit()
        ast = BooleanExprVisitor().visitCompileUnit(tree)
        value = EvaluationVisitor().visit_for_var_list(node=ast)

        # 更新self.variables，默认设置为False
        self.variables = {}
        for i in value:
            self.variables[i] = False

        return value

def main(argv):
    while True:
        text = str(InputStream(input(">")))
        p = AntlrFacility()
        print('=', str(p.get_variable_list(text)))

if __name__ == '__main__':
    main(sys.argv)