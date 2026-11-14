str="hey im learning python from appna college"
print(str.upper())# upper se hum ek string ke characters ko capital kar sakte hai, aur lower se hum ek string ke characters ko small kar sakte hai, aur ek naya string bana sakte hai.  
print(str.lower())# lower se hum ek string ke characters ko small kar sakte hai, aur ek naya string bana sakte hai.
print(str.endswith("college"))#with the endswith method, we can check if a string ends with a specific substring. It returns True if the string ends with the specified substring, and False otherwise. 
print(str.startswith("Hey"))# startswith se hum ek string ke starting characters ko check kar sakte hai, aur agar string uss characters se start hota hai to True return karta hai, otherwise False return karta hai.
print(str.count("a"))# count se hum ek string ke characters ki sankhya jaan sakte hai, aur ek integer value return karta hai.
print(str.find("python")) #find se hum ek string ke characters ko search kar sakte hai, aur uske index ko return karta hai, agar character nahi milta hai to -1 return karta hai.
print(str.replace("python","java")) # replace se hum ek string ke characters ko replace kar
print(str.capitalize()) # capitalize se hum ek string ke first character ko capital kar sakte hai, aur baaki characters ko small kar sakte hai.