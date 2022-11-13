def inputFloat(inputUsuario):
    str = inputUsuario
    if str.find(".")!=-1:
        sstr = str.rfind(".")
        newstr = str.replace(".", "")
        if newstr.find("-")!=-1:
            return print("Es un valor negativo, ERROR")
        else:
            othstr = newstr.replace(" ", "")
            ytr = othstr.isalpha()
            if ytr == True:
                return print("No se puede, ERROR")
            elif ytr == False:
                nnewstr = newstr[:sstr] + '.' + newstr[sstr:]
                nowfloat = float(nnewstr)
                return nowfloat
    else:
        return print("ERROR, introduzca un valor valido")

def inputInt(inputUsuario2):
    str2 = inputUsuario2
    #Empieza proceso, no hay punto, revisar si es una palabra. (Analiza que no sea un valor negativo).
    xtr = str2.replace(" ", "")
    if xtr.find("-")!=-1:
        print("Es un valor negativo, ERROR")
    else:
        nwstr = xtr.isalpha()
    if nwstr == True:
        print("No se puede")
    elif nwstr == False:
        nowint = int(xtr)
    return nowint
  #Termina proceso, no hay punto, revisar si es una palabra. (Analiza que no sea un valor negativo).