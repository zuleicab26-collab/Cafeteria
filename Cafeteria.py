def menu():
 print("************MENU***********")
 print("a. Donas")
 print("b. Bebidas")
 print("c. Combos")
 print("d. Salir / Ver factura")

def donas(factura):
 print("*****************DONAS*****************")
 print("a. Dona clásica ................. $2.00")
 print("b. Dona de chocolate ............ $2.50")
 print("c. Dona de manjar ............... $2.50")
 pedido = input("Ingrese su pedido: ")
 cantidad = int(input("Ingrese la cantidad que desee adquirir:"))

 if pedido == "a":
  factura = factura + 2.00 * cantidad
 elif pedido == "b":
  factura = factura + 2.50 * cantidad
 elif pedido == "c":
  factura = factura + 2.50 * cantidad
 else:
  print("Opción no válida.")
 return factura

def bebidas(factura):
 print("****************BEBIDAS****************")
 print("a. Café Americano ............... $2.75")
 print("b. Chocolate caliente ........... $1.50")
 print("c. Capuccino .................... $2.00")
 print("d. Ice Coffee ................... $2.75")
 pedido = input("Ingrese su pedido: ")
 cantidad = int(input("Ingrese la cantidad que desee adquirir:"))

 if pedido == "a":
  factura = factura + 2.75 * cantidad
 elif pedido == "b":
  factura = factura + 1.50 * cantidad
 elif pedido == "c":
  factura = factura + 2.00 * cantidad
 elif pedido == "d":
  factura = factura + 2.75 * cantidad
 else:
  print("Opción no válida.")
 return factura

def combos(factura):
 print("*****************COMBOS****************")
 print("a. Combo Individual ............. $4.50")
 print("b. Combo Duo .................... $8.00")
 pedido = input("Ingrese su pedido:")
 cantidad = int(input("Ingrese la cantidad que desa adquirir:"))

 if pedido == "a":
  factura = factura + 4.50 * cantidad
 elif pedido == "b":
  factura = factura + 8.00 * cantidad
 else:
  print("Opción no válida.")
 return factura


def factura_final(factura, nombre, cedula):

 print("Seleccione su método de pago")
 print("1. Efectivo")
 print("2. Tarjeta")
 print("3. Transferencia")
 metodo = input("Seleccione una opción:")

 if metodo == "1":
  print("Pago en efectivo")
 elif metodo == "2":
  print("Pago con tarjeta")
 elif metodo == "3":
  print("Pago por transferencia")
 else:
  print("Su método de pago no es válido.")
 confirmar = input("¿Desea confirmar el pedido? (a = Sí / b = No):")

 if confirmar == "a":
  subtotal = factura
  iva = subtotal * 0.15
  total = subtotal + iva

  print("*************FACTURA*************")
  print("Cliente:", nombre)
  print("CI/RUC:", cedula)
  print("Subtotal: $", subtotal)
  print("IVA (15%): $", iva)
  print("TOTAL: $", total)
  print("Gracias por visitarnos", nombre)

 elif confirmar == "b":
  print("Su pedido ha sido cancelado.")
  print("Gracias por visitarnos,", nombre)


factura = 0
print("Antes de comenzar con su pedido, por favor ingrese su información")

nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su CI/RUC: ")

print("Sea bienvenido a Pink Dream,", nombre)
print("Momentos instagrameables, sabores inolvidables")

while True:
  menu()
  opcion = input("Por favor seleccione una opción:")

  if opcion == "a":
   factura = donas(factura)
  elif opcion == "b":
   factura = bebidas(factura)
  elif opcion == "c":
   factura = combos(factura)
  elif opcion == "d":
   break
  else:
   print("Opción no válida, por favor ingrese una de las opciones del menú")
if factura > 0:
    factura_final(factura, nombre, cedula)
else:
    print("Gracias, vuelva pronto", nombre)