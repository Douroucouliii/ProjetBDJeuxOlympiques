from bs4 import BeautifulSoup as bs
import urllib.request

#SPORTS ET EPREUVES
url_sports  = 'https://www.paris2024.org/fr/sports-les-sports-olympiques/'
page_sports=urllib.request.urlopen(url_sports,timeout=5)
soup_sports=bs(page_sports,"html.parser")
sport = soup_sports.find_all('a',{'rel':'noreferrer noopener'})
#NOM DES SPORTS
sports = []
url_epreuves=[]
sports_epreuves={}
nom_epreuves=[]
for s in sport:
    url_epreuves.append(s.get("href"))
    s = s.text
    s=s.replace('\n','')
    sports.append(s)
del sports[0]
del url_epreuves[0]
sports.pop(-1)
url_epreuves.pop(-1)
sports_epreuves = dict(zip(sports, [None]*len(sports)))
i=0
for e in url_epreuves:
    tmp=[]
    ep=bs(urllib.request.urlopen(e,timeout=5),"html.parser").find_all('ul')[4]
    for p in ep:
        p = p.text
        p = p.replace('\n','')
        p = p.replace("\u202f", "")
        p = p.replace("\xa0", "")
        p = p.replace("(femmes/hommes)","")
        if p == "Double":
            p += str(i)
        if p == 'Simple ':
            p += str(i)
        if p == "Double (femmes/hommes/mixte)":
            p += str(i)
        tmp.append(p)
    sports_epreuves[sports[i]]=tmp
    i+=1
sports_epreuves["boxe"]=["tournoi de boxe"]
#ATHLETES
athletes = [
             ["Yuto","HORIGOME","Japon","skateboard",1999,0,0,1],
             ["Rayssa","LEAL","Brésil","skateboard",2008,0,1,0],
             ["Katie","LEDECKY","États-Unis","natation artistique",1997,0,3,7],
             ["Kristof","MILAK","Hongrie","natation artistique",2000,0,1,1],
             ["Kaylee","MCKEOWN","Australie","natation artistique",2001,1,0,3],
             ["Caeleb","DRESSEL","États-Unis","natation artistique",1996,0,0,7],
             ["Flora","DUFFY","Bermudes","triathlon",1987,0,0,1],
             ["Neeraj","CHOPRA","Inde","Athlétisme",1997,0,0,1],
             ["Armand","DUPLANTIS","Suède","Athlétisme",1999,0,0,1],
             ["Shelly-Ann","FRASER-PRYCE","Jamaïque","Athlétisme",1986,1,4,3],
             ["Yaroslava","MAHUCHIKH","Ukraine","Athlétisme",2001,1,0,0],
             ["Winfred","MUTILE YAVI","Bahreïn","Athlétisme",1999,0,0,0],
             ["Yulimar","ROJAS","Venezuela","Athlétisme",1995,0,1,1],
             ["Carlos","E.YULO","Philippines","gymnastique artistique",2000,0,0,0],
             ["Pusarla Venkata","SINDHU","Inde","badminton",1995,1,1,0],
             ["Alaa","MASO","Équipe Olympique des Réfugiés du CIO","natation artistique",2000,0,0,0],
             ["Serena","WILLIAMS","États-Unis","tennis",1981,0,0,4],
             ["Elin","RUBENSSON","Suède","football",1993,0,1,0],
             ["Carissa","MOORE","États-Unis","surf",1992,0,0,1],
             ["Filipe","TOLEDO","Brésil","surf",1995,0,0,0],
             ["Tomoa","NARASAKI","Japon","escalade sportive",1996,0,0,0],
             ["Tadej","POGACAR","Slovénie","cyclisme sur route",1998,1,0,0],
             ["Eliud","KIPCHOGE","Kenya","Athlétisme",1984,1,1,2],
             ["Alberto","GINES LOPEZ","Espagne","escalade sportive",2002,0,0,1]
           ]

#PAYS
lpays = []
for a in athletes:
    if a[2] not in lpays:
        lpays.append(a[2])

#TRANSPORT
transport=["Métro,RER,Tramway,Autobus,Vélib,Taxi,VTC"]

#SITES
sites = [
    ["Arena Porte de la Chapelle", 6700, "58 boulevard Ney, 18e arrondissement, Paris"],
    ["Grand Palais", 8000, "3 Av. du Général Eisenhower, Paris"],
    ["La Concorde", 30000, "Pl. de la Concorde, Paris"],
    ["Hôtel de Ville", 0 ,"Pl. de l Hôtel de Ville, Paris"],
    ["Pont Alexandre III", 1000, "Pont Alexandre III, Paris"],
    ["Pont d’Iéna", 3349, "Pont d Iéna, Paris"],
    ["Stade Tour Eiffel", 12860, "Champ de Mars, 5 Av. Anatole France, Paris"],
    ["Invalides", 8000, "129 Rue de Grenelle, Paris"],
    ["Arena Champ de Mars", 8356, "2 All. Adrienne Lecouvreur, Paris"],
    ["Stade Roland-Garros", 14962, "2 Av. Gordon Bennett, Paris"],
    ["Parc des Princes", 47926, "24 Rue du Commandant Guilbaud, Paris"],
    ["Arena Bercy", 15000, "8 Bd de Bercy, Paris"],
    ["Arena Paris Sud 1", 12000, "15 arrondissement, Paris"],
    ["Arena Paris Sud 4", 6650, "15 arrondissement, Paris"],
    ["Arena Paris Sud 6", 7500, "15 arrondissement, Paris"],
    ["Stade Yves-du-Manoir", 15000, "12 Rue François Faber, Colombes"],
    ["Arena Paris Nord", 6000, "Villepinte, Seine-Saint-Denis"],
    ["Site d’escalade du Bourget", 6000, "Le Bourget"],
    ["Centre Aquatique", 5000, "Saint-Denis, Seine-Saint-Denis"],
    ["Paris La Défense Arena", 17000, "99 Jard. de l Arche, Nanterre"],
    ["Stade nautique de Vaires-sur-Marne", 24000, "Rte de Torcy, Vaires-sur-Marne"],
    ["Château de Versailles", 40000, "Place d Armes, Versailles"],
    ["Stade BMX de Saint-Quentin-en-Yvelines", 3000, "Montigny-le-Bretonneux"],
    ["Vélodrome National de Saint-Quentin-en-Yvelines", 5000, "1 Rue Laurent Fignon, 78180 Montigny-le-Bretonneux"],
    ["Golf National", 32720, "2 Av. du Golf, Guyancourt"],
    ["Colline d’Elancourt", 15000, "Saint-Quentin-en-Yvelines, Yvelines"],
    ["Stade Pierre Mauroy", 27000, "261 Bd de Tournai, Villeneuve-d Ascq"],
    ["Stade de la Beaujoire", 37473, "Route de Saint-Joseph, 44300 Nantes"],
    ["Centre National de Tir de Châteauroux", 0 ,"Route de Lignières, D925, 36130 Déols"],
    ["Stade de Lyon", 59186, "10 Av. Simone Veil, Décines-Charpieu"],
    ["Stade Geoffroy-Guichard", 41965,"14 Rue Paul et Pierre Guichard, Saint-Étienne"],
    ["Stade de Bordeaux", 42000, "Cr Jules Ladoumegue, Bordeaux"],
    ["Stade de Nice", 36178, "Bd des Jardiniers, Nice"],
    ["Stade de Marseille", 67394, "3 Bd Michelet, Marseille"],
    ["Marina de Marseille", 12262, "Marseille"],
    ["Tahiti Teahupoo", 600, "Tahiti"]
]

#DATES
dates =[
    #Date Epreuve
    [1,"2024-08-01"],
    [2,"2024-08-01"],
    [3,"2024-08-01"],
    [4,"2024-08-01"],
    [5,"2024-08-01"],
    [6,"2024-08-01"],
    [7,"2024-08-01"],
    [8,"2024-08-01"],
    [9,"2024-08-01"],
    [10,"2024-08-01"],
    [11,"2024-08-01"],
    [12,"2024-08-01"],
    [13,"2024-08-01"],
    [14,"2024-08-01"],
    [15,"2024-08-01"],
    [16,"2024-08-01"],
    [17,"2024-08-01"],
    [18,"2024-08-01"],
    [19,"2024-08-01"],
    [20,"2024-08-01"],
    [21,"2024-08-01"],
    [22,"2024-08-01"],
    [23,"2024-08-01"],
    [24,"2024-08-01"],
    [25,"2024-08-01"],
    [26,"2024-08-01"],
    [27,"2024-07-27"],
    [28,"2024-07-27"],
    [29,"2024-07-27"],
    [30,"2024-07-27"],
    [31,"2024-07-27"],
    [32,"2024-07-27"],
    [33,"2024-07-27"],
    [34,"2024-07-27"],
    [35,"2024-07-27"],
    
    [36,"2024-07-27"],
    
    
    [37,"2024-07-30"],
    
    [38,"2024-07-27"],
    
    
    [39,"2024-08-05"],
    [40,"2024-08-05"],
    [41,"2024-08-05"],
    [42,"2024-08-05"],
    [43,"2024-08-05"],
    [44,"2024-08-05"],
    
    [45,"2024-07-27"],
    [46,"2024-07-27"],
    
    [47,"2024-07-30"],
    
    [48,"2024-08-01"],
    
    [49,"2024-07-28"],
    
    [50,"2024-07-27"],
    [51,"2024-07-27"],
    [52,"2024-07-27"],
    [53,"2024-07-27"],
    [54,"2024-07-27"],
    [55,"2024-07-27"],
    
    [56,"2024-07-24"],
    
    [57,"2024-07-27"],
    [58,"2024-07-27"],
    [59,"2024-07-27"],
    [60,"2024-07-27"],
    [61,"2024-07-27"],
    [62,"2024-07-27"],
    
    [63,"2024-08-08"],
    [64,"2024-08-08"],
    
    [65,"2024-08-02"],
    
    [66,"2024-08-07"],
    [67,"2024-08-07"],
    [68,"2024-08-07"],
    [69,"2024-08-07"],
    [70,"2024-08-07"],
    [71,"2024-08-07"],
    
    [72,"2024-07-25"],
    
    [73,"2024-07-27"],
    
    [74,"2024-07-27"],
    [75,"2024-07-27"],
    [76,"2024-07-27"],
    
    [77,"2024-08-05"],
    [78,"2024-08-05"],
    [79,"2024-08-05"],
    [80,"2024-08-05"],
    [81,"2024-08-05"],
    [82,"2024-08-05"],
    
    [83,"2024-08-08"],
    [84,"2024-08-08"],
    [85,"2024-08-08"],
    [86,"2024-08-08"],
    
    [87,"2024-07-24"],
    
    [88,"2024-08-05"],
    [89,"2024-08-05"],
    [90,"2024-08-05"],
    [91,"2024-08-05"],
    [92,"2024-08-05"],
    
    [93,"2024-07-27"],
    [94,"2024-07-27"],
    [95,"2024-07-27"],
    [96,"2024-07-27"],
    
    [97,"2024-07-27"],
    
    [98,"2024-08-07"],
    [99,"2024-08-07"],
    [100,"2024-08-07"],
    [101,"2024-08-07"],
    [102,"2024-08-07"],
    [103,"2024-08-07"],
    [104,"2024-08-07"],
    [105,"2024-08-07"],
    
    [106,"2024-07-27"],
    
    [107,"2024-07-27"],
    [108,"2024-07-27"],
    [109,"2024-07-27"],
    
    [110,"2024-07-27"],
    [111,"2024-07-27"],
    [112,"2024-07-27"],
    [113,"2024-07-27"],
    [114,"2024-07-27"],
    [115,"2024-07-27"],
    
    [116,"2024-07-30"],
    [117,"2024-07-30"],
    
    [118,"2024-07-28"],
    [119,"2024-07-28"],
    [120,"2024-07-28"],
    
    [121,"2024-07-27"],
    
    [122,"2024-08-09"],
    [123,"2024-08-09"],
    
    [124,"2024-08-05"],
    [125,"2024-08-05"],
    
    
    [126,"2024-07-27"],
    [127,"2024-07-27"],
    #Date création sites
    [128,"2023-02-01"],
    [129,"1897-01-01"],
    [130,"1757-01-01"],
    [131,"1357-01-01"],
    [132,"1896-01-01"],
    [133,"1814-01-01"],
    [134,"1887-01-01"],
    [135,"1671-01-01"],
    [136,"2021-01-01"],
    [137,"1927-01-01"],
    [138,"1967-07-08"],
    [139,"1981-03-30"],
    [140,"1923-01-01"],
    [141,"1923-01-01"],
    [142,"1923-01-01"],
    [143,"1928-01-01"],
    [144,"2020-01-01"],
    [145,"2024-01-01"],
    [146,"1967-01-01"],
    [147,"2013-01-01"],
    [148,"2019-01-01"],
    [149,"1634-01-01"],
    [150,"2011-10-03"],
    [151,"2014-01-01"],
    [152,"1990-10-05"],
    [153,"1970-01-01"],
    [154,"2010-09-27"],
    [155,"1984-01-01"],
    [156,"2012-01-01"],
    [157,"2012-01-01"],
    [158,"1931-01-01"],
    [159,"2012-01-01"],
    [160,"2011-08-06"],
    [161,"1935-04-28"],
    [162,"2024-01-01"],
    [163,"1997-01-01"]
    ]

#Integration dans le fichier sql
string_pays=""
for p in lpays :
    string_pays+="('"+p+"'),"+"\n"
string_pays=string_pays[:-2]
string_pays+=";"

string_dates=""
k=0
for d in dates:
    string_dates+='('+str(dates[k][0])+",'"+dates[k][1]+"'),"+"\n"
    k+=1
string_dates=string_dates[:-2]
string_dates+=";"

string_sites=""
j=0
for i in sites:
    string_sites+="('"+i[0]+"',"+str(i[1])+",'"+i[2]+"',"+str(dates[127+j][0])+",'"+transport[0]+"'),"+"\n"
    j+=1
string_sites=string_sites[:-2]
string_sites+=";"

string_transport=""
for i in transport:
    string_transport+="('"+i+"'),"+"\n"
string_transport=string_transport[:-2]
string_transport+=";"

string_athletes=""
for i in athletes:
    string_athletes+="('"+i[0]+"','"+i[1]+"',"+str(i[4])+","+str(+i[5])+','+str(i[6])+','+str(i[7])+",'"+i[2]+"','"+i[3]+"'),"+"\n"
string_athletes=string_athletes[:-2]
string_athletes+=";"

string_sport=""
for s in sports:
    string_sport+="('"+s+"'),"+"\n"
string_sport=string_sport[:-2]
string_sport+=";" 


string_epreuve=""
date=1
for s in sports_epreuves:
    for e in sports_epreuves[s]:
            string_epreuve+="('"+e+"','"+s+"',"+str(date)+"),"+"\n"
            date+=1
string_epreuve=string_epreuve[:-2]
string_epreuve+=";"                

fichier = open("base.sql", "a", encoding="utf-8")   
fichier.write(
    "\nINSERT INTO Pays VALUES\n"+string_pays+"\n"+"\nINSERT INTO Dates(ID_Date,Jour) VALUES\n"+string_dates+"\n"+"\nINSERT INTO Sites(Nom_Sites,Capacite_Spectateur_Sites,Adresse_Sites,ID_Date,Nom_Transport) VALUES\n"+string_sites+"\n\nINSERT INTO Transport_en_commun VALUES\n"+string_transport+"\n"+"\nINSERT INTO Participants(Prenom_Participants,Nom_Participants,Date_Naissance_Participants,Nb_Medaille_Bronze_Participants,Nb_Medaille_Argent_Participants,Nb_Medaille_Or_Participants,Nom_Pays,Nom_Epreuve) VALUES \n"+string_athletes+"\n"+"\nINSERT INTO Sport VALUES\n"+string_sport+"\n\nINSERT INTO Epreuve(Nom_Epreuve,Nom_Sport,ID_Date) VALUES\n"+string_epreuve
    )
fichier.close()


               
