# Simples sistema de cadastramento de funcionários

class Funcionario:
    def __int__(self, nome, idade, cargo, matricula, cpf):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.matricula = matricula
        self.cpf = cpf
        
def cadastrar_funcionario():
    nome = input('Digite o nome do funcionário: ')
    idade = int(input('Digite a idade do funcionário'))
    cargo = input('Digite o cargo do funcionário: ')
    matricula = int(input('Digite a matricula do funcionário: '))
    cpf = int(input('Digite o CPF do funcionário: '))

    novo_funcionario = Funcionario(nome, idade, cargo, matricula, cpf)
    return novo_funcionario

def listar_funcionario(funcionarios):
    print("\nLista de funcionários: ")
    for i, funcionario in enumerate(funcionarios, start=1):
        print(f"{i}, Nome: {funcionario.nome}, Idade: {funcionario.idade}, Cargo: {funcionario.cargo}, Matricula: {funcionario.matricula},"
            f"CPF: {funcionario.cpf}")

def excluir_funcionario(funcionarios):
