
from televisores.tv import TV

class Control:
    def __init__(self):
        self._tv=None
    def enlazar(self, TV):
        TV._control=self
        self._tv=TV
    def getTv(self):
        return self._tv
    def setTv(self, TV):
        self._tv=TV

    def setVolumen(self, volumen):
        if self._tv._estado==True and (volumen<=0 and volumen<=7):
            self._tv._volumen=volumen
    def getVolumen(self):
        return self._tv._volumen
    def setNumTV(self, numTV):
        TV._numTV=numTV
    def getNumTV(self):
        return TV._numTV
    def turnOn(self):
        if self._tv._estado==False:
            self._tv._estado=True
    def turnOff(self):
        if self._tv._estado==True:
            self._tv._estado=False
    def canalUp(self):
        if self._tv._estado==True:
            if self._tv._canal>=1 and self._tv._canal<120:
                self._tv._canal+=1
    
    def canalDown(self):
        if self._estado==True:
            if self._tv._canal>1 and self._tv._canal<=120:
                self._tv._canal-=1

    def volumenUp(self):
        if self._tv._estado==True:
            if self._tv._volumen>=0 and self._tv._volumen<7:
                self._tv._volumen+=1
    def volumenDown(self):
        if self._estado==True:
            if self._tv._volumen>0 and self._tv._volumen<=7:
                self._tv._volumen-=1
    
    def setCanal(self,canal):
        if self._tv._estado==True:
            self._tv._canal=canal
    def getCanal(self):
        return self._tv._canal