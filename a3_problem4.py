# Find the missing string in O(N)

def compare_string(a, b):
    return a < b

def partition(C, start, end, pivot):
    i = start
    for j in range(start, end):
        if compare_string(C[j], pivot):
            temp = C[i]
            C[i] = C[j]
            C[j] = temp
            i += 1
    print("List of C after Comparing with Pivot: ", C)
    print("Index of pivot in C:", i)
    return i 

def find_missing(D, C, start, end, recursion):
    print("------Recursion {}------".format(recursion))
    if start == end:
        return D[start]
    mid = int((start + end) / 2)
    pivot = D[mid]
    print("pivot from D: ", pivot)
    i = partition(C, start, end, pivot)
    if C[i] == D[mid]:
        print("(C[i], D[mid]) = ({}, {})".format(C[i], D[mid]))
        print("Since two values are equal, the right side will be examined for the next round. \n")
        return find_missing(D, C, mid+1, end, recursion+1)
    else:
        print("(C[i], D[mid]) = ({}, {})".format(C[i], D[mid]))
        print("Since two values are not equal, the left side will be examined for the next round. \n")
        return find_missing(D, C, start, mid, recursion+1)

recursion = 1
C = ['Y', 'Z', 'W']
D = ['W', 'X', 'Y', 'Z']
print(find_missing(D, C, 0, len(D)-1, recursion))
