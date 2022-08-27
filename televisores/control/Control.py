from tv import TV
class Control:
    def __init__(self,TV):
        self._tv=TV
    def enlazar(self, TV):
        TV._control=self
    def getTV(self):
        return self._tv
    def setTV(self, TV):
        self._tv=TV

    def setVolumen(self, volumen):
        if self._tv._estado==True and (volumen<=0 and volumen<=7):
            self._tv._volumen=volumen
    def getVolumen(self):
        return self._tv._volumen
    def setNumTV(self, numTV):
        self._tv._numTV=numTV
    def getNumTV(self):
        return self._tv._numTV
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

    def volumenUP(self):
        if self._estado==True:
            if self._volumen>=0 and self._tv._volumen<7:
                self._tv._volumen+=1
    def volumenDown(self):
        if self._estado==True:
            if self._tv._volumen>0 and self._tv._volumen<=7:
                self._tv._volumen-=1
    