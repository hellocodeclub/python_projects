
def multiply(multiplicant, factor):
    result=0
    for index in range(1,abs(factor)+1):
        result = result + multiplicant

    if factor<0:
        return -result
    else:
        return result

print(" 20 x 5 = "+str(multiply(20,5)))
print(" -20 x 5 = "+str(multiply(-20,5)))
print(" 20 x -5 = "+str(multiply(20,-5)))
print(" -20 x -5 = "+str(multiply(-20,-5)))
print(" 20 x 0 = "+str(multiply(20,0)))

def todos_numeros_del_1_al_100():
    numeros = []

    for i in range(1,101):
        numeros.append(i)

    return numeros

print(todos_numeros_del_1_al_100())