# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 14:31:12 2022

@author: oscar
"""
from pyfirmata import Arduino
import time
from concurrent.futures import ThreadPoolExecutor

class ControlMotores:
    
    '''Argumentos str:puerto del arduino y list:lista con los pines para control de motores
    [dirX,MovX,dirY,MovY,movZ]'''
    
    def __init__(self,sp,defpines):
        self._puertoSerial=sp
        self._pines=defpines
        self._arduino=Arduino(self._puertoSerial)
        self._dirX=self._arduino.get_pin("d:{0}:o".format(self._pines[0]))
        self._MovX=self._arduino.get_pin("d:{0}:o".format(self._pines[1]))
        self._dirY=self._arduino.get_pin("d:{0}:o".format(self._pines[2]))
        self._MovY=self._arduino.get_pin("d:{0}:o".format(self._pines[3]))
        self._MovZ=self._arduino.get_pin("d:{0}:o".format(self._pines[4]))
        
    def __str__(self):
        info='Objeto para control CNC:'
        info+='sp:puerto del arduino(str), ' 
        info+='pines:lista con los pines para control de motores [dirX,MovX,dirY,MovY,movZ] '
        info+='****Argumetos:'
        info+='puertoSerial,pines'
        info+='****Metodos:'
        info+='cerralControl(),moverPostivoX(),moverNegativoX(),idem para Y,Z'
        return info
        
    def get_puertoSerial(self):
        return self._puertoSerial
    
    def set_puertoSerial(self,sp):
        self._arduino.exit()
        self._puertoSerial=sp
        self._arduino=Arduino(self._puertoSerial)
        
    def get_pines(self):
        definicion="DireccionX:{0},MovimientoX:{1},".format(self._pines[0],self._pines[1])
        definicion+="DireccionY:{0},MovimientoY:{1},".format(self._pines[2],self._pines[3])
        definicion+="MovimientoZ:{0}".format(self._pines[4])
        return definicion
    
    def set_pines(self,defpines):
        self._arduino.exit()
        self._pines=defpines
        self._arduino=Arduino(self._puertoSerial)
        self._dirX=self._arduino.get_pin("d:{0}:o".format(self._pines[0]))
        self._MovX=self._arduino.get_pin("d:{0}:o".format(self._pines[1]))
        self._dirY=self._arduino.get_pin("d:{0}:o".format(self._pines[2]))
        self._MovY=self._arduino.get_pin("d:{0}:o".format(self._pines[3]))
        self._MovZ=self._arduino.get_pin("d:{0}:o".format(self._pines[4]))
        
    puertoSerial=property(get_puertoSerial, set_puertoSerial)
    pines=property(get_pines,set_pines)
        
    def cerrarControl(self):
        print ('Control CNC cerrado')
        self._arduino.exit()
    
    def moverPositivoX(self,d,T):
        self._dirX.write(1)
        for i in range(d):
            self._MovX.write(1)        
            time.sleep(T)
            self._MovX.write(0)
            time.sleep(T)
        
    def moverNegativoX(self,d,T):
        self._dirX.write(0)
        for i in range(d):
            self._MovX.write(1)        
            time.sleep(T)
            self._MovX.write(0)
            time.sleep(T)
        
    def moverPositivoY(self,d,T):
        self._dirY.write(1)
        for i in range(d):
            self._MovY.write(1)        
            time.sleep(T)
            self._MovY.write(0)
            time.sleep(T)
        
    def moverNegativoY(self,d,T):
        self._dirY.write(0)
        for i in range(d):
            self._MovY.write(1)        
            time.sleep(T)
            self._MovY.write(0)
            time.sleep(T)
        
    def moverPositivoZ(self):
        print ('mover z+')
        
    def moverNegativoZ(self):
        print ('mover z-')
        
if __name__ == "__main__":
    
    salir=False
    print ("Inicia Prueba")
    cntrl=ControlMotores('/dev/ttyUSB0',[4,5,6,7,8])
    
    ejecutor = ThreadPoolExecutor(max_workers=2)
    ejecutor.submit(cntrl.moverPositivoX,500,0.001)
    ejecutor.submit(cntrl.moverPositivoY,800,0.001)
    
    cmd=input('Ingresar Comando Salir:')
    print(cmd)
    cntrl.cerrarControl()
    
    
    