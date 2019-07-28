def addthree(a, b, c):
    added = a + b + c
    return added

def addminusthree(x, y, z):
    addminus = x + y - z
    return addminus

def minusaddthree(d, e, f):
    minusadd = d - e + f
    return minusadd

x1 = addthree(1, 1, 1)
x2 = addminusthree(1, 2, 1)
x3 = minusaddthree(4, 4, 1)

print('Program1:',x1,x2,x3)

print('Program2:')
def greet(lang):
    if lang == 'eng' :
        return 'Hello'
    elif lang == 'spa' :
        return 'Hola'
    elif lang == 'jap' :
        return 'Konichiwa'
    else :
        return 'Whats up'
print(greet('eng'),'Jordan')
print(greet('spa'),'Jordan')
print(greet('jap'),'Jordan')
print(greet('som'),'Jordan')
