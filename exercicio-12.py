numeroeleitores=int(input("Digite o numero de eleitores:"))
brancos=int(input("Digite o numero de votos brancos:"))
nulos=int(input("Digite o número de votos nulos:"))
validos=numeroeleitores-(brancos+nulos)
porcentbrancos=(brancos/numeroeleitores)*100
porcentnulos=(nulos/numeroeleitores)*100
porcentvalidos=(validos/numeroeleitores)*100
print("A porcentagem de votos brancos é:",porcentbrancos,"%")
print("A porcentagem de votos nulos é:",porcentnulos,"%")
print("A porcentagem de votos válidos é:",porcentvalidos,"%")
