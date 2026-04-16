import random, json, os

#JSON CON LAS PALABRAS QUE SE USAN EN EL JUEGO

ruta = "ahorcadito.json"

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
	letrasUsadas = []

	while not vic and contErrores > 0:
		
		mostrarCiclo(palabraAdiv, contErrores)

		letrasUsadas.sort()

		listarLetrasUsadas(letrasUsadas)

		letraAdiv = input("INGRESE UNA LETRA: ").upper()
		
		if letraAdiv not in letrasUsadas:
			
			letrasUsadas.append(letraAdiv)

			palabraAdiv = list(palabraAdiv)
			
			error = letraALetra(palabra, palabraAdiv, letraAdiv)
			
			contErrores = siErrores(error, contErrores)
				
			palabraAdiv = listaToString(palabraAdiv)	
		
			vic = verificarEstado(palabra, palabraAdiv, contErrores)
		
		else: 
			print("LETRA YA USADA")

#FUNCIONES USADAS DENTRO DEL BUCLE PRINCIPAL

def mostrarPalabraAdiv(palabraAdiv):
	print("PALABRA A ADIVINAR: ", palabraAdiv)
	
def mostrarErrores(contErrores):
	print("ERRORES RESTANTES: ", contErrores)
	
def mostrarCiclo(palabraAdiv, contErrores):
	mostrarPalabraAdiv(palabraAdiv)
	mostrarErrores(contErrores)

def listarLetrasUsadas(letrasUsadas):
	print(*letrasUsadas)

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
	print(*listaPalabras)

def listarPalabrasUI(listaPalabras):
	texto = ""
	i = 1
	for palabra in listaPalabras:
		
		if len(listaPalabras) == i:
			texto += f"{palabra}"
		else:
			texto += f"{palabra}, "
		i += 1
	return texto

def agregarPalabra(listaPalabras):
	nuevaPalabra = input("NUEVA PALABRA: ").upper()
	listaPalabras.append(nuevaPalabra)

def limpiar_espacios(texto):
    # strip() elimina espacios al inicio y final de la cadena
    # split() separa por cualquier cantidad de espacios
    # join() une las palabras con un solo espacio
    return " ".join(texto.strip().split())

def esPalabraValida(palabra):
	for letra in palabra:
		if not (letra.isalpha() or letra.isspace()):
			return False
	return True
		
def agregarPalabraUI(listaPalabras, palabraNueva):
	limpiar_espacios(palabraNueva)
	if len(palabraNueva) != 1 and esPalabraValida(palabraNueva):
		palabraNueva = palabraNueva.upper()
		listaPalabras.append(palabraNueva)
		return (True, False)
	else: 
		if not esPalabraValida(palabraNueva):
			return (False, True)
		else:	
			return (False, False)

def eliminarPalabra(listaPalabras):
	palabra = input("INGRESE PALABRA A ELIMINAR: ")
	if palabra in listaPalabras:
		listaPalabras.remove(palabra)
	else:
		input("PALABRA NO ENCONTRADA")

def eliminarPalabraUI(listaPalabras, palabraEliminar):
	limpiar_espacios(palabraEliminar)
	palabraEliminar = palabraEliminar.upper()
	if palabraEliminar in listaPalabras:
		listaPalabras.remove(palabraEliminar)
		return True
	else:
		return False

#CUERPO PRINCIPAL
"""
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
"""