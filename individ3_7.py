import math
import sys

if __name__ == '__main__':
    for i in range(10, 100):
        if i % 2 != 0:
            a = []
            cout = 0
            srt = int(math.sqrt(i))
            for d in range(1, srt + 1):
                if i % d == 0:
                    a.append(d)
                    cout += 1
                    if d != i // d:
                        a.append(i // d)

            if cout % 2 != 0:
                summ = sum(a)
                print(i)
