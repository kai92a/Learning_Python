#Assume s is a string of lower case characters.
#Write a program that counts up the number of vowels 
#contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:
#Number of vowels: 5

s=input("Enter a string")
x=len(s)
s2="aeiou"
z=0
for y in s:
    for a in s2:
        if y==a:
            z+=1
print ("Number of vowels: "+ str(z))