def is_armstrong(num:int):
    # Negative numbers are not Armstrong numbers
    if num<0:
        return False

    original_num=0

    # Count how many digits the number has (this is our power)
    power=len(str(num))
    total=0

    while num>0:
        last_digit=num%10
        total=total+(last_digit**power)

        # chop off the last digit
        num=num//10

        # Compare the backup copy with our final total
    if original_num==total:
        return True
    else:
        return False

print(is_armstrong(153))
print(is_armstrong(1634))
