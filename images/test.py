def solution(M, A):
    N = len(A)
    count = [0] * (M + 1)
    maxOccurence = 1
    index = -1
    for i in range(N):
        if count[A[i]] > 0:
            tmp = count[A[i]] + 1
            if tmp > maxOccurence:
                maxOccurence = tmp
                index = i
            count[A[i]] = tmp
        else:
            count[A[i]] = 1
    return A[index]


M = 3
A = [2, 1, 1, 2, 3, 3, 3, 1, 1]
##A = [1, 2, 3, 3, 1, 3, 1]
#A = [2]

print(solution(M,A))