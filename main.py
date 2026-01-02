print("Gerenciador de Estudos")

print("Bem-vindo ao Gerenciador de Estudos!")
print("Aqui você pode organizar seus estudos de forma eficiente.\n")

print("Escolha uma opção:")
print("1. Adicionar matéria")
print("2. Ver matérias")
print("3. Horas de estudo")
print("4. Ver total de horas estudadas")
print("5. Sair\n")

materias = []
horas_estudo = []

while True:
    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        materia = input("Digite o nome da matéria que deseja adicionar: ")
        materias.append(materia)
        print(f"Matéria '{materia}' adicionada com sucesso!")

    elif escolha == '2':
        if materias:
            print("Matérias cadastradas:")
            for i, mat in enumerate(materias, start=1):
                print(f"{i}. {mat}")
        else:
            print("Nenhuma matéria cadastrada.")

    elif escolha == '3':
        materia = input("Digite a matéria que você estudou: ")
        if materia not in materias:
            print(f"A matéria '{materia}' não está cadastrada.")
        else:
            horas_input = input(f"Quantas horas você estudou em '{materia}' hoje? ")

        if horas_input.isdigit():
            horas = int(horas_input)
            horas_estudo.append((materia, horas))
            print(f"{horas} horas registradas para a matéria '{materia}'.")
        else:
            print("Valor inválido. Por favor, digite um número.")

    elif escolha == '4':
        if horas_estudo:
            total_horas = sum(horas for _, horas in horas_estudo)
        
        print("Detalhes das horas estudadas:")
        print(f"Total de horas estudadas: {total_horas} horas")
        for materia, horas in horas_estudo:
            print(f"{materia}: {horas} horas")
            

    elif escolha == '5':
        print("Saindo do Gerenciador de Estudos. Até a próxima!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")

