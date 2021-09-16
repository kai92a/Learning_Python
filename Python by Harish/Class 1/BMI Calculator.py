"""Program for BMI Calculation"""
Height = float(input("Height"))
print(Height)
Weight = float(input("Weight"))
print(Weight)
BMI = Weight*703//(Height*Height)
print(BMI)
if BMI >= 30:
    print("Fat")
elif BMI  >=20:
    print("Fit boy")
else:
    print("Try tomorrow after lossing few pounds")
    
print type
 
  