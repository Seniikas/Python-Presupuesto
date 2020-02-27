# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:22:50 2020

@author: Javier
"""
from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (para widgets nuevos 8.5+)

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Presupueto Pilotes CHSL')  
        
        #Mediciones
        self.num_pil = IntVar(value=1)
        self.num_can = IntVar(value=3)
        self.longitud = IntVar(value=1)       
        self.precioM = DoubleVar(value=8.5)
        
        #Viaticos
        self.transporte = IntVar(value=0)
        self.num_viajes = IntVar(value=2)
        self.costo_viajes = IntVar(value=500)
        self.comida = IntVar(value=500)
        self.num_dias = IntVar(value=1)
        self.hospedaje = IntVar(value=0)
        
        self.total = DoubleVar(value=0.0)
        
        #PARTE GRAFICA 
        
        """ DECLARACION DE WIDGETS"""
        
        
        self.frameMed = ttk.Frame(self.raiz, borderwidth=0)
        
        self.etiqPrin1 = ttk.Label(self.frameMed, text="Mediciones")  
        
        
        self.frame1 = ttk.Frame(self.frameMed, borderwidth=0)
                                     
        
        self.etiqM1 = ttk.Label(self.frame1, 
                               text="Nº de pilotes:")
       
        self.etiqM2 = ttk.Label(self.frame1, 
                               text="Nº de caños por pilote:")
        
        self.etiqM3 = ttk.Label(self.frame1, 
                               text="Longitud (metros):")   
        
        
        
        
        self.frame2 = ttk.Frame(self.frameMed, borderwidth=0)
    
        self.canios = Spinbox(self.frame2, from_=3, to=6, wrap=True,
                             textvariable=self.num_can, 
                             state='readonly', width=5)
        self.npil = ttk.Entry(self.frame2, textvariable=self.num_pil, 
                              width=5)
        #self.ncan = ttk.Entry(self.frame2, textvariable=self.num_can, 
         #                     width=5)
        self.long = ttk.Entry(self.frame2, textvariable=self.longitud, 
                              width=5)
        
        
        
        
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)  
        
        
        
        self.frameViat = ttk.Frame(self.raiz, borderwidth=0)
                                      
        
        self.etiqPrin2 = ttk.Label(self.frameViat, text="Viaticos:")
     
        
        
        self.frame3 = Frame(self.frameViat,borderwidth = 0)
        
        self.etiqV1 = ttk.Label(self.frame3, 
                               text="$ Transporte:")
        
        self.etiqV2 = ttk.Label(self.frame3, 
                               text="Nº de viajes:")
        
        self.etiqV3 = ttk.Label(self.frame3, 
                               text="$ por viaje:")       
        
        
        self.frame4 = Frame(self.frameViat,borderwidth = 0)
        
        
        self.transp = ttk.Entry(self.frame4, textvariable =self.transporte, 
                              width=5)
    
        self.nviaj = ttk.Entry(self.frame4, textvariable=self.num_viajes, 
                              width=5)
       
        self.pViaje = ttk.Entry(self.frame4, textvariable=self.costo_viajes, 
                              width=5)
        
        
        self.frame5 = Frame(self.frameViat,borderwidth = 0)
                
        self.etiqV4 = ttk.Label(self.frame5, 
                               text="$ Comida:")
        self.etiqV5 = ttk.Label(self.frame5, 
                               text="Nº de días:")
        self.etiqV6 = ttk.Label(self.frame5, 
                               text="Total Hospedaje:")
        
        
        
        self.frame6 = Frame(self.frameViat,borderwidth = 0)
        self.comi = ttk.Entry(self.frame6, textvariable=self.comida, 
                              width=5)       
        self.ndias = ttk.Entry(self.frame6, textvariable=self.num_dias, 
                              width=5)       
        self.hosp = ttk.Entry(self.frame6, textvariable=self.hospedaje, 
                              width=5)                    
                            
                
        self.boton1 = ttk.Button(self.raiz, text="Calcular", 
                                 command=self.CalcularTotal)
        
        
        """UBICACION DE LOS WIDGETS"""
        
        self.frameMed.pack(side = TOP, fill = BOTH, expand = False)
        self.etiqPrin1.pack(side = TOP) 
        self.frame1.pack(side = TOP, fill = BOTH, expand = True)
        
        self.etiqM1.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=20, pady=5)        
        self.etiqM2.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=10, pady=5)        
        self.etiqM3.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        
        
        
        self.frame2.pack(side = TOP, fill = BOTH, expand = True) 
        
        self.npil.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)        
        self.canios.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)        
        self.long.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)
        
        
        self.frameViat.pack(side = TOP, fill = BOTH, expand = False)
        
        self.etiqPrin2.pack(side = TOP) 
        
        self.frame3.pack(side = TOP, fill = BOTH, expand = True)
        
        self.etiqV1.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=20, pady=5)        
        self.etiqV2.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=10, pady=5)        
        self.etiqV3.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        
        
        
        
        self.frame4.pack(side = TOP, fill = BOTH, expand = True)
        
        self.transp.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)        
        self.nviaj.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)        
        self.pViaje.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)
              
        
        
        self.frame5.pack(side = TOP, fill = BOTH, expand = True)
        
        self.etiqV4.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=40, pady=5)       
        self.etiqV5.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=10, pady=5)        
        self.etiqV6.pack(side=LEFT, fill=BOTH, expand=True, 
                        padx=10, pady=5)
        
        
        
        
        self.frame6.pack(side = TOP, fill = BOTH, expand = True)
        
        self.comi.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)       
        self.ndias.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)       
        self.hosp.pack(side=LEFT, fill=X, expand=True, 
                        padx=10, pady=5)
        
        
        
        self.boton1.pack(side = LEFT,padx = 20)
        
        self.botonSalir = ttk.Button(self.raiz, text='Salir', 
                   command=self.raiz.destroy).pack(side=RIGHT, pady = 5, padx= 20)
        self.raiz.mainloop()
        
        
        
    def CalcularTotal(self, *args):
        
        med1 = Mediciones(self.num_pil.get(),self.num_can.get(), self.longitud.get(), self.precioM.get())
        viat1 = Viaticos(self.transporte.get(), self.num_viajes.get(), self.costo_viajes.get(), self.comida.get(), self.num_dias.get(), self.hospedaje.get())
        pilotes1 = PrecioPorPilote(med1.ncombinaciones, med1.longitud,med1.precioM)
        totalpilotes1 = PrecioTotalPilotes(pilotes1,med1.npilotes)
        viaticos1 = CostoViaticos(viat1.transporte,viat1.nviajes,viat1.costoviaje,viat1.comida,viat1.dias,viat1.hospedaje)
        total = totalpilotes1 + viaticos1
        self.Presupuesto = Toplevel()
        self.precioPilote = ttk.Label(self.Presupuesto, text="PRECIO POR PILOTE: $" + str(round(iibb(total/med1.npilotes),2))).pack(side=TOP, padx = 20, pady = 10)
        self.totalPilotes = ttk.Label(self.Presupuesto, text="TOTAL POR PILOTES: $" + str(round(iibb(totalpilotes1),2))).pack(side=TOP, padx = 20, pady = 10)
        self.viaticos = ttk.Label(self.Presupuesto, text="VIATICOS: $" + str(round(iibb(viaticos1),2))).pack(side=TOP, padx = 20, pady = 10)
        self.totalAbonar = ttk.Label(self.Presupuesto, text="TOTAL A ABONAR: $" + str(round(iibb(total),2))).pack(side=TOP, padx = 20, pady = 10)
        self.adelantoSolicitado = ttk.Label(self.Presupuesto, text="ADELANTO SOLICITADO: $" + str(round(iibb(total)*.75,2))).pack(side=TOP, padx = 20, pady = 10)
        self.viaticosComida = ttk.Label(self.Presupuesto, text="VIATICOS POR COMIDA: $" + str(round(viat1.comida*viat1.dias,2))).pack(side=TOP, padx = 20, pady = 10)
        self.honorarios = ttk.Label(self.Presupuesto, text="HONORARIOS OPERADOR: $" + str(round(totalpilotes1*.25,2))).pack(side=TOP, padx = 20, pady = 10)


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


class Viaticos():
    def __init__(self,transporte,nviajes,costoviaje,comida,dias,hospedaje):
        self.transporte = transporte
        self.nviajes = nviajes
        self.costoviaje = costoviaje
        self.comida = comida
        self.dias = dias
        self.hospedaje = hospedaje


def PrecioPorPilote(combinaciones,long,costometro):
    return(combinaciones*long*costometro)
        
def PrecioTotalPilotes(tot,npilotes):
    return(tot*npilotes)

def CostoViaticos(transporte,viajes,costoViaje,comida,dias,hospedaje):
    return(transporte + viajes*costoViaje + comida*dias + hospedaje)
    
def iibb(n):
    return(n*1.035)
    
    
    
    

def main():
    mi_app = Aplicacion()
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es 
# importado:

if __name__ == '__main__':   
    main()