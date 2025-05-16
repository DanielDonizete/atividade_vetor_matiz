notas = []

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    notaum = float(input("Digite a primeira nota do aluno: "))
    notadois = float(input("Digite a segunda nota do aluno: "))

    media = (notaum + notadois) / 2

    notas.append({
        "nome": nome,
        "Nota 1": notaum,
        "Nota 2": notadois,
        "Média": media

    })
    print("\n---Proximo Aluno---")

for nota in notas:
    print(f"{nota['nome']} - Nota 1: {nota['Nota 1']} | Nota 2: {nota['Nota 2']} | Média: {nota['Média']}:.2f")