def fact(n):
    if n == 0:
        return 1

    ans = n * fact(n-1)
    print(ans)
    return ans

fact(5)