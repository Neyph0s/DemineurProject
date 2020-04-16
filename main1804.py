#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from random import *
from time import *



WIDTH = 800 #dimmension largeur
HEIGHT = 306 #dimension hauteur

my_root = Tk() 
my_root.title("LE DEMINEUR 1.0 ACCES ANTICIPE") #titre de la fenetre

cnv=Canvas(my_root, width=WIDTH, height=HEIGHT, background='ivory') #création de la fenetre
my_root.resizable(width=False, height=False) #bloquer le redimmensionement de la fenetre
 
cnv.pack()


#==================#
#gestion du chrnono#
#==================#
actu=0
Minuteur=Label(my_root,text="Debut depuis 0 s")
Minuteur.place(x= -100, y = -100, width=100, height=25)

lblNbMines = Label(my_root, text="nombre de mines: ")
lblNbMines.place(x= -100, y = -200, width=120, height=25)


###############
global lvl
lvl=0#initialisation du niveau 0, debut de jeu
#===========================#
#fonction pour gerer le menu#
#===========================#
def menu():
    menubar = Menu(my_root) 
    menu1 = Menu(menubar, tearoff=0) 
    menubar.add_cascade(label="Nouvelle partie", command=nouvellePartie) 
    menu2 = Menu(menubar, tearoff=0) 
    menu2.add_command(label="Facile", command=niveau1) 
    menu2.add_command(label="Moyen", command=niveau2) 
    menu2.add_command(label="Difficile", command=niveau3) 
    menubar.add_cascade(label="Difficulté", menu=menu2)
    menu3 = Menu(menubar, tearoff=0) 
    menubar.add_cascade(label="Recommencer", command=recommencer)  
    my_root.config(menu=menubar)


#==================================================#
#permet de generer une grille en fonction du niveau#
#==================================================#
def genererGrille(lvl):
   
    if lvl==1:                
        M=matriceNulle(8,8)
        
    if lvl==2:
        M=matriceNulle(16,16)
                
    if lvl==3:
        M=matriceNulle(16,30)
            
    return(M)


#=================================================#
#permet de visualiser la matrice qui a ete generee#
#=================================================#
def afficher(M):
    "Affiche une matrice en respectant les alignements par colonnes"
    w=[max([len(str(M[i][j])) for i in range(len(M))]) for j in range(len(M[0]))]
    for i in range(len(M)):
        for j in range(len(M[0])):
            print("%*s" %(w[j],str(M[i][j])), end= ' ')
        print()  


#===================================#
#permet de generer une matrice nulle#
#===================================#
def matriceNulle(n, p):
    "Constructeur de matrice de dimensions données"
    M=[]
    for i in range(n):
        L=[]
        for j in range(p):
            L.append(0)
        M.append(L)
    return M

def dimensions(A):
    return [len(A), len(A[0])]



        
#=================================================#
#petites fonctions pour faciliter def clcNbMine(M)#
#=================================================#
def testN(M,x,y):
    if M[x-1][y]== -1:
       return(True)
    else:
        return(False)
    
def testE(M,x,y):
    if M[x][y+1] == -1:
       return(True)
    else:
        return(False)
    
def testS(M,x,y):
    if M[x+1][y]== -1:
       return(True)
    else:
        return(False)
    
def testW(M,x,y):
    if M[x][y-1]== -1:
       return(True)
    else:
        return(False)
    
def testNW(M,x,y):
    if M[x-1][y-1]== -1:
       return(True)
    else:
        return(False)
    
def testNE(M,x,y):
    if M[x-1][y+1]== -1:
       return(True)
    else:
        return(False)
    
def testSE(M,x,y):
    if M[x+1][y+1]== -1:
       return(True)
    else:
        return(False)
    
def testSW(M,x,y):
    if M[x+1][y-1]== -1:
       return(True)
    else:
        return(False)

#=================================================#
#calcul du nombre de mines autour de chaques cases#
#=================================================#
def nbMineHG(M,x,y):
    nbMine=0
    if testE(M,x,y)==True:
        nbMine=nbMine+1
    if testSE(M,x,y)==True:
        nbMine=nbMine+1
    if testS(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineHD(M,x,y):
    nbMine=0
    if testW(M,x,y)==True:
        nbMine=nbMine+1
    if testSW(M,x,y)==True:
        nbMine=nbMine+1
    if testS(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineBG(M,x,y):
    nbMine=0
    if testN(M,x,y)==True:
        nbMine=nbMine+1
    if testNE(M,x,y)==True:
        nbMine=nbMine+1
    if testE(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineBD(M,x,y):
    nbMine=0
    if testN(M,x,y)==True:
        nbMine=nbMine+1
    if testNW(M,x,y)==True:
        nbMine=nbMine+1
    if testW(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineLS(M,x,y):
    nbMine=0
    if testW(M,x,y)==True:
        nbMine=nbMine+1
    if testSW(M,x,y)==True:
        nbMine=nbMine+1
    if testS(M,x,y)==True:
        nbMine=nbMine+1
    if testSE(M,x,y)==True:
        nbMine=nbMine+1
    if testE(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineLI(M,x,y):
    nbMine=0
    if testW(M,x,y)==True:
        nbMine=nbMine+1
    if testNW(M,x,y)==True:
        nbMine=nbMine+1
    if testN(M,x,y)==True:
        nbMine=nbMine+1
    if testNE(M,x,y)==True:
        nbMine=nbMine+1
    if testE(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineCG(M,x,y):
    nbMine=0
    if testN(M,x,y)==True:
        nbMine=nbMine+1
    if testNE(M,x,y)==True:
        nbMine=nbMine+1
    if testE(M,x,y)==True:
        nbMine=nbMine+1
    if testSE(M,x,y)==True:
        nbMine=nbMine+1
    if testS(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineCD(M,x,y):
    nbMine=0
    if testN(M,x,y)==True:
        nbMine=nbMine+1
    if testNW(M,x,y)==True:
        nbMine=nbMine+1
    if testW(M,x,y)==True:
        nbMine=nbMine+1
    if testSW(M,x,y)==True:
        nbMine=nbMine+1
    if testS(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def nbMineMiddle(M,x,y):
    nbMine=0
    if testN(M,x,y)==True:
        nbMine=nbMine+1
    if testNE(M,x,y)==True:
        nbMine=nbMine+1
    if testE(M,x,y)==True:
        nbMine=nbMine+1
    if testSE(M,x,y)==True:
        nbMine=nbMine+1
    if testS(M,x,y)==True:
        nbMine=nbMine+1
    if testSW(M,x,y)==True:
        nbMine=nbMine+1
    if testW(M,x,y)==True:
        nbMine=nbMine+1
    if testNW(M,x,y)==True:
        nbMine=nbMine+1
    return(nbMine)

def clcNbMine(M):
    lx, ly = dimensions(M)
    for i in range(lx):
        for j in range(ly):
            nbMine=0
            if M[i][j]==0:
                if i==0 and j==0:
                    nbMine=nbMineHG(M,i,j)
                if i==0 and j==(ly-1):
                    nbMine=nbMineHD(M,i,j)
                if i==(lx-1) and j==(ly-1):
                    nbMine=nbMineBD(M,i,j)
                if i==(lx-1) and j==0:
                    nbMine=nbMineBG(M,i,j)        
                if i==0 and j!=(ly-1) and j!=0:
                    nbMine=nbMineLS(M,i,j)
                if i==(lx-1) and j!=(ly-1) and j!=0:
                    nbMine=nbMineLI(M,i,j)            
                if j==0 and i!=0 and i!=(lx-1):
                    nbMine=nbMineCG(M,i,j)                  
                if j==(ly-1 )and i!=0 and i!=(lx-1):
                    nbMine=nbMineCD(M,i,j)
                if i!=0 and i!=(lx-1) and j!=0 and j!=(ly-1):
                    nbMine=nbMineMiddle(M,i,j)
                
                M[i][j]=nbMine


def centre(x,y):
    x=(x+17)/2
    y=(y+17)/2
    return(x,y)

def recommencer():
    global arret
    arret = 0
    cnv.delete("all")
    genererCadre(cadre)
    global actu #variable pour le chronomètre
    actu = 0 #variable pour le chronomètre
    global nbMines
    nbMines = minesTmp
    lblNbMines.config(text='il reste '+str(nbMines)+' mines' )
    
    

def nouvellePartie():
    global arret
    arret = 0
    cnv.delete("all")
    genererCadre(cadre)
    global M
    M=genererGrille(cadre)
    global nbMines
    nbMines=genMine(M, cadre)
    lblNbMines.config(text='il reste '+str(nbMines)+' mines' )
    clcNbMine(M)
    afficher(M)
    global actu #variable pour le chronomètre
    actu = 0 #variable pour le chronomètre

#===================#
#generation du cadre#
#===================#
def genererCadre(lvl):
    
    global cadre
    if lvl==1:
        Minuteur.place(x= 180, y = 17, width=100, height=25)
        lblNbMines.place(x= 180, y = 47, width=120, height=25)
        cadre = 1
        cnv.delete("all")
        a=17
        c=17
        for i in range(9):
            A=(a,c)
            B=(a,17*9)
            C=(c,a)
            D=(17*9,a)
            cnv.create_line(A,B)
            cnv.create_line(C,D)
            a=a+17

    if lvl==2:
        Minuteur.place(x= 320, y = 17, width=100, height=25)
        lblNbMines.place(x= 320, y = 47, width=120, height=25)
        cadre = 2
        cnv.delete("all")
        a=17
        c=17
        for i in range(17):
            A=(a,c)
            B=(a,17*17)
            C=(c,a)
            D=(17*17,a)
            cnv.create_line(A,B)
            cnv.create_line(C,D)
            a=a+17

    if lvl==3:
        Minuteur.place(x= 550, y = 17, width=100, height=25)
        lblNbMines.place(x= 550, y = 47, width=120, height=25)
        cadre = 3
        cnv.delete("all")
        a=17
        c=17
        for i in range(31):
            A=(a,c)
            B=(a,17*17)
            cnv.create_line(A,B)
            a=a+17      
        a=17
        c=17
        for i in range(17):
            C=(c,a)
            D=(17*31,a)
            cnv.create_line(C,D)
            a=a+17



#============================#
#choix du niveau dans le menu#
#============================#


M=[]
def niveau1():
    global arret
    arret = 0
    global actu
    if actu==0:
        chrono()
    if actu>0:
        actu=0
    my_root.geometry("300x170")
    lvl=1
    global M
    global D
    D=genererGrille(lvl)
    M=genererGrille(lvl)
    
    global nbMines
    nbMines=genMine(M,lvl)
    lblNbMines.config(text='il reste '+str(nbMines)+' mines' )
    global minesTmp
    minesTmp=nbMines
    
    clcNbMine(M)
    afficher(M)
    genererCadre(lvl)
       
    return(lvl)

M=[]
def niveau2():
    global arret
    arret = 0
    global actu 
    if actu==0:
        chrono()
    if actu>0:
        actu=0 
    my_root.geometry("450x306")
    lvl=2
    global M
    global D
    D=genererGrille(lvl)
    M=genererGrille(lvl)
    
    global nbMines
    nbMines=genMine(M,lvl)
    lblNbMines.config(text='il reste '+str(nbMines)+' mines' )
    global minesTmp
    minesTmp=nbMines
    
    clcNbMine(M)
    afficher(M)
    genererCadre(lvl)
    return(lvl)

M=[]
def niveau3():
    global arret
    arret = 0
    global actu
    if actu==0:
        chrono()
    if actu>0:
        actu=0 
    my_root.geometry("675x306")
    lvl=3
    global M
    global D
    D=genererGrille(lvl)
    M=genererGrille(lvl)
    
    global nbMines
    nbMines=genMine(M,lvl)
    lblNbMines.config(text='il reste '+str(nbMines)+' mines' )
    global minesTmp
    minesTmp=nbMines
    
    clcNbMine(M)
    afficher(M)
    genererCadre(lvl)
    return(lvl)


#=====================================================================================#
#permet de determiner les coordonnées du coin gauche supérieur de la case ou on clique#
#=====================================================================================#
def coordModulo(xSouri, ySouri):
    while xSouri%17!=0:
        xSouri = xSouri - 1
    while ySouri%17!=0:
        ySouri = ySouri - 1
    return (xSouri, ySouri)
   
#==================================#
#permet de determiner à partir     #
#de la case dans laquelle on clique#
#à quelle coordonée  du tableau de #
#mines ca correspond               #
#==================================#
def grilleToTab(xC, yC):
    i = (xC//17)-1
    j = (yC//17)-1
    return(i, j)

#=====================================#
#Permet d'afficher une valeur dans    #
#le canvas à partir du tableau de jeu #
#=====================================#
def afficherVal(i, j, M):
    var = M[j][i]
    xC = ((i+1)*17)+7
    yC = ((j+1)*17)+9    
    C=(xC,yC)
    cnv.create_text(C, anchor =W,text =var, fill ="black", font="Arial 10")

    
#====================================================#
#codes de retour:                                    #
#   0=> colonne extrême                              #
#   1=> valeur adjacente = 0                         #
#   2=> valeur adjacente indiquant un nombre de mines#
#   3=> valeur adjacente = -1                        #
#====================================================#
#=============================================#
#Permet de verifier la valeur à gauche du clic#
#=============================================#
def verifW(i, j, M):    
    if i==0:
        return 0 
    if M[j][i-1]==0:
        afficherVal(i-1, j, M)
        return 1
    if M[j][i-1]!= -1 and M[j][i-1]!= 0:
        afficherVal(i-1, j, M)
        return 2
    if M[j][i-1]== -1:
        return 3
    
#=============================================#
#Permet de verifier la valeur à droite du clic#
#=============================================#
def verifE(i, j, M):
    x = len(M[0])
    if i==x-1:
        return 0
    if M[j][i+1]==0:        
        afficherVal(i+1, j, M)
        return 1
    if M[j][i+1]!= -1 and M[j][i+1]!= 0:
        afficherVal(i+1, j, M)
        return 2
    if M[j][i+1]== -1:
        return 3

#=============================================#
#Permet de verifier la valeur en bas du clic  #
#=============================================#
def verifN(i, j, M):    
    if j==0:
        return 0 
    if M[j-1][i]==0:
        afficherVal(i, j-1, M)
        return 1
    if M[j-1][i]!= -1 and M[j-1][i]!= 0:
        afficherVal(i, j-1, M)
        return 2
    if M[j-1][i]== -1:
        return 3

#==============================================#
#Permet de verifier la valeur en haut du clic  #
#==============================================#
def verifS(i, j, M):
    x = len(M)
    if j==x-1:
        return 0
    if M[j+1][i]==0:
        afficherVal(i, j+1, M)
        return 1
    if M[j+1][i]!= -1 and M[j+1][i]!= 0:
        afficherVal(i, j+1, M)
        return 2
    if M[j+1][i]== -1:
        return 3

#=============================================#
#Permet de verifier la valeur en bas du clic  #
#=============================================#
def verifNW(i, j, M):
    x = len(M)
    if j==0 or i==0:
        return 0 
    if M[j-1][i-1]==0:
        afficherVal(i-1, j-1, M)
        return 1
    if M[j-1][i-1]!= -1 and M[j-1][i-1]!= 0:
        afficherVal(i-1, j-1, M)
        return 2
    if M[j-1][i-1]== -1:
        return 3

#=============================================#
#Permet de verifier la valeur en bas du clic  #
#=============================================#
def verifNE(i, j, M):
    x = len(M)
    y = len(M[0])
    if j==0 or i==y-1:
        return 0 
    if M[j-1][i+1]==0:
        afficherVal(i+1, j-1, M)
        return 1
    if M[j-1][i+1]!= -1 and M[j-1][i+1]!= 0:
        afficherVal(i+1, j-1, M)
        return 2
    if M[j-1][i+1]== -1:
        return 3

#======================================================#
#Permet de verifier la valeur en bas à gauche du clic  #
#======================================================#
def verifSW(i, j, M):
    x = len(M)
    if j==x-1 or i==0:
        return 0 
    if M[j+1][i-1]==0:
        afficherVal(i-1, j+1, M)
        return 1
    if M[j+1][i-1]!= -1 and M[j+1][i-1]!= 0:
        afficherVal(i-1, j+1, M)
        return 2
    if M[j+1][i-1]== -1:
        return 3

#=============================================#
#Permet de verifier la valeur en bas du clic  #
#=============================================#
def verifSE(i, j, M):
    x = len(M)
    y = len(M[0])
    if j==x-1 or i==x-1:
        return 0 
    if M[j+1][i+1]==0:
        afficherVal(i+1, j+1, M)
        return 1
    if M[j+1][i+1]!= -1 and M[j+1][i+1]!= 0:
        afficherVal(i+1, j+1, M)
        return 2
    if M[j+1][i+1]== -1:
        return 3



#=============================#
#verifie et decouvre les cases#
#autour de celle ou on clique #
#si on clique sur un 0        #
#=============================#
def verif(i, j, M):
    if M[j][i]==0:
        afficherVal(i, j, M)
        verifN(i, j, M)
        verifS(i, j, M)
        verifE(i, j, M)
        verifW(i, j, M)
        verifNW(i, j, M)
        verifNE(i, j, M)
        verifSW(i, j, M)
        verifSE(i, j, M)
    if M[j][i]!=0:
        return 0
    

#==============================#
#affiche la valeur sur laquelle#
#on a cliqué                   #
#==============================#
def verif2(i, j, M):
        afficherVal(i, j, M)
               
        
   
#==============================#
#permet de supprimer tout les 0#
#adjacents à la case cliquée   #
#==============================#
def verifAuto(i, j, M):
    x, y = len(M), len(M[0])
    CroixAuto(i, j, M)
    verifMine(i, j, M)


    
def CroixAuto(i, j, M):
    x, y = len(M), len(M[0])

    for k in range(j, -1, -1):
        if M[k][i]!=0:
            break 
        for l in range(i, y, 1):
            if M[k][l]!=0:
                break
            verifCroix(l, k, M)
            

    for k in range(j, -1, -1):
        if M[k][i]!=0:
            break
        for l in range(i, -1, -1):
            if M[k][l]!=0:
                break
            verifCroix(l, k, M)

    for k in range(j, x, 1):
        if M[k][i]!=0:
            break
        for l in range(i, -1, -1):
            if M[k][l]!=0:
                break
            verifCroix(l, k, M)

    for k in range(j, x, 1):
        if M[k][i]!=0:
            break
        for l in range(i, y, 1):
            if M[k][l]!=0:
                break
            verifCroix(l, k, M)

def verifCroix(i, j, M):
    verifLigne(i, j, M)
    verifColonne(i, j, M)
     
def verifBas(i, j, M):
    x, y = len(M), len(M[0])
    for k in range(j, x, 1):
        verif(i, k, M)
        
        if M[k][i]!=0 or j==x-1:
            return 0

def verifHaut(i, j, M):
    x, y = len(M), len(M[0])
    for k in range(j, -1, -1):
        verif(i, k, M)
        
        if M[k][i]!=0 or j==0:
            return 0
        
def verifDroite(i, j, M):
    x, y = len(M), len(M[0])
    for k in range(i, y, 1):
        verif(k, j, M)
       
        if M[j][k]!=0 or i==y-1:
            return 0

def verifGauche(i, j, M):
    y = len(M[0])
    for k in range(i, -1, -1):
        verif(k, j, M)
        
        if M[j][k]!=0 or i==0:
            return 0

def verifLigne(i, j, M):
    verifDroite(i, j, M)
    verifGauche(i, j, M)
    
    

def verifColonne(i, j, M):
    verifBas(i, j, M)
    verifHaut(i, j, M)
    
##############################

def je_cliqueG(event):
    x, y = event.x, event.y
    xC, yC = coordModulo(x,y)
    i, j = grilleToTab(xC, yC)
    
    global M
    global arret
    if M[j][i]==-1:
        verifMine(i,j,M)
        arret=1
    if arret==1:
        return(0)
    
    
    xC = xC+9
    yC = yC+9
    if cadre==1 and xC<=152 and xC>=17 and yC>=17 and yC<=152:
        verifAuto(i, j,M)
        verif2(i, j,M)
    if cadre==2 and xC<=288 and xC>=17 and yC>=17 and yC<=288:
        verifAuto(i, j,M)
        verif2(i, j,M)
    if cadre==3 and xC<=526 and xC>=17 and yC>=17 and yC<=288:
        verifAuto(i, j,M)
        verif2(i, j,M)
    
    

def je_cliqueD(event):
    global nbMines
    global arret
    global D
    DejClic=0
    x, y = event.x, event.y
    xC, yC = coordModulo(x,y)   
    if arret==1:
        return 0 
    
    xC = xC+9
    yC = yC+9
    i,j=grilleToTab(xC, yC)
    
    if D[j][i]==-1:
        t=cnv.find_closest(x, y)
        if t:
            cnv.delete(t[0])
        nbMines = nbMines+1
        lblNbMines.config(text='il reste '+str(nbMines)+' mines' )
        D[j][i]=0
        DejClic=1
    if D[j][i]==0 and DejClic==0 and nbMines>0:
        if cadre==1 and xC<=152 and xC>=17 and yC>=17 and yC<=152:
            placerImage = cnv.create_image(xC, yC, image = imgDrapeau)
            nbMines = nbMines-1
        if cadre==2 and xC<=288 and xC>=17 and yC>=17 and yC<=288:
            placerImage = cnv.create_image(xC, yC, image = imgDrapeau)
            nbMines = nbMines-1
        if cadre==3 and xC<=526 and xC>=17 and yC>=17 and yC<=288:
            placerImage = cnv.create_image(xC, yC, image = imgDrapeau)
            nbMines = nbMines-1
        lblNbMines.config(text='il reste '+str(nbMines)+' mines' )
        D[j][i]=-1
    
    if nbMines==0:
        Victoire()
    
    
    
        

def chrono():    
    global actu
    Minuteur.config(text='Debut depuis '+str(actu)+' s' )
    actu=actu+1
    my_root.after(1000,chrono)
    


#=====================#
#nb de Mines selon lvl#
#      lvl1 => 10     #
#      lvl2 => 40     #
#      lvl3 => 99     #
#=====================#
def genMine(A, lvl):
    n,p = dimensions(A)
    xyMine=[]
    if lvl == 1:
        for i in range(10):
            k = randint(0,n-1)
            l= randint(0,p-1)
            A[k][l]=-1            
    if lvl == 2:
        for i in range(40):
            k = randint(0,n-1)
            l= randint(0,p-1)
            A[k][l]=-1           
    if lvl == 3:
        for i in range(99):
            k = randint(0,n-1)
            l= randint(0,p-1)
            A[k][l]=-1
    return nbMinesM(A,n,p)


def nbMinesM(A,n,p):
    nbMines=0
    for i in range(n):
        for j in range(p):
            if A[i][j]==-1:
                nbMines = nbMines + 1
    return nbMines
#=================#
#Clic sur une mine#
#=================#

    
    
def verifMine(i,j,M):
    n,p=dimensions(M)
    if cadre==1:
        wi=300
        he=170
    if cadre==2:
        wi=450
        he=306
    if cadre==3:
        wi=675
        he=306
    if M[j][i]==-1:
        C=(wi,he//1.5 )
        cnv.create_text(C, anchor =E,text ="Perdu !", fill ="red", font="Arial 30 bold")
        for k in range (n):
            for m in range (p):
                if M[k][m]==-1:
                    afficherMin(m, k, M)
    

def afficherMin(i, j, M):
    var = M[j][i]
    xC = ((i+1)*17)+9
    yC = ((j+1)*17)+9    
    C=(xC,yC)
    placerImage = cnv.create_image(C, image = imgMine)

#====================#
#Vérification victoire#
#====================#

def Victoire():
    global D
    global M
    global arret
    if cadre==1:
        wi=300
        he=170
    if cadre==2:
        wi=450
        he=306
    if cadre==3:
        wi=675
        he=306
    n,p=dimensions(M)
    TabMines=matriceNulle(n,p)
    gagner=1
    for i in range (n):
        for j in range (p):
            if M[i][j]==-1:
                TabMines[i][j]=-1
    for i in range (n):
        for j in range (p):
            if TabMines[i][j]!=D[i][j]:
                gagner=0
    if gagner == 1:
        C=(wi,he//1.5 )
        cnv.create_text(C, anchor =E,text ="Victoire !", fill ="green", font="Arial 20 bold")
        arret=1
    






imgPerdu = PhotoImage(file="sprite/perdu.png")
imgDrapeau = PhotoImage(file="sprite/drapeau.png")
imgMine = PhotoImage(file="sprite/mine.png")

   
cnv.bind("<Button-3>",je_cliqueD)
cnv.bind("<Button-1>",je_cliqueG)

menu()
my_root.mainloop()



# In[ ]:




