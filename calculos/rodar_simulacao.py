"""
A partir de inputs, calcular a evolução das contribuições, com retorno do investimento, pelo prazo de diferimento
O prazo de diferimento corresponde ao periodo entre a idade atual do participante e a data de saída (
Data de saída é a data em que o participante completa a idade que fez opção por começar a receber o beneficio de renda
Os dados necessários para o cálculo são
Data de nascimento ou idade(anos ou meses)
Data de saída ou idade de saida(anos ou meses)
Rentabilidade Real Anual (acima da inflação)
Valor do contribuição mensal

Para conversão em benefício é necessário informar o sexo ("M" ou "F")
Tabua de sobrevivência
taxa de juros da tábua

"""


from inputao import input as inputao

from calculos.atuarial.fat import FAT


def calcula_diferimento_em_meses(idade_atual, idade_saida):
    return (idade_saida - idade_atual) * 12


def calcula_rentabilidade_mensal(rentabilidade_anual):
    return (((1 + (rentabilidade_anual) / float(100)) ** (1 / 12)) - 1)


def calcula_evolucao_das_contribuicoes(idade_atual, idade_saida, rentabilidade_anual, contribuicao_mensal):
    diferimento = calcula_diferimento_em_meses(idade_atual, idade_saida)
    rentabilidade_mensal = calcula_rentabilidade_mensal(rentabilidade_anual)
    saldo = 0

    for i in range(diferimento):
        saldo = (saldo + contribuicao_mensal) * (1 + rentabilidade_mensal)

    return saldo


def calcula_valor_renda_mensal_vitalicia(saldo, sexo, idade_saida):
    fator_conversao_em_renda = FAT('BREMS_NS', sexo, 'F', 0.02).ax[idade_saida]
    return saldo / fator_conversao_em_renda


def calcula(idade_atual, idade_saida, rentabilidade_anual, contribuicao_mensal, sexo):
    saldo = calcula_evolucao_das_contribuicoes(idade_atual, idade_saida, rentabilidade_anual, contribuicao_mensal)
    renda_mensal_vitalicia = calcula_valor_renda_mensal_vitalicia(saldo, sexo, idade_saida)
    return saldo, renda_mensal_vitalicia


if __name__ == '__main__':
    idade_atual = inputao("Entre com sua idade em anos: ", int)
    idade_saida = inputao("Com qual idade deseja iniciar a renda: ", int)
    rentabilidade_anual = inputao("Defina a rentabilidade real anual dos investimentos ex: 4%a.a entre com valor 4: ", float)
    contribuicao_mensal = inputao("Defina o valor que quer contribuir mensalmente: ", float)
    sexo = inputao('Informe o sexo ("M" ou "F"):', str)

    assert idade_atual >= 0
    assert idade_saida >= 0
    assert rentabilidade_anual >= 0
    assert contribuicao_mensal >= 0
    assert sexo == "M" or sexo == "F"
    assert calcula_diferimento_em_meses(idade_atual, idade_saida) > 0
    assert calcula_rentabilidade_mensal(rentabilidade_anual) >= 0
    assert calcula_evolucao_das_contribuicoes(idade_atual, idade_saida, rentabilidade_anual, contribuicao_mensal) >= 0

    saldo = calcula_evolucao_das_contribuicoes(idade_atual, idade_saida, rentabilidade_anual, contribuicao_mensal)
    assert calcula_valor_renda_mensal_vitalicia(saldo, sexo, idade_saida) >= 0
    renda_mensal_vitalicia = calcula_valor_renda_mensal_vitalicia(saldo, sexo, idade_saida)
    print()
    print(f'Saldo aos {idade_saida} anos: {saldo:0.2f}')
    print(f'Renda vitalicia sem continuidade: {renda_mensal_vitalicia:0.2f}')
