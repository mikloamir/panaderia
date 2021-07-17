import padarias
import comprovante_compra

padarias = padarias.padarias

class Comprar:

    qtds_compra = []

    qtd_pao_de_sal = int(input('Quantidade de Pão de Sal: '))

    qtd_baguete = int(input('Quantidade de Baguete: '))

    qtd_manteiga = int(input('Quantidade de Manteiga: '))

    qtds_compra.extend([qtd_pao_de_sal, qtd_baguete, qtd_manteiga])

    dia_semana = input('Qual é o dia da semana? ')
    dia_semana.lower()

    def onde_comprar(self) :
        if (self.qtd_pao_de_sal > 0) and (self.qtd_baguete == 0 and self.qtd_manteiga == 0) :
            print('Vale do Trigo')
        elif (self.qtd_baguete > 0) and (self.qtd_pao_de_sal == 0 and self.qtd_manteiga == 0) :
            print('Super Pão')
        elif (self.qtd_manteiga > 0) and (self.qtd_pao_de_sal == 0 and self.qtd_baguete == 0) :
            print('Panificadora Verona')
        elif (self.qtd_manteiga == 0) and (self.qtd_pao_de_sal > 0 and self.qtd_baguete > 0) :
            print('Super Pão')
        elif (self.qtd_baguete == 0) and (self.qtd_pao_de_sal > 0 and self.qtd_manteiga > 0) :
            print('Panificadora Verona')
        elif (self.qtd_pao_de_sal == 0) and (self.qtd_baguete > 0 and self.qtd_manteiga > 0) :
            print('Panificadora Verona')
        else :
            print('Panificadora Verona')

    if (dia_semana == "sabado") or (dia_semana == "sábado") or (dia_semana == "domingo") :
        ajuste_preco = 0.2
    else :
        ajuste_preco = 0

    '''
    for id, info in padarias.items():
        print("\nPadaria ID:", id)

        #print(padarias[id]['distancia'])

        print(padarias[id]['pão de sal'])
        print(padarias[id]['baguete'])
        print(padarias[id]['manteiga'])
        
        for key in info:
            print(key + ':', info[key])


    total_padarias = {
        'super_pao' : 0,
        'vale_do_trigo' : 0,
        'padaria_do_tunico' : 0,
        'panificadora_verona' : 0
    }
    '''

    total_padarias = {}
    total_valores_padaria = []
    distancias_padarias = []
    nome_padaria = ''

    for id in padarias.keys():

        #print("\nPadaria:", id)

        #print(padarias[id]['distancia'])

        total_pao_de_sal = float(padarias[id]['pão de sal']) * qtd_pao_de_sal
        total_pao_de_sal = total_pao_de_sal + (total_pao_de_sal * ajuste_preco)
        #print('pão de sal (R$ / KG) | ' + str(padarias[id]['pão de sal']) + ' | ' + str(total_pao_de_sal))
        
        total_baguete = float(padarias[id]['baguete']) * qtd_baguete
        total_baguete = total_baguete + (total_baguete * ajuste_preco)
        #print('baguete (R$ / KG) | ' + str(padarias[id]['baguete']) + ' | ' + str(total_baguete))
        
        total_manteiga = float(padarias[id]['manteiga']) * qtd_manteiga
        total_manteiga = total_manteiga + (total_manteiga * ajuste_preco)
        #print('manteiga (Unid.) | ' + str(padarias[id]['manteiga']) + ' | ' + str(total_manteiga))
        
        total = total_pao_de_sal + total_baguete + total_manteiga
            
        total_padarias[id]=[total, padarias[id]['distancia']]

        total_valores_padaria.append(total)
        distancias_padarias.append(padarias[id]['distancia'])

    #print(total_padarias)
    #print(min(total_valores_padaria))

    menor_valor_padaria = min(total_valores_padaria)
    menor_distancia_padarias = max(distancias_padarias)

    for id in total_padarias.items():

        #print("\nPadaria:", id[0])
        #print(id[1][0])
        #print(id[1][1])

        if (id[1][0] == menor_valor_padaria) :
            if (id[1][1] <= menor_distancia_padarias) :
        
                nome_padaria = id[0]
                menor_distancia_padarias = id[1][1]
                menor_valor_padaria = id[1][0]

    #print(nome_padaria)
    #print(menor_distancia_padarias)
    #print(menor_valor_padaria)
    print('')

    fim_compra = comprovante_compra.cupom(nome_padaria, menor_distancia_padarias, menor_valor_padaria)
    fim_compra.imprimir()