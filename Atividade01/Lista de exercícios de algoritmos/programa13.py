import time
contador = 10
while contador >=0:
    print(f"Após: {contador} segundos poderá ser aberto")
    time.sleep(1)
    contador -= 1
    print("O resfriamento foi concluído")