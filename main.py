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
        horas = input("Digite o número de horas que você estudou hoje: ")
        materia = input("Digite a matéria que você estudou: ")
        print(f"Você estudou {horas} horas hoje. Continue assim!")
        if horas.isdigit():
            print("Total de horas:")
            for i, horas in enumerate(horas, start=1):
                print(f"{i}. {horas} horas em {materia}")
            horas_estudo.append((materia, int(horas)))
        else:
            print("Nenhuma hora registrada.")

    elif escolha == '4':
        total_horas = sum(horas for _, horas in horas_estudo)
        print(f"Total de horas estudadas: {total_horas} horas")
        print("Detalhes das horas estudadas:")
        for materia, horas in horas_estudo:
            print(f"{materia}: {horas} horas")
        total_horas = sum(horas for _, horas in horas_estudo)
        print(f"Total de horas estudadas: {total_horas} horas")

    elif escolha == '5':
        print("Saindo do Gerenciador de Estudos. Até a próxima!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")



