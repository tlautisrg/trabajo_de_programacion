def pedir_nota(materia, nro_nota):
    while True:
        try:
            nota = int(input(f"{nro_nota} nota de {materia}:"))
            if 0 <= nota <= 10:
                return nota
            else:
                print("si vas a mentir almenos que sea creible usa numeros del 1 al 10")
        except ValueError:
            print("si vas a mentir almenos que sea creible usa numeros del 1 al 10")

usuario=input("ingrese usuario:")
print("hola")
print(usuario)
matematica=0
lengua=0
quimica=0
fisica=0
materia=0
continiu="true"

acsion=input("si desea ingresar las notas de las materias ingrese (promedio)")

while True: 

 if acsion == ("promedio") and continiu==("true"):
  materia=input("selecsione la materia deseada(matematica)(quimica)(lengua)(fisica):")

 if materia == ("matematica"):
  v3=pedir_nota("matematica", "primer")
  v1=pedir_nota("matematica", "segundo")
  v2=pedir_nota("matematica", "tercer")
  matematica= (v1 + v2 + v3 )// 3
  print("la nota de matematica es:")
  print(matematica)
 if materia == ("quimica"):
  v3=pedir_nota("quimica", "primer")
  v1=pedir_nota("quimica", "segundo")
  v2=pedir_nota("quimica", "tercer")
  quimica= (v1 + v2 + v3) // 3
  print("la nota de quimica es:")
  print(quimica)
 if materia == ("lengua"):
  v3=pedir_nota("lengua", "primer")
  v1=pedir_nota("lengua", "segundo")
  v2=pedir_nota("lengua", "tercer")
  lengua= (v1 + v2 + v3) // 3
  print("la nota de lengua es:")
  print(lengua)
 if materia == ("fisica"):
  v3=pedir_nota("fisica", "primer")
  v1=pedir_nota("fisica", "segundo")
  v2=pedir_nota("fisica", "tercer")
  fisica= (v1 + v2 + v3) // 3
  print("la nota de fisica es:")
  print(fisica)
 continiu=input("desea continuar si es si esctiba (true) si es no escriba (false):")
 if continiu==("false"):
  break

print("nota de matematica:")
print(matematica)
print("nota de fisica:")
print(fisica)
print("nota de quimica:")
print(quimica)
print("nota de lengua:")
print(lengua)

