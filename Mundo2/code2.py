from random import randint
from datetime import date
from time import sleep
from math import factorial

class Simulador:
    def __init__(self, valor, renda, parcela):
        self.vl = float(input(valor))
        self.rnd = float(input(renda))
        self.pcl = int(input(parcela))

    def emprestimo(self):
        self.parcela_mensal = self.vl / (self.pcl * 12)
        self.limite_parcela = self.rnd * 30 / 100

        if self.parcela_mensal <= self.limite_parcela:
            print(f'PARABÉNS! Financiamento aprovado com parcelas de: R${self.parcela_mensal:.2f}')
        else:
            print(f'NEGADO! Parcela de: R${self.parcela_mensal:.2f} excede 30% da sua renda.')

v = 'Qual o valor? '
r = 'Qual o salario? '
qtd = 'Quantos anos? '

class Conversor:
    def __init__(self, numero, conversor):
        self.num = int(input(numero))
        print('Escolha uma opção:\n'
              '[1] para BINÁRIO\n'
              '[2] para OCTAL\n'
              '[3] para HEXADECIMAL')
        self.con = int(input(conversor))
        
    def base_numericas(self):
        if self.con == 1:
            print(f'Valor {self.num} em BINÁRIO: {bin(self.num)[2:]}') #'[2:]' Elimina as posições 1 e 2
        elif self.con == 2:
            print(f'Valor {self.num} em OCTAL: {oct(self.num)[2:]}')
        elif self.con == 3:
            print(f'Valor {self.num} em HEXADECIMAL: {hex(self.num)[2:]}')
        else:
            print('Opção INVÁLIDA, escolha um número entre 1 e 3.')

n = 'Qual número? '
op = 'Qual opção? '

class Comparador:
    def __init__(self, numero1, numero2):
        self.n1 = int(input(numero1))
        self.n2 = int(input(numero2))

    def numeros(self):
        if self.n1 > self.n2:
            print(f'PRIMEIRO número é o MAIOR!')
        elif self.n1 == self.n2:
            print('Não existe MAIOR os dois são IGUAIS!')
        else:
            print('SEGUNDO número é o MAIOR!')

p1 = 'Primeiro Número: '
s2 = 'Segundo Número: '

class Verificador:
    def __init__(self, data):
        self.dt = int(input(data))

    def alistamento(self):
        self.ano_atual = date.today().year - self.dt
        self.tempo_falta = 17 - self.ano_atual
        self.ano_alistar = self.dt + self.ano_atual + self.tempo_falta
        self.tempo_passou = self.ano_atual - 18
        self.ano_passou = self.dt + self.ano_atual - self.tempo_passou

        if self.ano_atual <= 17:
            print(f'Ainda não é a hora do alistamento, falta {self.tempo_falta} ano(s)\n'
                  f'O ano do alistamento é {self.ano_alistar}')
        elif self.ano_atual == 18:
            print('Chegou a hora do alistamento!')
        else:
            print(f'Perdeu o prazo do seu alistamento em {self.tempo_passou} anos\n'
                  f'O ano que deveria ter se alistado era {self.ano_passou}')

    def classf_atletas(self):
        self.aa = date.today().year
        self.categ = self.aa - self.dt
        print(f'Com {self.categ} anos sua categoria é:',end=' ')

        if self.categ <= 9:
            print('MIRIM')
        elif (self.categ <= 14):
            print('INFANTIL')
        elif (self.categ <= 19):
            print('JUNIOR')
        elif (self.categ <= 25):
            print('SENIOR')
        else:
            print('MASTER')

nas = 'Ano Nascimento: '

class Notas:
    def __init__(self, nota1, nota2):
        self.nt1 = float(input(nota1))
        self.nt2 = float(input(nota2))

    def medias(self):
        self.media = (self.nt1 + self.nt2) / 2

        if self.media < 5:
            print(f'Sua média é {self.media}, está REPROVADO!')
        elif (self.media >= 5) and (self.media < 7):
            print(f'Sua média foi {self.media} está em RECUPERAÇÃO!')
        else:
            print(F'PARABÉNS! sua média foi {self.media} está APROVADO!')

pn1 = 'Primeira Nota: '
sn2 = 'Segunda Nota: '

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.l1 = float(input(lado1))
        self.l2 = float(input(lado2))
        self.l3 = float(input(lado3))

    def tipos(self):
        if self.l1 < (self.l2 + self.l3) and self.l2 < (self.l1 + self.l3) and self.l3 < (self.l1 + self.l2):
            print('Os valores formam um TRIÂNGULO!')
            if self.l1 == self.l2 == self.l3:
                print('Triângulo EQUILÁTERO')
            elif self.l1 != self.l2 != self.l3 != self.l1:
                print('Triângulo ESCALENO')
            else:
                print('Triângulo ISÓCELES')
        else:
            print('Os valores digitados NÃO formam um TRIÂNGULO!')

pl = 'Primeiro lado: '
sl = 'Segundo lado: '
tl = 'Terceiro lado: '

class Peso:
    def __init__(self, peso, altura):
        self.p = float(input(peso))
        self.a = float(input(altura))

    def imc(self):
        self.i = self.p / (self.a ** 2)
        if self.i < 18.5:
            print(f'CUIDADO! seu IMC de {self.i:.2f} está ABAIXO DO PESO!')
        elif self.i <= 25:
            print(f'PARÁBENS! seu IMC de {self.i:.2f} está no peso IDEAL!')
        elif self.i <= 30:
            print(f'ALERTA! seu IMC de {self.i:.2f} está no SOBREPESO!')
        elif self.i <= 40:
            print(f'CUIDADOS MÉDICOS! seu IMC de {self.i:.2f} está OBESO!')
        else:
            print(f'ATENÇÃO MÁXIMA! seu IMC de {self.i:.2f} está com OBESIDADE MÓRBIDA!')
             
p = 'Qual seu peso? '
a = 'Qual sua altura: ' 

class Desconto:
    def __init__(self, preco, f_pagamento):
        self.pco = float(input(preco))
        print('Escolha a forma de PAGAMENTO:\n'
              '[1] À vista DINHEIRO ou CHEQUE [10%] off.\n'
              '[2] À vista CARTÃO [5%] off.\n'
              '[3] Em 2 vezes CARTÃO, preço NORMAL.\n'
              '[4] Em 3 vezes CARTÃO [20%] acréscimo.')
        self.fp = int(input(f_pagamento))

    def descontos(self):
        self.avista = self.pco - (self.pco * 10/100)
        self.avista_cartao = self.pco - (self.pco * 5/100)
        self.parc2_cartao = self.pco / 2
        self.parc3_cartao = self.pco + (self.pco * 20/100)
        if self.fp == 1:
            print(f'Escolhido a forma {self.fp}, valor ficou em R${self.avista:.2f}')
        elif self.fp == 2:
            print(f'Escolhido a forma {self.fp}, valor ficou em R${self.avista_cartao:.2f}')
        elif self.fp == 3:
            print(f'Escolhido a forma {self.fp}, valor ficou em 2 vezes de R${self.parc2_cartao:.2f}')
        elif self.fp == 4:
            self.total_parcela = int(input('Total de Parcelas: '))
            self.parcela = self.parc3_cartao / self.total_parcela
            print(f'Escolheu a forma {self.fp}, em {self.total_parcela} vezes de R${self.parcela:.2f}.')
        else:
            print('OPÇÃO INVÁLIDA! escolha entre 1 e 4')

vp = 'Valor do Produto:R$ '
fp = 'Forma de Pagamento: '

class Jogos:
    def __init__(self, escolha):
        self.esc = str(input(escolha)).strip().upper()

    def jokempo(self):
        self.jogo = randint(1, 3)
        print('JO...', end='')
        sleep(1)
        print('KEN...', end='')
        sleep(1)
        print('PÔ.')
        
        # Variáveis da PEDRA e 1
        if (self.jogo == 1) and (self.esc == 'PEDRA'):
            print('Também pensei em PEDRA, ninguem venceu!')
        elif (self.jogo == 1) and (self.esc == 'TESOURA'):
            print('Pensei em PEDRA, VENCI!')
        elif (self.jogo == 1) and (self.esc == 'PAPEL'):
            print('PARABÉNS, pensei em PEDRA, você VENCEU!')

        # Variáveis do PAPEL e 2
        elif (self.jogo == 2) and (self.esc == 'PAPEL'):
            print('Também pensei em PAPEL, ninguem venceu!')
        elif (self.jogo == 2) and (self.esc == 'PEDRA'):
            print('Pensei em PAPEL, VENCI!')
        elif(self.jogo == 2) and (self.esc == 'TESOURA'):
            print('PARABÉNS, pensei em PAPEL, você VENCEU!')

        # Variáveis da TESOURA e 3:
        elif (self.jogo == 3) and (self.esc == 'TESOURA'):
            print('Também pensei em TESOURA, ninguem venceu!')
        elif (self.jogo == 3) and (self.esc == 'PAPEL'):
            print('Pensei em TESOURA, VENCI!')
        elif(self.jogo == 3) and (self.esc == 'PEDRA'):
            print('PARABÉNS, pensei em PAPEL, você VENCEU!')
        else:
            print('[OPÇÃO INVÁLIDA] digite [PEDRA, PAPEL OU TESOURA]!!!')

escolha = 'Jogando JOKEMPÔ, escolha sua opção: '

class Estruturas:
    def __init__(self):
        print('Trabalhando com [for], [While]')

    def num_pares(self):
        for self.p in range(1, 51):
            if self.p % 2 == 0:
                print(self.p, end=' ')
        print('ACABOU!!')
        print()
        print('Outra maneira de contagem:')
        for self.p2 in range(2, 51, 2):
            print(self.p2, end=' ')
        print('Finalizado...')

    def cont_regressiva(self):
        for self.cr in range(51, -1, -1):
            print(self.cr, end=' ')
        print('Acabou!!')

    def tabuada(self):
        self.t = int(input('Qual número quer saber a tabuada? '))
        for self.num in range(1, 11):
            print(f'A tabuada de {self.t} X {self.num} = {self.t * self.num}') 

    def num_primo(self):
        self.pr = int(input('Digite um número: '))
        self.total = 0  # Para contar quantos foram divisíveis
        for self.cont in range(1, self.pr + 1):
            if self.pr % self.cont == 0:
                print('\033[33m', end='') # Colore em amarelo todos os que são divisíveis
                self.total += 1
            else:
                print('\033[31m', end='') # Colore em vermelho os que não são divisíveis.
            print(self.cont, end=' ')
        print(f'\n\033[mO número {self.pr} foi divisível {self.total} vezes')

        # Verificando se é primo
        if self.total == 2:
            print('O número é PRIMO!')
        else:
            print('Não é PRIMO!')
       
    def palindromo(self):
        self.frase = str(input('Digite uma frase: ')).strip().upper()
        self.separa = self.frase.split()
        self.juntar = ''.join(self.frase)
        self.inverte = self.juntar[::-1]
        
        print(f'O inverso de {self.juntar} é {self.inverte}')
        if self.inverte == self.juntar:
            print('Temos um PALINDROMO')
        else:
            print('Não temos um PLÍNDROMO')

    def maior_menor_idade(self):
        self.ano_atual = date.today().year
        self.tot_maior = 0
        self.tot_menor = 0

        for self.pessoa in range(1, 8):
            self.data_nasc = int(input(f'Ano de Nascimento da {self.pessoa}ª pessoa: '))
            self.idade = self.ano_atual - self.data_nasc

            if self.idade >= 18:
                self.tot_maior += 1
                self.data_nasc += 1
            else:
                self.tot_menor += 1

        print(f'Total de MAIORES: {self.tot_maior}\nTotal de MENORES: {self.tot_menor} ')

    def maior_menor_peso(self):
        self.mai_peso = 0
        self.men_peso = 0

        for self.pessoas in range(1, 6):
            self.peso = float(input(f'Peso da {self.pessoas}ª pessoa: '))

            if self.pessoas == 1:
                self.mai_peso = self.peso
                self.men_peso = self.peso
            else:
                if self.peso > self.mai_peso:
                    self.mai_peso = self.peso

                if self.peso < self.men_peso:
                    self.men_peso = self.peso
        print(f'MAIOR PESO foi: {self.mai_peso}\nMENOR PESO foi: {self.men_peso}')

    def nome_idade_sexo(self):
        self.soma_idade = 0
        self.media_idade = 0
        self.maior_idade = 0
        self.nome_mais_velho = ''
        self.total_mulheres20 = 0

        for self.pes in range(1, 5):
            print(f'{self.pes}ª PESSOA')
            self.no = str(input('NOME: ')).strip().upper
            self.i = int(input('IDADE: '))
            self.sx = str(input('SEXO[M/F]')).strip().upper()
            self.soma_idade += self.i

            if self.pes == 1 and self.sx == 'M':
                self.maior_idade = self.i
                self.nome_mais_velho = self.no

            if self.sx == 'M' and self.i > self.maior_idade:
                self.maior_idade = self.i
                self.nome_mais_velho = self.no

            if self.sx == 'F' and self.i < 20:
                self.total_mulheres20 += 1

        self.media_idade = self.soma_idade / 4

        print(f'Média de idade: {self.media_idade}\nHomem mais velho tem: {self.maior_idade}\n'
              f'Total mulheres com menos de 20 anos: {self.total_mulheres20}')

    def qual_sexo(self):
        self.qs = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
        self.masc = 'M'
        self.fem = 'F'

        if self.masc == self.qs:
            print(f'Sexo {self.qs} registrado com sucesso!!')
        elif self.fem == self.qs:
            print(f'Sexo {self.qs} registrado com sucesso!!')
        
        while self.qs not in 'MF':
            self.qs = str(input('Dados inválidos, informe seu sexo: ')).strip().upper()[0]
            if self.masc == self.qs:
                print(f'Sexo {self.qs} registrado com sucesso!!')
            elif self.fem == self.qs:
                print(f'Sexo {self.qs} registrado com sucesso!!')

    def menu_opcoes(self):
        self.vl1 = int(input('Primeiro Valor: '))
        self.vl2 = int(input('Segundo Valor: '))
        self.opcao = 0

        while self.opcao != 5:
            print('''
            [1] SOMAR
            [2] MULTIPLICAR
            [3] MAIOR
            [4] NOVOS NÚMEROS
            [5] SAIR
            ''')
            self.opcao = int(input('Qual sua opção? '))
            if self.opcao == 1:
                print(f'A soma entre {self.vl1} + {self.vl2} = {self.vl1 + self.vl2}')
            elif self.opcao == 2:
                print(f'A multiplicação de {self.vl1} x {self.vl2} = {self.vl1 * self.vl2}')
            elif self.opcao == 3:
                if self.vl1 > self.vl2:
                    self.maior = self.vl1
                else:
                    self.maior = self.vl2
                print(f'O maior número entre {self.vl1} e {self.vl2} é {self.maior}')
            elif self.opcao == 4:
                print('Informe os números novamente: ')
                self.vl1 = int(input('Primeiro Valor: '))
                self.vl2 = int(input('Segundo Valor: '))
            elif self.opcao == 5:
                print('Finalizando....')
                sleep(2)
            else:
                print('Opção Inválida, tente novamente!!')
        print('Fim do Programa!')

class Progressao:
    def __init__(self, ptermo, razao, qtermo):
        self.a1 = int(input(ptermo))
        self.rz = int(input(razao))
        self.qt = int(input(qtermo))

    def prog_aritimetica(self):
        self.an = self.a1 + (self.qt + 1 - 1) * self.rz       # '(self.qt + 1)' porque o Python conta sempre 1 a menos
        for self.termo in range(self.a1, self.an, self.rz):
            print(self.termo, end=' ¬ ')
        print('Acabou...')
        
prim_termo = 'Digite o primeiro termo: '
razao = 'Digite a razão: '
q_termo = 'Qual termo? '

class Advinhe:
    def __init__(self, palpite):
        print('Advinhe qual número pensei entre 0 e 10???')
        self.compt = randint(0, 10)
        self.tent = 0
        self.jog = 0

    def qual_num(self):
        while self.jog != self.compt:
            self.jog = int(input(palpite))
            self.tent += 1

            if self.jog < self.compt:
                print('Vamos ver....')
                sleep(2)
                print('É MAIS, tente novamente!')
            elif self.jog > self.compt:
                print('Será que foi dessa vez...')
                sleep(2)
                print('É MENOS, tente novamente!')
            else:
                print(f'Agora Foi!\nAcertou com {self.tent} tentativas.')

palpite = 'Qual seu Palpite? '

class Fatorial:
    def __init__(self, fatorial):
        self.fat = int(input(fatorial))
        self.cont = self.fat
        self.ft = 1
        print(f'Calculando {self.fat}!')

    def forma_tradicional(self):
        while self.cont > 0:
            print(f'{self.cont}', end=' ')
            print('x ' if self.cont > 1 else ' = ', end='') # Exclui o último 'x'
            self.ft *= self.cont
            self.cont -= 1
        print(self.ft)

    def forma_pratica(self):
        self.fa = factorial(self.fat)
        print(f'O fatorial de {self.fat} é: {self.fa}')
         
valor = 'Número para calcular o fatorial: '

class Sequencia:
    def __init__(self, fibo):
        self.fb = int(input(fibo))
        self.termo1 = 0
        self.termo2 = 1
        print(f'{self.termo1} ¬ {self.termo2}', end='')
        self.cont = 3

    def seq_fibo(self):
        while self.cont <= self.fb:
            self.termo3 = self.termo1 + self.termo2
            print(f' ¬ {self.termo3}', end='')
            self.termo1 = self.termo2
            self.termo2 = self.termo3
            self.cont += 1
        print(' ¬ Fim...')

fibonacci = 'Quantos termos: '

class Banco:
    def __init__(self, saque):
        self.sq = float(input(saque))
        self.total = self.sq
        self.cedula = 50
        self.tot_cedula = 0

    def saque(self):
        while True:
            if self.total >= self.cedula:
                self.total -= self.cedula
                self.tot_cedula += 1
            else:
                if self.tot_cedula > 0:
                    print(f'Total de {self.tot_cedula} cédulas de {self.cedula}')
                if self.cedula == 50:
                    self.cedula = 20
                elif self.cedula == 20:
                    self.cedula = 10
                elif self.cedula == 10:
                    self.cedula = 1
                self.tot_cedula = 0
                if self.total == 0:
                    break
        print('Volte Sempre!!!')

v_saque = 'Qual o valor R$ '

# Chame aqui o objeto que quer executar
if __name__ == '__main__':
    obj = Banco(v_saque)
    obj.saque()
    
    