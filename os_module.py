import os
print(os.getcwd())
#we can change cwd by os.chdir("C://")
# os.chdir("C://")
# print(os.getcwd())
# os.mkdir("os")
#os.makedirs("this/that")
#os.rename("does.txt","does2.txt")
#print(os.listdir())
#print(os.environ.get('path'))
# print(os.path.join('C:/',"//harry.txt"))
print("Sum of the number :-")
print("From :- ")
n1=int(input())
print("TO :- ")
n2=int(input())
sum=0
for i in range(n1,n2+1):
    sum+=i

print("Sum of the numbser is  :- ",sum)
