number=[[1,2],[4,5]]
max_value=number[0][0]
min_value=number[0][0]
for i in range(len(number)):
    for j in range(len(number[i])):
        num=number[i][j]
        if max_value <num:
            num=max_value
        if min_value >num:
            num=min_value
max_value
min_value