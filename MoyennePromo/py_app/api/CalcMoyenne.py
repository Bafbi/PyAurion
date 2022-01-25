from . import TableNotes, getnotes
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR')


def maths(result):
    maths,partiel,coef,TP,IE,sumIE = [],[],3,[],[],0
    # print(result)
    for i in range(len(result)):
        if (("MATH" in result[i][1][4])):
            # print(result[i][1])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            elif (("TP" in result[i][1][5])):
                if (result[i][1] != result[i-1][1]):
                    TP.append(result[i])
            elif (("IE" in result[i][1][5])):
                if (result[i][1] != result[i-1][1]):
                    IE.append(result[i])
                    sumIE += float(locale.atof(result[i][3]))
            else:
                if (result[i][1] != result[i-1][1]):
                    maths.append(result[i])
    # print(IE,"\n",partiel,"\n",TP,"\n",maths) 

    IE = (Moyenne(matiere(IE)[0]))
    maths = matiere(maths)
    maths[0].append(IE)
    note = Moyenne(maths[0])
    # print(note)
    notep = Moyenne(matiere(partiel)[0])
    # print(notep)

    notetp = Moyenne(matiere(TP)[0])
    # print(notetp)

    note = (note*0.4) + (notep*0.6)
    # print(note)
    notes = [note,notetp]
    coefs = [12,4]
    final = MoyenneC(notes, coefs)
    # print(final)
    # Maths coef 12 + TP coef 4
    return final

def prog(result):
    prog,partiel,ds,tp,coef = [],[],[],[],3
    for i in range(len(result)):
        if (("PROG1" in result[i][1]) or ("PROG2" in result[i][1])):
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1]) and ("DS" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    prog.append(result[i])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            if (("TP1" in result[i][1]) or ("TP2" in result[i][1]) or ("TP3" in result[i][1]) or ("TP4" in result[i][1]) or ("TP5" in result[i][1]) or ("TP6" in result[i][1]) or ("TP7" in result[i][1]) or ("TP8" in result[i][1]) or ("TP9" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    tp.append(result[i])
            if ("DS" in result[i][1]):
                if (result[i][1] != result[i-1][1]):
                    ds.append(result[i])
    return prog, partiel, ds, coef

def web(result):
    web,partiel,ds,tp,coef = [],[],[],[],2
    for i in range(len(result)):
        if ("WEB" in result[i][1]):
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1]) and ("DS" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    web.append(result[i])
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            if (("TP1" in result[i][1]) or ("TP2" in result[i][1]) or ("TP3" in result[i][1]) or ("TP4" in result[i][1]) or ("TP5" in result[i][1]) or ("TP6" in result[i][1]) or ("TP7" in result[i][1]) or ("TP8" in result[i][1]) or ("TP9" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    tp.append(result[i])
            if ("DS" in result[i][1]):
                if (result[i][1] != result[i-1][1]):
                    ds.append(result[i])
    return web, partiel, ds, coef

def physique(result):
    elec,partiel,TP,coef = [],[],[],3
    for i in range(len(result)):
        if ("ELEC" in result[i][1]) : 
            if (("P1" in result[i][1]) or ("P2" in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
            elif (("TP" in result[i][1][5])) :
                if (result[i][1] != result[i-1][1]):
                    TP.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    elec.append(result[i])
                    
    note = Moyenne(matiere(elec)[0])
    # print(note)
    notep = Moyenne(matiere(partiel)[0])
    # print(notep)
    TPelec = Moyenne(matiere(TP)[0])
    # print(notetp)
    noteelec = (note*0.4) + (notep*0.6)
    # print(noteelec,TPelec)


    opt,partiel,coef = [],[],2
    for i in range(len(result)):
        if ("OPTIQUE" in result[i][1]) : 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    opt.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
                    

    note = Moyenne(matiere(opt)[0])
    notep = Moyenne(matiere(partiel)[0])
    # print(note,notep)
    noteopt = (note*0.4) + (notep*0.6)
    # print(noteopt)

    note = [noteopt, noteelec, TPelec]
    coef = [2,3,3]
    final = MoyenneC(note, coef)
    return(final)


def mecanique(result):
    meca,partiel,coef = [],[],3
    for i in range(len(result)):
        if ("MECANIQUE" in result[i][1]) : 
            if (("P1" not in result[i][1]) and ("P2" not in result[i][1])):
                if (result[i][1] != result[i-1][1]):
                    meca.append(result[i])
            else:
                if (result[i][1] != result[i-1][1]):
                    partiel.append(result[i])
    return meca, partiel, coef

def anglais(result):
    ang,coef = [],2
    for i in range(len(result)):
        if ("ANGLAIS" in result[i][1]): 
            ang.append(result[i])
    return ang,coef
def comm(result):
    com,coef = [],2
    for i in range(len(result)):
        if ("COMM" in result[i][1]): 
            com.append(result[i])
    return com,coef
def sport(result):
    spo, coef = [],2
    for i in range(len(result)):
        if ("SPORT" in result[i][1]): 
            spo.append(result[i])
    return spo,coef



# Calcul par rapport au coef des notes de result
def matiere(result):
    Notes = []
    Coefs = []
    for i in range (len(result)):
        # print(result[i])
        if (len(result[i]) == 5):
            Notes.append(float(locale.atof(result[i][3])))
            Coefs.append(float(locale.atof(result[i][4])))
    return Notes,Coefs
    
# moyenne a partir d'une liste de note du module
def Moyenne(Notes):
    return sum(Notes)/len(Notes)

def MoyenneC(Notes, Coefs):
    return sum(Notes[g] * Coefs[g] / sum(Coefs) for g in range(len(Notes)))


def MATHS(resultats):
    final = maths(resultats)
    return(round(final,2))
# MATHS()


def PROG(resultats):
    # print(matiere(prog(resultats)[0]))
    # print(matiere(prog(resultats)[1]))
    # print(matiere(prog(resultats)[2]))
    note = (Moyenne(matiere(prog(resultats)[0])[0]))
    notep = (Moyenne(matiere(prog(resultats)[1])[0]))
    noteds = (Moyenne(matiere(prog(resultats)[2])[0]))
    
    
    if (notep == 0):
        note = note*0.4 + noteds*0.6
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    return (round(note,2))

def WEB(resultats):
    # print(matiere(web(resultats)[0]))
    # print(matiere(web(resultats)[1]))
    # print(matiere(web(resultats)[2]))
    note = (Moyenne(matiere(web(resultats)[0])[0]))
    notep = (Moyenne(matiere(web(resultats)[1])[0]))
    noteds = (Moyenne(matiere(web(resultats)[2])[0]))
    
    
    if (notep == 0):
        note = (note*0.4) + (noteds*0.6)
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    return(round(note,2))

def INFO(resultats):
    noteprog = PROG(resultats)
    noteweb = WEB(resultats)
    if (noteprog == 0): note = noteweb
    if (noteweb == 0): note = noteprog
    else:
        note = [noteprog, noteweb]
        coef = [3,2]
        note = MoyenneC(note, coef)
    return(round(note,2))
# INFO()    


def PHYSIQUE(resultats):
    note = physique(resultats)
    return(round(note,2))
# PHYSIQUE()

def DEV(resultats):
    noteang = (Moyenne(matiere(anglais(resultats)[0])[0]))
    notecomm = (Moyenne(matiere(comm(resultats)[0])[0]))
    notespo = (Moyenne(matiere(sport(resultats)[0])[0]))
    note = [noteang, notecomm, notespo]
    coef = [2,2,2]
    note = MoyenneC(note, coef)
    return(round(note,2))
# DEV()


def main(username,password):
    result = getnotes.main(username,password)
    # print(result)
    resultats = TableNotes.table(result)  #Liste de liste de note sous forme ['07/01/2022', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'P1'], 'Partiel de Technologies Web', ' 16.60', '24']
    # print(resultats)
    return MATHS(resultats),PHYSIQUE(resultats),INFO(resultats),DEV(resultats)