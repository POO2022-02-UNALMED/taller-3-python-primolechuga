
class TV:
    _numTV=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None
        TV._numTV+=1
        
    
    def setMarca(self, marca):
        self._marca=marca
    def getMarca(self):
        return self._marca
    def setCanal(self,canal):
        if self._estado==True:
            if canal<=120 and canal>=1:
                self._canal=canal
    def getCanal(self):
        return self._canal
    def setPrecio(self, precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio
    def setEstado(self,estado):
        self._estado=estado
    def getEstado(self):
        return self._estado
    def setVolumen(self, volumen):
        if (self._estado==True) and (volumen>=0 and volumen<=7):
            self._volumen=volumen
    def getVolumen(self):
        return self._volumen
    def setNumTV(numTV):
        TV._numTV=numTV
    def getNumTV():
        return TV._numTV
    def turnOn(self):
        if self._estado==False:
            self._estado=True
    def turnOff(self):
        if self._estado==True:
            self._estado=False
    def canalUp(self):
        if self._estado==True:
            if self._canal>=1 and self._canal<120:
                self._canal+=1
    
    def canalDown(self):
        if self._estado==True:
            if self._canal>1 and self._canal<=120:
                self._canal-=1

    def volumenUp(self):
        if self._estado==True:
            if self._volumen>=0 and self._volumen<7:
                self._volumen+=1
    def volumenDown(self):
        if self._estado==True:
            if self._volumen>0 and self._volumen<=7:
                self._volumen-=1
    def getControl(self):
        return self._control
