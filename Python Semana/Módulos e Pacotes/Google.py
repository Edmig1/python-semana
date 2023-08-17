from googletrans import Translator
tradutor = Translator()
texto = str(input('Digite o Texto: '))
ingles = tradutor.translate(texto, dest='en')
print('Texto em inglês:',ingles.text)