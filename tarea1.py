
#funcion que realiza operaciones basicas


def basic_ops(op1,op2,sel):  #op1 y op2 opernados y sel es el selector de la operacion

#-------------------------------------------------------------------------------------------------
#-----------------------------------datos invalidos-----------------------------------------------
#-------------------------------------------------------------------------------------------------



    #error cuando no se usa un entero
    if( isinstance(op1, int)==False) | (isinstance(op2, int)==False ):
        return 'error de operando invalido, solo puede ser entero'



    #error cuando se supera -+127
    if(op1 > 127) | (op2 > 127) |(-127 > op1) | (-127 > op2):
        return 'error entero invalido no puede ser mayor a 127 ni menor a -127'


    #error cuando se seleciona una operacion que no este entre 0-3 
    if(sel > 3) | (0 > sel ):
        return 'error operacion invalidad'



#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

    if(sel==0):
        resul=op1+op2  #si el selector es 0 hace la suma
        return resul
    
    if(sel==1):
        resul=op1-op2  #si el selector es 1 hace la resta
        return resul
    
    if(sel==2):
        resul=op1&op2  #si el selector es 2 hace la AND
        return resul
    
    if(sel==3):
        resul=op1|op2   #si el selector es 3 hace la OR
        return resul




def array_ops(arre1,arre2,sel):

    n=len(arre1)
    m=len(arre2)
    resul=[]
    aux=0


#error cuando se seleciona una operacion que no este entre 0-3 
    if(sel > 3) | (0 > sel ):
        return 'error operacion invalidad'

#error cuando se seleciona una operacion que no este entre 0-3 
    if(m!=n ):
        return 'error los arreglos no son del mismo tamaño'

    
    
    while (m > aux):
        resul.append(basic_ops(arre1[aux],arre2[aux],sel))
        aux=aux+1

    return resul















    