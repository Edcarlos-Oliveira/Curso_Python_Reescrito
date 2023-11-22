import urllib
import urllib.request
from random import randint
from datetime import date

class Numeros:
    def __init__(self, dados):
        self.da = dados

    def getNumeros(self):
        for self.n in range(0, len(self.da)):
            self.num = int(input('Digite um Número: '))
            if 0 <= self.num <= 20:
                break
            print('Digite um número entre 0 e 20!')
        print(f'Você digitou o número: {self.da[self.num]}')

    def outra_maneira(self):
        while True:
            self.nr = int(input('Digite um número entre 0 e 20: '))
            if 0 <= self.nr <= 20:
                break
            print('Tente Novamente!')
        print(f'Você digitou o número: {self.da[self.nr]}')

    def vogais(self):
        for self.analise in self.da:
            print(f'\nNa palavra {self.analise.upper()} temos as vogais: ', end='')
            for self.vog in self.analise:
                if self.vog.lower() in 'aeiou':
                    print(f'{self.vog}', end=' ')
    
dados = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
         'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezanovo', 'Vinte')

class Brasileirao:
    def __init__(self, times):
        self.tm = times

    def getPosicao(self):
        print(f'Lista Times: {self.tm}\nOs 5 primeiros: {self.tm[:5]}\n'
              f'Os 4 últimos: {self.tm[15:]}\nTimes em ordem alfabética: {sorted(self.tm)}\n'
              f'O Corinthians está na {self.tm.index("Corinthians") + 1}ª posição.')

clubes = ('Palmeiras', 'Internacional', 'Fluminesse', 'Corinthians', 'Flamengo', 'Athletico Pr', 'Fortaleza', 'Sao Paulo', 'America MG',
          'Botafogo', 'Santos', 'Goias', 'Bragantino', 'Coritiba', 'Cuiaba', 'Ceara', 'Atletico Go', 'Avai', 'Juventude')

class Sorteio:
    def __init__(self):
        self.aleatorio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)) # Pode ser reescrito com loop

    def getSorteio(self):
        print('Números Sorteados: ', end='')
        for self.num in self.aleatorio:
            print(f'{self.num}', end=' ')
        print(f'\nO MAIOR é: {max(self.aleatorio)}\nO MENOR é: {min(self.aleatorio)}')

class Analisador:
    def __init__(self, p_num, s_num, t_num, q_num):
        self.n = (int(input(p_num)),
                  int(input(s_num)),
                  int(input(t_num)),
                  int(input(q_num)))

    def getAnalisador(self):
        print(f'Você digitou: {self.n}\nO número 10 apareceu {self.n.count(10)} vez(es)')
        if 5 in self.n:
            print(f'O número 5 apareceu na posição {self.n.index(5) + 1}ª posição.')
        else:
            print('O valor 5 não foi digitado em nenhuma posição!')
        print('Números Pares digitados: ', end='')
        for self.pares in self.n:
            if self.pares % 2 == 0:
                print(f'{self.pares}', end=' , ')

pri = 'Primeiro Número: '
seg = 'Segundo Número: '
ter = 'Terceiro Número: '
qua = 'Quarto Número: '

class Precos:
    def __init__(self, itens):
        self.it = itens
        print('-' * 40)
        print(f'{"Listagem de Preços" :^40}')
        print('-' * 40)

    def lista(self):
        for self.p in range(0, len(self.it)):
            if self.p % 2 == 0:
                print(f'{self.it[self.p]:.<30}', end='')
            else:
                print(f'R${self.it[self.p]:>7.2f}')
        print('-'*40)

lista = ['Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
         'Compasso', 9.99, 'Mochila', 120.00, 'Canetas', 22.30, 'Livro', 34.9]

class Dimensao:
    def __init__(self, p_texto):
        self.txt1 = str(input(p_texto))
                    
    def getLinhas(self):
        self.tam1 = len(self.txt1) + 4
        print('~' * self.tam1)
        print(f'  {self.txt1}')
        print('~' * self.tam1)

p_txt = 'Digite uma frase: '

class Votacao:
    def __init__(self, ano_nasc):
        self.an = int(input(ano_nasc))
        self.aa = date.today().year - self.an

    def votar(self):
        if 18 <= self.aa <= 65:
            print(f'Com {self.aa} anos, VOTO OBRIGATÓRIO.')
        elif 16 <= self.aa < 18 or self.aa > 65:
            print(f'Com {self.aa} anos, VOTO FACULTATIVO.')
        else:
            print(f'Com {self.aa} anos, NÃO VOTA.')

ano_nasc = 'Qual ano de nascimento [XXXX]? '

class Verificador:
    def __init__(self, verf_site):
        self.verf_s = str(input(verf_site))
        
    # Verifica se o site está disponível
    def getSite(self):
        try:
            self.site = urllib.request.urlopen(self.verf_s)
        except urllib.error.URLError:
            print('Site não está acessível!')
        else:
            print('Site está acessivel!')

site = 'Digite o site completo: '

# Chame aqui o objeto que quer executar
if __name__ == '__main__':
    obj = Verificador(site)
    obj.getSite()
