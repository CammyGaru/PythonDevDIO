T = int(input())

for i in range(T):
    N, K = input().split(' ')
    N = int(N)
    K = int(K)
    if N > K:
        A = N // K
        B = N % K
        R = A + B
    else:
        R = N
    print(R)
