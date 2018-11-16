# Base de donnée contenant l'historique des sequences de demandes de
# mise à jour de rank.
# { id: [(src, rank), ...], ...}
# Example: {1:[(10,4), (10,4), (42, 1), (69, 1), (96, 1), (10,4), (10,4), (10,4), (10,4)]}
# où le noeud d'ID = 1 a reçu d'abord 4* de 10, puis de nouveau 4 de 10, puis 1 de 42, etc.
db = dict()

#def compute_rank(src, dst, rank, db):
#"""
#src: identifiant de celui qui veut donner le rank
#dst: identifiant de celui qui voit sont rank mis à jour
#rank: proposition de rank

#return valeur du rank sur base de la nouvelle proposition et de l'historique.
#"""
dstList=[]
rankList = list()
print(rankList)

sum1=0

def compute_rank(src, dst, rank, db):
	rank1 = [src,rank]
	dst1 = dst
	rankList.append(rank1)
	db.update({dst1:rankList})
	print("db dst",db[dst1])
	return db
q="foo"
while q != 'q' and q != 'Q':

	src = input("ID_Client: ")
	dst = input("ID_Chauffeur: ")

	rank = input("Note: ")
	src=int(src)
	dst=int(dst)
	rank=(rank)
	
	compute_rank(src, dst, rank, db)

	q = input('q? ')



print(db[dst])
print("Contenu db ", db)

i=0
rnk=[]
pretend_votes=[2,2,2,2,2,2]
item_votes=[]
votes=[]
utilities=[-5,1,2,3,4,5]

while i < len(db[dst]):
	print("\n db",db[dst][i][1])
	rnk.append(int(db[dst][i][1]))
	i=i+1
print("Rank = ",rnk)
item_votes.append(rnk.count(0))
item_votes.append(rnk.count(1))
item_votes.append(rnk.count(2))
item_votes.append(rnk.count(3))
item_votes.append(rnk.count(4))
item_votes.append(rnk.count(5))

print("item_votes = ",item_votes)
i = 0
while i < 6:
	temp=item_votes[i] + pretend_votes[i]
	votes.append(temp)
	i=i+1
print("votes = ",votes)
i=0
while i < 6:
	sum1 = sum1 + (utilities[i] * votes[i])
	sum2 = sum(votes)
	i=i+1
score=round(sum1 / sum2,1)
print("score = ",score)
