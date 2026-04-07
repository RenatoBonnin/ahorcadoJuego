import random, json, os

#JSON CON LAS PALABRAS QUE SE USAN EN EL JUEGO

ruta = "grupos.json"

def ejecutarArchivo():
    if not os.path.exists(ruta):
        with open(ruta, "w") as f: 
            json.dump([], f)

def modificarArchivo(archivoNuevo):
    with open(ruta, "w") as f:
        f.seek(0)
        json.dump(archivoNuevo, f)
        f.truncate()

def leerArchivo():
    with open(ruta, "r") as f:
        archivo = json.load(f)
        return archivo

#FUNCIONES PARA LA PRIMERA PARTE DE DEF JUEGO(). ASIGNAN UNA PALABRA RANDOM DE LA LISTA

def asignarPalabraAdiv(palabra):
	palabraAdiv = ""
	for letra in palabra:
		palabraAdiv = palabraAdiv + "_"
	return palabraAdiv

def asignarPalabraRandom(listaPalabras):
	palabra = random.choice(listaPalabras)
	return palabra

#INICIALIZACIÓN DEL JUEGO Y BUCLE PRINCIPAL

def juego(listaPalabras):
	vic = False
	contErrores = 7
	palabra = asignarPalabraRandom(listaPalabras)
	palabraAdiv = asignarPalabraAdiv(palabra)
	
	while not vic and contErrores > 0:
		
		mostrarCiclo(palabraAdiv, contErrores)
	
		letraAdiv = input("INGRESE UNA LETRA: ").upper()
		
		palabraAdiv = list(palabraAdiv)
		
		error = letraALetra(palabra, palabraAdiv, letraAdiv)
		
		contErrores = siErrores(error, contErrores)
			
		palabraAdiv = listaToString(palabraAdiv)	
	
		vic = verificarEstado(palabra, palabraAdiv, contErrores)

#FUNCIONES USADAS DENTRO DEL BUCLE PRINCIPAL

def mostrarPalabraAdiv(palabraAdiv):
	print("PALABRA A ADIVINAR: ", palabraAdiv)
	
def mostrarErrores(contErrores):
	print("ERRORES RESTANTES: ", contErrores)
	
def mostrarCiclo(palabraAdiv, contErrores):
	mostrarPalabraAdiv(palabraAdiv)
	mostrarErrores(contErrores)

def letraALetra(palabra, palabraAdiv, letraAdiv):
	error = True
	i = 0
	for letra in palabra:
		if letraAdiv == letra:
			error = False
			palabraAdiv[i]= letra
		i += 1
	return error

def listaToString(string):
	return "".join(string)

def siErrores(error, contErrores):
	if error:
		contErrores -= 1
	return contErrores

def condVictoria(palabra, palabraAdiv):
	if palabra == palabraAdiv:
		print("GANASTE!!! :)")
		mostrarPalabra(palabra)
		input()
		return True

def condMuerte(contErrores, palabra):
	if contErrores <= 0:
		print("PERDISTE :(")
		mostrarPalabra(palabra)
		input()
	
def mostrarPalabra(palabra):
	print("LA PALABRA ERA: ", palabra)
								
def verificarEstado(palabra, palabraAdiv, contErrores):
	condMuerte(contErrores, palabra)
	return condVictoria(palabra, palabraAdiv)

#MENU DE CONFIGURACIÓN

def config(listaPalabras):
	
	op = 8
	
	while op != "0":
		print("0 - SALIR")
		print("1 - LISTAR PALABRAS")
		print("2 - AGREGAR PALABRA")
		print("3 - ELIMINAR PALABRA")
		op = input("SELECCIONE UNA OPCION: ")
		match op:
			case "1":
				listarPalabras(listaPalabras)
			case "2":
				agregarPalabra(listaPalabras)
			case "3":
				if listaPalabras:
					eliminarPalabra(listaPalabras)
				else:
					print("LISTA VACIA")
			case _:
				if op != "0":
					print("OPCION INVALIDA")
	
	modificarArchivo(listaPalabras)
	
#FUNCIONES PARA CONFIG	
	
def listarPalabras(listaPalabras):
	for palabra in listaPalabras:
		print(palabra)

def agregarPalabra(listaPalabras):
	nuevaPalabra = input("NUEVA PALABRA: ").upper()
	listaPalabras.append(nuevaPalabra)

def eliminarPalabra(listaPalabras):
	palabra = input("INGRESE PALABRA A ELIMINAR: ").upper()
	if palabra in listaPalabras:
		listaPalabras.remove(palabra)
	else:
		input("PALABRA NO ENCONTRADA")
		
#CUERPO PRINCIPAL

ejecutarArchivo()

listaPalabras = leerArchivo()
op =8

while op != "0":
	print("0 - SALIR")
	print("1 - JUGAR")
	print("2 - CONFIGURACION")
	op = input("SELECCIONE UNA OPCION: ")
	match op:
		case "1":
			if listaPalabras:
				juego(listaPalabras)
			else:
				print("LISTA VACIA")
		case "2":
			config(listaPalabras)
		case _:
			if op != "0":
				print("OPCION INVALIDA")
	
	