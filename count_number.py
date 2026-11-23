def count_digits(n:int):
    # edge case 0 itselg has one digit 
    if n==0:
        return 1
    # handle negative number 
    n=abs(n)
    count=0

    # Keep chopping off the last digit until nothing is left
    while n>0:
        n=n//10
        count+=1
    return count

print(count_digits(-5783))



# n=5873
# result=len(str(abs(n)))
# print(result)