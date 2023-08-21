# Simples sistema de cadastramento de funcionários

class Funcionario:
    def __int__(self, nome, idade, cargo, matricula, cpf):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo


def cadastrar_funcionario():
    nome = input('Digite o nome do funcionário: ')
    idade = int(input('Digite a idade do funcionário'))
    cargo = input('Digite o cargo do funcionário: ')

    novo_funcionario = Funcionario(nome, idade, cargo)
    return novo_funcionario


def listar_funcionario(funcionarios):
    print("\nLista de funcionários: ")
    for i, funcionario in enumerate(funcionarios, start=1):
        print(
            f"{i}, Nome: {funcionario.nome}, Idade: {funcionario.idade}, Cargo: {funcionario.cargo}")


def excluir_funcionario(funcionarios):
    listar_funcionario(funcionarios)
    indice = int(input('Digite o número do funcionário que deseja excluir: '))

    if 0 <= indice <len(funcionarios):
        funcionarios.pop(indice)
        print('Funcionário excluído com sucesso.')
    else:
        print('Indice invalida.')