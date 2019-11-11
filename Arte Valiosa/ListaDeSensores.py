from Sensor import *

class ListaDeSensores:
    def __init__( self , numeroQueIrarFicarNaAreaDoSensor = 2):
        self.listaDeSensores = []
        self.numeroQueIrarFicarNaAreaDoSensor = numeroQueIrarFicarNaAreaDoSensor

    def addSensor( self, posicaoX, posicaoY, raio ):
        self.listaDeSensores.append( Sensor( posicaoX, posicaoY, raio ) )
    
    def clear( self ):
        self.listaDeSensores = []
    
    def montaTodasAsAreasDeUmaListaDeSensores( self, matriz2D ):
        aux = matriz2D.copy()

        for sensor in self.listaDeSensores:
            aux = self.montaAreaDoSensorNaMatriz2D( aux.copy(), sensor )
        
        return aux.copy()

    def montaAreaDoSensorNaMatriz2D( self, matriz2D, sensor ):

        for linha in range( len( matriz2D ) ):

            for coluna in range( len( matriz2D[ linha ] ) ):
                #Verifica se a linha e a coluna estão dentro da área do sensor
                '''if (
                    ( linha >= sensor.negativoX() and linha <= sensor.positivoX() ) and
                    ( coluna >= sensor.negativoY() and coluna <= sensor.positivoY() )
                    ):
                '''
                if ( sensor.estaDentroDoRaioDoSensor( linha, coluna ) ):
                    matriz2D[ linha ][ coluna ] = self.numeroQueIrarFicarNaAreaDoSensor

        return matriz2D.copy()