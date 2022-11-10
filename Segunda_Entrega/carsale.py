import psycopg2
try:
	conexion = psycopg2.connect(user="postgres", password="0000",database= "carsale",host="localhost", port="5432")
	print("Conected!!")
	nombre_tablas = ["carro_estado", "carro_color_interior", "carro_color_exterior", "sistema_tipo_transmision", "sistema_tipo_motor" , "sistema_tipo_combustible", "sistema_tipo_drivetrain", "vendedor_tipo","vendedor_estado", "vendedor", "sistema", "carro", "referencia"]
	count = 0
	for nombre in nombre_tablas:
		print(nombre_tablas[count])
		sql1 = """SELECT* 
			FROM """ + nombre_tablas[count]+""";"""
		count +=1
		cursor=conexion.cursor()
		cursor.execute(sql1)
		data_base = cursor.fetchone()
		tuple_counter = 0
		while data_base:
			tuple_counter +=1
			print(data_base[0:])
			data_base = cursor.fetchone()
			if tuple_counter >50:
				break
	
finally:
	cursor.close()
	conexion.close()