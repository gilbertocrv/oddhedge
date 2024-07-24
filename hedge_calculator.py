def calcular_odd_lay(aposta_back, odd_back, lucro_desejado):
    """
    Calcula a odd de lay necessária para garantir um lucro desejado.

    :param aposta_back: Valor da aposta de back
    :param odd_back: Odd da aposta de back
    :param lucro_desejado: Lucro desejado
    :return: Odd de lay necessária
    """
    # Lucro garantido com a aposta de back
    lucro_garantido = aposta_back * (odd_back - 1)
    
    # Calcular a odd de lay necessária para garantir o lucro desejado
    odd_lay = (lucro_garantido + aposta_back - lucro_desejado) / aposta_back
    
    return odd_lay

def main():
    try:
        aposta_back = float(input("Informe o valor da aposta de back (R$): "))
        odd_back = float(input("Informe a odd de back: "))
        lucro_desejado = float(input("Informe o lucro desejado (R$): "))
        
        odd_lay = calcular_odd_lay(aposta_back, odd_back, lucro_desejado)
        
        print(f'A odd de Lay necessária para garantir um lucro de R$ {lucro_desejado:.2f} é: {odd_lay:.2f}')
    except ValueError:
        print("Erro: Por favor, insira números válidos.")
    
    # Pausa para exibir o resultado
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
