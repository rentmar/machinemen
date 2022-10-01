

class Motor:

    def __init__(self, pinsentido, pinmovimiento):
        self._psentido = pinsentido
        self._pmovimiento = pinmovimiento
        self._frecuencia = 0

    #Setters y getters 
    def get_sentido(self):
        return self._psentido

    def set_sentido(self, sentido):
        self._psentido = sentido 

    def get_movimiento(self):
        return self._pmovimiento

    def set_movimiento(self, movimiento):
        self._pmovimiento = movimiento

    def get_frecuencia(self):
        return self._frecuencia  

    def set_frecuencia(self, frecuencia):
        self._frecuencia = frecuencia    

    pinSentido = property(get_sentido, set_sentido)
    pinMovimiento = property(get_movimiento, set_movimiento);
    frecuencia = property(get_frecuencia, set_frecuencia)              


    
    #Metodo para la Impresion de la clase
    def __str__(self):
        return '<%s: sentido=> pin %s , movimiento=> pin %s, frecuencia=> %s >' %( self.__class__.__name__, self._psentido, self._pmovimiento, self._frecuencia)
            

if __name__ == '__main__':

    mx = Motor(4, 5)
    
    print(mx)
    print(mx.pinSentido)
    print(mx.pinMovimiento)
   