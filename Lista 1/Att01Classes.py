class person: 
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, envelhecer):
        print(f"Você envelheceu {self.idade + envelhecer} anos.")

    def engordar(self):
        print("Você engordou.")

    def emagrecer(self):
        print("Você emagreceu.")

    def crescer(self, cresceu):
        if self.idade < 21:
            print(f"Você envelheceu {envelhecer} anos e por isso cresceu {cresceu}cm.")
        else: 
            print("Você já passou de 21 ano e por isso não cresce mais")   

nome = input("Digite eu nome: ")
idade = int(input("Digite sua idade: "))
peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")
envelhecer = int(input("Você deseja envelhecer quantos anos? "))
cresceu = envelhecer * 0.5

pessoa1 = person(nome, idade, peso, altura)

print(pessoa1.nome)
print(pessoa1.crescer(cresceu))