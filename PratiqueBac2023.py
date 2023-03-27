# Créé par NOAM.MANFALOTI, le 06/02/2023 en Python 3.7
#1
"""
def verifie(tab):
    for i in range(len(tab)-1):
        if tab[i+1]<tab[i]:
            return False
    return True
print(verifie([8, 12, 4]))
"""
"""#1.2
urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin]=1
    return resultat

def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if election[candidat] > nmax :
            nmax = election[candidat]
            vainqueur = candidat
    liste_finale = [nom for nom in election if election[nom] == nmax]
    return liste_finale
election = depouille(urne)
print(election)
print(vainqueur(election))
"""
"""#6.1
def recherche(tab,n):
    id=len(tab)
    for i in range(len(tab)):
        if tab[i]==n:
            id=i
    return id
print(recherche([5, 3],1))
print(recherche([2,3,5,2,4],2))
"""
''''#6.2
from math import sqrt     # import de la fonction racine carrée

def distance(point1, point2):
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point,depart)
    for i in range (1, len(tab)):
        if distance(tab[i], depart)<min_dist:
            point = tab[i]
            min_dist = distance(tab[i],depart)
    return point
print(distance((1, 0), (5, 3)))
print(distance((1, 0), (0, 1)))
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))
'''
"""10
def maxliste(tab):
    max=0
    for i in tab:
        if i>max:
            max=i
    return max
print(maxliste([98, 12, 104, 23, 131, 9]))
"""
'''
class Pile:
    """ Classe définissant une pile """
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        """Renvoie True si la pile est vide, False sinon"""
        return self.valeurs == []

    def empiler(self, c):
        """Place l’élément c au sommet de la pile"""
        self.valeurs.append(c)

    def depiler(self):
        """Supprime l’élément placé au sommet de la pile, à condition qu’elle soit non vide"""
        if self.est_vide() == False:
            self.valeurs.pop()

def parenthesage(ch):
    """Renvoie True si la chaîne ch est bien parenthésée et False sinon"""
    p = Pile()
    for c in ch:
        if c == '(':
            p.empiler(c)
        elif c == ')':
            if p.est_vide():
                return False²
            else:
                p.depiler()
    return p.est_vide()
'''
"""13
def recherche(n,tab):
    occu=0
    for i in range(len(tab)):
        if tab[i]==n:
            occu+=1
    return occu
print(recherche(5, [-2, 3, 1, 5, 3, 7, 4]))
print(recherche(5, [-2, 5, 3, 5, 4, 5]))
"""
"""
def rendu_monnaie(somme_due, somme_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = []
    a_rendre = somme_versee-somme_due
    i = len(pieces) - 1
    while a_rendre > 0 :
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i])
            a_rendre -=pieces[i]
        else :
            i-=1
    return rendu
print(rendu_monnaie(102,500))
"""
"""15
t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

def mini(releve, date):
    temp_mini = releve[0]
    date_mini = date[0]
    for i in range(len(releve)):
        if releve[i] < temp_mini:
            temp_mini = releve[i]
            date_mini = date[i]
    return temp_mini, date_mini
"""
"""
def inverse_chaine(chaine):
    result = ''
    for caractere in chaine:
        result = caractere + result
    return result

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return chaine == inverse

def est_nbre_palindrome(nbre):
    chaine = str(nbre)
    return est_palindrome(chaine)

print(est_nbre_palindrome(213312))
print(est_palindrome('ISN-NSI'))
"""
"""19
def recherche(tab, n):
    ind_debut = 0
    ind_fin = len(tab) - 1
    while ind_debut <= ind_fin:
        ind_milieu = (ind_debut + ind_fin) // 2
        if tab[ind_milieu] == n:
            return ind_milieu
        elif tab[ind_milieu] < n:
            ind_debut = ind_milieu + 1
        else:
            ind_fin = ind_milieu - 1
    return -1
"""
"""
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def position_alphabet(lettre):
    return ord(lettre) - ord('A')

def cesar(message, decalage):
    resultat = ''
    for c in message:
        if 'A' <= c and c <= 'Z':
            indice = ( position_alphabet(c)+ decalage ) % 26
            resultat = resultat + ALPHABET[indice]
        else:
            resultat = resultat+c
    return resultat
print(cesar('BONJOUR A TOUS. VIVE LA MATIERE NSI !', 4))
"""
"""26
def multiplication(n1, n2):
    positif=1
    nb=0
    if n1<0 and n2>0:
        n1=-n1
        positif=0
    if n1>0 and n2<0:
        n2=-n2
        positif=0
    if n1<0 and n2<0:
        n1=-n1
        n2=-n2
        positif=0
    for i in range(n2):
        nb+=n1
    if positif==1:
        return nb
    else:
        return -nb

print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))
"""
'''
def dichotomie(tab, x):
    """
    tab : tableau d’entiers trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
'''
"""27
def recherchemin(tab):
    min=tab[0]
    ind=0
    for i in range(len(tab)):
        if tab[i]<min:
            ind=i
    return ind
print(recherchemin([2, 4, 1]))
"""
"""
def separe(tab):
    gauche = 0
    droite = len(tab)-1
    while gauche < droite :
        if tab[gauche] == 0 :
            gauche +=1
        else :
            tab[gauche], tab[droite] = tab[droite],tab[gauche]
            droite -=1
    return tab
print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
"""
"""28
def moyenne (tab):
    '''
    moyenne(list) -> float
    Entrée : un tableau non vide d'entiers
    Sortie : nombre de type float
    Correspondant à la moyenne des valeurs présentes dans le
    tableau
    '''
    somme=0
    for i in tab:
        somme+=i
    return somme/len(tab)

assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5
"""
'''
def dichotomie(tab, x):
    """
    tab : tableau trié dans l’ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    # cas du tableau vide
    if tab==[]:
        return False, 1

    # cas où x n'est pas compris entre les valeurs extrêmes
    if (x < tab[0]) or (x>tab[len(tab)-1]):
        return False, 2

    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut+fin)//2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m-1
    return False,3
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],28))
print(dichotomie([15, 16, 18, 19, 23, 24, 28, 29, 31, 33],27))
'''
"""30
def moyenne(tab):
    somme=0
    for i in tab:
        somme+=i
    return somme/len(tab)
print(moyenne([1.0, 2.0, 4.0]))
"""
"""
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a!=0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a
print(binaire(83))
"""
"""31
def nb_repetitions(elt,tab):
    tot=0
    for i in tab:
        if i==elt:
            tot+=1
    return tot
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
""""""
def binaire(a):
    bin_a = str(a%2)
    a = a // 2
    while a!=0 :
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a
print(binaire(83))
"""
"""34
def moyenne(tab):
    somme=0
    if tab==[]:
        return "Votre Tableau est aussi vide que votre cerveau :D"
    for i in tab:
        somme+=i
    return somme/len(tab)
print(moyenne([1.0, 2.0, 4.0]))
print(moyenne([]))
"""
"""
def tri(tab):
    # i est le premier indice de la zone non triée,
    # j est le dernier indice de cette zone non triée.
    # Au début, la zone non triée est le tableau complet.
    i = 0
    j = len(tab)-1
    while i != j:
        if tab[i]== 0:
            i += 1
        else:
            valeur = tab[j]
            tab[j]= tab[i]
            tab[i]=valeur
            j-=1
    return tab
"""
"""41
def recherche(caractere, chaine):
    tot=0
    for i in chaine:
        if i==caractere:
            tot+=1
    return tot
print(recherche('i',"mississippi"))
"""
"""
valeurs = [100, 50, 20, 10, 5, 2, 1]
def rendu_glouton(a_rendre, rang):
    if a_rendre == 0:
        return []
    v = valeurs[rang]
    if v <= a_rendre :
        return [v] + rendu_glouton(a_rendre - v, rang)
    else :
        return rendu_glouton(a_rendre,rang+1)
"""
"""2.0
def indices_maxi(tab):
    val_max = tab[0]
    ind_max = []
    for i in range(len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
    for i in range(len(tab)):
        if tab[i] == val_max:
            ind_max.append(i)
    return (val_max, ind_max)
print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
"""
"""2.1
def positif(pile):
    pile_1 = list(pile)
    pile_2 = []
    while pile_1 != []:
        x = pile_1.pop()
        if x >= 0:
            pile_2.append(x)
    while pile_2 != []:
        x = pile_2.pop()
        pile_1.append(x)
    return pile_1
print(positif([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
"""
"""
def max_dico(dico):
    valmax=0
    clemax=''
    for i in dico:
        if dico[i]>valmax:
            valmax=dico[i]
            clemax=i
    return clemax,valmax
print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
"""
'''
class Pile:
    """Classe définissant une structure de pile."""
    def __init__(self):
        self.contenu = []

    def est_vide(self):
        """Renvoie le booléen True si la pile est vide, False sinon."""
        return self.contenu == []

    def empiler(self, v):
        """Place l'élément v au sommet de la pile"""
        self.contenu.append(v)

    def depiler(self):
        """
        Retire et renvoie l’élément placé au sommet de la pile,
        si la pile n’est pas vide.
        """
        if not self.est_vide():
            return self.contenu.pop()


def eval_expression(tab):
    p = Pile()
    for element in tab:
        if element != '+' and element != '*':
            p.empiler(element)
        else:
            if element == '+':
                resultat = p.depiler() + p.depiler()
            else:
                resultat = p.depiler() * p.depiler()
            p.empiler(resultat)
    return resultat
print(eval_expression([2, 3, '+', 5, '*']))
'''
"""9.1
def multiplication(n1, n2):
    positif=1
    nb=0
    if n1<0 and n2>0:
        n1=-n1
        positif=0
    if n1>0 and n2<0:
        n2=-n2
        positif=0
    if n1<0 and n2<0:
        n1=-n1
        n2=-n2
    for i in range(n2):
        nb+=n1
    if positif==1:
        return nb
    else:
        return -nb
print(multiplication(-4,-8))
"""
"""
def chercher(tab, n, i, j):
    if i < 0 or j > len(tab) :
        return None
    if i > j :
        return None
    m = (i + j) // 2
    if m < n :
        return chercher(tab, n, m+1 , j)
    elif m > n :
        return chercher(tab, n, i , m-1 )
    else :
        return 0
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
"""
"""14
def recherche(elt,tab):
    for i in range(len(tab)):
        if tab[i] == elt:
            return i
    return -1
print(recherche(1,[10,12,1,56]))
"""
"""
def insere(a, tab):
    l = list(tab) #l contient les mêmes éléments que tab
    l.append(a)
    i = len(l) - 2
    while a < l[i] and i >= 0:
        l[i+1] = l[i]
        l[i] = a
        i = i - 1
    return l
print(insere(3, [1, 2, 4, 5]))
"""
"""17
def moyenne(list_notes):
    sommecoef=0
    somme=0
    for i in list_notes:
        notes=i[0]
        coef=i[1]
        somme+=notes*coef
        sommecoef=sommecoef+coef
    return somme/sommecoef
print(moyenne([(15,2),(9,1),(12,3)]))
"""
"""##A apprendre
def pascal(n):
    triangle = [[1]]
    for k in range(1,n+1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(1)
        triangle.append(ligne_k)
    return triangle
print(pascal(4))
"""
"""18
def max_et_indice(tab):
    max=tab[0]
    for i in range(len(tab)):
        if tab[i]>max:
            max=tab[i]
            maxi=i
    return max,maxi
print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
"""
"""#Dur
def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les entiers
    de 1 à n, False sinon
    '''
    for i in range(1,len(tab)+1):
        if i not in tab:
            return False
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente un ordre
    de gènes de chromosome
    '''
    assert est_un_ordre(ordre) # ordre n'est pas un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n-1:
        if ordre[i+1]-ordre[i] not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[n-1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb
print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))
"""
"""21
def delta(liste):
    l=[liste[0]]
    for i in range(1,len(liste)):
        l.append(liste[i]-liste[i-1])
    return l
print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))
"""
"""#Dur
class Noeud:
    '''
    classe implémentant un noeud d'arbre binaire
    '''

    def __init__(self, g, v, d):
        '''
        un objet Noeud possède 3 attributs :
        - gauche : le sous-arbre gauche,
        - valeur : la valeur de l'étiquette,
        - droit : le sous-arbre droit.
        '''
        self.gauche = g
        self.valeur = v
        self.droit = d

    def __str__(self):
        '''
        renvoie la représentation du noeud en chaine de caractères
        '''
        return str(self.valeur)

    def est_une_feuille(self):
        '''
        renvoie True si et seulement si le noeud est une feuille
        '''
        return self.gauche is None and self.droit is None

def expression_infixe(e):
    s = ''
    if e.gauche is not None:
        s = '(' + s + expression_infixe(e.gauche)
    s = s + str(e.valeur)
    if e.droit is not None:
        s = s + expression_infixe(e.droit) + ')'
    return s
e = Noeud(Noeud(Noeud(None, 3, None), '*', Noeud(Noeud(None, 8, None),
'+', Noeud(None, 7, None))), '-', Noeud(Noeud(None, 2, None), '+',
Noeud(None, 1, None)))
print(expression_infixe(e))
"""
"""24
def nbr_occurrences(chaine):
    occ={}
    for cara in chaine:
        if cara in occ:
            occ[cara]+=1
        else:
            occ[cara] = 1
    return occ
print(nbr_occurrences("Hello world !"))
"""
"""Dur
def fusion(lst1,lst2):
    n1 = len(lst1)
    n2 = len(lst2)
    lst12 = [0] * (n1 + n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1 < n1 and i2<n2 :
        if lst1[i1] < lst2[i2]:
            lst12[i] = lst1[i1]
            i1 = i1+1
        else:
            lst12[i] = lst2[i2]
            i2 = i2+1
        i += 1
    while i1 < n1:
        lst12[i] = lst1[i1]
        i1 = i1 + 1
        i = i+1
    while i2 < n2:
        lst12[i] = lst2[i2]
        i2 = i2 + 1
        i = i+1
    return lst12
print(fusion([1, 6, 10],[0, 7, 8, 9]))
"""
"""32"""
def min_et_max(tab):
    dic={}
    max,min=tab[0],tab[0]
    for i in tab:
        if i>max:
            max=i
        if i<min:
            min=i
    dic['min']=min
    dic['max']=max
    return dic
print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
""""""
'''Dur
class Carte:
    def __init__(self, c, v):
        """ Initialise les attributs couleur (entre 1 et 4), et valeur (entre 1 et 13). """
        self.couleur = c
        self.valeur = v

    def get_valeur(self):
        """ Renvoie la valeur de la carte : As, 2, ..., 10, Valet, Dame, Roi """
        valeurs = ['As','2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi']
        return valeurs[self.valeur - 1]

    def get_couleur(self):
        """ Renvoie la couleur de la carte (parmi pique, coeur, carreau, trèfle). """
        couleurs = ['pique', 'coeur', 'carreau', 'trèfle']
        return couleurs[self.couleur - 1]

class Paquet_de_cartes:
    def __init__(self):
        """ Initialise l'attribut contenu avec une liste des 52 objets Carte possibles
            rangés par valeurs croissantes en commençant par pique, puis coeur,
            carreau et tréfle. """
        self.contenu = [Carte(c, v) for c in range(1, 5) for v in range(1, 14)]

    def get_carte(self, pos):
        """ Renvoie la carte qui se trouve à la position pos (entier compris entre 0 et 51). """
        assert 0 <= pos <= 51,  'paramètre pos invalide'
        return self.contenu[pos]
'''
"""35
def ou_exclusif(tab1, tab2):
    resultat = []
    taille = len(tab1)
    for i in range(taille):
        resultat.append(tab1[i] ^ tab2[i])
    return resultat
a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
print(ou_exclusif(a, b))
""""""
class Carre:
    def __init__(self, liste, n):
        self.ordre = n
        self.tableau = [[liste[i + j * n] for i in range(n)] for j in range(n)]

    def affiche(self):
        '''Affiche un carré'''
        for i in range(self.ordre):
            print(self.tableau[i])

    def somme_ligne(self, i):
        '''Calcule la somme des valeurs de la ligne i'''
        somme = 0
        for j in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def somme_col(self, j):
        '''Calcule la somme des valeurs de la colonne j'''
        somme = 0
        for i in range(self.ordre):
            somme = somme + self.tableau[i][j]
        return somme

    def est_semimagique(self):
        s = self.somme_ligne(0)

        #test de la somme de chaque ligne
        for i in range(self.ordre):
            if self.somme_ligne(i) != s:
                return False

        #test de la somme de chaque colonne
        for j in range(self.ordre):
            if self.somme_col(j) != s:
                return False

        return True

""""""37
def recherche(elt,tab):
    for i in range(len(tab)-1,-1,-1):
        if tab[i] == elt:
            return i
    return -1
print(recherche(1, [2, 3, 4]),recherche(1, [10, 12, 1, 56]),recherche(1, [1, 0, 42, 7]),recherche(1, [1, 50, 1]))
"""
'''Dur
class AdresseIP:
    def __init__(self, adresse):
        self.adresse = adresse

    def liste_octet(self):
        """renvoie une liste de nombres entiers,
        la liste des octets de l'adresse IP"""
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """renvoie True si l'adresse IP est une adresse
        réservée, False sinon"""
        return self.liste_octet()[3] == 0 or self.liste_octet()[3] == 255

    def adresse_suivante(self):
        """renvoie un objet de AdresseIP avec l'adresse
        IP qui suit l’adresse self
        si elle existe et False sinon"""
        if self.liste_octet()[3] < 254:
            octet_nouveau = self.liste_octet()[3] + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False

adresse1 = AdresseIP('192.168.0.1')
adresse2 = AdresseIP('192.168.0.2')
adresse3 = AdresseIP('192.168.0.0')
'''
"""
def tri_selection(tab):
    for i in range(len(tab)-1):
        indice_min = i
        for j in range(i+1, len(tab)):
            if tab[j] < tab[indice_min]:
                indice_min = j
        tab[i], tab[indice_min] = tab[indice_min], tab[i]
    return tab
print(tri_selection([1, 52, 6, -9, 12]))
""""""
from random import randint

def plus_ou_moins():
    nb_mystere = randint(1,99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 0

    while nb_mystere != nb_test and compteur < 11 :
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print ("Bravo ! Le nombre était ",nb_mystere)
        print("Nombre d'essais: ",compteur)
    else:
        print ("Perdu ! Le nombre était ",nb_mystere)

plus_ou_moins()
""""""
def moyenne(tab):
    somme = 0
    coeffs = 0
    for couple in tab:
        somme += couple[0] * couple[1]
        coeffs += couple[1]
    if coeffs == 0:
        return None
    return somme / coeffs
print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
"""


































































































