#反转一个只有3位数的整数。(Reverse a 3-digit integer)
#你可以假设输入一定是一个只有三位数的整数，这个整数大于等于100，小于1000。
#Example :123 反转之后是 321  900 反转之后是 9
def reservenumber(self,number):
    h = int(number/100)
    t = int(number%100/10)
    z = int(number%10)
    return (100*z+10*t+h)
