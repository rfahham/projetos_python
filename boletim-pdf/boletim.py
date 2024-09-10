# pip3 install fpdf2
# pip install locate

# Precisa verificar se o locate está instalado no sistema

import locale
from fpdf import FPDF
from datetime import datetime

# Configurar o locale para Português do Brasil
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

ano = datetime.now().strftime("%Y")
data = datetime.now().strftime("%d de %B de %Y")

# Ler do arquivo dados.csv
nome_aluno = input('Nome do aluno: ')
nota1 = int(input('Nota do primeiro trimestre: '))
nota2 = int(input('Nota do segundo trimestre: '))
nota3 = int(input('Nota do terceiro trimestre: '))
nota4 = int(input('Nota do quarto trimestre: '))
media = (nota1+nota2+nota3+nota4)/4

if media >= 7:
    texto = f"Assunto: Parabéns! {nome_aluno} foi Aprovado !\n" \
            f"Prezados Pais/Responsáveis,\n" \
            f"É com grande satisfação que comunicamos que {nome_aluno} alcançou as notas necessárias para ser aprovado no ano letivo de {ano}.\n" \
            f"Durante o período escolar, {nome_aluno} demonstrou dedicação e esforço, resultando em um desempenho acadêmico notável. Agradecemos pelo apoio contínuo e pela colaboração na jornada educacional de {nome_aluno}.\n" \
            f"Estamos muito felizes com o progresso de {nome_aluno} e ansiosos para acompanhá-lo(a) em mais um ano de aprendizado e crescimento.\n" \
            f"Se houver qualquer dúvida ou se precisar de mais informações, não hesite em nos contatar.\n" \
            f"Atenciosamente,\n"
else:
    texto = f"Prezados Pais/Responsáveis,\n" \
            f"Informamos que, infelizmente, {nome_aluno} não alcançou as notas necessárias para ser aprovado no ano letivo de {ano}\n" \
            f"Apesar dos esforços de {nome_aluno} ao longo do ano, o desempenho acadêmico não foi suficiente para a aprovação nesta etapa. Recomendamos que se agende uma reunião para discutirmos os próximos passos e estratégias para apoiar {nome_aluno} em sua continuidade educacional.\n" \
            f"Estamos à disposição para fornecer mais detalhes e trabalhar juntos para ajudar {nome_aluno} a alcançar seus objetivos acadêmicos.\n" \
            f"Agradecemos pela compreensão e colaboração.\n" \

f"Atenciosamente,\n"

pdf = FPDF()
pdf.add_page()
pdf.image('hqa.png', 85, 8, 33)
pdf.ln(30)
pdf.set_font("helvetica", "B", 20)
pdf.ln(20)
pdf.set_font("helvetica", "B", 14)
pdf.multi_cell(190, 10, texto)

pdf.ln(5)
pdf.cell(180, 10, f"Rio de Janeiro, {data}", align="C")
pdf.ln(10)
pdf.cell(180, 10, "__________________________", align="C")
pdf.ln(5)
pdf.cell(180, 10, "Ricardo Fahham", align="C")
pdf.ln(5)
pdf.cell(180, 10, "Diretor", align="C")
pdf.ln(5)
pdf.cell(180, 10, "Hora do QA", align="C")
pdf.ln(5)
pdf.output(f"boletim-aluno-{nome_aluno}.pdf")