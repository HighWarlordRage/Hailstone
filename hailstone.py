#Title: Project-4c

#Definig a Function:
def hailstone(a):
    start = 0

    while a != 1:
        if a % 2 == 0:
            a = a // 2
        else:
            a = 3 * a + 1
        start = start + 1
    return start

#answer = hailstone(1000)
#print(answer)