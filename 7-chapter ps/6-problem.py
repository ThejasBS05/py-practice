#factorial using while loop
i = 1
ans = 1
n = int(input("Enter a number: "))
while (i <= n):
    ans *= i
    i += 1
print(ans)