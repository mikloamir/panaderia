from tabulate import tabulate

class cupom:

    def __init__ (self, nome_padaria, menor_distancia_padarias, menor_valor_padaria):

        self.nome_padaria = nome_padaria
        self.menor_distancia_padarias = menor_distancia_padarias
        self.menor_valor_padaria = menor_valor_padaria

    def imprimir(self) :
    
        cabecalho = ['Padaria', 'Distância (Km)', 'Valor Compra (R$)']

        tabela = [
            [f'{self.nome_padaria}', self.menor_distancia_padarias, self.menor_valor_padaria]
        ]

        print(tabulate(tabela, headers=cabecalho, tablefmt='fancy_grid'))