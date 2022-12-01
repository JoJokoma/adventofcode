import numpy as np
if __name__ == '__main__':
    inputfile = open('input.txt', 'r')
    inputvalues = inputfile.readlines()
    value = np.array([0, 0, 0])
    inputfile.close()
    valuenow = 0
    for line in inputvalues:
        if line == '\n':
            if value[0] < valuenow:
                value[0] = valuenow
                value.sort()
            valuenow = 0
        else:
            valuenow += int(line)
    print(value.sum())

