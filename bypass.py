from random import*

acho = ''
senha = input("Digite a senha: ")
letras =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', "'", '"', ',', '.', '<', '>', '/', '?', '|', '\\', '`', '~', ' ']

while (acho!=senha):
    acho = ""
    for letra in senha:
        acholetras = letras[randint(0, 49)]
        acho = str(acholetras)+str(acho)
    
    print (acho)
print (" A senha encontarda foi: ", acho)
