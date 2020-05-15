import funciones

def confirmarIngredientes(ingredientes):
	return input("Desea modificar la cantidad de unidades?: ")

def mostrarReceta():
	with open ("prepnormal.txt", "r") as file:
		text1 = file.read()
		print(text1)
	
	with open ("coccnormal.txt", "r") as file:
		text2 = file.read()
		print(text2)

def modificarAzucares(tipoAzucar, ingredientes):
	if (tipoAzucar == "azucar blanca: "):
		ingredientes["azucar blanca: "] = funciones.azucALT(ingredientes["azucar blanca: "], ingredientes["azucar marron: "])
		del ingredientes["azucar marron: "]

	elif(tipoAzucar == "azucar negra: "):
		ingredientes["azucar negra: "] = funciones.azucALT(ingredientes["azucar blanca: "], ingredientes["azucar marron: "])
		del ingredientes["azucar marron: "]
		del ingredientes["azucar blanca: "]
	
	return ingredientes

def mostrarIngredientes(ingredientes, unidades):
	for key, value in ingredientes.items():
		print(key + str(value))
	print("Estas medidas de ingredientes alcanzan para hacer ", unidades ," galletas hechas con un scoop de helado de 3 pulgadas o 7.5cm.", "\n")
	print("\n")

def Cantidades(azucar_tipo_main):
	ingredientes = {"azucar blanca: ": 340 , "azucar marron: ": 250 , "manteca: ": 340 , "harina 0000 leudante: ": 625 , "sal: ": 1.5 , "polvo de hornear: ": 1, "bicarbonato de sodio: ": 1 , "esencia de vainilla: ": 1, "huevos: ": 2, "yema de huevo: ": 2, "chocolate cobertura: ": 450  }
	ingredientes_alt = {}
	Unidades = 24

	print("Los ingredientes para estas galletas con chips de chocolate (sin modificar la textura original) son los siguientes: ", "\n")
	mostrarIngredientes(ingredientes, Unidades)

	confirmacionUsuario = confirmarIngredientes(ingredientes)

	while(confirmacionUsuario != "n"):
		if(confirmacionUsuario == "n"):
			ingredientes_alt = ingredientes
			ingredientes_alt = modificarAzucares(azucar_tipo_main, ingredientes_alt)
		elif(confirmacionUsuario == "s"):
			unidadesAlt = int(input ("Para cuantas unidades desea ajustar la receta?: "))
			ingredientes_alt =  Cant_Textura(azucar_tipo_main, ingredientes, unidadesAlt, Unidades, ingredientes_alt)
			ingredientes_alt = modificarAzucares(azucar_tipo_main, ingredientes_alt)
			mostrarIngredientes(ingredientes_alt, unidadesAlt) 
		else:
			print("ingrese 'si' o 'no'")

		confirmacionUsuario = confirmarIngredientes(ingredientes)

	mostrarReceta()

def Textura():
    
    azucar_tipo = ""
    confirmacion = ""    

    while(confirmacion.lower() != "continuar" and confirmacion.lower() != "c"):
        print("\n")
        print("Las texturas posibles para las galletas son las siguientes: " "\n""\n" "a) Crocantes" "\n" "b) intermedias" "\n" "c) Suaves")
        textura_galleta = input("Ingrese la opcion deseada o ingrese `atras` para volver a la seleccion de recetas: ")
        textura_galleta_m = textura_galleta.lower()
        print(textura_galleta)

		#la opcion B, al ser default, no esta considerada en estas condiciones
        if(textura_galleta_m == "a"):
            azucar_tipo = "azucar blanca: "     
        elif (textura_galleta_m == "c"):
            azucar_tipo = "azucar negra: "  
                            
        if (textura_galleta_m == "a" or textura_galleta_m == "b" or textura_galleta_m == "c"):
            confirmacion = input("Si esta seguro de su eleccion, ingrese `[c]ontinuar` o  `[a]tras` para volver a la seleccion de recetas: ")
            print(confirmacion)
            
    return(azucar_tipo)

def Cant_Textura(azucar_tipo_main, ingredientes, Unidades_Alt, Unidades, ingredientes_alt):

	#En el caso de haber unidades alternativas, modifico las cantidades de ingredientes
	for key, value in ingredientes.items():
		ing_alt = funciones.ingALT(Unidades_Alt,value,Unidades)
		ingredientes_alt[key] = ing_alt 
    
	return(ingredientes_alt)