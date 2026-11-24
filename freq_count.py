def freq_count(nums):
    #create a blank dict 
    freq={}
    for num in nums:
        if num in freq:
            freq[num]=freq[num]+1
        else:
            freq[num]=1

    return freq

nums=[2,5,2,8,5,2]
print(freq_count(nums))