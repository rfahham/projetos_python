import time

cores = {
			'limpa':'\033[m',
			'vermelho':'\033[31m',
			'verde':'\033[32m',
			'amarelo':'\033[33m',
			'azulescuro':'\033[34m',	
			'roxo':'\033[35m',
			'azulclaro':'\033[36m',	
			'pretoebranco':'\033[7;30m',	
        }

print('-'*16)
print('Starting Hack...')
print('-'*16)
print()

target = 0 

while target <= 100:
	print('\033[32m' 'Hacking FBI', target, '%' '\033[m')
	target = target + 10
	time.sleep(1)

print()
print('System hacked with success!!!')
print()
