#Olá, vamos montar um acampamento!

#Aqui tem as coisas que vamos precisar:

coisas_acampamento = "tenda, sacos de dormir, água, café, faca, morangos, cabo ethernet, flash drive, marshmallows, escova de dentes, pasta, pão, suco, garrafa, jogos de tabuleiro, toalha, cesta."

#LISTA PYTHON

suprimentos = ["tenda","sacos de dormir","água","café","faca","morangos","cabo ethernet","flash drive","marshmallows","escova de dentes","pasta","pão","suco","garrafa","jogos de tabuleiro","toalha","cesta"]

acampamento_local = ["Lago de Cristal", 317, 128.5]

#Caramba! Levar tudo isso fica muito pesado, vamos remover algumas coisas:

del (suprimentos[9])
del (suprimentos[9])
del (suprimentos[12])

print ("Ok. Vamos levar " + str(suprimentos) + ", acho que não vai ficar tão pesado assim.\n")
print ("Só preciso ver o lugar, hmm, vamos ver. Aqui, o lugar do acampamento será no " + str(acampamento_local) + ".\nParece um lugar bom.\n")
