
#funcion que realiza operaciones basicas

#-----------------------------------------------------------------------
#-------------- Método para operaciones básicas ------------------------
#-----------------------------------------------------------------------

def basic_ops(op1,op2,sel):  #op1 y op2 opernados y sel es el selector de la operacion

    #----------------------- Datos inválidos -------------------------------

    #error cuando no se usa un entero
    if( isinstance(op1, int)==False) | (isinstance(op2, int)==False ):
        return 'error de operando invalido, solo puede ser entero'

    #error cuando se supera -+127
    if(op1 > 127) | (op2 > 127) |(-127 > op1) | (-127 > op2):
        return 'error entero invalido no puede ser mayor a 127 ni menor a -127'

    #------------------------- Operaciones ---------------------------------

    if(sel==0):
        resul=op1+op2  #si el selector es 0 hace la suma
        return resul
    elif(sel==1):
        resul=op1-op2  #si el selector es 1 hace la resta
        return resul
    elif(sel==2):
        resul=op1&op2  #si el selector es 2 hace la AND
        return resul
    elif(sel==3):
        resul=op1|op2   #si el selector es 3 hace la OR
        return resul
    else:#error cuando se seleciona una operacion que no este entre 0-3 
        return 'error operacion invalidad'

    
#-----------------------------------------------------------------------
#--------------- Método para trabajar arreglos -------------------------
#-----------------------------------------------------------------------
def array_ops(arre1,arre2,sel):#Metodo para realizar operaciones a dos arreglos del mismo tamaño 

    n=len(arre1) #obtiene la cantidad de elementos en el arreglo
    m=len(arre2)
    resul=[]#resul es arreglo de salida
    aux=0 #contador auxiliar

    #error cuando se seleciona una operacion que no este entre 0-3 
    if(sel > 3) | (0 > sel ):
        return 'error operacion invalida'

    #error cuando los arreglos no son del mismo tamaño
    if(m!=n ):
        return 'error los arreglos no son del mismo tamaño'
    
    while (m > aux): 
        resul.append(basic_ops(arre1[aux],arre2[aux],sel)) #llama la funcion anterior con los elementes correspindientes del arreglo mediante el contador aux
        aux=aux+1

    return resul















    
