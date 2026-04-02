import random

def asignarPalabraAdiv(palabra = "HOMBRE"):
	palabraAdiv = ""
	for letra in palabra:
		palabraAdiv = palabraAdiv + "_"
	return palabraAdiv

def asignarPalabraRandom(listaPalabras):
	palabra = random.choice(listaPalabras)
	return palabra

def juego(listaPalabras):
	vic = False
	contErrores = 0
	palabra = asignarPalabraRandom(listaPalabras)
	print(palabra)
	input()
	palabraAdiv = asignarPalabraAdiv(palabra)
	while not vic and contErrores < maxFallos:
		print("PALABRA A ADIVINAR: ", palabraAdiv) 
		print("ERRORES: ", contErrores)
		letraAdiv = input("INGRESE UNA LETRA: ").upper()
		i = 0
		error = True
		palabraAdiv = list(palabraAdiv)
		for letra in palabra:
			if letraAdiv == letra:			
				error = False
				palabraAdiv[i] = letra
			i += 1
		
		contErrores = siErrores(error, contErrores)
			
		palabraAdiv = listaToString(palabraAdiv)	
	
		vic = verificarEstado(palabra, palabraAdiv, contErrores)

def listaToString(string):
	return "".join(string)

def siErrores(error, contErrores):
	if error:
		contErrores += 1
	return contErrores

def condVictoria(palabra, palabraAdiv):
	if palabra == palabraAdiv:
		input("VICTORIA!!!")
		return True

def condMuerte(contErrores):
	if contErrores >= maxFallos:
		input("PERDISTE :(")
		
def verificarEstado(palabra, palabraAdiv, contErrores):
	condMuerte(contErrores)
	return condVictoria(palabra, palabraAdiv)

listaPalabras = ["CONJUNTO", "HOMBRE"]
maxFallos = 4

op =8
while op != "0":
	print("0 - SALIR")
	print("1 - JUGAR")
	print("2 - CONFIGURACION")
	op = input("SELECCIONE UNA OPCION: ")
	match op:
		case "1":
			juego(listaPalabras)
		case "2":
			pass
		case _:
			if op != "0":
				print("OPCION INVALIDA")
	