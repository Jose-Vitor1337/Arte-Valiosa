class Sensor:
    def __init__( self, posicaoX, posicaoY, raio ):
        self.posicaoX = posicaoX
        self.posicaoY = posicaoY
        self.raio = raio

    def estaDentroDoRaioDoSensor( self, posicaoX, posicaoY ):
        if ( self.distanciaEntreDoisPontos( self.posicaoX, self.posicaoY, posicaoX, posicaoY ) <= self.raio):
            return True
        else:
            return False

    def distanciaEntreDoisPontos( self, x1, y1, x2, y2 ):
        return ( ( ( x2 - x1 ) ** 2 ) + ( ( y2 - y1 ) ** 2 ) ) ** 1/2

    def positivoX( self ):
        return self.posicaoX + self.raio
    
    def positivoY( self ):
        return self.posicaoY + self.raio

    def negativoX( self ):
        return self.posicaoX - self.raio
    
    def negativoY( self ):
        return self.posicaoY - self.raio