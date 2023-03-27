"""Relou
coeur = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], \
        [0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0], \
        [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0], \
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], \
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], \
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0], \
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], \
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def affiche(dessin):
    ''' affichage d'une grille : les 1 sont représentés par
    des " *" , les 0 par deux espaces "  " '''
    for ligne in dessin:
        for col in ligne:
            if col == 1:
                print(' *',end='')
            else:
                print('  ',end='')
        print()

def zoomListe(liste_depart, k):
    '''renvoie une liste contenant k fois chaque
    élément de liste_depart'''
    liste_zoom = []
    for elt in liste_depart:
        for i in range(k):
            liste_zoom.append(elt)
    return liste_zoom

def zoomDessin(grille, k):
    '''renvoie une grille où les lignes sont zoomées k fois
    ET répétées k fois'''
    grille_zoom = []
    for elt in grille:
        liste_zoom = zoomListe(elt, k)
        for i in range(k):
            grille_zoom.append(liste_zoom)
    return grille_zoom
print(affiche(zoomDessin(coeur,3)))
"""
"""4
def a_doublon(lst):
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return True
    return False
print(a_doublon([1, 2, 4, 6, 6]),a_doublon([0, 2, 3]),a_doublon([2, 5, 7, 7, 7, 9]))
"""
'''Dur
def voisinage(n, ligne, colonne):
    """ Renvoie la liste des coordonnées des voisins de la case
    (ligne, colonne) en gérant les cases sur les bords. """
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins


def incremente_voisins(grille, ligne, colonne):
    """ Incrémente de 1 toutes les cases voisines d'une bombe."""
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1: # si ce n'est pas une bombe
            grille[l][c] += 1  # on ajoute 1 à sa valeur



def genere_grille(bombes):
    """ Renvoie une grille de démineur de taille nxn où n est
    le nombre de bombes, en plaçant les bombes à l'aide de
    la liste bombes de coordonnées (tuples) passée en
    paramètre. """
    n = len(bombes)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    # Place les bombes et calcule les valeurs des autres cases
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1 # place la bombe
        incremente_voisins(grille, ligne, colonne) # incrémente ses voisins

    return grille
'''
"""5
from random import *
def lancer(n):
    list=[]
    for i in range(n):
        r=randint(1,6)
        list.append(r)
    return list

def paire_6(list):
    c=0
    for i in list:
        if i==6:
            c+=1
    if c>=2:
        return True
    else:
        return False

lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))
lancer4 = lancer(0)
print(lancer4)
"""
"""7 #FDP #dur
def fusion(tab1, tab2):
    tab_fusion = []
    i1 = 0
    i2 = 0
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_fusion.append(tab1[i1])
            i1 += 1
        else:
            tab_fusion.append(tab2[i2])
            i2 += 1

    if i1 == len(tab1):
        while i2 < len(tab2):
            tab_fusion.append(tab2[i2])
            i2 += 1
    else:
        while i1 < len(tab1):
            tab_fusion.append(tab1[i1])
            i1 += 1

    return tab_fusion
"""
"""Relou
romains = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
def traduire_romain(nombre):
    if len(nombre) == 1:
        return romains[nombre]
    elif romains[nombre[0]] >= romains[nombre[1]]
        return romains[nombre[0]] + traduire_romain(nombre[1:])
    else:
        return traduire_romain(nombre[1:]) - romains[nombre[0]]
"""
"""11.1
def convertir(tab):
    puissance = 0
    total = 0
    for i in range(len(tab)-1, -1, -1):
        total += tab[i]*(2**puissance)
        puissance += 1
    return total
print(convertir([1, 0, 1, 0, 0, 1, 1]))
"""
"""#FDP #Dur
def tri_insertion(tab):
    n = len(tab)
    for i in range(1, n):
        valeur_insertion = tab[i]
        # la variable j sert à déterminer où placer la valeur à ranger
        j = i
        # tant qu'on a pas trouvé la place de l'élément à insérer
        # on décale les valeurs du tableau vers la droite
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j - 1
        tab[j] = valeur_insertion
liste = [9, 5, 8, 4, 0, 2, 7, 1, 10, 3, 6]
print(tri_insertion(liste))
""""""12.1 #Relou
def ajoute(cle, a):
    if a is None:
        a = ABR(None, cle, None)
    elif cle > a.cle:
        a.droit = ajoute(cle, a.droit)
    elif cle < a.cle:
        a.gauche = ajoute(cle, a.gauche)
    return a
""" #Sava
"""
def empaqueterR(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses :
        i = 0
        while i <= nb_boites and boites[i] + masse > c:
            i = i + 1
        if i == nb_boites + 1:
            nb_boites = nb_boites + 1
        boites[i] = boites[i] + masse
    return nb_boites + 1
""""""16.1
def recherche_indices_classement(elt,tab):
    lst=[]
    lst2=[]
    lst3=[]
    for i in range(len(tab)):
        if tab[i] < elt:
            lst.append(i)
        elif tab[i] == elt:
            lst2.append(i)
        elif tab[i]> elt:
            lst3.append(i)
    return lst,lst2,lst3
print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
"""
"""16.2
resultats = {'Dupont': {
                        'DS1': [15.5, 4],
                        'DM1': [14.5, 1],
                        'DS2': [13, 4],
                        'PROJET1': [16, 3],
                        'DS3': [14, 4]
                    },
            'Durand': {
                        'DS1': [6 , 4],
                        'DM1': [14.5, 1],
                        'DS2': [8, 4],
                        'PROJET1': [9, 3],
                        'IE1': [7, 2],
                        'DS3': [8, 4],
                        'DS4':[15, 4]
                    }
            }
def moyenne(nom, dico_result):
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0.
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round( total_points / total_coefficients, 1 )
    else:
        return -1
print(moyenne('Durand',resultats))
"""
"""20.1 Relou
def ajoute_dictionnaires(d1, d2):
    for cle in d2:
        if cle in d1:
            d1[cle] += d2[cle]
        else:
            d1[cle] = d2[cle]
    return d1
""""""20.2
from random import randint
def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1, 6)
        case_en_cours = (case_en_cours + x) % nbre_cases
        if case_en_cours not in cases_vues:
            cases_vues.append(case_en_cours)
        n+=1
    return n
"""
"""22.1 #Dur
def liste_puissances(a,n):
    puissances = [a]
    for i in range(n-1):
        puissances.append(puissances[-1] * a)
    return puissances

def liste_puissances_borne(a, borne):
    lst = []
    val = a
    while val < borne:
        lst.append(val)
        val = val * a
    return lst
"""
"""RELOU 22.2
dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


def est_parfait(mot):
    # mot est une chaîne de caractères (en lettres majuscules)
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene % code_additionne == 0:
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait
"""
##A Fair 23
"""25.1
def enumere(L):
    d = {}
    for i in range(len(L)):
        if L[i] in d:
            d[L[i]].append(i)
        else:
            d[L[i]] = [i]
    return d
print(enumere([1, 1, 2, 3, 2, 1]))
"""
"""25.2
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste


def insere(arbre, cle):
    if arbre.v<cle:
        if arbre.fg is not None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd is not None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)
"""
"""29.1 #Dur
class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille(a):
    if a is None:
        return 0
    else:
        return 1 + taille(a.fg)+taille(a.fd)
def hauteur(a):
    if a is None:
        return 0
    else:
        return 1 + max(hauteur(a.fg, hauteur(a.fd)))
"""
"""29.2 #Dur
def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts :
        for i in range(indice):
            L[i] = liste(i)
        L[indice] = element
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = list(i-1)
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[nbre_elts]=element
    return L
"""
"""#Relou 33.1
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],'H':['','']}

def taille(arbre,lettre):
    fg=arbre[lettre][0]
    fd=arbre[lettre][1]
    if fg!='' and fd!='':
        return 1 + taille(arbre,fg)+taille(arbre,fd)
    if fg!=''and fd=='':
        return 1 + taille(arbre,fg)
    if fg=='' and fd!='':
        return 1 + taille(arbre,fd)
    else:
        return 1

print(taille(a, 'F'))
""""""#Sa marche po 33.2
def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]

liste = [41, 55, 21, 18, 12, 6, 25]
print(tri_selection(liste))
"""
"""36.1 #Facile
def couples_consecutifs(tab):
    l=[]
    for i in range(len(tab)-1):
        if tab[i]+1==tab[i+1]:
            l.append((tab[i], tab[i+1]))
    return l
print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs([1, 4, 5, 3]))
"""
"""36.2 #Facile
def propager(M, i, j, val):
    if M[i][j] == 1:
        M[i][j] = val

    # l'element en haut fait partie de la composante
    if i-1 >= 0 and M[i-1][j] == 1:
        propager(M, i-1, j, val)

    # l'element en bas fait partie de la composante
    if i+1 < len(M) and M[i+1][j] == 1:
        propager(M, i+1, j, val)

    # l'element à gauche fait partie de la composante
    if j-1>=0 and M[i][j-1] == 1:
        propager(M, i, j-1, val)

    # l'element à droite fait partie de la composante
    if j+1 < len(M) and  M[i][j+1] == 1:
        propager(M, i, j+1, val)
M = [[0, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 0], [0, 1, 1, 0]]
propager(M, 2, 1, 3)
print(M)
"""
"""38.1#Facile
def correspond(mot,mottrous):
    if len(mot)!=len(mottrous):
        return False
    for i in range(len(mot)):
        if mottrous[i]!='*' and mot[i]!=mottrous[i]:
            return False
    return True
print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
"""
"""38.2 #Facile
def est_cyclique(plan):
    '''
    Prend en paramètre un dictionnaire `plan` correspondant à un plan d'envoi de messages (ici entre les personnes A, B, C, D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et False sinon.
    '''
    expediteur = 'A'
    destinataire = plan[expediteur]
    nb_destinaires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire]
        nb_destinaires += 1

    return nb_destinaires == len(plan)
print(est_cyclique({'A':'E', 'F':'A', 'C':'D', 'E':'B', 'B':'F', 'D':'C'}))
print(est_cyclique({'A':'E', 'F':'C', 'C':'D', 'E':'B', 'B':'F', 'D':'A'}))
"""
""" 39.1 #Relou a app
def fibonacci(n):
    a = 1
    b = 1
    for k in range(n-2):
        t = b
        b = a + b
        a = t
    return b
"""
"""39.2 #facil
def pantheon(eleves, notes):
    note_maxi = 0
    meilleurs_eleves = []

    for i in range(len(notes)) :
        if notes[i] == note_maxi:
            meilleurs_eleves.append(eleves[i])
        elif notes[i] > note_maxi:
            note_maxi = notes[i]
            meilleurs_eleves = [eleves[i]]

    return (note_maxi,meilleurs_eleves)

eleves_nsi = ['a','b','c','d','e','f','g','h','i','j']
notes_nsi = [30, 40, 80, 60, 58, 80, 75, 80, 60, 24]
print(pantheon(eleves_nsi, notes_nsi))
print(pantheon([],[]))
"""
"""40.1
def nombre_de_mots(phrase):
    nb=1
    for i in range(len(phrase)-1):
        if phrase[i]==' ' and phrase[i+1] not in ['?','!']:
            nb+=1
    return nb
print(nombre_de_mots('Le point d exclamation est separe !'))
print(nombre_de_mots('Il y a un seul espace entre les mots !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))
"""
"""40.2 #Facile
class Noeud:
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur (str)'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud
        Aucun paramètre en entrée'''
        return self.valeur

    def droitExiste(self):
        '''Méthode renvoyant True si l'enfant droit existe
        Aucun paramètre en entrée'''
        return (self.droit is not None)

    def gaucheExiste(self):
        '''Méthode renvoyant True si l'enfant gauche existe
        Aucun paramètre en entrée'''
        return (self.gauche is not None)

    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de recherche
        Paramètre d'entrée : cle (int)'''
        if cle < self.valeur:
            # on insère à gauche
            if self.gaucheExiste():
                # on descend à gauche et on retente l'insertion de la clé
                Noeud.inserer(self.gauche,cle)
            else:
                # on crée un fils gauche
                self.gauche = Noeud(cle)
        elif cle > self.valeur :
            # on insère à droite
            if self.droitExiste():
                # on descend à droite et on retente l'insertion de la clé
                Noeud.inserer(self.droit,cle)
            else:
                # on crée un fils droit
                self.droit = Noeud(cle)
arbre = Noeud(7)
for cle in (3, 9, 1, 6):
        arbre.inserer(cle)
print(arbre.gauche.getValeur(),arbre.droit.getValeur(),arbre.gauche.gauche.getValeur(),arbre.gauche.droit.getValeur())
"""
"""43.1 #Facile
def ecriture_binaire_entier_positif(n):
    b=[]
    if n ==0:
        return [0]
    while n!=0:
        b.append(n%2)
        n=n//2
    b.reverse()
    return b
print(ecriture_binaire_entier_positif(105))
print(ecriture_binaire_entier_positif(2))
""""""43.2 #Facile
def tri_bulles(T):
    '''
    Renvoie le tableau T trié par ordre croissant
    '''
    n = len(T)
    for i in range(n-1,-1,-1):
        for j in range(i):
            if T[j] > T[i]:
                T[j+1],T[j]=T[j],T[j+1]
    return T
print( tri_bulles([]))
print(tri_bulles([7]))
print(tri_bulles([9, 7, 4, 3]))
print(tri_bulles([9, 3, 7, 2, 3, 1, 6]))
"""
"""44.1 #Facile
def renverse(mot):
    mott=""
    for i in range(len(mot)-1,-1,-1):
        mott+=mot[i]
    return mott
print(renverse("informatique"))
"""
"""44.2 #Moyen
def crible(n):
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(0, n):
        if tab[i] == True:
            premiers.append(i)
            for multiple in range(2*i, n, i):
                tab[multiple] = False
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
"""
"""45.1 #Relou
def rangement_valeurs(notes_eval):
    lst = [0]*11
    for note in notes_eval:
        lst[note] += 1
    return lst

def rangement_valeurs(notes_eval):
    lst = [0]*11
    for note in notes_eval:
        lst[note] += 1
    return lst

def notes_triees(effectifs_notes):
    triees = []
    for i in range(11):
        if effectifs_notes[i] != 0:
            for _ in range(effectifs_notes[i]):
                triees.append(i)
    return triees
"""
"""45.2 #Moyen
def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0:
        return str(r)
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if nb_bin == '0':
        return 0
    elif nb_bin=='1':
        return 1
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit
"""

