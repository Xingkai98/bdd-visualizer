list = ['x1','x2','y1']
encoded_str = []
var_values = {}

def get_int_from_values(var_values):
    sum = 0
    p = len(var_values)-1
    for i in var_values:
        sum += var_values[i] * (2 ** p)
        p -= 1
    return sum

def get_values_of_vars(num):
    for i in list:
        var_values[i] = 0
    n = num
    while n:
        i = 0
        while 2**i<=n:
            i+=1
        i -= 1
        n -= 2**i
        var_values[list[i]] = 1

    s = ''
    for i in list:
        s += str(var_values[i])
    encoded_str.append(s)



if __name__ == '__main__':
    print(get_int_from_values({'x1': 1, 'x2': 1, 'y1': 0}))
