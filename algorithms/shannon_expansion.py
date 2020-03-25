from ParsingUtility import *
from binary import *
class BoolExprToINF:

    variables = {}
    var_list = []
    result_table = {}

    INF_list = []

    def __init__(self, var_list, default_var='t'):
        self.var_list = var_list
        self.default_var = default_var
        self.generate_result_table()

    def generate_inf_list(self):
        self.create_inf(a='',current_var=self.var_list[0])

    def create_inf(self, a='', current_var=None):
        # 推导current_var为0或1的两种情况，填入b1和b2

        inf = INFExpr(a=a,current_var=current_var,b1='',b2='')

        # 继续递归调用b1和b2，若b1以及b2都为0或1则退出

    # '{'x1'=1,x2=0' ==> '10'
    def get_value_str(self, variables):


    def generate_result_table(self):
        pass


class INFExpr:

    def __init__(self, t='t', a='', current_var=None, b1='', b2='',
                 tree_position=None):
        self.t = t
        self.a = str(a)
        self.new_var = str(current_var)
        self.b1 = str(b1)
        self.b2 = str(b2)
        self.tree_position = tree_position

    def to_str(self):
        return self.t + self.a + ' = ' + self.new_var + ' -> ' + \
               self.t + self.b1 +',' + self.t + self.b2

if __name__ == '__main__':
    inf = INFExpr(current_var='x1',b1='1',b2='0')
    b = BoolExprToINF()
    print(inf.to_str())