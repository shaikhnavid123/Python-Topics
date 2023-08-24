#practice of if, else, elif statements :
#Q. Take input from user about the age, show the prompt that, they are eligible or not for driving.

#######################################################################################

#Solution-01 :
print("What is your age? :")

min_age = 18
var0 = int(input())

if min_age<var0:
    print("You are eligible for driving vehicles")
elif min_age==var0:
    print("You are eligible for driving vehicles")
else :
    print("Sorry, You are not eligible for driving vehicles")

#######################################################################################

#Solution-02 :
print("What is your age :")
age = int(input())
if age<18:
    print("You cannot drive")

elif age==18:
    print("We will think about you")

else:
    print("You can drive")

#######################################################################################