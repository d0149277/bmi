height = input('請輸入身高(公分): ')
weight = input('請輸入體重(公斤): ')
height = float(height)
weight = float(weight)
height = height/100
bmi = weight/(height*height)
print('bmi值', bmi)
if bmi < 18.5:
    print('過輕')
elif bmi >= 18.5 and bmi < 24:
    print('正常')
elif bmi >=24 and bmi < 27:
    print('輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('中度肥胖')
else:
	print('重度肥胖')