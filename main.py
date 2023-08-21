# Sistema de cadastramento de funcionários

class Funcionario:
    def __init__(self, nome, idade, cpf, matricula, cargo, nascimento):
        self.nome = nome
        self. idade = idade
        self.cpf = cpf
        self.matricula = matricula
        self.cargo = cargo
        self.nascimento = nascimento

def cadastrar_funcionario():
    nome = input('Digite o nome do funcionário: ')
    idade = int(input('Digite a idade do funcionário: '))
    cpf = int(input('Digite o CPF: '))
    matricula = int(input('Digite a matricula do funcionário: '))
    cargo = input('Digite o cargo: ')
    nascimento = input('Digite a data de nascimento do funcionário: ')

    novo_funcionario = Funcionario(nome, idade, cpf, matricula, cargo, nascimento)
    return novo_funcionario

def listar_funcionarios(funcionarios):
    print("\nLista de funcionários: ")
    for idx, funcionario in enumerate(funcionarios, start=1):
        print(f"{idx}, Nome: {funcionario.nome}, Idade: {funcionario.idade}, CPF: {funcionario.cpf}, Matricula: {funcionario.matricula},"
              f"Cargo: {funcionario.cargo}, Nascimento:{funcionario.nascimento}")


def excluir_funcionario(funcionarios):
    listar_funcionarios(funcionarios)
    indice = int(input('Digite o número do funcionário que deseja excluir: ')) -1

    if 0 <= indice <len(funcionarios):
        funcionarios.pop(indice)
        print('Funcionário excluído com sucesso')
    else:
        print('Indice invalida')


def main():
    funcionarios = []


    while True:
        print("\nOpções:")
        print("1. Cadastrar funcionário: ")
        print("2. Listar funcionários: ")
        print("3. Excluir funcionários: ")
        print("4. Sair: ")

        opcao = int(input('Esolha uma opção: '))

        if opcao == 1:
            novo_funcionario = cadastrar_funcionario()
            funcionarios.append(novo_funcionario)
            print('Funcionário cadsatrado com sucesso!')
        elif opcao == 2:
            if funcionarios:
                listar_funcionarios(funcionarios)
            else:
                print('Nenhum funcionario cadastrado.')
        elif opcao == 3:
            if funcionarios:
                excluir_funcionario(funcionarios)
            else:
                print('Nenhum funcionário cadastrado para excluir')
        elif opcao == 4:
            print('Saindo do sistema')
            break
        else:
            print('Opção invalida')

if __name__ == "__main__":
    main()