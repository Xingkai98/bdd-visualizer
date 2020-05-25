import os
import filecmp, fileinput
import pickle

# 图片文件管理
class ImageFile:
    pass

# 状态文件管理
class StatusFile:

    def __init__(self, var_list=None, variables=None, h=None, w=None, expr=None):
        self.var_list = var_list
        self.variables = variables
        self.h = h
        self.w = w
        self.expr = expr

    def save(self, dir):
        data_list = [
            self.var_list,
            self.variables,
            self.h,
            self.w,
            self.expr
        ]
        with open(dir,'wb') as output_data:
            pickle.dump(data_list, output_data, pickle.HIGHEST_PROTOCOL)

    def read(self, dir):
        with open(dir,'rb') as input_data:
            data_list = pickle.load(input_data)
            self.var_list = data_list[0]
            self.variables = data_list[1]
            self.h = data_list[2]
            self.w = data_list[3]
            self.expr = data_list[4]

# 文件输入输出管理
class FileManager:
    pass