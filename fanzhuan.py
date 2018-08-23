#反转一个三位整数
#while True:
#	for a in range(100,1000):
		#print("你的输入正确")
               # break
#if a not in range(100,1000):
        # print('你的输入有误，请重新输入。')
	


def reservenumber(self,number):
	h = int(number/100)
	t = int(number%100/10)
	z = int(number%10)
	return (100*z+10*t+h)

