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
    if (IE == 21):
        return "ERREUR maths IE"
    maths = matiere(maths)
    maths[0].append(IE)
    note = Moyenne(maths[0])
    # print(note)
    notep = Moyenne(matiere(partiel)[0])
    if (notep == 21):
        return "ERREUR maths Partiel"
    # print(notep)

    notetp = Moyenne(matiere(TP)[0])
    # print(notetp)
    if (notetp == 21):
        return "ERREUR maths TP"

    note = (note*0.4) + (notep*0.6)
    # print(note)
    notes = [note,notetp]
    coefs = [12,4]
    final = MoyenneC(notes, coefs)
    # print(final)
    # Maths coef 12 + TP coef 4
    return (round(final,2))

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
    if (note == 21):
        return "ERREUR elec CC"
    # print(note)
    notep = Moyenne(matiere(partiel)[0])
    if (notep == 21):
        return "ERREUR elec partiel"
    # print(notep)
    TPelec = Moyenne(matiere(TP)[0])
    if (TPelec == 21):
        return "ERREUR maths TP"
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
    if (note == 21):
        return "ERREUR optique CC"
    notep = Moyenne(matiere(partiel)[0])
    if (notep == 21):
        return "ERREUR optique Partiel"
    # print(note,notep)
    noteopt = (note*0.4) + (notep*0.6)
    # print(noteopt)

    note = [noteopt, noteelec, TPelec]
    coef = [2,3,3]
    final = MoyenneC(note, coef)
    final = (round(note,2))
    return final


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
    if (Notes != []):
        moy = sum(Notes)/len(Notes)
    else: 
        moy = 21
    return moy

def MoyenneC(Notes, Coefs):
    try:
        moy = sum(Notes[g] * Coefs[g] / sum(Coefs) for g in range(len(Notes)))
        return 
    except:
        return "ERREUR calcul moyenne"


def MATHS(resultats):
    final = maths(resultats)
    return(final)
# MATHS()


def PROG(resultats):
    # print(matiere(prog(resultats)[0]))
    # print(matiere(prog(resultats)[1]))
    # print(matiere(prog(resultats)[2]))
    note = (Moyenne(matiere(prog(resultats)[0])[0]))
    if (note == 21):
        return "ERREUR prog CC"
    notep = (Moyenne(matiere(prog(resultats)[1])[0]))
    if (notep == 21):
        return "ERREUR prog partiel"
    noteds = (Moyenne(matiere(prog(resultats)[2])[0]))
    if (noteds == 21):
        return "ERREUR optique DS"
    
    
    if (notep == 0):
        note = note*0.4 + noteds*0.6
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    final = (round(note,2))
    return final

def WEB(resultats):
    # print(matiere(web(resultats)[0]))
    # print(matiere(web(resultats)[1]))
    # print(matiere(web(resultats)[2]))
    note = (Moyenne(matiere(web(resultats)[0])[0]))
    if (note == 21):
        return "ERREUR web CC"
    notep = (Moyenne(matiere(web(resultats)[1])[0]))
    if (notep == 21):
        return "ERREUR web partiel"
    noteds = (Moyenne(matiere(web(resultats)[2])[0]))
    if (noteds == 21):
        return "ERREUR web DS"
    
    
    if (notep == 0):
        note = (note*0.4) + (noteds*0.6)
    if (noteds == 0):
        note = (note*0.4) + (notep*0.6)
    if ((notep == 0) and (noteds == 0)):
        note = note  
    if ((note != 0) and (noteds != 0) and (notep != 0)):
        note = (note*0.4) + (((noteds*0.33)+(notep*0.67))*0.6) 
    final = (round(note,2))
    return final

def INFO(resultats):
    noteprog = PROG(resultats)
    noteweb = WEB(resultats)
    if (noteprog == 0): note = noteweb
    if (noteweb == 0): note = noteprog
    else:
        note = [noteprog, noteweb]
        coef = [3,2]
        note = MoyenneC(note, coef)
    if (type(note) == int):
        final = (round(note,2))
        return final
    else:
        return "ERREUR calcul info"
# INFO()    


def PHYSIQUE(resultats):
    final = physique(resultats)
    return final
# PHYSIQUE()

def DEV(resultats):
    noteang = (Moyenne(matiere(anglais(resultats)[0])[0]))
    if (noteang == 21):
        return "ERREUR anglais"
    notecomm = (Moyenne(matiere(comm(resultats)[0])[0]))
    if (notecomm == 21):
        return "ERREUR Comm"
    notespo = (Moyenne(matiere(sport(resultats)[0])[0]))
    if (notespo == 21):
        return "ERREUR sport"
    note = [noteang, notecomm, notespo]
    coef = [2,2,2]
    note = MoyenneC(note, coef)
    final = (round(note,2))
    return final
# DEV()


def main(username,password):
    # result = getnotes.main(username,password)
    # # print(result)
    # resultats = TableNotes.table(result)  #Liste de liste de note sous forme ['07/01/2022', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'P1'], 'Partiel de Technologies Web', ' 16.60', '24']
    # # print(resultats)
    resultats = [['07/01/2022', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'P1'], 'Partiel de Technologies Web', ' 14.20', '24'],['18/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'LV2', 'DS'], 'Devoir surveill� de LV2', ' 0.00', '1'], ['18/12/2021',['2122', 'ISEN', 'CIR1', 'S1', 'LV2', 'ECRIT'], 'Expression �crite', ' 6.50', '1'], ['18/12/2021', ['2122', 'ISEN','CIR1', 'S1', 'LV2', 'ORAL'], 'Expression orale', ' 17.00', '1'], ['18/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'LV2','PART'], 'Participation', ' 12.00', '1'], ['14/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'MATH', 'TP6', '3'], 'Evaluationdu TP6', ' 9.50', '1'], ['10/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'MATH2', 'CC5'], 'Contr�le Continu deMath�matiques n�5', ' 11.60', '1'], ['10/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'CC2'], 'Contr�le Continu deTechnologies Web n�2', ' 14.00', '12'], ['09/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'ELEC', 'DS'], "Devoir Surveill�d'�lectronique", ' 12.50', '1'], ['07/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'ELEC', 'TP4', '3'], 'Evaluation du TP4',' 13.00', '1'], ['06/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'ANGLAIS', '5', 'NOTE'], "Moyenne d'Anglais (groupe 5)", '13.20', '1'], ['06/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'SPORT', 'T3'], 'Note de Sport Tiers 3', ' 16.00', '1'],['06/12/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'WEB', 'PROJ'], 'Projet de Technologies Web', ' 13.00', '20'],['26/11/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'MATH2', 'CC4'], 'Contr�le Continu de Math�matiques n�4', ' 9.10', '1'],['26/11/2021', ['2122', 'ISEN', 'CIR1', 'S1', 'PROG1', 'CC2'], 'Contr�le Continu n�2', ' 11.50', '1'], ['24/11/2021',['2122', 'ISEN', 'CIR1', 'S1', 'MATH2', 'IE3'], 'Interrogation de cours n�3', ' 7.00', '0,33'], ['24/11/2021', ['2122','ISEN', 'CIR1', 'S1', 'MATH2', 'IE3'], 'Interrogation de cours n�3', ' 7.00', '1'], ['23/11/2021', ['2122', 'ISEN','CIR1', 'S1', 'ELEC', 'TP3', '3'], 'Evaluation du TP3', ' 9.50', '1'], ['20/11/2021', ['2122', 'ISEN', 'CIR1', 'S1','OPTIQUE', 'P2'], "Partiel d'Optique - 2nde session", ' 8.40', '1'], ['19/11/2021', ['2122', 'ISEN', 'CIR1', 'S1','WEB', 'DS'], 'DS Technologies Web', ' 12.98', '12']]
    print(MATHS(resultats),PHYSIQUE(resultats),INFO(resultats),DEV(resultats))
    
main("fds", "dsf")