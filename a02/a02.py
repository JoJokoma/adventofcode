def winlose(one, two):
    match one:
        case "A":
            if two == 'Y':
                return 8
            elif two == "X":
                return 4
            else:
                return 3

        case "B":
            if two == 'Z':
                return 9
            elif two == "X":
                return 1
            else:
                return 5
        case "C":
            if two == 'X':
                return 7
            elif two == "Z":
                return 6
            else:
                return 2
    return 0


def winlose2(one, two):
    match two:
        case "X":
            if one == 'A':
                return 3
            elif one == "B":
                return 1
            else:
                return 2

        case "Y":
            if one == 'A':
                return 4
            elif one == "B":
                return 5
            else:
                return 6
        case "Z":
            if one == 'A':
                return 8
            elif one == "B":
                return 9
            else:
                return 7
    return 0


if __name__ == '__main__':
    inputfile = open('input', 'r')
    inputvalues = inputfile.readlines()

    inputfile.close()
    points = 0
    for line in inputvalues:
        va = line.split()
        points += winlose(va[0], va[1])
    print(points)
