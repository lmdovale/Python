#coding: utf-8

import math

print("\nCALCULANDO A CORREÇÃO DO FATOR DE POTÊNCIA!\n")

continua = True
while continua:
    op1 = int(input("Vamos calcular? Digite:\n 1(Sim)\n 2(Não)\n : \n"))
    if op1>=2:
        continua = False
    else:
        op2 = int(input("Qual o tipo de sistema? Digite:\n 1(Monofásico)\n 2(Trifásico)\n : \n"))
        if op2==1:
            tensao = float(input("Tensão eficaz da linha (em V): "))
            f = float(input("Freqüência do sistema (em Hz): "))
            tca = float(input("Informe tarifa (kVarh/R$): "))
            fp = float(input("Fator de potência desejado após a correção: "))
            med_kwh = float(input("Número de medições que serão considerados: "))
            som_kwh = 0
            div_kwh = 0
            som_kvarh = 0
            div_kvarh = 0
            som_horas = 0
            div_horas = 0

            while med_kwh != 0:
                kwh = float(input("Quantidade de kWh: "))
                som_kwh += kwh
                div_kwh += 1
                media_kwh = som_kwh/div_kwh

                kvarh = float(input("Quantidade de kVArh: "))
                som_kvarh += kvarh
                div_kvarh += 1
                media_kvarh = som_kvarh/div_kvarh

                horas = float(input("Quantidade média em horas de trabalho ((dias x horas)/meses): "))
                som_horas += horas
                div_horas += 1
                media_horas = som_horas/div_horas

                med_kwh -= 1
                pa = media_kwh/media_horas
                pr = media_kvarh/media_horas
                fp_antes = math.cos(math.atan(pr/pa))
                s1 = pa / fp_antes
                q1 = math.sqrt((s1 ** 2) - (pa ** 2))
                i1 = s1 / (tensao / 1000)
            if fp_antes >=0.92:
                print("\nMédia kWh: %.0f kWh" % media_kwh)
                print("Média kVarh: %.0f kVarh" % media_kvarh)
                print("Média h: %.0f h" % media_horas)
                print("Tensão eficaz do sistema: %.0f V" % tensao)
                print("Freqüência do sistema: %.0f Hz\n" % f)
                print("Potência ativa antes da correção: %.2f kW" % pa)
                print("Potência reativa antes da correção: %.2f kVAr" % q1)
                print("Potência aparente antes da correção: %.2f kVA" % s1)
                print("Fator de potência antes da correção: %.2f" % fp_antes)
                print("Corrente na linha antes da correção: %.2f A\n" % i1)
                print("Não será necessário corrigir o Fator de Potencia!\n")
            elif fp_antes<0.92:
                s2 = pa/fp
                q2 = math.sqrt((s2**2)-(pa**2))
                fp_depois = math.cos(math.atan(q2/pa))
                i2 = s2/(tensao/1000)
                pc = q1-q2
                ca = ((10**3)*pc)/(2*math.pi*f*((tensao/1000)**2))
                ic = pc/(tensao/1000)
                fer = (media_kwh*((0.92/fp_antes)-1))*tca
                print("\nMédia kWh: %.0f kWh" % media_kwh)
                print("Média kVarh: %.0f kVarh" % media_kvarh)
                print("Média h: %.0f h" % media_horas)
                print("Tensão eficaz do sistema: %.0f V" % tensao)
                print("Freqüência do sistema: %.0f Hz" % f)
                print("Consumo de energia reativa excedente atual: R$ %.2f DESPERDÍCIO!\n" % fer)
                print("Potência ativa antes da correção: %.2f kW" % pa)
                print("Potência reativa antes da correção: %.2f kVAr" % q1)
                print("Potência aparente antes da correção: %.2f kVA" % s1)
                print("Fator de potência antes da correção: %.2f" % fp_antes)
                print("Corrente na linha antes da correção: %.2f A\n" % i1)
                print("Potência ativa depois da correção: %.2f kW" % pa)
                print("Potência reativa depois da correção: %.2f kVAr" % q2)
                print("Potência aparente depois da correção: %.2f kVA" % s2)
                print("Fator de potência depois da correção: %.2f" % fp_depois)
                print("Corrente na linha depois da correção: %.2f A\n" % i2)
                print("Capacitância do capacitor a ser ligado em paralelo com a carga: %.2f uF" % ca)
                print("Potência reativa do capacitor: %.2f kVAr" % pc)
                print("Corrente do capacitor: %.2f A" % ic)
                print("Tensão do capacitor: %.0f V\n" % tensao)
                inv = float(input("Informe o valor do orçamento da correção: R$ "))
                re_inv = inv / fer
                print("Retorno do capital investido: %.2f meses" % re_inv)
        else:
            op2==2
            tensao = float(input("Tensão eficaz da linha (em V): "))
            f = float(input("Freqüência do sistema (em Hz): "))
            tca = float(input("Informe a tarifa (kVarh/R$): "))
            fp = float(input("Fator de potência desejado após a correção: "))
            med_kwh = float(input("Número de medições que serão considerados: "))
            som_kwh = 0
            div_kwh = 0
            som_kvarh = 0
            div_kvarh = 0
            som_horas = 0
            div_horas = 0

            while med_kwh != 0:
                kwh = float(input("Quantidade de kWh: "))
                som_kwh += kwh
                div_kwh += 1
                media_kwh = som_kwh / div_kwh

                kvarh = float(input("Quantidade de kVArh: "))
                som_kvarh += kvarh
                div_kvarh += 1
                media_kvarh = som_kvarh / div_kvarh

                horas = float(input("Quantidade média em horas de trabalho ((dias x horas)/meses): "))
                som_horas += horas
                div_horas += 1
                media_horas = som_horas / div_horas

                med_kwh -= 1
                pa = media_kwh / media_horas
                pr = media_kvarh / media_horas
                fp_antes = math.cos(math.atan(pr / pa))
                s1 = pa / fp_antes
                q1 = math.sqrt((s1 ** 2) - (pa ** 2))
                i1 = s1 / 1.7321*(tensao / 1000)
            if fp_antes >= 0.92:
                print("\nMédia kWh: %.0f kWh" % media_kwh)
                print("Média kVarh: %.0f kVarh" % media_kvarh)
                print("Média h: %.0f h" % media_horas)
                print("Tensão eficaz do sistema: %.0f V" % tensao)
                print("Freqüência do sistema: %.0f Hz\n" % f)
                print("Potência ativa antes da correção: %.2f kW" % pa)
                print("Potência reativa antes da correção: %.2f kVAr" % q1)
                print("Potência aparente antes da correção: %.2f kVA" % s1)
                print("Fator de potência antes da correção: %.2f" % fp_antes)
                print("Corrente na linha antes da correção: %.2f A\n" % i1)
                print("Não será necessário corrigir o Fator de Potencia!\n")
            elif fp_antes < 0.92:
                s2 = pa / fp
                q2 = math.sqrt((s2 ** 2) - (pa ** 2))
                fp_depois = math.cos(math.atan(q2 / pa))
                i2 = s2 /1.7321*(tensao / 1000)
                pc = q1 - q2
                ca = ((10 ** 3) * pc) / (2 * math.pi * f * ((tensao / 1000) ** 2))
                ic = pc /1.7321*(tensao / 1000)
                fer = (media_kwh * ((0.92 / fp_antes) - 1)) * tca
                print("\nMédia kWh: %.0f kWh" % media_kwh)
                print("Média kVarh: %.0f kVarh" % media_kvarh)
                print("Média h: %.0f h" % media_horas)
                print("Tensão eficaz do sistema: %.0f V" % tensao)
                print("Freqüência do sistema: %.0f Hz" % f)
                print("Consumo de energia reativa excedente atual: R$ %.2f DESPERDÍCIO!\n" %fer)
                print("Potência ativa antes da correção: %.2f kW" % pa)
                print("Potência reativa antes da correção: %.2f kVAr" % q1)
                print("Potência aparente antes da correção: %.2f kVA" % s1)
                print("Fator de potência antes da correção: %.2f" % fp_antes)
                print("Corrente na linha antes da correção: %.2f A\n" % i1)
                print("Potência ativa depois da correção: %.2f kW" % pa)
                print("Potência reativa depois da correção: %.2f kVAr" % q2)
                print("Potência aparente depois da correção: %.2f kVA" % s2)
                print("Fator de potência depois da correção: %.2f" % fp_depois)
                print("Corrente na linha depois da correção: %.2f A\n" % i2)
                print("Capacitância do capacitor a ser ligado em paralelo com a carga: %.2f uF" % ca)
                print("Potência reativa do capacitor: %.2f kVAr" % pc)
                print("Corrente do capacitor: %.2f A" % ic)
                print("Tensão do capacitor: %.0f V\n" % tensao)
                inv = float(input("Informe o valor do orçamento da correção: R$ "))
                re_inv = inv/fer
                print("Retorno do capital investido: %.2f meses" %re_inv)
                