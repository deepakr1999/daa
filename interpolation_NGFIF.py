import math
from numpy import interp
class Interpolation:
    values=[]
    y=[]
    del_array=[]
    temp=[]
    prev=[]
    h=0
    xp=0
    coef=0
    ans=0
    equation=""
    def __init__(self,l):
        self.values=l
        self.y=[i[1] for i in self.values]
        self.prev=self.y
        self.del_array.append(self.prev)
        while len(self.prev) !=2 :
            self.temp=self.prev
            self.prev=[]
            for i in range(len(self.temp)-1):
                self.prev.append(self.temp[i+1]-self.temp[i])
            self.del_array.append(self.prev)
        #
        # print("xp = ",self.values[1][0]," h = ",self.values[0][0])
        self.h=round(self.values[1][0]-self.values[0][0],4)



    def factorial(self,n):
        if n <= 1 :
            return 1
        else:
            return n*self.factorial(n-1)
    def combination(self,a,b):
        return self.factorial(a)/(self.factorial(b)*self.factorial(a-b))

    def find_for_value(self,x):
        #xp=p-x0/h
        self.xp=(x-self.values[0][0])/self.h
        print("xp = ",self.xp)
        print("h = ",self.h)
        for i,items in enumerate(self.del_array):
            self.equation+="xC{}*{} + ".format(int(i),round(items[0],5))
            self.coef=self.combination(self.xp,i)
            self.ans+=self.coef*items[0]



    def display(self):
        print("f(x) = ",self.equation,"\b\b\b",end="")
        print("       ")
        print("The anwer is : ",self.ans)

fib=[]
fib.append(1)
fib.append(1)
def fibonacci(n):
    c=0
    a=1
    b=1
    while(len(fib)<n+1):
        c=a+b
        a,b=b,c
        fib.append(c)

inp=""
l=[]
x=""
temp=[]
fibonacci(20)
print(fib)
print("==============INTERPOLATION USING NEWTON GREGORY FORWARD INTERPOLATION============")
op=int(input("Enter for\n1.Automated\n2.Manual\n"))
if(op==2):
    while 1:
        inp=input("Enter x y or done to exit : ")
        if inp=="done":
            break
        else:
            x=inp.split()
            l.append([float(x[0]),float(x[1])])
elif(op==1):
    temp=[1,1,2,3,5,8,13,21,34,55,89,144]
    l=[[i,fib[i-1]] for i in range(1,len(fib))]

print("The values are as follows : ")
for i in l:
    print(i)


i=Interpolation(l)
i.find_for_value(float(input("For what value of y : ")))
i.display()
