def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1

        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1

        A[i +1] = key

def calculate_range(A):
    result = A[-1] - A[0]
    return result


def median(A):
    if(len(A) % 2 == 0):
        median = (A[len(A) // 2] + A[(len(A) // 2) - 1]) / 2
    else:
        median = A[len(A) // 2]
    return median
A = []

for i in range(9):
    num = int(input("mark:"))
    A.append(num)
insertionSort(A)    
    
        
print("Range is :", calculate_range(A))
print("Median is:", median(A))
    

    
    
