notas = []

for i in range(5):
    nome = input("Digite o nome do aluno(a): ")
    notaum = float(input("Digite a primeira nota do aluno: "))
    notadois = float(input("Digite a segunda nota do aluno: "))

    media = (notaum + notadois) / 2
    status = "Aprovado" if media >= 6 else "Reprovado"

    notas.append([nome, notaum, notadois, media, status])
    if (i < 4):
        print("\n---Proximo Aluno---")

print("\n---Resultado final---")

for nota in notas:
        print(f"{nota[0]} - Nota 1: {nota[1]} | Nota 2: {nota[2]} | Média: {nota[3]:.2f} | Situação: {nota[4]}")
