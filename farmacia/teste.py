import datetime
from clientes import *
from medicamentos import *
from laboratorio import *
from vendas import *

marco = Cliente('Marco', '11111111111', '01011980')
Cliente.dic_clientes['11111111111'] = marco

lucas = Cliente('Lucas', '22222222222', '01011980')
Cliente.dic_clientes['22222222222'] = lucas

rhuan = Cliente('Rhuan', '33333333333', '01011980')
Cliente.dic_clientes['33333333333'] = rhuan

leonardo = Cliente('Leonardo', '44444444444', '01011980')
Cliente.dic_clientes['44444444444'] = leonardo

ache = Laboratorio('Aché', 'Rod. Pres. Dutra-Pista Lateral, s/n - Porto da Igreja, 07034-904', '1122221111', 'Guarulhos', 'SP')
Laboratorio.dic_laboratorios['Aché'] = ache

ems = Laboratorio('EMS', 'Jornalista Francisco Aguirre Proença, KM 08, Chacara Assay, 13186-901', '1122221111', 'Hortolândia', 'SP')
Laboratorio.dic_laboratorios['EMS'] = ems

novocilin = Quimioterapicos('Novocilin', 'amoxicilina', 'Aché', 'Cápsulas duras de 500 mg: embalagem com 21 cápsulas', 's')
Medicamento.dic_medicamentos['Novocilin'] = novocilin

decongex = Fitoterapicos('Decongex Plus', 'maleato de bronfeniramina + cloridrato de fenilefrina', 'Aché', 'Comprimidos revestidos de liberação programada 12 mg + 15 mg: embalagens com 12 e 100 comprimidos')
Medicamento.dic_medicamentos['Decongex Plus'] = decongex

amoxicilina = Quimioterapicos('Amoxicilina', 'amoxicilina', 'EMS', '250mg/5ml, suspensão oral, frasco com 150ml', 's')
Medicamento.dic_medicamentos['Amoxicilina'] = amoxicilina

acetilcisteina = Fitoterapicos('Acetilcisteína', 'acetilcisteína', 'EMS', '20mg/ml, xarope pediátrico, frasco com 120ml')
Medicamento.dic_medicamentos['Acetilcisteína'] = acetilcisteina

venda1 = ProdutosVendidos('Novocilin', 1, 10)
venda2 = ProdutosVendidos('Decongex Plus', 1, 10)
venda3 = ProdutosVendidos('Amoxicilina', 1, 10)
venda4 = ProdutosVendidos('Acetilcisteína', 1, 10)

cadvenda1 = Vendas(datetime.datetime.now().date(), datetime.datetime.now().time(), [venda1], '11111111111', 10)
cadvenda2 = Vendas(datetime.datetime.now().date(), datetime.datetime.now().time(), [venda2], '11111111111', 10)
cadvenda3 = Vendas(datetime.datetime.now().date(), datetime.datetime.now().time(), [venda3], '22222222222', 10)
cadvenda4 = Vendas(datetime.datetime.now().date(), datetime.datetime.now().time(), [venda4], '33333333333', 10)

Vendas.dict_venda['11111111111'] = cadvenda1
Vendas.dict_venda['11111111111'].produtos_vendidos.append(cadvenda2)
Vendas.dict_venda['22222222222'] = cadvenda3
Vendas.dict_venda['33333333333'] = cadvenda4
