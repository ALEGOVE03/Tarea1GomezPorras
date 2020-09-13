# -----------------------------------------------------------------------
# -------------- Método para operaciones básicas ------------------------
# -----------------------------------------------------------------------

def basic_ops(op1, op2, sel):
    # Error cuando no se usa un entero
    if not(isinstance(op1, int) and isinstance(op2, int)):
        return "E1"

    # Error cuando se supera -+127
    if(op1 > 127) or (op2 > 127) or (-127 > op1) or (-127 > op2):
        return "E2"

    # ------------------------- Operaciones --------------------------------
    if(sel == 0):
        resul = op1 + op2  # Si el selector es 0 hace la suma
        return resul
    elif(sel == 1):
        resul = op1 - op2  # Si el selector es 1 hace la resta
        return resul
    elif(sel == 2):
        resul = op1 & op2  # Si el selector es 2 hace la AND
        return resul
    elif(sel == 3):
        resul = op1 | op2  # Si el selector es 3 hace la OR
        return resul
    else:  # Error cuando se seleciona una operacion que no este entre 0-3
        return "E3"


# -----------------------------------------------------------------------
# --------------- Método para trabajar arreglos -------------------------
# -----------------------------------------------------------------------

def array_ops(arre1, arre2, sel):
    n = len(arre1)  # Obtiene la cantidad de elementos en el arreglo
    m = len(arre2)
    resul = []  # Resul es arreglo de salida
    aux = 0  # Contador auxiliar

    if(sel > 3) | (0 > sel):  # Operacion fuera de rango
        return "E3"
    elif(m != n):  # Error cuando los arreglos no son del mismo tamaño
        return "E4"
    else:
        while(m > aux):
            resul.append(basic_ops(arre1[aux], arre2[aux], sel))
            # Llama la funcion anterior con los elementes correspondientes
            # del arreglo mediante el contador aux
            aux = aux + 1

        return resul
