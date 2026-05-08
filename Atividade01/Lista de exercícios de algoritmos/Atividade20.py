quantidade_blusas = int(input("Digite a quantidade de blusas necessárias: "))
metros_totais = quantidade_blusas * 120
novelos = metros_totais // 125

if metros_totais % 125 > 0:

 print(f"total de novelos necessários {novelos}")
