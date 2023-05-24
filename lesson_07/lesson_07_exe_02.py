my_dict = {
    'Student_1': {'P', 'J'},
    'Student_2': {'F_E', 'F_S'},
    'Student_3': {'P', 'F_E'},
    'Student_4': {'F_E'}
    }

b_E = {'P', 'J'}
for name, groups in my_dict.items():
    if len(groups)>1:
        print('2 or more groups: ', name, groups)
    if 'F_E' not in groups:
        print('no F_E: ', name, groups)
    if b_E & groups:
        print('b_E: ', name, groups)
