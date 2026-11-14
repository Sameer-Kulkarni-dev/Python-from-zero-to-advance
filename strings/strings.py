# str1='sam\teer' # the \t is an escape sequence that represents a tab character.
# str2="sameer"
# str3='''sameer'''
# str4="""sameer"""
# print(str1)

# the reason behind using different types of quotes is to allow the use of quotes within
#  the string without the need for escaping them. 
# For example, if we want to include a single quote in a string,
#  we can use double quotes to define the string, and vice versa. 
# This makes it easier to write strings that contain quotes without having to worry about escaping them.


# string concatination
# str1="sameer"
# str2="kumar"
# print(str1+str2) # string concatination se hum do string ko jod sakte hai, aur ek naya string bana sakte hai.
# print(str1*3) # string multiplication se hum ek string ko multiple times repeat kar sakte hai, aur ek naya string bana sakte hai.



# string length 
# str1="sameer"
# print(len(str1)) # string length se hum ek string ke characters ki sankhya jaan sakte hai, aur ek integer value return karta hai.
# len1=len(str1)
# print(type(len1)) # string length se hum ek string ke characters ki sankhya jaan sakte hai, aur ek integer value return karta hai.      


#INDEXING AND SLICING
str1="sameer"
print(str1[3]) # string indexing se hum ek string ke characters ko access kar sakte hai, aur ek naya string bana sakte hai.
print(str1[-1]) # string indexing se hum ek string ke characters ko access kar sakte hai, aur ek naya string bana sakte hai.

#string sclicing
print(str1[1:4])
print(str1[:4]) # string slicing se hum ek string ke characters ko access kar sakte hai, aur ek naya string bana sakte hai.
print(str1[2:]) # string slicing se hum ek string ke characters ko access kar sakte hai, aur ek naya string bana sakte hai.
print(str1[:]) # string slicing se hum ek string ke characters ko access kar sakte hai, aur ek naya string bana sakte hai.
print(str1[::2]) # string slicing se hum ek string ke characters ko access kar sakte hai, aur ek naya string bana sakte hai.
print(str1[1:5:2]) # string slicing se hum ek string ke characters ko access kar sakte hai, aur ek naya string bana sakte hai.
print(str1[0:len(str1)])
