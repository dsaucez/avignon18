# -*- coding: utf-8 -*-
import requests
import socket
import uuid
import hashlib 

valeur_hash = dict()
chaine = uuid.uuid4()
print "la valeur de la chaine est :", chaine


#on applique la fonction de hashage sur la chaine générer aléatoirement 
valeur_hash = hash(chaine)
print ":", valeur_hash

#on converti la valeur en chaîne de caractére 
change = str(valeur_hash)

#on modifie le resultat obtenue aprés hashage en insérant un id 
id1 = raw_input("message: ")
longeur = len(change)/2
a = change[0: longeur] + id1
b = a + change[longeur: len(change)]
print "la nouvelle chaîne est :",   b #la nouvelle valeur du hashe avec l'identifiant insérer au milieu 

#-----------------------------dans cette partie on traite la géolocalisation----------------------------- 

ip = raw_input('entrez votre adresse IP:')      
def getGeoInfo(ip):
    r = requests.get('http://ip-api.com/json/'+ip)
    geoData = r.json()
    return geoData

def filterGeoData(geoData):
    lon =''
    lat =''
    ipAddress =''
    country =''
    city =''
    isp =''

    for key,value in geoData.iteritems():
        if key == 'lon':
            lon = value
        if key == 'lat':
            lat = value
        if key == 'query':
            ipAddress = value
        if key == 'country':
            country = value
        if key == 'city':
            city = value
        if key == 'isp':
            isp = value


    return lon, lat, ipAddress, country, city, isp

    
    
geoData = getGeoInfo(ip)

    
lon, lat, ipAddress, country, city, isp = filterGeoData(geoData)

    
print ' IP Address: '+str(ipAddress)+'\t Country: '+str(country)+'\t City: '+str(city)+'\t Lon: '+str(lon)+'\t Lat: '+str(lat)+'\t ISP: '+str(isp)

message_final= b +str(city)
print message_final
