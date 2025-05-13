def selectionSort(A):
    n = len(A)
    for j in range (0, n - 1):
        smallest = j
        for i in range (j + 1, n):
            if A[i] < A[smallest]:
                smallest = i
        A[j], A[smallest] = A[smallest], A[j]

def maxsize(A):
    maxsize = A[-1]
    #print("Maxsize", maxsize)
    return maxsize

def minsize(A):
    minsize = A[0]
    return minsize

def cal_range(A):
    result = A[-1] - A[0]
    return result

def median(A):
    if(len(A) % 2 == 0):
        median = (A[len(A) // 2] + A[(len(A) // 2) - 1]) / 2
    else:
        median = A[len(A) // 2]
    return median
    

A = []        

while(True):
    num = int(input("Enter integers : "))
    if (num == -1):
        print("Program ended")
        break
    elif (num < -1):
        print("Number should be positive")
        continue

    else:
        A.append(num)

print("Before sorting", A)
selectionSort(A)
print("After sorting", A)
maxsize(A)       
print("Maxsize", maxsize(A))
minsize(A)
print("Minsize", minsize(A))
cal_range(A)
print("Range",cal_range(A))
median(A)
print("Median", median(A))

descending = sorted(A, reverse=True)
print("Descending:", descending)

      

