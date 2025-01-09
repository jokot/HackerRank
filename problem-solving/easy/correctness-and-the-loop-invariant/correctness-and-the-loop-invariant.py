

def insertion_sort(l):
    for i in range(1, len(l)):
        minIndex = i
        while (minIndex > 0) and (l[minIndex-1] > l[minIndex]):
           l[minIndex],l[minIndex-1] = l[minIndex-1],l[minIndex]
           minIndex -= 1
    return l

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))