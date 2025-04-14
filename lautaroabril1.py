usuario=input("ingrese usuario:")
print("hola")
print(usuario)
matematica=0
lengua=0
quimica=0
fisica=0
materia=0

acsion=input("si desea ingresar el promedio de las materias ingrese (promedio)")


if acsion == ("promedio"):
 materia=input("selecsione la materia deseada:")

 if materia == ("matematica"):
  v3=int(input("primer nota de matematica:"))
  v1=int(input("segundo nota de matematica:"))
  v2=int(input("tercer nota de matematica:"))
  matematica= v1 + v2 + v3 // 3
  print("la nota de matematica es:")
  print(matematica)
 if quimica == ("quimica"):
  v3=int(input("primer nota de quimica:"))
  v1=int(input("segundo nota de quimica:"))
  v2=int(input("tercer nota de quimica:"))
  quimica= v1 + v2 + v3 // 3
  print("la nota de quimica es:")
  print(quimica)
 if lengua == ("lengua"):
  v3=int(input("primer nota de lengua:"))
  v1=int(input("segundo nota de lengua:"))
  v2=int(input("tercer nota de lengua:"))
  lengua= v1 + v2 + v3 // 3
  print("la nota de lengua es:")
  print(lengua)
 if fisica == ("fisica"):
  v3=int(input("primer nota de fisica:"))
  v1=int(input("segundo nota de fisica:"))
  v2=int(input("tercer nota de fisica:"))
  fisica= v1 + v2 + v3 // 3
  print("la nota de fisica es:")
  print(fisica)


