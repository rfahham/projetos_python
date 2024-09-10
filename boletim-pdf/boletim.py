# pip3 install fpdf2
from fpdf import FPDF
from datetime import datetime

nome_aluno = input('Nome do aluno: ')
ano_letivo = 2024

nota1 = int(input('Nota do primeiro bimestre: '))
nota2 = int(input('Nota do segundo bimestre: '))
nota3 = int(input('Nota do terceiro bimestre: '))
nota4 = int(input('Nota do quarto bimestre: '))
media = (nota1+nota2+nota3+nota4)/4

if media >= 7:
    texto = f"Assunto: Parabéns! {nome_aluno} foi Aprovado !\n" \
            f"Prezados Pais/Responsáveis,\n" \
            f"É com grande satisfação que comunicamos que {nome_aluno} alcançou as notas necessárias para ser aprovado no ano letivo de {ano_letivo}.\n" \
            f"Durante o período escolar, {nome_aluno} demonstrou dedicação e esforço, resultando em um desempenho acadêmico notável. Agradecemos pelo apoio contínuo e pela colaboração na jornada educacional de {nome_aluno}.\n" \
            f"Estamos muito felizes com o progresso de {nome_aluno} e ansiosos para acompanhá-lo(a) em mais um ano de aprendizado e crescimento.\n" \
            f"Se houver qualquer dúvida ou se precisar de mais informações, não hesite em nos contatar.\n" \
            f"Atenciosamente,\n"
else:
    texto = f"Prezados Pais/Responsáveis,\n" \
            f"Informamos que, infelizmente, {nome_aluno} não alcançou as notas necessárias para ser aprovado no ano letivo de {ano_letivo}\n" \
            f"Apesar dos esforços de {nome_aluno} ao longo do ano, o desempenho acadêmico não foi suficiente para a aprovação nesta etapa. Recomendamos que se agende uma reunião para discutirmos os próximos passos e estratégias para apoiar {nome_aluno} em sua continuidade educacional.\n" \
            f"Estamos à disposição para fornecer mais detalhes e trabalhar juntos para ajudar {nome_aluno} a alcançar seus objetivos acadêmicos.\n" \
            f"Agradecemos pela compreensão e colaboração.\n" \

f"Atenciosamente,\n"

pdf = FPDF()
pdf.add_page()
pdf.image('harvard-university.png', 85, 8, 33)
pdf.ln(40)
pdf.set_font("helvetica", "B", 20)
pdf.ln(20)
pdf.set_font("helvetica", "", 14)
pdf.multi_cell(190, 10, texto)

pdf.ln(5)
pdf.cell(180, 10, "Rio de Janeiro, 10 de agosto de 2024", align="C")
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

print(texto)