# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 11:14:45 2020

@author: Javier
"""

class Mediciones():
    
    def __init__(self,npilotes,ncanios,longitud,precioM ):
        self.npilotes = npilotes
        self.ncanios = ncanios
        self.longitud = longitud
        self.precioM = precioM
        self.ncombinaciones = self.cantcombinaciones(self.ncanios)        
    def cantcombinaciones(self,ncanios):
        if ncanios== 3:
            return 3
        elif ncanios== 4:
            return 6
        elif ncanios== 5:
            return 10
        elif ncanios== 6:
            return 9
        else:
            print('Numero de caños inválido')
            return None
            
    """      
    def setCanios(self,n):
        self.ncanios = n
        self.ncombinaciones = self.cantcombinaciones(self.ncanios)
    
    def setPilotes(self,n):
        self.npilotes=n
    
    def setLongitud(self,n):
        self.longitud = n
    
    def setPrecioM(self,n):
        self.precioM = n  """
        


class Viaticos():
    def __init__(self,transporte,nviajes,costoviaje,comida,dias,hospedaje):
        self.transporte = transporte
        self.nviajes = nviajes
        self.costoviaje = costoviaje
        self.comida = comida
        self.dias = dias
        self.hospedaje = hospedaje
    """    
    def setTransporte(self,n):
        self.transporte = n
    
    def setViajes(self,n):
        self.nviajes = n
    
    def setCostoViaje(self,n):
        self.costoviaje = n
        
    def setComida(self,n):
        self.comida = n
        
    def setDias(self,n):
        self.dias = n
    
    def setHospedaje(self,n):
        self.hospedaje = n  """
        
 

               
def PrecioPorPilote(combinaciones,long,costometro):
    return(combinaciones*long*costometro)
        
def PrecioTotalPilotes(tot,npilotes):
    return(tot*npilotes)

def CostoViaticos(transporte,viajes,costoViaje,comida,dias,hospedaje):
    return(transporte + viajes*costoViaje + comida*dias + hospedaje)
    
def iibb(n):
    return(n*1.035)


#Costo para 1 trabajo de 1 solo tipo de pilotes

med1 = Mediciones(int(input('Cantidad de pilotes: ')), int(input('Cantidad de caños por pilote: ')),
                  int(input('Longitud de los pilotes: ')),float(input('Precio por metro: ')))

viat1 = Viaticos(int(input('Precio total (ida y vuelta) de transporte: ')),int(input('Cantidad de viajes: ')),
                 int(input('Costo por viaje: ')),int(input('Viatico por comida: ')),int(input('Cantidad de dias: ')),
                 int(input('Costo total del hospedaje por todos los dias: ')))
'''
med1.setCanios(int(input('Cantidad de caños por pilote: ')))
med1.setLongitud(int(input('Longitud de los pilotes: ')))
med1.setPilotes(int(input('Cantidad de pilotes: ')))
med1.setPrecioM(float(input('Precio por metro: ')))
viat1.setTransporte(int(input('Precio total (ida y vuelta) de transporte: ')))
viat1.setCostoViaje(int(input('Costo por viaje: ')))
viat1.setViajes(int(input('Cantidad de viajes: ')))
viat1.setComida(int(input('Viatico por comida: ')))
viat1.setDias(int(input('Cantidad de dias: ')))
viat1.setHospedaje(int(input('Costo total del hospedaje por todos los dias: ')))'''

pilotes1 = PrecioPorPilote(med1.ncombinaciones, med1.longitud,med1.precioM)
totalpilotes1 = PrecioTotalPilotes(pilotes1,med1.npilotes)
viaticos1 = CostoViaticos(viat1.transporte,viat1.nviajes,viat1.costoviaje,viat1.comida,viat1.dias,viat1.hospedaje)

total = totalpilotes1 + viaticos1

print('PRECIO POR PILOTE:', iibb(total/med1.npilotes))
print('TOTAL PILOTES: ', iibb(totalpilotes1))
print('VIATICOS: ', round(iibb(viaticos1),2))
print('TOTAL A ABONAR: ', round(iibb(total),2))
print('Adelanto solicitado: ',round(iibb(total)*.75,2))
print('Viaticos por comida: ', viat1.comida*viat1.dias)
print('Honorarios: ', round(totalpilotes1*.25,2))