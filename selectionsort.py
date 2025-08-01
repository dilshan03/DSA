def selectionSort(A):
    n = len(A)
    for j in range(0, n):
        smallest = j
        for i in range(j+1, n):
            if A[i] < A[smallest]:
                smallest = i;
        A[j], A[smallest] = A[smallest], A[j]

A =[]

while(True):
    num = int(input("Enter numbers:"))
    if(num == -1):
        print("Program ended")
        break
    elif(num < 0):
        print("Enter a positive number")
        continue

    A.append(num)
    
print("before sorting",A)  
selectionSort(A)
print("after sorting",A)

highest = A[-1]
minimum = A[0]
calRange = A[-1] - A[0]

print(highest)
print(minimum)
print(calRange)

descending = sorted(A, reverse = True)
print(descending)

def cal_median(A):
    if(len(A) %2 == 0):
        return A[len(A) // 2] + A[(len(A) // 2 )-1] / 2
        
    else:
      return A[len(A) // 2]

print(cal_median(A))    
    

#desecending = sorted(A, reverse = True)
#print()
