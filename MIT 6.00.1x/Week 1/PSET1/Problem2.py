#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' 
#occurs in s. For example, if s = 'azcbobobegghakl', 
#then your program should print
#Number of times bob occurs is: 2
s=input("Enter a string: ")
s2="bob"
y=0
z=0
for x in s:
    if x=="b":
        if s[y:y+3]==s2:
            z+=1
    y+=1
print ("Number of times bob occurs is: " + str(z))    