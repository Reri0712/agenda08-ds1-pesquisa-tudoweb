# =========================================================
# Empresa: TudoWeb - Pesquisa de Satisfação no Atendimento
# Autor: Renato
# Agenda 08 - Desenvolvimento de Sistemas I
# Centro Paula Souza
# =========================================================

# Definição da quantidade de entrevistados
# Nota: Altere para 10 ao realizar os testes exigidos na atividade.
TOTAL_ENTREVISTADOS = 50;
# Inicialização dos contadores
qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0

print("=" * 55)
print("   PESQUISA DE SATISFAÇÃO DE ATENDIMENTO - TUDOWEB   ")
print("=" * 55)

# Estrutura de repetição para coletar os dados dos entrevistados
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\n--- Entrevistado {i} de {TOTAL_ENTREVISTADOS} ---")
    
    nome = input("Digite o nome: ").strip()
    
    # Validação da idade
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                break
            else:
                print("Por favor, digite uma idade válida (maior que 0).")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros para a idade.")

    # Exibição do menu de opções
    print("\nOpções de Opinião:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    # Validação da opinião do entrevistado
    opiniao = input("Digite a sua opinião (1, 2 ou 3): ").strip()
    while opiniao not in ['1', '2', '3']:
        print("Opção inválida! Escolha apenas 1, 2 ou 3.")
        opiniao = input("Digite a sua opinião (1, 2 ou 3): ").strip()

    # Estruturas de decisão para contabilizar as respostas
    if opiniao == '1':
        qtd_excelente += 1
    elif opiniao == '2':
        qtd_bom += 1
    elif opiniao == '3':
        qtd_ruim += 1

# Exibição do Relatório Final
print("\n" + "=" * 55)
print("               RESULTADO DA PESQUISA                 ")
print("=" * 55)
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print(f"   (Quantidade de respostas 'BOM': {qtd_bom})")
print("=" * 55)