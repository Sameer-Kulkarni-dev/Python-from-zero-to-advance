def find_factors(n:int):
    factors=[]
    # range(1, n + 1) checks every number from 1 up to n
    for i in range(1,n+1):
        if n%i==0:
            factors.append(i)
    return factors

print(find_factors(36))