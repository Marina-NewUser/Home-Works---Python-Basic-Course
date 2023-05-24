my_dict = {"Uchenik_1":[7, 8, 9],
           "Uchenik_2":[10, 11, 12, 9, 10],
           "Uchenik_3":[6, 10, 11, 2, 12]}

def ser_znach (x):
    return sum(x)/len(x)
maximum  = ['', 0]
minimum = ['', 15]
for k, v in my_dict.items():
    if ser_znach(v)>maximum[1]:
        maximum[0], maximum[1] = k, ser_znach(v)
    if ser_znach(v)<minimum[1]:
        minimum[0], minimum[1] = k, ser_znach(v)

print(maximum)
print(minimum)
        
