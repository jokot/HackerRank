# find median from array of numbers

def findMedian(arr):
    arr.sort()
    return(arr[len(arr)//2])

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    median = findMedian(arr)
    print(median)