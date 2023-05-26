import math
def dobro_tresN(n1):
        n2 = n1*2
        return n2
def elevado(n1,n2):
        n3 = n1**n2
        return n3
def string(n1):
        n2 = str(n1)
        return n2
def media(n1,n2,n3):
        n4 = (n1+n2+n3)/3
        print(n4)
def media2(n1,n2):
        n4 = (n1+n2)/2
        print(n4)
        if(n4 >= 6):
                print('Aluno aprovado')
        else:
                print('Aluno reprovado')
def mediaponde(n1,n2,n3):
        n5= n1+n2+n3
        n4 = n1/2 + n2/2 + n3/2
def coseno(n1):
    cos = math.cos(n1)
    return (cos)
def hipotenusa(a,b):
        hipotenusa = math.sqrt((a**2)+(b**2))
        print(f"{hipotenusa:.2f}")
def salario(a,b):
        sr = (a/100)*b
        a = a+sr
        print(a)
def volume(pi,r,alt):
        vol = pi*(r**2)*alt
        print(vol)
def quadrado(n1):
        print(n1**2)
def twocarac(c1):
        print('o usuário digitou:', c1[0],'&', c1[1])
def cessor(n1):
        print(n1 - 1, n1+1)

def perimetroarea(b,a):
        print('perímetro é:', (b*2)+(a*2))
        print('área é:', (b)*(a))
def jurossimples(v,ta,te):
        print('a prestação será de:', v+(v*(ta/100)*te))