from vetores import vetor

print(30 * "-", "MENU", 30 * "-")
print("1. Vetores")
print("2. Listas Ligadas")

menu = int(input("Digite a opcão desejada: "))

if menu == 1:
    vetor_teste = vetor.Vetor(3)
    vetor_teste.inserir_elemento_posicao(1, 0)
    print(vetor_teste.listar_elemento(0))
