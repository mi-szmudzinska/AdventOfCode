with open(__file__.rstrip("Day5.py") + "input.txt") as f:
    ns = list(map(int, f.readline().strip().split(",")))


def run(input):
    p = list(ns)
    i = 0
    while True:
        xx = str(p[i]).zfill(5)
        opcode = int(xx[3:])
        mode1 = int(xx[2])
        mode2 = int(xx[1])
        p1 = p[i + 1] if int(xx[2]) else p[p[i + 1]]
        try:
            p2 = p[i + 2] if int(xx[1]) else p[p[i + 2]]
        except IndexError:
            pass
        if opcode == 1:
            p[p[i + 3]] = p1 + p2
            i += 4
        elif opcode == 2:
            p[p[i + 3]] = p1 * p2
            i += 4
        elif opcode == 3:
            p[p[i + 1]] = input
            i += 2
        elif opcode == 4:
            if p1 != 0:
                return p1
            i += 2
        elif opcode == 5:
            i = p2 if p1 != 0 else i + 3
        elif opcode == 6:
            i = p2 if p1 == 0 else i + 3
        elif opcode == 7:
            p[p[i + 3]] = int(p1 < p2)
            i += 4
        elif opcode == 8:
            p[p[i + 3]] = int(p1 == p2)
            i += 4


# Part one
print("Part 1:",run(1))

# Part two
print("Part 2:",run(5))