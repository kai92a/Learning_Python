#Assume s is a string of lower case characters.
#Write a program that prints the longest substring of s 
#in which the letters occur in alphabetical order. 
#For example, if s = 'azcbobobegghakl', then your program should print
#Longest substring in alphabetical order is: beggh
#In the case of ties, print the first substring. For example, 
#if s = 'abcbcd', then your program should print
#Longest substring in alphabetical order is: abc
def F(x,y):
    if ord(x)<=ord(y):
        return (True)
    else:
        return(False)
s="rmfsntggmsuqemcvy"
a=0
s1=str()
w=bool()
while a<(len(s)-1):
    w=F((s[a]),(s[a+1]))
    if w==True:
        s1=s1+s[a]
        if a==len(s)-2:
            s1=s1+s[a+1]
        a+=1
    elif w==False:
        s1=s1+s[a]+" "
        a+=1
print(s1)
s2=str()
s3=str()
for x in s1:
    if x!=" ":
        s2=s2+x
    if x==" ":
        if len(s3) < len(s2):
            s3=s2
        s2=str()
if len(s3)>=len(s2):
    print (s3)
if len(s2)>len(s3):
    print (s2)
