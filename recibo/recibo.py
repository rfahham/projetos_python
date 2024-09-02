# https://www.4devs.com.br/gerador_de_cpf
# https://pyfpdf.github.io/fpdf2/Tutorial-pt.html

# pip3 install fpdf2

from fpdf import FPDF
from datetime import datetime

print()
print('{:-^40}'.format(''))
print('{:-^40}'.format(' RECIBO '))
print('{:-^40}'.format(''))
print()

recebedor_nome = input('Nome do recebedor: ')
recebedor_cpf = input('CPF do recebedor: ')

pagador_nome = input('Nome do pagador: ')
pagador_cpf = input('CPF do pagador: ')

servico = input('Serviço realizado: ')
valor = input('Valor do Serviço realizado: ')
tipo = input('Forma de pagamento: ')

texto = f'Pelo presente, eu {recebedor_nome}, inscrito no CPF sob número {recebedor_cpf},\
 declaro que RECEBI na data de hoje, o valor de R$ {valor}, por meio de {tipo},\
 de {pagador_nome}, inscrito no CPF sob número {pagador_cpf}, referente a {servico}.'

pdf = FPDF()
pdf.add_page()
pdf.image('starwars_yoda.png', 85, 8, 33)
pdf.ln(40)
pdf.set_font("helvetica", "B", 20)
pdf.cell(180, 10, "RECIBO", align="C")
pdf.ln(20)
pdf.set_font("helvetica", "", 14)
pdf.multi_cell(190, 10, texto)

pdf.ln(20)
pdf.cell(180, 10, "Sendo expressão de verdade e sem qualquer coação, firmo o presente.")

pdf.ln(20)
pdf.cell(180, 10, "Rio de Janeiro, _____ de ______________ de 20___", align="C")

pdf.ln(20)
pdf.cell(180, 10, "_________________________________", align="C")
pdf.ln(10)
pdf.cell(180, 10, recebedor_nome, align="C")

pdf.output("recibo.pdf")

print(texto)
