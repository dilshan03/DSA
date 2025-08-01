def bubble_sort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
            
        
A = []

for i in range(7):
    while(True):
        amount = float(input("Enter Expense for day:"))
        if (amount < 0):
            print("Enter positive integers")
            continue
        
        A.append(amount)
        break

bubble_sort(A)

total = sum(A)
average = total / 7
highest = A[-1]
lowest = A[0]

print("Expenses:", A)
print("lowest:", lowest)
print("highest:", highest)
print("Total:", total)
print("average:", average)
