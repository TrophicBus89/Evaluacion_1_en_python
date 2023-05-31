C=0
Cnino=0
Cjoven=0
Cadulto=0
Ctotal=0
res=0
G=0
while res==0:
	nino=0
	joven=0
	adulto=0
	print("Bienvenido al Cine Morø, a continuación se mostrarán los precios de las entradas según las categorías:")
	print("")
	print("1) Niño    =   $5500 (1-13 años)")
	print("2) Joven   =   $7000 (14-21 años)")
	print("3) Adulto  =   $9000 (Mayor a 21 años)")
	print("")
	print("Ingrese la cantidad de entradas para grupo niño")
	nino=int(input())
	Cnino=Cnino+nino;
	print("Ingrese la cantidad de entradas para grupo joven")
	joven=int(input())
	Cjoven=Cjoven+joven
	print("Ingrese la cantidad de entradas para grupo adulto")
	adulto=int(input())
	Cadulto=Cadulto+adulto
	total=(nino*5500)+(joven*7000)+(adulto*9000);
	G=G+total
	print("")
	print("Categoría:")
	print("Niño   = ",nino)
	print("Joven  = ",joven)
	print("Adulto = ",adulto)
	print("Cantidad de entradas = ",(nino+joven+adulto))
	print("Total a pagar = $",total)
	print("Gracias por su compra, disfrute la función")
	print("")
	print("")
	print("¿Desea ingresar otro grupo de personas?")
	print("Ingrese 0 para ingresar a otro grupo / Ingrese 1 para cerrar la jornada y mostrar resultados")
	res=int(input())
	print("")
	print("__________________________________________________________________________________________________________")
	print("")
#Total de gente durante toda la jornada
Ctotal=Cnino+Cjoven+Cadulto
#Porcentajes de niños, jovenes y adultos respectivamente
pn=Cnino*100/Ctotal
pj=Cjoven*100/Ctotal
pa=Cadulto*100/Ctotal
print("//FINAL DE JORNADA//")
print("")
print("Entradas vendidas por categoría:")
print("Niño   = ",Cnino," entradas (",int(pn),"%)")
print("Joven  = ",Cjoven," entradas (",int(pj),"%)")
print("Adulto = ",Cadulto," entradas (",int(pa),"%)")
print("")
print("Ganancia por categorías:")
print("Niño   = $",(Cnino*5500))
print("Joven  = $",(Cjoven*7000))
print("Adulto = $",(Cadulto*9000))
print("")
print("Ganancia total = $", G)