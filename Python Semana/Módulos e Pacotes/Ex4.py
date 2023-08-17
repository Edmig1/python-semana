from Pacotes.OpMat import celsius_farenheit, farenheit_celsius
esc = int(input('1-Celsius -> Farenheit\n2- Farenheit -> Celsius\n: '))
if esc == 1:
    temp = int(input('Diga a temperatura: '))
    celsius = celsius_farenheit(temp)
elif esc == 2:
    temp = int(input('Diga a temperatura: '))
    celsius = farenheit_celsius(temp)
