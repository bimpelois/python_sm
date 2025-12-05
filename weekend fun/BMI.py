weight= int(input('enter integer'))
heigt= int(input('enter integer'))

bmi= height * height/weight
    print(bmi)

if weight < 18.5:
    print(underweight)

if weight <=18.5 and >=24.9:
    print(normal)

if weight <=25 and >=29.9:
    print(overweight)

else:
    print(obese)

