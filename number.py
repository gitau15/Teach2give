#Power of Two
def checkNum(num):
    if num<=0:
        return False
    return(num & (num - 1)) ==0

usernum = int(input("Enter an integer: "))
result =checkNum(usernum)
print(f"{usernum} is a power of two:{result}")