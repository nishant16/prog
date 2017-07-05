def fact(num):
    f=1
    for i in range(1,num+1):
        f=f*i
    print f

num=input("enter the no." )
a=fact(num)


class Box:
    def area(self):
        return self.width*self.height

    def __init__(self,width,height):
        self.width=width
        self.height=height

#Create an instance of Box
x= Box(10,2)

#print area
print(x.area())


