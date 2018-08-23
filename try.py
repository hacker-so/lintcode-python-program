
#1．有li = [1,2,3,4,5,6,7,8,8]能组成多少个互不相同且不重复的数字的两位数
li = [1,2,3,4,5,6,7,8,8]

result1 = []
result2 = []
for b in li :
	for c in li:
		if  b != c:
			d = b*10 +c      
			result1.append(d)
print(result1)
print(len(result1))

#请编写1 - 100 所有数的和
e = 0 
resultend = []
for f in range(0,101):
 	e += f
 	resultend.append(f)
 	print(resultend)

#b.实现用户输入用户名和密码，当用户名为 seven且密码为123时，显示登陆成功，否则登陆失败，失败时允许重复输入三次

error_num = 0
while True:
	username = input(" Please write your username")
	password = input(" Please write your password ")
	if username == 'seven' and password == '123':
	    print("signin successful")                                                                                                                                                                    
        break
    else:
    	print("signin fial")
    	error_num += 1
        if error_num ==3
        exit()
        else:
        	continue



