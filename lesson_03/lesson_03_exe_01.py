x = int(input('Please give me a number:'))

if not x:
    print('Zero is neither even nor odd')
else:
    if(x%2):
        print('It is ODD!')
    else:
        print('It is EVEN!')
