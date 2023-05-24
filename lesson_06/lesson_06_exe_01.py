def n_reg(n):
    return n.lower()
def v_reg(n):
    return n.upper()
print (n_reg(str('I like PyThon')))
print (v_reg(str('I like PyThon')))
a='I learn Python Basic Course'.split()
print(list(map(n_reg,a)))
print(list(map(v_reg,a)))
