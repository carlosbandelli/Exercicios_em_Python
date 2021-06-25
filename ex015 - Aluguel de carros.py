km = float(input('Quantos KM você percorreu: '))
dias = float(input('Quantos dias voce alugou: '))
tk = km * 0.15
td = dias * 60
print(f'Voce percorreu {km} km e ficou R${tk}.\nVocê alugou {dias} dias e ficou R${td}.\nPortanto o total de km rodados R${tk} e total de dias alugados R${td} é igual a {tk + td:.2f}')