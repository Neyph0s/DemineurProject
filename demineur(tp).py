from tkinter import *
from random import *

WIDTH = 510 #dimmension largeur
HEIGHT = 272 #dimension hauteur

my_root = Tk() 
my_root.title("LE DEMINEUR ALPHA v1.0") #titre de la fenetre

cnv=Canvas(my_root, width=WIDTH, height=HEIGHT, background='ivory') #création de la fenetre
my_root.resizable(width=False, height=False) #bloquer le redimmensionement de la fenetre
cnv.pack()


#======================================================================================#
lvl=0#initialisation du niveau 0, debut de jeu
#===========================#
#fonction pour gerer le menu#
#===========================#
def menu():
    menubar = Menu(my_root) #appel de la methode pour créer les menus
    menu1 = Menu(menubar, tearoff=0) #creation du 1er menu
    menubar.add_cascade(label="Nouvelle partie", command=my_root.quit) #on y associe l'action voulue, ici on quitte car on a pas encore fini
    menu2 = Menu(menubar, tearoff=0) #creation du 2eme menu
    menu2.add_command(label="Facile", command=niveau1) #on y associe l'action voulue, ici on quitte car on a pas encore fini
    menu2.add_command(label="Moyen", command=niveau2) #on y associe l'action voulue, ici on quitte car on a pas encore fini
    menu2.add_command(label="Difficile", command=niveau3) #on y associe l'action voulue, ici on quitte car on a pas encore fini
    menubar.add_cascade(label="Difficulté", menu=menu2)
    menu3 = Menu(menubar, tearoff=0) #creation du 3eme menu
    menubar.add_cascade(label="Recommencer", command=my_root.quit) #on y associe l'action voulue, ici on quitte car on a pas encore fini
    my_root.config(menu=menubar) #ici on peut configurer notre menu

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
            
#============================#
#choix du niveau dans le menu#
#============================#
def niveau1():
    lvl=1
    print(lvl)
    M=genererGrille(lvl)
    genMine(M,lvl)
    clcNbMine(M)
    afficher(M)
    Case=genererCadre(lvl)
    return(lvl)

def niveau2():
    lvl=2
    print(lvl)
    M=genererGrille(lvl)
    genMine(M,lvl)
    clcNbMine(M)
    afficher(M)
    Case=genererCadre(lvl)
    return(lvl)

def niveau3():
    lvl=3
    print(lvl)
    M=genererGrille(lvl)
    genMine(M,lvl)
    clcNbMine(M)
    afficher(M)
    Case=genererCadre(lvl)
    return(lvl)

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

imgDrapeau = PhotoImage(file="sprite/drapeau.png")
imgUn = PhotoImage(file="sprite/1.png")
imgDeux = PhotoImage(file="sprite/2.png")
imgTrois = PhotoImage(file="sprite/3.png")
imgQuatre = PhotoImage(file="sprite/4.png")
imgCinq = PhotoImage(file="sprite/5.png")
imgSix = PhotoImage(file="sprite/6.png")
imgSept = PhotoImage(file="sprite/7.png")
imgHuit = PhotoImage(file="sprite/8.png")
imgRien = PhotoImage(file="sprite/rien.png")
imgPerdu = PhotoImage(file="sprite/perdu.png")
imgNonPassee = PhotoImage(file="sprite/nonpassee.png")
imgMine2 = PhotoImage(file="sprite/mine2.png")
imgMine = PhotoImage(file="sprite/mine.png")

def centre(x,y):
    x=(x+17)/2
    y=(y+17)/2
    return(x,y)

def genererCadre(lvl):
    x0=17
    y0=17
    coordCase=[]
    if lvl==1:
        while x0<(8*17):
            L=[]
            while y0<(8*17):
                placerImage = cnv.create_image(x0, y0, image = imgNonPassee)
                x,y=centre(x0,y0)
                L.append(x)
                L.append(y)
                y0+=17
            coordCase.append(L)
            x0+=17
            y0=17
    if lvl==2:
        while x0<(16*17):
            L=[]
            while y0<(16*17):
                placerImage = cnv.create_image(x0, y0, image = imgNonPassee)
                x,y=centre(x0,y0)
                L.append(x)
                L.append(y)
                y0+=17
            coordCase.append(L)
            x0+=17
            y0=17
    if lvl==3:
        while x0<(30*17):
            L=[]
            while y0<(16*17):
                placerImage = cnv.create_image(x0, y0, image = imgNonPassee)
                x,y=centre(x0,y0)
                L.append(x)
                L.append(y)
                y0+=17
            coordCase.append(L)
            x0+=17
            y0=17
    return(coordCase)
               
        







menu()
my_root.mainloop()






