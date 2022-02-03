# Enter your code here. Read input from STDIN. Print output to STDOUT
def printEvenOdd(s):
    even = ''
    odd = ''
    for i in range(len(s)):
        if i%2 == 0:
            even += s[i]
        else:
            odd += s[i]
    print(even, odd)
            


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        s = input()
        printEvenOdd(s)
    