if inicio < 1 or inicio > 24:    
  print("hora inicial inválida")

if fim < 1 or fim > 24:    
  print("hora final inválida")
else:    
  if fim > inicio:        
    print("O tempo da partida foi de",fim-inicio,"hora(s)")    
  if fim < inicio:        
    print("O tempo de partida foi de ", 24-inicio+fim,"hora(s)")