import pymysql

class vehiculo():
    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
    def estado(self):
        print("El carro es de la marca:",self.marca,"\ny es modelo:",self.modelo)
    def conexion(self):   
        conex= pymysql.connect(db="practica",
        user="root",
        password="----",
        host="Localhost",
        port=3306) 
        cur= conex.cursor()
        
        cur.execute('''CREATE TABLE VEHICULOS(
        ID INTEGER PRIMARY KEY AUTO_INCREMENT,
        Marca VARCHAR(50),
        Modelo INTEGER)''')
        
        datss= [(self.marca,self.modelo)]
        cur.executemany("INSERT INTO VEHICULOS VALUES(NULL, %s,%s)",datss)
        conex.commit()
print("Ingrese datos del vehículo: Marca y modelo.")
datos=input()
dato=datos.split(",")
marc=dato[0]
model=int(dato[1])

Carro=vehiculo(marc,model)
Carro.conexion()






