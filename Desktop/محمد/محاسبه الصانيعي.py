str_lenght =input("please enter lenght \n")
str_width = input("please enter width \n")
str_meter = input("how much for 1 meter \n")
lenght = float(str_lenght)
width = float(str_width)
meter = float(str_meter)
area = lenght+width
price = meter*area
print("the total area is " + str (area))
print("give to the guy $" +  str (price))