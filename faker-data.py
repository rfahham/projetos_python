# pip install faker

from faker import Faker

fake = Faker()

nome = fake.name()
primeiro_nome_feminino = fake.first_name_female()
primeiro_nome_masculino = fake.first_name_male()
usuario = fake.user_name()
senha = fake.password()
mes = fake.month()

print(f"Nome: {nome}")
print(f"Nome feminino: {primeiro_nome_feminino}")
print(f"Nome feminino: {primeiro_nome_masculino}")
print(f"Usuário: {usuario}")
print(f"Senha: {senha}")
print(f"Mês: {mes}")