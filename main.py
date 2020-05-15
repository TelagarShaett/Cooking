import galletas

a = "Galletas con chips de chocolate"
b = "Brownies de chocolate"
c = "Budin de limon"

listado =[a, b, c]

#innecesario encerrar entre parentesis
Recetas = ("a) Galletas con chips de chocolate" "\n" "b) Brownies de chocolate" "\n" "c) Budin de limon")


Comida = input ("Por favor, ingrese A, B o C a continuacion dependiendo de la receta que quiera preparar, si necesita ayuda ingrese la palabra `Recetas` o ingrese `salir`:  ")
Comida_m = Comida.lower()
print ("\n")
azucar_tipo_main =""

while (Comida_m != "salir"):
	if (Comida_m == "recetas"):
		#innecesario extraer el string para arriba
		print (Recetas)
		print ("\n")
	
	elif(Comida_m == "a"):
		azucar_tipo_main = galletas.Textura()
		print ("\n")
		galletas.Cantidades(azucar_tipo_main)

        
	elif(Comida_m == "b"):
		print ("La receta para " + listado[1] + " esta en contruccion")
		print ("\n")

	elif(Comida_m == "c"):
		print ("La receta para " + listado[2] + " esta en contruccion")
		print ("\n")

	else:
		print ("La opcion ingresada no es valida")
		print ("\n")

	Comida = input ("Por favor, ingrese A, B o C a continuacion dependiendo de la receta que quiera preparar, si necesita ayuda ingrese la palabra `Recetas`:  ")
	Comida_m = Comida.lower()
	print ("\n")

Salir = input ("Muchas gracias por probar el programa, pero se paso se vivo y por eso lo invito a escribir `salir` para terminar el programa: ")
print ("\n")

while (Salir != "salir"):
	Salir = input ("La opcion ingresada no es valida, por favor vuelta a intentarlo: ")
	print ("\n")
	