#Count how many vowels are in a given string.
string=input("Enter a string: ")
vowels="aeiouAEIOU" 
count=0
for char in string:
    if char in vowels:
        count+=1    
print("Number of vowels in the string:", count)