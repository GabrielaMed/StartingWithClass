'''Classe Conta de Investimento: Faça uma classe contaInvestimento que seja semelhante a classe 
contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que 
configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros (sem parâmetro 
explícito) que adicione juros à conta. Escreva um programa que construa uma poupança com um saldo inicial 
de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo 
resultante.'''

class contaInvestimento:
    def __init__(self, saldoInicial, taxaJuros):
        self.saldoInical = saldoInicial
        self.taxaJuros = taxaJuros

    def adicioneJuros (self, saldoResultante):
        saldoResultante += ((self.taxaJuros/100) * self.saldoInical) + self.saldoInical
        return saldoResultante

saldoResultante = 0
poupanca1 = contaInvestimento(1000, 10)
poupanca1.adicioneJuros(saldoResultante)
poupanca1.adicioneJuros(saldoResultante)
poupanca1.adicioneJuros(saldoResultante)
poupanca1.adicioneJuros(saldoResultante)
poupanca1.adicioneJuros(saldoResultante)

print(f"O saldo resultante é de R${poupanca1.adicioneJuros(saldoResultante)}.")