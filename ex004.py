entrada = input('Digite algo »')
print('O que voce digitou foi {}, e do tipo {}'.format(entrada,type(entrada)))
print('É um numero? ', entrada.isalnum())
print('Só tem espeço? ', entrada.isspace())