# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Tool for healthcare professionals 
print(type(height))
print(type(weight))

w_height = float(height)
w_weight = float(weight)

BMI = int(w_weight / (w_height*w_height))
print(BMI)






