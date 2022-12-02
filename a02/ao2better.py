class RPS:
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    VICTORY = 6
    DRAW = 3
    LOSS = 0


def winlose(elfrps, humanrps):
    if elfrps == humanrps:
        return humanrps + RPS.DRAW
    if (elfrps % 3) - humanrps == -1:
        return RPS.VICTORY + humanrps
    return RPS.LOSS + humanrps


def matchfix(elfrps, humancomand):
    match humancomand:
        case 1:
            return winlose(elfrps, (elfrps == 1 and 3 or elfrps - 1))
        case 2:
            return winlose(elfrps, elfrps)
        case 3:
            return winlose(elfrps, (elfrps == 3 and 1 or elfrps + 1))


def getRPS(var):
    tmpvar = []
    for i in var:
        match i:
            case 'X' | 'A':
                tmpvar.append(RPS.ROCK)
            case 'Y' | 'B':
                tmpvar.append(RPS.PAPER)
            case 'Z' | 'C':
                tmpvar.append(RPS.SCISSORS)
    return tmpvar


if __name__ == '__main__':
    inputfile = open('input', 'r')
    inputvalues = inputfile.readlines()
    inputfile.close()
    points = 0
    for line in inputvalues:
        line = getRPS(line.split())
        points += matchfix(line[0], line[1])
    print(points)
