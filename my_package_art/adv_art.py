def isprime(n):
    if n==2:
        return True
    for val in range(2,(n//2)+1):
        if n%val==0:
            return False
    return True
