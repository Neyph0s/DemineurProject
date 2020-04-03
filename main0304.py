from tkinter import *
from random import *

WIDTH = 544 #dimmension largeur
HEIGHT = 306 #dimension hauteur

my_root = Tk() 
my_root.title("LE DEMINEUR 1.0 ACCES ANTICIPE") #titre de la fenetre

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



#===================#
#generation du cadre#
#===================#
def genererCadre(lvl):
    if lvl==1:
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
    my_root.geometry("170x170")
    lvl=1
    global M
    M=genererGrille(lvl)
    genMine(M,lvl)
    clcNbMine(M)
    afficher(M)
    genererCadre(lvl)
       
    return(lvl)

M=[]
def niveau2():
    
    my_root.geometry("306x306")
    lvl=2
    global M
    M=genererGrille(lvl)
    genMine(M,lvl)
    clcNbMine(M)
    afficher(M)
    genererCadre(lvl)
    return(lvl)

M=[]
def niveau3():
    my_root.geometry("544x306")
    lvl=3
    global M
    M=genererGrille(lvl)
    genMine(M,lvl)
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
    cnv.create_text(C, anchor =W,text =var, fill ="blue", font="Arial 10")

    
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
#adjacents à la case cliqué    #
#==============================#
def verifAuto(i, j, M):
    x, y = len(M), len(M[0])
    if M[j][i]==0:
        for l in range(j,x,1):
            for k in range(i,y,1):
                if M[l][k]==0:
                   verif(k,l,M)
                   
                
            for k in range(i,0,-1):
                if M[l][k]==0:
                   verif(k,l,M)
        for l in range(j,0,-1):
            for k in range(i,y,1):
                if M[l][k]==0:
                   verif(k,l,M)
            for k in range(i,0,-1):
                if M[l][k]==0:
                   verif(k,l,M)
        
        

   
def je_cliqueG(event):
    x, y = event.x, event.y
    xC, yC = coordModulo(x,y)
    #cnv.create_oval(x-3, y-3, x+3, y+3,fill='red', outline='')
    i, j = grilleToTab(xC, yC)
    verifAuto(i, j,M)
    verif2(i, j,M)

def je_cliqueD(event):
    x, y = event.x, event.y
    xC, yC = coordModulo(x,y)
    cnv.create_oval(x-3, y-3, x+3, y+3,fill='red', outline='')



   
cnv.bind("<Button-3>",je_cliqueD)
cnv.bind("<Button-1>",je_cliqueG)

menu()
my_root.mainloop()


































