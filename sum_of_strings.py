def count(str):

    num = 0
    for d in str:
        if d.replace('-','').isdigit():
            num = num + (int)(d)
    return num

def count_recursive(str,num):
    if str[0].replace('-','').isdigit():
        num = num + (int)(str[0])

    if len(str) == 1:
        return num
    
    return count(str[1:len(str)],num)


str = ["spam500", "bungee", "10", "100swallow", "5", "okay", "25", "-5", "5", "100s", "hi", "-25"]

num = count(str)
print(num)
num = count_recursive(str)
print(num)
