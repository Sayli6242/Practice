# Find minimum and maximum element in an


def getMinMax(a, n):
    min = 100000000
    max = 0
    for i in a:
        if min > i:
            min = i
        if max < i:
            max = i
    return min, max


def main():
    T = int(input())
    while T > 0:
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])
        T -= 1


if __name__ == "__main__":
    main()
