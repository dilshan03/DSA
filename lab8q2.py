def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def main():
    A = list(map(int, input("Enter numbers: ").split()))

    p = 0
    r = len(A) - 1
    pivot_index = partition(A, p, r)

    print("Partitioned array:", A)
    print("Pivot element is at index:", pivot_index)
    print("Pivot element is:", A[pivot_index])

main()
