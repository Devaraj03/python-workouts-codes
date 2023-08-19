def add_my(n):
    if n == 1:
        return 1
    else:
        return n+add_my(n-1)
print(add_my(5))
