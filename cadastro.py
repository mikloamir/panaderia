from tabulate import tabulate

class Cadastro():

    cabecalho = ['Padaria', 'Distância', 'Pão de Sal (R$ / KG)', 'Baguete (R$ / KG)', 'Manteiga (R$)']

    tabela = [
        ['super_pao', 2, 5, 7, 10],
        ['vale_do_trigo', 5, 4, 9, 9],
        ['padaria_do_tunico', 0.5, 4.5, 8, 9.5],
        ['panificadora_verona', 9, 6, 9, 3]
    ]

    def imprimir(self) :
        print(tabulate(self.tabela, headers=self.cabecalho, tablefmt='fancy_grid'))