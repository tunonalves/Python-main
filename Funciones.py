def imprime_mensaje():
	print("Hola")
	print("Mundo")
	print("Python")

imprime_mensaje()

print("Fin de la funcion")

def imprime_mensaje2():
	return "Devolucion"

print(imprime_mensaje2())

valor_mensaje = imprime_mensaje2()

print(valor_mensaje)

def imprime_mensaje_personalizado(mensaje,valor1,valor2):
	return mensaje + str((valor1 + valor2))

print(imprime_mensaje_personalizado("La suma es: ",5,7))