import math
import  sys

if __name__ == '__main__':
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))

    if a != 0:
        d = math.pow(b,2) - 4 * a * c
        print(f"d = {d}")
        if d < 0:
            x = -b / (2 * a)
            print(f"x1 = {x}")
            print(f"x2 = {-x}")

        else:
            x1 = -b - math.sqrt(d) / (2 * a)
            x2 = -b + math.sqrt(d) / (2 * a)
            x3 = -x1
            x4 = -x2
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
            print(f"x3 = {x3}")
            print(f"x4 = {x4}")

    else:
        print("Действительных корней нет", file=sys.stderr)
        exit(1)