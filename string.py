texto = 'Giuseppe'
texto_minusculo = texto.lower()

quantidade_a = texto_minusculo.count("a")

if quantidade_a > 0:
    print(f'A letra "a" aparece {quantidade_a} vezes na string!')

else:
    print(f'A letra "a" nao aparece na string!')