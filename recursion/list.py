names=["sameer","pavan","abhi","annu","anirudh","vayu"]

def print_list(list , idx=0):
    if(idx == len(list)):  # stopping case or base case
        return
    print(list[idx])
    print_list(list , idx+1)  # everytime i call the func it should print the idx of list and incriment the the idx value 

print_list(names) # func call eplict to print the names 
