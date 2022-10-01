from concurrent.futures import ThreadPoolExecutor
import threading
from pyfirmata import Arduino
from motor import Motor
import time


class ControlMotores:
    #datMotores [numero_pinsentidox, numero_pinpasosx, numero_pinsentidoy, numero_pinpasosy]
    # por defecto:
    # Motorx:
    #           sentido: pin4
    #           pasos: pin5
    # Motory:
    #           sentido: pin6
    #           sentido: pin7
    #     
    def __init__(self, puerto, datMotores = [4,5,6,7,8]):
        self._puerto = puerto
        self._arduino = Arduino(self._puerto)
        self._motorx = Motor(datMotores[0], datMotores[1])
        self._motory = Motor(datMotores[2], datMotores[3])
        self._sx = self._arduino.get_pin('d:{0}:o'.format(self._motorx.pinSentido))
        self._px = self._arduino.get_pin('d:{0}:o'.format(self._motorx.pinMovimiento))
        self._sy = self._arduino.get_pin('d:{0}:o'.format(self._motory.pinSentido))
        self._py = self._arduino.get_pin('d:{0}:o'.format(self._motory.pinMovimiento))
        self._mz = self._arduino.get_pin('d:{0}:o'.format(datMotores[4]))


    #Setter y getterst
    def get_puerto(self):
        return self._puerto

    def set_puerto(self, puerto):
        self._puerto = puerto 

    puertoConexion = property(get_puerto, set_puerto)

    #cerrar la comunicacion
    def cerrarPuerto(self):
        self._arduino.exit()
        print("Puerto cerrado")
        
    
    #Movimiento positivo del motor x
    def moverPositivoX(self,  pulsos = 0, frecuencia=0):
        #Establecer el sentido
        self._sx.write(1)
        for i in range(pulsos):
            #print("pulso alto x %d" %i)
            self._px.write(1)
            #self._arduino.pass_time(frecuencia)
            time.sleep(frecuencia)
            #print("pulso bajo x %d" %i)
            self._px.write(0)
            time.sleep(frecuencia)
            #self._arduino.pass_time(frecuencia)
    
    def moverNegativoX(self,  pulsos = 0, frecuencia=0):
        #Establecer el sentido
        self._sx.write(0)
        for i in range(pulsos):
            #print("pulso alto x %d" %i)
            self._px.write(1)
            #self._arduino.pass_time(frecuencia)
            time.sleep(frecuencia)
            #print("pulso bajo x %d" %i)
            self._px.write(0)
            time.sleep(frecuencia)
            #self._arduino.pass_time(frecuencia)        

    #Movimiento del motor y
    def moverPositivoY(self, pulsos = 0, frecuencia = 0):
        self._sy.write(0)
        for i in range(pulsos):
            #print("pulso alto y %d" %i)
            self._py.write(1)
            #self._arduino.pass_time(frecuencia)
            time.sleep(frecuencia)
            #print("pulso bajo y %d" %i)
            self._py.write(0)
            time.sleep(frecuencia)
            #self._arduino.pass_time(frecuencia)

    #Movimiento del motor y
    def moverNegativoY(self, pulsos = 0, frecuencia = 0):
        self._sy.write(1)
        for i in range(pulsos):
            #print("pulso alto y %d" %i)
            self._py.write(1)
            #self._arduino.pass_time(frecuencia)
            time.sleep(frecuencia)
            #print("pulso bajo y %d" %i)
            self._py.write(0)
            time.sleep(frecuencia)
            #self._arduino.pass_time(frecuencia)

    
    #Movimiento del motor xy
    def moverXY(self, sentidox = 0, sentidoy = 0, pulsos=0, frecuencia = 0):
        self._sx.write(sentidox)
        self._sy.write(sentidoy)
        self._px.write(1)
        estadopx=True
        self._py.write(1)
        estadopy=True
        cnt=0
        for i in range(pulsos):
            #print("pulso alto y %d" %i)
            time.sleep(frecuencia)
            cnt+=1
            #print("pulso bajo y %d" %i
            if estadopy==True:
                self._py.write(0)
                estadopy=False
            else:
                self._py.write(1)
                estadopy=True
            if cnt==2:
                if estadopx==True:
                    self._px.write(0)
                    estadopx=False
                else:
                    self._px.write(1)
                    estadopx=True
                cnt=0#'''
    #Iniciar el movimiento
    def iniciar(self, mx = [1, 300, 0.002], my = [0, 400, 0.003] ):
        print("inciar xy")
        px = threading.Thread(target=self.moverX, args = (mx[0], mx[1], mx[1]))
        py = threading.Thread(target=self.moverY, args = (my[0],my[1],my[2]))
        px.start()
        py.start()
        print("fin xy")
    

    #Informacion de la clase
    def __str__(self):
         return '<%s: puerto=> %s, MotorX(%s), MotorY(%s) >' %(self.__class__.__name__, self._puerto, self._motorx, self._motory)



if __name__ == '__main__':
    ejecutor = ThreadPoolExecutor(max_workers=2)
    control = ControlMotores('/dev/ttyUSB0')
    T = 0.002
    salir = False
    """while salir == False:
        cmd = input('OPCION: x-y-xy-q:')
        if(cmd == 'x'):
            pasosx = int(input('pasosX: '))
            control.moverPositivoX(pasosx, T)
        elif(cmd == 'y'):
            pasosy = int(input('pasosY: '))
            control.moverPositivoY(pasosy, T)
        elif(cmd == 'xy'):
            pasosx = int(input('Pasos X: '))
            pasosy = int(input('Pasos Y: '))
            ejecutor.submit(control.moverPositivoX, pasosx, T)
            ejecutor.submit(control.moverPositivoY, pasosy, T)
     
        elif(cmd == 'q'):
            salir = True"""
    ejecutor.submit(control.moverPositivoX, 400, T)
    ejecutor.submit(control.moverPositivoY, 500, T)

    a = input("Presione para salir....")        


    control.cerrarPuerto()

