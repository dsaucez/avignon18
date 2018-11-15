#!/urs/bin/python2.7
# coding: utf-8

#GROUPE : BAUMEL Baptiste, RASSU Michaël, ISLAHI Chaimae, BOUZID Fares, MONETTA Quentin

import os
from math import sqrt
from binarytree import tree
from datetime import *
from scipy.interpolate import lagrange
import random 

hashh = list()
node = []
Blockchain = dict(); #Définition du dictionnaire blockchain prinçipal

g = "Je suis le premier block"
Block = "Block"
nombre = "0"


#on a décidé de faire
class Polynome:
    def __init__(self,secret,degree):
	self.var = []
	self.expo = []
        self.secret = secret
	self.degree = degree
	self.var.append(secret)
	for i in xrange(1,degree):
		a = random.randint(1,1500)
		self.var.append(a)
    
    def Disp(self):
        for i in xrange(0,len(self.var)):
            if i == 0:
                print self.var[i],
            else:
                print "+",self.var[i]," *Xexp",i,
        print
'''	
    def Display(self):
	d = self.degree
	s = self.secret
	size = len(self.var)
	exposant,mono = ' ',''
	for i, j in enumerate(self.var):
	    if j == 0:
		    continue
	    if i < 2:
		    expo = ''
	    else:
		    expo = str(i)
	    exposant += "{0: >6s}".format(expo)
	    if i == 0:
		    m = "{0:d}".format(j)
	    else:
		    m = " {0:+d}X".format(j)
	    mono += "{0: >6s}".format(m)
        print ("\n P(X) = ".join([exposant,mono]))

'''

def generer_listID(nbr):
	pays = ["FR","DZ","MA","ES","DD","AR","AO","AT","CN","DK","ET","EG"]
	dep = ["80","45","65","14","74","65","21","15","65","14","23","74"]
	list_ID = []
	for i in range(1,nbr) :
		id_u = random.randint(1,100000)
		id_H = hash(id_u)
		id_c = pays[random.randint(0,11)]+dep[random.randint(0,11)]+str(id_H)
		list_ID.append(id_c)
        return list_ID

def computeX(polynome, x):
	temp = 0
        degres  = len(polynome.var)
        print len(polynome.var)
	for i in xrange(1,degres):
            print i 
	    print pow(x,i)*polynome.var[i]
	return temp



		# on fourni le secret , le degré du polynome (le nombre de personne pour le reconstruire), l'identifiant du noeud ou stocker le secret

def prime(x):
    if x%2==0:return False
    elif any(x%i==0 for i in xrange(3,int(sqrt(x))+1,2)):return False
    else:return True
		# on fourni le secret , le degré du polynome (le nombre de personne pour le reconstruire), l'identifiant du noeud ou stocker le secret

def reconstitution(point,P):
	
        Liste = []
        Liste = recupNode(node)
        print Liste
        m = len(point)
	point_x = []
	point_y = [] 
	for i in range(0,m):
		x,y = point[i]
		point_x.append(x)
		point_y.append(y)
	p = lagrange(point_x,point_y)
	y = p(0)
	message = pow(int(y),P)
	return message

def storeSecret(secret, k, idd):
	polynome = Polynome(secret,k) # recupere la liste
        polynome.Disp()
        global node
	nombreUsers = getNumberOfUsers() #sensé retourné le nombre d'utilisateurs total du réseau
	for x in xrange(1,nombreUsers):
            print " x = ",x
            a = computeX(polynome,x)
	    prime_list=[x for x in xrange(secret,99999) if prime(x)] # p entre secret et l'infini
	    p = random.choice(prime_list)
	    node.append(pow(a,1,p)) # modulo p
  #On a maintenant notre liste de noeud pour les stocker
        shareSecret(node,nombreUsers)
        print 
        print 
        print 
        print reconstitution(recupNode(node),p)

def recupNode(liste):
    L = []
    global node
    for i in xrange(1,len(liste)):
        L.append((i,liste[i]))
    return L


def cryptByKeyRSA(key,mot): #methode qui crypt un message avec une clé donné et retourne une liste de bloc crypté
	listeBloc = []
	taille_du_mot = len(mot)
	if taille_du_mot%2!=0:
	    mot=mot+" " # vue qu'on crypte par deux on rajoute un espace pour que la longueur du message soit pair
	i = 0
	# jusqu'a la fin du mot on crypte 2 lettre par 2 lettres
	while i < taille_du_mot :
	    lettre1 = ord(mot[i])
	    lettre2 = ord(mot[i+1])
	    c = int(str(lettre1) + str(lettre2))
	    lettre_crypt = pow(c,key[0])%key[1] # on crypte le bloc
	    listeBloc.append(lettre_crypt) # on ajoute le bloc a l'indice voulu
	    i = i + 2 # on avance au deux prochaine slettres

        

def getPublicKeyByID(id):
	rsaKey = []
        rsaKey.append(71)
        rsaKey.append(179)
	return rsaKey #On suppose une méthode qui retourne la clé publique sous forme (e,n)

def sendMsgToID(msg,idd):
	for bloc in msg:
		r = requests.post('http://localhost:5000/users/'+idd, data={bloc})

def shareSecret(node,nombreUsers): #node et
	listeUsers = generer_listID(nombreUsers)
	userIndex=0
	for noeud in node: # on va envoyer une partie du secret a chaque users de notre liste
		# on recupere d'abord la clé publique du destinataire pour que personne sur le réseau puisse lire le message si il l'intercepte
		publicKeyReceiver = getPublicKeyByID(listeUsers[userIndex])
		# on doit maintenant crypter notre message a envoyé
		msg = cryptByKeyRSA(publicKeyReceiver,str(noeud)) #msg est la liste de bloc crypté pret a envoyé
		#sendMsgToID(msg,listeUsers[userIndex]) # on envoi le msg crypté au destinataire
		userIndex+=1



def getNumberOfUsers():
	return 29 #sensé retourné le nombre d'utilisateurs total du réseau

def prime(x):
	if x%2==0:
            return False
	if any(x%i==0 for i in xrange(3,int(sqrt(x))+1,2)):
            return False
	else:
	    return True

		# On choisi au hasard notre p, un nombre premier entre secret et l'infini





class Node:
	def __init__(self,data):
	    self.left = None
	    self.right = None
	    self.data = data

	def insert(self, data):
	# Compare the new value with the parent node
	    if self.data:
		if data < self.data:
		    if self.left is None:
		        self.left = Node(data)
		    else:
		        self.left.insert(data)
		elif data > data:
		    if self.right is None:
		        self.right = Node(data)
		    else:
		        self.right.insert(data)
	    else:
		self.data = data

def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.data),


print "\nPostorder traversal of binary tree is"


def AjouterBlock():
	for element in os.listdir('./data'):
		with open("./data/"+ element, "r") as line:
			for my_line in line:
				column = my_line.split(':')
				id_demandeur = column[0]
				id_chauffeur = column[1]
				p_d = column[2]
				p_a = column[3]
				distance = column[4]
				prix = column[5]

				mon_hashh = hash(id_demandeur+id_chauffeur+p_d+p_a+distance+prix)
				hashh.append(mon_hashh)

	merkletree()
        print
        print
	time = datetime.now()
	ha = hash(g)
	nonce = random.randint(1,100)
	#Blockchain["tx_route"] = hashhhh[0]
	Blockchain["time"] = time
	Blockchain["nonce"] = nonce
	Blockchain["hash_precedent"] = ha
        print hashh


def merkletree():
    inc = 0
    for element in hashh:
	    if inc == 0:
		    root = Node(element)
	    else:
		    root.insert(element)
	    inc = inc + 1
    printPostorder(root)

AjouterBlock()
print
print
print Blockchain
print
print


#def ConcaHash():

# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree

storeSecret(5,6,123)
