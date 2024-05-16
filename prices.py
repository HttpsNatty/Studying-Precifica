def exportar_ingredientes_texto(ingredientes, tabuleiro, porcoes, nome_bolo):
    #Cria e escreve no arquivo
    nome_arquivo = f"{nome_bolo}.txt"
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"Nome do bolo: {nome_bolo}\n")
        arquivo.write("Ingredientes:\n")
        #Lista dos ingredientes e o valor de custo
        for ingrediente in ingredientes:
            linha = f"{ingrediente['nome']}: R${ingrediente['custo']:.2f}\n"
            arquivo.write(linha)
        #Mostra os valores totais
        custo_total = calcular_custo_total_ingredientes(ingredientes)
        arquivo.write(f"\nCusto total dos ingredientes: R${custo_total:.2f}\n")
        #Mostra os dados sobre o tabuleiro e as porções
        arquivo.write(f"Tamanho do tabuleiro: {tabuleiro['largura']}x{tabuleiro['comprimento']} cm\n")
        area_por_porcao = dividir_tabuleiro(tabuleiro, porcoes)
        arquivo.write(f"Área de cada porção: {area_por_porcao:.2f} cm²\n")
        custo_por_porcao = custo_total / porcoes
        arquivo.write(f"Custo por porção: R${custo_por_porcao:.2f}\n")
        
        # Calcula o valor de venda por porção e lucro total
        valor_venda_porcao = custo_por_porcao * 4
        lucro_total = valor_venda_porcao * porcoes
        arquivo.write(f"Valor de venda por porção: R${valor_venda_porcao:.2f}\n")
        arquivo.write(f"Lucro total: R${lucro_total:.2f}\n")
    print(f"Confira a lista de ingredientes exportada para {nome_arquivo}")

def calcular_custo_ingrediente(valor_pacote, quantidade_pacote, quantidade_usada):
    # Calcula o valor por unidade do ingrediente
    valor_por_unidade = valor_pacote / quantidade_pacote
    # Calcula o custo do ingrediente usado na receita
    custo_ingrediente = valor_por_unidade * quantidade_usada
    return custo_ingrediente

def calcular_custo_total_ingredientes(ingredientes):
    # Calcula o custo total dos ingredientes
    custo_total = sum(ingrediente['custo'] for ingrediente in ingredientes)
    return custo_total

def dividir_tabuleiro(tabuleiro, porcoes):
    # Calcula a área de cada porção
    area_tabuleiro = tabuleiro['largura'] * tabuleiro['comprimento']
    area_por_porcao = area_tabuleiro / porcoes
    return area_por_porcao

def main():
    nome_bolo = input("Digite o nome do bolo: ")
    # Informações dos ingredientes
    ingredientes = []
    while True:
        nome = input("Nome do ingrediente: ")
        valor_pacote = float(input(f"Valor do pacote de {nome}: ").replace(',', '.'))
        quantidade_pacote = float(input(f"Quantidade do pacote de {nome} (em gramas, litros, etc.): ").replace(',', '.'))
        quantidade_usada = float(input(f"Quantidade usada na receita de {nome} (em gramas, ml, etc.): ").replace(',', '.'))
        
        custo = calcular_custo_ingrediente(valor_pacote, quantidade_pacote, quantidade_usada)
        ingredientes.append({'nome': nome, 'custo': custo})
        
        while True:
            escolha = input("Você deseja inserir mais um ingrediente? (sim/não) ou desfazer o anterior? (desfazer): ").strip().lower()
            if escolha in ['sim', 's', 'ss']:
                break
            elif escolha in ['não', 'nao', 'n']:
                break
            elif escolha == 'desfazer':
                if ingredientes:
                    ingredientes.pop()
                    print("Ingrediente anterior removido.")
                else:
                    print("Não há ingredientes para remover.")
            else:
                print("Opção inválida. Por favor, digite 'sim', 'não' ou 'desfazer'.")

        if escolha in ['não', 'nao', 'n']:
            break
    
    # Calcula o custo total dos ingredientes
    custo_total = calcular_custo_total_ingredientes(ingredientes)
    print(f"\nCusto total dos ingredientes: R${custo_total:.2f}")
    
    # Informações do tabuleiro
    largura_tabuleiro = float(input("Largura do tabuleiro (em cm): ").replace(',', '.'))
    comprimento_tabuleiro = float(input("Comprimento do tabuleiro (em cm): ").replace(',', '.'))
    porcoes = int(input("Número de porções desejadas: "))
    
    tabuleiro = {'largura': largura_tabuleiro, 'comprimento': comprimento_tabuleiro}
    # Calcula a área de cada porção
    area_por_porcao = dividir_tabuleiro(tabuleiro, porcoes)
    
    print(f"\nÁrea de cada porção: {area_por_porcao:.2f} cm²")
    custo_por_porcao = custo_total / porcoes
    print(f"Custo por porção: R${custo_por_porcao:.2f}")
    
    # Calcula o valor de venda por porção e lucro total
    valor_venda_porcao = custo_por_porcao * 4
    lucro_total = valor_venda_porcao * porcoes
    print(f"Valor de venda por porção: R${valor_venda_porcao:.2f}")
    print(f"Lucro total: R${lucro_total:.2f}")
    
    # Exporta a lista de ingredientes e informações do tabuleiro para um arquivo de texto
    exportar_ingredientes_texto(ingredientes, tabuleiro, porcoes, nome_bolo)

if __name__ == "__main__":
    main()