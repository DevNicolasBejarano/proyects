#Importa la librería de vuelo Tello
from djitellopy import tello
# Realiza conexión a 
from time import sleep
drone = tello.Tello()
drone.connect()

# Funcion para medir la bateria del dron
def status_batery():
	bateria = drone.get_battery() 
	#Método drone.connect() se ocupa de la genearación de la ip y puertos de conexión
	print("Estado de la batería:",str(bateria))

status_batery()

def up_fly():

	drone.takeoff()
	#vectores 
	#(0,0,0,0) 
	#primero -> izquierda,derecha 
	#segundo Adelante atras(con negativos)
	#tercero arriba y (con negativos)
	#cuarto -> Velocidad(-100 a 100)
	drone.send_rc_control(0, 30, 0, 0)
	sleep(2)
	drone.send_rc_control(0, 0, 0, 0)
	sleep(2)
	drone.send_rc_control(0, 0, 30, 0)
	sleep(2)
	drone.send_rc_control(0, 0, 0, 0)
	sleep(2)
	drone.send_rc_control(0, 0, -30, 0)
	sleep(2)
	drone.send_rc_control(0, 0, 0, 0)
	sleep(2)
	drone.send_rc_control(0, -30, 0, 0)
	sleep(2)
	drone.send_rc_control(0, 0, 0, 0)
	sleep(2)
	# drone.send_rc_control(0, 0, -30, 0)
	# sleep(2)
	drone.send_rc_control(30, 0, 0, 0)
	sleep(2)
	drone.send_rc_control(-30, 0, 0, 0)
	sleep(2)
	drone.send_rc_control(0, 0, 0, 0)
	drone.land()

up_fly()

