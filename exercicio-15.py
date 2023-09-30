numero1=float(input("Insira o primeiro numero:"))
numero2=float(input("Insira o segundo numero:"))

while numero1==numero2:    
  numero1=float(input("Numeros não podem ser iguais, por favor insira novamente\n"                        
  "Insira o primeiro número:"))
  numero2 = float(input("Insira o segundo número:"))
  
  if numero1<numero2:    
    print(numero1, numero2)
  else:    
    print(numero2, numero1)

inicio=int(input("Insira a hora inicial:"))
fim=int(input("Insira a hora final:"))