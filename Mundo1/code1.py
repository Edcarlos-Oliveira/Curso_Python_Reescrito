import math
import random
import pygame 
from time import sleep
from datetime import date

class Tipos_Primitivos:
    def __init__(self, dados, flutuante, boleano):
        self.d = input(dados)
        self.f = float(input(flutuante))
        self.b = bool(input(boleano))
    
    def getTp(self):
        return(f'Foi digitado: {self.d}\n\
                Tipo Primitivo de {self.d} é: {type(self.d)}\n\
                Tem espaços: {self.d.isspace()}\n\
                É um número? {self.d.isnumeric()}\n\
                É alfabetico? {self.d.isalpha()}\n\
                É alfanumerico? {self.d.isalnum()}\n\
                Está em maiusculo: {self.d.isupper()}\n\
                Está em minusculo: {self.d.islower()}\n\
                Alguma letra em maiusculo: {self.d.istitle()}\n\
                Número digitado: {self.f}\n\
                Tipo de {self.f} é: {type(self.f)}\n\
                Valor digitado: {self.b}\n\
                Tipo de {self.b} é: {type(self.b)}')

tipos = ('Digite algo: ', 'Digite um número com ponto: ', 'Digite outro valor: ')

class Numeros:
    def __init__(self, numero):
        self.num = int(input(numero))
        
    def sucessor_antecessor(self):
        return(f'O sucessor de {self.num} é: {self.num + 1}\nO antecessor de {self.num} é: {self.num - 1}')

    def operacoes_matematicas(self):
        return(f'O dobro de {self.num} é: {self.num * 2}\nO triplo é: {self.num * 3}\nA raiz quadrada é: {self.num ** (1/2)}')

    def tabuada(self):
        self.c = 1
        while self.c <= 10:
            res = self.num * self.c
            print(f'A tabuada de {self.num} x {self.c} = {res}')
            self.c += 1

    def parte_inteira(self):
        self.p_int = float(self.num)
        return(f'A parte inteira de {self.p_int} é: {trunc(self.p_int)}')   # 'trunc' retorna a parte inteira do número

    def separador(self):
        return (f'O número digitado foi: {self.num}\n'
                f'Unidade: {self.num // 1 % 10}\n'
                f'Dezena: {self.num // 10 % 10}\n'
                f'Centena: {self.num // 100 % 10}\n'
                f'Milhar: {self.num // 1000 % 10}')

    def advinhar(self):
        self.pensei = random.randint(0,5)
        print('Processando....')
        sleep(3)
        if self.pensei == self.num:
            print('PARABENS! você acertou!')
        else:
            print(f'ERROU! pensei no número: {self.pensei}')

    def par_impar(self):
        if self.num % 2 == 0:
            print(f'O número {self.num} é PAR!')
        else:
            print(f'O número {self.num} é IMPAR!')

    def verificar_ano(self):
        '''
        Se o ano for divisível por 4 e tiver resto 0,
        e divisível por 100 tiver resto diferente de 0,
        Ou divisivel por 400 tiver resto igual a 0.

        '''
        if self.num == 0:
            self.num = date.today().year # Pega a data do sistema atual
        if self.num % 4 == 0 and self.num % 100 != 0 or self.num % 400 == 0:
            print(f'O Ano {self.num} é BISSEXTO!')
        else:
            print(f'O Ano {self.num} NÃO é BISSEXTO!')

    def maior_menor(self):
        self.n2 = int(input('Digite outro número: '))
        self.n3 = int(input('Digite o último número: '))
        
        # Verificando o MENOR
        self.menor = self.num
        if self.n2 < self.num and self.n2 < self.n3:
            self.menor = self.n2
        if self.n3 < self.num and self.n3 < self.n2:
            self.menor = self.n3

        # Verificando o MAIOR
        self.maior = self.num
        if self.n2 > self.num and self.n2 > self.n3:
            self.maior = self.n2
        if self.n3 > self.num and self.n3 > self.n2:
            self.maior = self.n3
        print(f'O MENOR número é: {self.menor}')
        print(f'O MAIOR número é: {self.maior}')

num = 'Digite um número: '

class Medias:
    def __init__(self, num1, num2):
        self.n1 = float(input(num1))
        self.n2 = float(input(num2))

    def media(self):
        return (f'A média entre {self.n1} e {self.n2} é igual a: {(self.n1 + self.n2)/2}')

    def area(self):
        return(f'A área total é: {self.n1 * self.n2:.2f} m² vai precisar de {(self.n1 * self.n2)/2:.1f} litros de tinta.')

    def aluguel(self):
        self.dias = int(self.n1)
        self.km = self.n2
        return(f'Custo dia: {self.dias * 60}\nCusto km: {self.km * 0.15}\nTotal a pagar: {(self.dias * 60) + (self.km * 0.15)}')

    def triangulo_retangulo(self):
        return(f'A hipotenusa do triângulo é: {math.sqrt((self.n1 ** 2) + (self.n2 ** 2)):.2f}')

    def verificador_triangulo(self):
        '''
        Condição de existência de um TRIÂNGULO:
        A soma de dois lados devem ser sempre menor que o terceiro
        '''
        self.n3 = float(input('Digite terceiro número: '))
        if self.n1 < self.n2 + self.n3 and self.n2 < self. n1 + self.n3 and self.n3 < self.n1 + self.n2:
            print('Os valores FORMAM um triângulo!')
        else:
            print('Os valores NÃO FORMAM um triângulo!')

pri_num = 'Digite primeiro número: '
seg_num = 'Digite segundo número: '

class Conversor:
    def __init__(self, valor):
        self.vl = float(input(valor))

    def metro(self):
        return(f'O valor de {self.vl} metro(s) equivale a: {self.vl * 100:.0f} centimetros e {self.vl * 1000:.0f} milimetros')

    def reais(self):
        return (f'Valor de R${self.vl:.2f} convertido em US$ é: {self.vl/5.15:.2f}')

    def celsius(self):
        return(f'A temperatura de {self.vl} °C, equivale a {self.vl * 1.8 + 32} °F')

    def fahren(self):
        return(f'A temperatura de {self.vl} °F, equivale a {(self.vl - 32) / 1.8} °C')

    def descPorcentagem(self):
        return(f'O valor do produto com 5% off é: R${self.vl - (self.vl * 5/100):.2f}')

    def aumentoSalario(self):
        return(f'Sálario de R${self.vl:.2f} com 15% de aumento é: {self.vl + (self.vl * 15/100):.2f}')

    def salario_condicao(self):
        self.reaj10 = self.vl + (self.vl * 10/100)
        self.reaj15 = self.vl + (self.vl * 15/100)
        if self.vl > 1250:
            print(f'Seu novo sálario é R${self.reaj10:.2f}')
        else:
            print(f'Seu novo sálario é R${self.reaj15:.2f}')

    def angulos(self):
        return(f'Seno: {math.sin(math.radians(self.vl))}\nCosseno: {math.cos(math.radians(self.vl))}\nTangente: {math.tan(math.radians(self.vl))}')

    def velocidade(self):
        self.km = (self.vl - 80) * 7
        if self.vl > 80:
            print(f'Você ULTRAPASSOU a velocidade permitida de [80 km/h] será multado em R${self.km:.2f} ')
        else:
            print('PARABÉNS! continue dirigindo com segurança!')

    def preco_viagem(self):
        self.vl1 = self.vl * 0.50
        self.vl2 = self.vl * 0.45
        if self.vl <= 200:
            print(f'O preço da sua viagem é: R${self.vl1:.2f}')
        else:
            print(f'O preço de sua viagem é: R${self.vl2:.2f}')

valor = ('Digite um valor: ')

class Seletor:
    def __init__(self, nome):
        self.lista_nomes = list()
        c = 1
        while c <= 4:
            self.nome = str(input(f'{c}º {nome}')).strip()
            self.lista_nomes.append(self.nome)
            c += 1

    def sorteio(self):
        self.dados = self.lista_nomes
        self.sorteio = random.choice(self.dados)
        return (f'Entre os nomes, o sorteado foi o: {self.sorteio}')

    def embaralhar(self):
        self.dados2 = self.lista_nomes
        random.shuffle(self.dados2)
        return (f'Ordem de apresentação: {self.dados2}')

    def analisar_texto(self):
        obj.sorteio()
        self.nome = (self.sorteio.split())
        print(f'O nome a analisar é: {self.sorteio}')
        print(f'Em MAIUSCULO é: {self.sorteio.upper()}')
        print(f'Em MINUSCULO é: {self.sorteio.lower()}')
        print(f'Quantidade SEM espaços é {len(self.sorteio) - self.sorteio.count(" ")}')
        print(f'Quantidade COM espaços é: {len(self.sorteio)}')
        print(f'O nome: {self.sorteio} e a letra ["A"] aparece {self.sorteio.upper().count("A")} vez(s)!')
        print(f'O nome {self.sorteio} tem a primeira letra ["A"] na posição {self.sorteio.upper().find("A") + 1}') # Procura da direita para esquerda(contagem sempre 1 a menos)
        print(f'O nome {self.sorteio} a ultima letra ["A"] na posição {self.sorteio.upper().rfind("A") + 1}') # Procura da esquerda para direita
        print(f'Primeiro nome é: {self.nome[0]} e tem {len(self.nome[0])} letras.')
        print(f'Último nome é: {self.nome[len(self.nome) - 1]} e tem {len(self.nome[len(self.nome) - 1])} letras')

    def analisar_condicao(self):
        if self.nome[:5].upper() == 'PEDRO':
            print(f'Temos: {self.nome} na última posição!')
            if 'SILVA' in self.nome.upper():
                print(f'Seu nome é {self.nome} e tem [SILVA]!')
            else:
                print(f'O nome é [PEDRO] e não tem [SILVA]!')
        else:
            print(f'Nenhum [PEDRO] na última posição, temos: {self.nome}!')

nome = ' Nome: '

class Leitor:
    def __init__(self, arqMp3):
        self.mp3 = arqMp3
        
    def getMp3(self):
        pygame.mixer.init()
        pygame.init()
        pygame.mixer.music.load(self.mp3)
        pygame.mixer.music.play()
        pygame.event.wait(timeout=True)
        print('Ouçam o som do MP3...')
        sleep(3)

arq = 'Mundo1\Teclado.mp3'

if __name__ == '__main__':
    # Crie aqui o objeto e chame a função
    obj = Leitor(arq)
    obj.getMp3()