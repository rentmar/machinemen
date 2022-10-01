from concurrent.futures import ThreadPoolExecutor
from pyfirmata import Arduino
import time
class HardCnc:
    def __init__(self, puerto,pines):
        self._puerto = puerto
        self._pines = pines
        self._arduino = Arduino(self._puerto)
        self._frecuencia = 0.002
        self._sx = self._arduino.get_pin('d:{0}:o'.format(pines[0]))
        self._px = self._arduino.get_pin('d:{0}:o'.format(pines[1]))
        self._sy = self._arduino.get_pin('d:{0}:o'.format(pines[2]))
        self._py = self._arduino.get_pin('d:{0}:o'.format(pines[3]))

    def get_puerto(self):
        return self._puerto

    def set_puerto(self, puerto):
        self._puerto = puerto

    def get_pines(self):
        return self._pines

    def set_pines(self,pines):
        self._pines=pines

    puerto = property(get_puerto, set_puerto)
    pines = property(get_pines,set_pines)

    def cerrarPuerto(self):
        print('Puerto cerrado')
        self._arduino.exit()


    def mover(self, sentidox, sentidoy, pulsos, movx, movy):
        self._sx.write(sentidox)
        self._sy.write(sentidoy)
        
        if(movx == 1 and movy == 1):
            for i in range(pulsos):
                self._px.write(1)
                self._py.write(1)
                time.sleep(self._frecuencia)
                self._px.write(0)
                self._py.write(0)
        elif(movx == 1 and movy == 0):        
            for i in range(pulsos):
                self._px.write(1)
                time.sleep(self._frecuencia)
                self._px.write(0)

        elif(movx == 0 and movy == 1):        
            for i in range(pulsos):
                self._py.write(1)
                time.sleep(self._frecuencia)
                self._py.write(0)
                



if __name__ == '__main__':

    m = HardCnc('/dev/ttyUSB0',[4,5,6,7,8])
    m.mover(0,0,400,1,0)

    m.cerrarPuerto()




