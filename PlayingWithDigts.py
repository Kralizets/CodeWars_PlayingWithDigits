def dig_pow(n, p):
    digStr = str(n)
    sum = 0
    for dig in digStr:
        sum += pow(int(dig), p)
        p += 1

    res = sum / n
    if res.is_integer():
        return int(res)
    
    return -1

res1 = dig_pow(89, 1)
res2 = dig_pow(46288, 3)
res3 = dig_pow(92, 1)

print(res1)
print(res2)
print(res3)