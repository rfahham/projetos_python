print('-_'*20)
print('Analizador de Triângulo')
print('-_'*20)
print('')

print('Triângulo Escaleno - Triângulos escalenos são aqueles que possuem os três lados diferentes e, consequentemente, três ângulos internos diferentes.')
print('Triângulo Isóceles - Triângulos isósceles são aqueles que possuem dois lados iguais (mesmo comprimento) e um diferente.Geralmente o lado diferente é a base do triângulo, caso em que os ângulos da base serão iguais.')
print('Triângulo Retângulo - Triângulos retângulos são aqueles que possuem um ângulo reto, ou seja, um ângulo de exatamente 90°. Nos triângulos retângulos, o lado oposto ao ângulo reto se chama hipotenusa e os outros lados se chamam catetos. Os demais ângulos são agudos e complementares, pois sua soma é igual a 90°.')
print('Triângulo Acutângulo - Triângulos acutângulos são aqueles que possuem os três ângulos agudos, ou seja, menores que 90°.')
print('Triângulo Obtusângulo - Triângulos obtusângulos são aqueles que possuem um ângulo obtuso, ou seja, um ângulo maior que 90°.')
print('Triângulo Equilátero - Triângulos equiláteros são aqueles que possuem os três lados iguais (mesmo comprimento) e, consequentemente, três ângulos internos iguais de 60°. Pode ser chamado de equiângulo.')
print('')

r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
	print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
