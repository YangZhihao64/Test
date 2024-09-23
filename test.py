import re

# print ("hello world")
# print ("First Change")
# '''
# firstname = input("Enter your first name: ")
# lastname = input("Enter your last name: ")
#
# fullname = firstname[0] + lastname[0]
#
# print (fullname)
# '''
# Sentence = "good morning my neighbors"
# Number = 2
# Float = 5.2
#
# print ("I say : %s, Integer is : %d , Float is : %.1f"%(Sentence, Number, Float))

#X = re.split("\s", Sentence, 2)
#X = re.sub("\s","0",Sentence)

#print(Sentence.upper())
#print(Sentence.lower())

#print ("no space on both side: " + Sentence.strip())
#print ("no hello in sentence: " + Sentence.lstrip("hello"))
#print ("no world in sentence: " + Sentence.rstrip("world"))


# def add(x,y = 5):
#     s = x+y
#     print(s)
#
#
# add(3,3)




class Employee:
    status = "current employee"

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def info(self):
        print("Name:",self.name,"Age:", self.age,"Gender:", self.gender)

class PartTimeEmployee(Employee):
    def GetHours(self,hours):
        print("{} work for {} hours a day".format(self.name,hours))


yzh = PartTimeEmployee("yzh",23,"male")
yzh.info()
yzh.GetHours(8)










