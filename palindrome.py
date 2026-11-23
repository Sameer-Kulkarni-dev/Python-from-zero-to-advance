def palindrome(num:int):
    # negative number cannot be palindrome
    if num<0:
        return False 

    original_num=num
    reversed_num=0
    while num>0:
        # Move 1: Grab the last digit
        last_digit=num%10
        # Move 2: Push old digits left and add the new digit
        reversed_num=reversed_num*10+last_digit  
                                                
        num=num//10

    # Compare the backup copy with the backwards number
    if original_num==reversed_num:
        return True
    else:
        return False

print(palindrome(123))
print(palindrome(121))



    