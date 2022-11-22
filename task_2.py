def fibonacci_sequence(n):
    result=[]
    a=0
    b=1
    if n== 0:
        return result
    if n==1:
        result.append(a)
        return result
    elif n==2:
        result.append(a)
        result.append(b)
        return result
    else:
        result.append(a)
        result.append(b)
        for i in range (2,n):
           c = a+b
           result.append(c)
           a = b
           b = c
        return result
