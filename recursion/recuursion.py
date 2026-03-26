def show(n):
    if( n==0): # base case 
                # stoppting condition 
        return
    print(n)
    show(n-1)
    
    
print("end")

show(5)