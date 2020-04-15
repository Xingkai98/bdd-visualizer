import copy

class ListPermuter:

    def permute(self, input):
        self.result = []
        self.iterate([],input)
        return self.result

    def iterate(self, temp, input):
        if len(temp) == len(input):
            self.result.append(temp)
            return
        else:
            for i in input:
                if i not in temp:
                    tmp = copy.copy(temp)
                    tmp.append(i)
                    self.iterate(temp=tmp, input=input)

if __name__ == '__main__':
    lp = ListPermuter()
    print(lp.permute(['a','b','c']))

