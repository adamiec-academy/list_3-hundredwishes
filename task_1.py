def is_perfect(n):
    to_sum=[]
    perfect= False
    for i in range(1,n):
        if (n%i)==0:
            to_sum.append(i)
    if sum(to_sum) == n:
        perfect = True
    return perfect


def get_perfect_numbers (n):
    result=[]
    i=1
    while (len(result) != n):
        if is_perfect(i) == True:
            result.append(i)
        i +=1       
    return result

print(get_perfect_numbers(2))
