    ############# MUNDO 1 #############


xxx = input('Digite seu nome: ')

print('Bem vindo {}'.format(xxx))

#desafio 3
numero1 = int(input('Digite um número'))
numero2 = int(input('Digite outro número'))
soma = numero1+numero2
print('A soma de {} e {} é {}'.format(numero1,numero2,soma))

#desafio 4
algo = input('Digite algo:')
print(type(algo))
print('Oq vc digitou é printable? {}'.format(algo.isprintable()))
print('É um número? {}'.format(algo.isalnum()))



#desafio 5
numero = int(input('Digite um número:'))
print('O antecessor desse numero é {} e o sucessor é {}'.format(numero-1,numero+1))

#desafio 6
alg = int(input('Digite um numero:'))
print('O dobro desse núemro é {}, o triplo é {} e a raiz quadrada é {}'.format(alg*2,alg*3, int(alg**(1/2)) ) )

#desafio 7
nota1 = float(input('Digite sua primeira nota:'))
nota2 = float(input('Digite sua segunda nota'))
print('A sua média é {}'.format((nota1+nota2)/2))

#desafio 8
metros = float(input('Digite o valor em metros a ser convertido:'))
print(' o valor em centimetros é {}cm e em milimetros é {}mm'.format(metros*100,metros*1000))

#desafio 9
numero = int(input('Digite um numero inteiro que voce desaja ver a tabuada:'))
print('A tabuada desse número é:\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}'.format(numero*1,numero*2,numero*3\
            ,numero*4,numero*5,numero*6,numero*7,numero*8,numero*9,numero*10))

#desafio 10
reais = float(input('Quantos reais vc tem na carteira?'))
print('Voce pode comprar {} dolares'.format(reais//3.27))


#desafio 11
altura = float(input('Qual a altura da parede em metros?'))
largura = float(input('Qual é a largura dessa parede em metros?'))
print('vc vai precisar de {} litros de tinta '.format(round(altura*largura/2,2)))


#desafio 12
preço = float(input('Qual o preço atual do produto?'))
print('O preço desse produto com desconto é {}'.format(preço*0.95))

#desafio 13
salario=float(input('Digite seu salário atual'))
print('Seu salário com aumento de 15% é {}'.format(salario*1.15))

#desafio 14
celsius = float(input('Digite a temperatura em graus celsius'))
print('A temperatura {}°C equivale a {}°F'.format(celsius,celsius/5*9+32))

#desafio 15
km = float(input('Quantos quilometros você rodou com o carro?'))
dias = int(input('Por quantos dias o carro foi alugado?'))
print('Seu preço a pagar é R${}'.format(dias*60+km*0.15))


#desafio 16
num = float(input('Digite um numero'))
print(' A parte inteira do número {} é {}'.format(num,int(num)))

#desafio 17
import math
cateto1 = float(input('Digite o valor de um cateto'))
cateto2 = float(input('Digite o valor do outro cateto'))
hipot=math.hypot(cateto1,cateto2)
print('A hipotenusa é {}'.format(hipot))

#desafio 18
angulo = float(input('Digite um ângulo em graus'))
radiano=math.radians(angulo)
print('O seno de {:.2} é {:.2}, o cosseno é {:.2} e a tangente é {:.2}'.format(angulo, math.sin(radiano), math.cos(radiano), math.tan(radiano)))

#desafio 19
import random
a1 = str(input('Digite o nome de um aluno'))
a2 = str(input('Digite o nome de outro aluno'))
a3 = str(input('Digite o nome de outro aluno'))
a4 = str(input('Digite o nome de outro aluno'))
print('O aluno sorteado é {}'.format(random.choice([a1,a2,a3,a4])))

#desafio 20
a1 = str(input('Digite o nome de um aluno'))
a2 = str(input('Digite o nome de outro aluno'))
a3 = str(input('Digite o nome de outro aluno'))
a4 = str(input('Digite o nome de outro aluno'))
lista = [a1,a2,a3,a4]
random.shuffle(lista)
print('O ordem sorteada é {}'.format(lista))

#desafio 21
import pygame
pygame.init()
pygame.mixer.music.load('3-old-ways.mp3')
pygame.mixer.music.play()
input('Agora voce escuta?')
#n funfa

#desafio 22
nome = input("Escreva seu nome completo")
maiusculas = nome.upper()
minusculas = nome.lower()
num_de_letras = len(nome.replace(' ',''))
Nomes_separados = nome.split()
num_de_letras_primeiro_nome = len(Nomes_separados[0])
print('Seu nome em letras maiúsculas é {}, em minusculas é {}, ele tem {} letras e seu primeiro nome tem {} letras.'.format(maiusculas, minusculas, num_de_letras, num_de_letras_primeiro_nome))
print(maiusculas)

#desafio 23
numero =  str(input('Digite um número entre 0 e 10000'))
num = int(numero)
unidade = num % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10
print("""Seu número é {} e apresenta:
      unidade = {}
      dezena = {}
      centena = {}
      milhar = {}""".format(numero,unidade,dezena, centena, milhar))

#desafio 24
cidade = input('Digite o nome de sua cidade:')
cidade_minus = cidade.lower()
if 'santo' in cidade_minus[0:5]:
    print('Sua cidade tem nome de Santo')
else:
    print("Sua cidade não tem nome de Santo")

#desafio 25
nome = input('Digite o seu nome:')
nome_minus = nome.lower()
if 'silva' in nome_minus:
    print('Você faz parte da família Silva')
else:
    print("Você não faz parte da família Silva cuzão, vaza")

#desafio 26
frase = input('Digite uma frase')
frase_min = frase.lower().strip()
count = frase_min.count('a')
primeira = frase_min.find('a')
ultima = frase_min.rfind('a')
print('Sua frase contêm {} letras A e ela aparece pela primeira vez na posição {} e pela última vez na posição {}'.format(count,primeira+1,ultima+1))


#desafio 27
nome = input('Digite o seu nome completo')
Lista_de_nomes = nome.split()
primeiro = Lista_de_nomes[0]
ultimo = Lista_de_nomes[len(Lista_de_nomes)-1]
print('Seu primeiro nome é {} e seu último é {}'.format(primeiro,ultimo))


#desafio 28
import numpy as np
import random
lista  = np.arange(6)
numero = random.choice(lista)
adivinho = int(input('Adivinhe um número de 0 a 5'))
if adivinho == numero:
    print("Parabéns, você acertou!")
else:
    print('Você errou')

#desafio 29
velocidade = int(input('Escreva a velocidade do carro'))
if velocidade> 80:
    multa = (velocidade - 80) * 7
    print("o valor da multa é {} reais".format(multa))
else:
    print('Não há multa')

#desafio 30
numero  = int(input("Digite um número"))
if numero%2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

#desafio 31
km = int(input("Digite a quilometragem da viagem"))
if km<= 200:
    preço = km*0.50
else:
    preço = km * 0.45
print("o custo de combustível é {} reais".format(preço))

#desafio 32
ano = int(input("Escreva um ano"))
if ano%4 == 0 & ano%100 != 0 or ano%400 == 0:
    print("O ano é bissesto")
else:
    print('O ano não é bissesto')

#desafio 33
x = input("Digite um número")
y = input("Digite outro número")
z = input("Digite mais um número")
lista = [x,y,z]
lista_org = sorted(lista)
print("O maior número é {} e o menor é {}".format(lista_org[2],lista_org[0]))

#desafio 34
salario = int(input("digite seu salário"))
if salario>= 1250:
    print('O aumento do salário será {} reais'.format(salario*0.1))
else:
    print('O aumento do salário será {} reais'.format(salario * 0.15))

#desafio 35
x = int(input("Digite um lado do triângulo"))
y = int(input("Digite outro lado do triângulo"))
z = int(input("Digite mais um lado do triângulo"))
lista = [x,y,z]
lista_org = sorted(lista)
if lista_org[2] < (lista_org[0] + lista_org[1]):
    print("Esse triângulo existe")
else:
    print('Esse triângulo não existe')



print('\033[0;31;45mCarai')



############# MUNDO 2 #############

#desafio 36

valor = int(input("Digite o valor da casa "))
salario = int(input("Digite o salário do individuo "))
prazo = int(input("Digite o prazo do financiamento "))

prestacao = valor/prazo
if prestacao > salario*0.3:
    print("Emprestimo Negado")
else:
    print("Empréstimo aceito")

#desafio 37
numero = int(input("Digite um numero"))
base = int(input('''Digite 1 caso deseje que  a conversão seja em base binária,
                 2 para base octal e 3 para base hexadecimal'''))
if base == 1:
    print(bin(numero))
elif base == 2:
    print(oct(numero))
elif base == 3:
    print(hex(numero))
else:
    print('Digite um codigo adquado')


#desafio 38
num1 = int(input("Digite um numero"))
num2 = int(input("Digite outro numero"))
if num1 > num2:
    print('O primeiro número, {}, é maior'.format(num1))
elif num1 == num2:
    print('Os numeros são iguais')
elif num1 < num2:
    print('O segundo número, {}, é maior'.format(num2))


#desafio 39
import datetime
ano = int(input("Digite o ano em que você nasceu"))
idade = (datetime.datetime.now()).year - ano
if idade < 18:
    print("Ainda não tem idade para se alistar.")
elif idade == 18:
    print("Você deve se alistar esse ano.")
else:
    print("Você já deve ter se alistado.")

#desafio 40
nota1 =  float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota2 + nota1) / 2
if media < 5:
    print("REPROVADO")
elif 5 <= media and media < 7:
    print("RECUPERAÇÂO")
else:
    print("APROVADO")

#desafio 41
import datetime
ano = int(input("Digite o ano em que você nasceu: "))
idade = (datetime.datetime.now()).year - ano
if idade <= 9:
    print('mirim')
elif 9 < idade <= 14:
    print('infantil')
elif 14 < idade <= 19:
    print('junior')
elif 19 < idade <= 20:
    print('sênior')
else:
    print("master")


#desafio 42
x = int(input("Digite um lado do triângulo: "))
y = int(input("Digite outro lado do triângulo: "))
z = int(input("Digite mais um lado do triângulo: "))
lista = [x,y,z]
lista_org = sorted(lista)
if lista_org[2] < (lista_org[0] + lista_org[1]):
    print("Esse triângulo existe")
    if x == y == z:
        print("O triângulo é equilatero")
    elif x == y or y == z or z == x:
        print("O triânulo é isósceles")
    else:
        print("o triângulo é escaleno")
else:
    print('Esse triângulo não existe')


#desafio 43
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))
imc = peso/altura**2
if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc < 25:
    print("peso ideal")
elif 25 <= imc < 30:
    print("acima do peso")
elif 30 <= imc < 40:
    print('obesidade')
else:
    print("obesidade morbida")

#desafio 44
preço = float(input('Digite o valor normal: '))
print('''Formas de pagamento:
      [1] - cheque ou dinheiro
      [2] - à vista no cartão
      [3] - 2x no cartão
      [4] - 3x ou mais no cartão''')
condicao = int(input('Digite sua escolha: '))
if condicao ==1:
    print(preço*0.9)
elif condicao ==2:
    print(preço*0.95)
elif condicao ==3:
    print(preço)
elif condicao == 4:
    print(preço*1.2)

#desafio 45
import random
jogador = input("Escolha pedra, papel ou tesoura")
comput = random.choice(['pedra', 'papel', 'tesoura'])
if comput == 'pedra' and jogador == 'pedra' or comput == 'papel' and jogador == 'papel' or comput == 'tesoura' and jogador == 'tesoura':
    print("Empate")
elif comput == 'pedra' and jogador == 'tesoura' or comput == 'papel' and jogador == 'pedra' or comput == 'tesoura' and jogador == 'papel':
    print("o computador ganhou hehe")
else:
    print("você ganhou")



#desafio 46
import time 
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)
print("FOGOS!!")


#desafio 47

for i in range(1, 51):
    if i % 2 == 0:
        print(i)
print('fim')


#desafio 48
soma = 0
for i in range(1, 501):
    if i % 3 == 0 and i % 2 ==1:
        soma = soma + i
print(soma)

#desafio 49
import numpy as np
num = int(input("De que número você deseja a tabuada? "))
for i in np.arange(0, 11):
    print('{}x{} = {}'.format(num, i, num*i))


#desafio 50
soma = 0
for i in range(0, 6):
    x = int(input('Digite um numero: '))
    if x % 2 == 0:
        soma = soma + x
print(soma)


#desafio 51
prim = int(input("O primeiro termo da PA "))
razao =int(input("A razão da PA "))
for i in np.arange(0,11):
    x = prim + razao*i
    print(x)

#desafio 52
y = 0
n = int(input("Digite um numero: "))
for i in np.arange(2, n-1):
    if n % i == 0:
        y = y + 1 
if y == 0:
    print('{} é primo'.format(n))
else:
    print('{} não é primo'.format(n))

#desafio 53
frase = input("Digite uma frase: ")
frase1 = frase.replace(' ','').lower()
tamanho = len(frase1)
novo = ''
for i in np.arange(tamanho - 1, -1, -1):
    novo = novo + frase1[i]
if novo == frase1:
    print("A frase é um palíndromo")
else: 
    print("A frase não é um políndromo")
    
    
#desafio 54
import datetime
quant = 0
for i in range(0,7):
    ano = int(input("Ano de nascimento: "))
    if (datetime.datetime.now()).year - ano >= 18:
        quant = quant + 1
print("Há {} maiores de idade e {} menores.".format(quant, 7- quant))



#desafio 55
import  numpy as np
pesos = []
for i in range(0,5):
    peso = int(input("Peso: "))
    pesos = np.append(pesos, peso)
pesos.sort()
print("A pessoa mais magra tem {} e a mais gorda tem {}".format(pesos[0],pesos[4]))



#desafio 56
import pandas as pd
nomes = []
idades = []
sexos = []
for i in range(0,4):
    nome = input("digite o nome: ")
    idade = int(input("digite a idade: "))
    sexo = input("digite o sexo [m/f]: ")
    nomes = np.append(nomes, nome)
    idades = np.append(idades, idade)
    sexos = np.append(sexos, sexo)
print('A média das idades é {}'.format(np.mean(idades)))

df = pd.DataFrame().assign(Nome = nomes, Sexo = sexos, Idade = idades)
df1 = df.sort_values(by = 'Idade').reset_index(drop = True)
df2 = df1[(df1['Sexo'] == 'm')]
print('O homem mais velho é {}'.format(df2['Nome'][len(df2)]))

df_1 = df[(df['Sexo'] == 'f') & (df['Idade'] > float(20) )]
print('O número de mulheres com mais de 20 anos é {}'.format(len(df_1)))


#desafio 57
sexo = ''
while sexo not in ['M','F'] :
    sexo = input("Informe seu sexo (M ou F): ")
print('FIM')

#desafio 58
import random 
comp = random.choice(range(0,10))
jogador = -1
while comp != jogador:
    jogador = int(input('Digite um número de 0 a 9: '))
print('Acertou')

#desafio 59
sinal = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while sinal !=5:

        
    print('''        [1]somar
        [2]multiplicar
        [3]maior
        [4]novos números
        [5]sair do programa''')
    
    sinal = int(input('Digite sua escolha: '))
    if sinal == 1:
        print(n1+n2)
    elif sinal == 2:
        print(n1*n2)
    elif sinal == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(maior)
    elif sinal == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif sinal == 5:
        print('FIM')

#desafio 60
numero = int(input('digite um número'))
n = numero
fatorial = 0
while n != 1:
    numero = numero * (n-1)
    n = n - 1
print(numero)
    
    
    
#desafio 61
n = 0
prim = int(input("O primeiro termo da PA "))
razao = int(input("A razão da PA "))
while n != 10:
    x = prim + razao*n
    print(x)
    n = n+1
    
#desafio 62
n = 1
total = 0
mais = 10
prim = int(input("O primeiro termo da PA "))
razao = int(input("A razão da PA "))
while mais != 0:
    total = total + mais
    while n <= total:
        print(prim)
        prim = prim + razao
        n = n+1
    mais = int(input('Você quer mostrar mais quantos termos? '))
print('FIM')
    



#desafio 63
n = int(input('Quantos termos vc quer mostrar? '))
t1 = 0
t2 = 1
print(t1)
print(t2)
count = 3
while count <= n:
    t3 = t1 + t2
    print(t3)
    t1 = t2
    t2 = t3
    count = count + 1 


#desafio 64
numero = 0
soma = 0
while numero != 999:
    numero = int(input('Digite um número '))
    soma = soma + numero 
print(soma-999)


#desafio 65
numero = 0
sim_nao = 0
soma = 0
quant = 0
while sim_nao != 1:
    numero = int(input('Digite um número '))
    print('''[1] - Estou satisfeito
[2] - Mais um número''')
    sim_nao = int(input('Sua escolha: '))
    soma = soma + numero 
    quant = quant + 1
print(soma/quant)

#desafio 66
numero = 0
soma = 0
count = 0
while True:
    numero = int(input('Digite um número '))
    if numero == 999:
        break
    soma = soma + numero 
    count = count + 1
print(f'Você digitou {count} némeros, e a soma deles é {soma}')


#desafio 67


while True:
    i = 10
    num = int(input("De que número você deseja a tabuada? "))
    if num < 0:
        break
    else:
        while i != 0:
            print('{}x{} = {}'.format(num, i, num*i))
            i = i -1
    

#desafio 68
import random
import numpy as np
count = 0
while True:
    escolha = random.choice([0,1,2,3,4,5,6,7,8,9,10])
    par_impar = input('Par ou Ímpar? ')
    numero = int(input('Escolha um número: '))
    if par_impar == 'Par' and (escolha + numero)% 2 == 1:
        break
    elif par_impar == 'Ímpar' and (escolha + numero)% 2 == 0:
        break
    else:      
        count = count + 1
print(f'Você ganhou {count} vezes, eu escolhi o número {escolha}')
        


#desafio 69
import numpy as np
import pandas as pd
lista_idades = []
lista_sexos = []
print('-'*10, 'CADASTRAMENTO', '-'*10)
while True:
    idade = -1
    sexo = ' '
    cont = ' '
    while idade < 0:
        idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = (input('Sexo [M/F]: ')).upper()
    lista_idades = np.append(lista_idades, idade)
    lista_sexos = np.append(lista_sexos, sexo)
    while cont not in 'SN':
        cont = input('Quer continuar? [S/N] ' ).upper()
    if cont == 'N':
        break
df = pd.DataFrame()
df['idade'] = lista_idades
df['sexo'] = lista_sexos
homi = len(df.loc[df['sexo'] =='M'])
maiores = len(df.loc[df['idade'] >=18])
mulheres = len(df.loc[(df['sexo'] =='F') & (df['idade'] >= 20)] )
print(f'Há {homi} homens.')
print(f'Há {maiores} maiores de idade')
print(f'Há {mulheres} mulheres com menos de 20 anos')
    

#desafio 70
import numpy as np
import pandas as pd
lista_nomes = []
lista_preços = []
print('-'*10, 'LISTA DE COMPRAS', '-'*10)
while True:
    nome = (input('Nome do Produto:'))
    preço = int(input('Preço:'))
    lista_nomes = np.append(lista_nomes, nome)
    lista_preços = np.append(lista_preços, preço)
    cont = input('Quer continuar? [S/N]' ).upper()
    if cont == 'N':
        break
df = pd.DataFrame()
df['nome'] = lista_nomes
df['preço'] = lista_preços
gasto = sum(df['preço'])
maiores = len(df.loc[df['preço'] >=1000])
dfbarato = df.sort_values(by = 'preço')
barato = dfbarato['nome']
print(f'O total gasto foi {gasto}.')
print(f'Há {maiores} produtos que custam mais de 1000 reais')
print(f'O/A {barato[0]} é o produto mais barato')
    

#desafio 71


saque = int(input('Quanto deseja sacar? '))
cinquenta = saque//50
resto = saque % 50
vinte = resto//20
resto = resto%20
dez = resto//10
resto = resto % 10
um = resto//1

print(f'Serão sacadas {cinquenta} notas de 50, {vinte} notas de 20, {dez} notas de 10 e {um} notas de 1')





############# Mundo 3 #############

#desafio 72
n = -1
while n not in range(0,21):
    n = int(input("Digite um número entre 0 e 20: "))
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
print(f"Você digitou o número {tupla[n]}.")


#desafio 73
tupla = ('Corinthians', 'Palmeiras', 'São Paulo', 'Santos', 'Flamengo', 'Vasco', 'Fluminense', 'Botafogo')
print(f"Os 4 primeiros colocados são {tupla[0:4]}")
print(f"Os 4 últimos colocados são {tupla[-4:]}")
print(f'A ordem alfabetica dos times é: {sorted(tupla)}.')
pos = tupla.index('Corinthians')+1
print(f'O Corinthians está na {pos}ª posição.')



#desafio 74
import random
tuplinha = (random.randint(0,10), random.randint(0,10), random.randint(0,10), random.randint(0,10))
print(f'Foram sorteados os números: {tuplinha}')
print(f'O maior é : {sorted(tuplinha)[-1]}')
print(f'O menor é : {sorted(tuplinha)[0]}')


#desafio 75 

import numpy as np

tupla = (int(input("Digite um número: ")),  int(input("Digite um número: ")),  int(input("Digite um número: ")),  int(input("Digite um número: ")))

print(f'O número 9 aparece {tupla.count(9)} vez(es).')

não_tres = 0
for i in tupla:
    if i != 3:
        não_tres = não_tres+1
if não_tres != 0:
    print(f'O número 3 não foi digitado.')
else:
    print(f'O primeiro 3 aparece na posição {tupla.index(3)+1}.')

x=[]
for i in tupla:
    if i%2 ==0:
        x = np.append(x, i)
print(f'Os número pares são {x}.')


#desafio 76

a = int(input("Digite o nome do produto: "))
b = int(input("Digite o nome do produto: ))
c = int(input("Digite um número: "))
d = int(input("Digite um número: "))

tupla = (a, b, c, d)
print('-'*20,
      'LISTA DE PREÇOS',
      '-'*20)
###### ACABAR









































