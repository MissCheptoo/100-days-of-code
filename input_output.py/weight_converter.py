weight = int(input("please enter your weight:"))
unit = input("convert weight to kg or lb?")
if unit == "kg":
        weightkg = weight/2.2
        print("weight in kg is :"+ str(weightkg))
else:
        weightlb = weight*2.2
        print("weight in lb is :"+ str(weightlb))
