import funciones

def Cantidades(azucar_tipo_main):
       

	ingredientes = {"azucar blanca: ": 340 , "azucar marron: ": 250 , "manteca: ": 340 , "harina 0000 leudante: ": 625 , "sal: ": 1.5 , "polvo de hornear: ": 1, "bicarbonato de sodio: ": 1 , "esencia de vainilla: ": 1, "huevos: ": 2, "yema de huevo: ": 2, "chocolate cobertura: ": 450  }

	ingredientes_alt = {}

	Unidades = 24


	print ("Los ingredientes para estas galletas con chips de chocolate (sin modificar la textura original) son los siguientes: ", "\n")

	for key, value in ingredientes.items():

		print(key, value, "\n")

	print("Estas medidas de ingredientes alcanzan para hacer ", Unidades ," galletas hechas con un scoop de helado de 3 pulgadas o 7.5cm.", "\n")
	Cantidad = input ("Desea modificar la cantidad?: ")
	print ("\n")

	while(Cantidad != "si" and Cantidad != "no"):

		Cantidad = input ("Desea modificar la cantidad?: ")
		print ("\n")


	if (Cantidad == "no"):
        
		Unidades_Alt = 24
		
		for key, value in ingredientes.items():

			ing_alt = funciones.ingALT(Unidades_Alt,value,Unidades)
			ingredientes_alt [key] = ing_alt
        
		if (azucar_tipo_main == "azucar blanca: "):
            
			for key in ingredientes:
                
				if (key == "azucar marron: "):
                    
					ingredientes_alt["azucar blanca: "] = funciones.azucALT(ingredientes_alt["azucar blanca: "], ingredientes_alt["azucar marron: "])
					del ingredientes_alt ["azucar marron: "]
                    
		elif (azucar_tipo_main == ""):
            
			azucar_tipo_main == ""
            
		else:
            
			for key in ingredientes:
                
				if (key == "azucar blanca: "):
                    
					ingredientes_alt["azucar negra: "] = funciones.azucALT(ingredientes_alt["azucar blanca: "], ingredientes_alt["azucar marron: "])
					del ingredientes_alt ["azucar marron: "]
					del ingredientes_alt ["azucar blanca: "]
                
		print("\n")
		print("Los ingredientes alterados tanto en cantidad como textura son los siguientes: ")
		for key, value in ingredientes_alt.items():

			print("\n", key, value)

		with open ("prepnormal.txt", "r") as file:
			text1 = file.read()
		print (text1)
	 
		with open ("coccnormal.txt", "r") as file:
			text2 = file.read()
		print(text2)

	elif (Cantidad == "si"):

		Unidades_Alt = int(input ("Para cuantas unidades desea ajustar la receta?: "))
		
		for key, value in ingredientes.items():

			ing_alt = funciones.ingALT(Unidades_Alt,value,Unidades)
			ingredientes_alt [key] = ing_alt
        
		if (azucar_tipo_main == "azucar blanca: "):
            
			for key in ingredientes:
                
				if (key == "azucar marron: "):
                    
					ingredientes_alt["azucar blanca: "] = funciones.azucALT(ingredientes_alt["azucar blanca: "], ingredientes_alt["azucar marron: "])
					del ingredientes_alt ["azucar marron: "]
                    
		elif (azucar_tipo_main == ""):
            
			azucar_tipo_main == ""
            
		else:
            
			for key in ingredientes:
                
				if (key == "azucar blanca: "):
                    
					ingredientes_alt["azucar negra: "] = funciones.azucALT(ingredientes_alt["azucar blanca: "], ingredientes_alt["azucar marron: "])
					del ingredientes_alt ["azucar marron: "]
					del ingredientes_alt ["azucar blanca: "]
                
		print("\n")
		print("Los ingredientes alterados tanto en cantidad como textura son los siguientes: ")
		for key, value in ingredientes_alt.items():

			print("\n", key, value)


	Confirmar_cant = input("Desea ajustar la receta?: ")
	print ("\n")

	while (Confirmar_cant != "no" and Confirmar_cant != "si"):

		Confirmar_cant = input("Desea ajustar la receta?: ")
		print ("\n")

	while (Confirmar_cant == "si"):

		Unidades_Alt = int(input ("Para cuantas unidades desea ajustar la receta?: "))
		
		for key, value in ingredientes.items():

			ing_alt = funciones.ingALT(Unidades_Alt,value,Unidades)
			ingredientes_alt [key] = ing_alt

		for key, value in ingredientes_alt.items():

			print("\n", key, value)

		Confirmar_cant = input("Desea volver a ajustar la receta?: ")
		print ("\n")

		while (Confirmar_cant != "no" and Confirmar_cant != "si"):

			Confirmar_cant = input("Desea volver a ajustar la receta?: ")
			print ("\n")

	if (Confirmar_cant == "no"):

		with open ("prepnormal.txt", "r") as file:
			text1 = file.read()
		print (text1)
	 
		with open ("coccnormal.txt", "r") as file:
			text2 = file.read()
		print(text2)
		print(ingredientes.get("azucar blanca: "))

	
def Textura():
    
    azucar_tipo = ""
    confirmacion_m = ""    

    while(confirmacion_m != "continuar"):
        print("\n")
        print("Las texturas posibles para las galletas son las siguientes: " "\n""\n" "a) Crocantes" "\n" "b) intermedias" "\n" "c) Suaves")
        textura_galleta = input("Ingrese la opcion deseada o ingrese `atras` para volver a la seleccion de recetas: ")
        textura_galleta_m = textura_galleta.lower()
         
        
        while(textura_galleta_m == "a" or textura_galleta_m == "b" or textura_galleta_m == "c"):
    
            if (textura_galleta_m == "a"):
           
                azucar_tipo = "azucar blanca: "
                textura_galleta_m = ""

            
            elif (textura_galleta_m == "b"):
        
                textura_galleta_m =""
    
            elif (textura_galleta_m == "c"):
        
                azucar_tipo = "azucar negra: "  
                textura_galleta_m =""
                            
    
            confirmacion = input("Si esta seguro de su eleccion, ingrese `continuar` o  `atras` para volver a la seleccion de recetas: ")
            confirmacion_m = confirmacion.lower()
            
            
    return(azucar_tipo)
           
        

#§revisar y debugear lo que queda