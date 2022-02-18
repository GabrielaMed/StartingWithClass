'''Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, 
com valor default zero e os demais atributos são obrigatórios.
'''

class contaCorrente:
    def __init__(self, conta, nomeCorrentista, saldo):
        self.conta = conta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, novoNome):
        self.nomeCorrentista = novoNome

    def deposito(self, entrada):
        self.saldo += entrada
        return print(f"Seu saldo é de R${self.saldo}")

    def saque(self, saida):
        self.saldo -= saida
        return print(f"Seu saldo é de R${self.saldo}")


novoNome = input("Digite seu nome: ")
conta1 = contaCorrente(123, novoNome, 0)

entrada = float(input("Quanto deseja depositar? "))
conta1.deposito(entrada)

saida = float(input("Quanto deseja retirar? "))
conta1.saque(saida)

 