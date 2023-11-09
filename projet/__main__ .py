import tkinter as tk
from tkinter import ttk
import sqlite3

class Interface:
    
    def __init__(self):

        self.__choix_table = "Pays"
        
        '''Création de la fenêtre'''

        self.__fen = tk.Tk()
        self.__fen.title("Visualisation de la base de donnée")
        self.__fen.geometry("1920x1080")
        
        '''Affichage des labels et des combobox'''
        
        self.__label_choix = tk.Label(self.__fen, text = "Quelles données voulez vous afficher ?")
        self.__label_choix.pack()
        
        self.__label_tables = tk.Label(self.__fen, text = "Nom de la table :")
        self.__label_tables.pack()

        #La liste des table et des attribut de notre base de données SQL
        self.__liste_tables=["Pays", "Participants","Epreuve","Transport_en_commun","Sport","Sites","Dates"]
        self.__attribut_Pays=["Nom"]
        self.__attribut_Participants=["Prénom","Nom","Naissance","Nb médailles bronze","Nb médailles argent","Nb médailles or","Pays","Nom_Sport"]
        self.__attribut_Epreuve=["Nom","ID_Date","Nom_Sport"]
        self.__attribut_Transport_en_commun=["Nom"]
        self.__attribut_Sport=["Nom"]
        self.__attribut_Sites=["Nom","Capacité","Adresse","ID_Date","Nom_Transport"]
        self.__attribut_Dates=["ID_Date","Jour"]

        #Combobox des tables
        self.__liste_combo_tables = ttk.Combobox(self.__fen, values=self.__liste_tables)
        self.__liste_combo_tables.bind("<<ComboboxSelected>>", self.get_choix)
        self.__liste_combo_tables.pack()

        
        '''Bouton pour terminer le programme'''

        self.__bouton_terminer = tk.Button(self.__fen, text = 'Quitter', command = self.__fen.destroy)
        self.__bouton_terminer.pack()
        
        '''On affiche un tableau vide de base'''

        self.__tableau = ttk.Treeview(self.__fen)
        self.__tableau.pack()
        
        '''On ajoute une scrollbar'''
        
        self.__scrollbar = ttk.Scrollbar(self.__fen, orient="vertical", command=self.__tableau.yview)
        self.__scrollbar.pack(side="right", fill="y")
        
    
        self.__fen.mainloop()
        
    def get_attribut(self):
        if self.__choix_table == "Pays":
            return self.__attribut_Pays
        elif self.__choix_table == "Participants":
            return self.__attribut_Participants
        elif self.__choix_table == "Epreuve":
            return self.__attribut_Epreuve
        elif self.__choix_table == "Transport_en_commun":
            return self.__attribut_Transport_en_commun
        elif self.__choix_table == "Sport":
            return self.__attribut_Sport
        elif self.__choix_table == "Sites":
            return self.__attribut_Sites
        elif self.__choix_table == "Dates":
            return self.__attribut_Dates
        
          
    def get_choix(self, event):
        '''On récupère les données de notre fichier sql pour les afficher'''
        self.__tableau.destroy()
        self.__choix_table = self.__liste_combo_tables.get()

        with open('base.sql', 'r', encoding='utf-8') as sql_file:
            self.__script = sql_file.read()

        try:
            self.__sqlite = None
            self.__sqlite = sqlite3.connect('base.db')
            self.__cursor = self.__sqlite.cursor()
            self.__cursor.executescript(self.__script)
            self.__chaine = "SELECT * FROM " + self.__choix_table + ";"
            self.__cursor.execute(self.__chaine)
            
            self.__donnees = self.__cursor.fetchall()
            #On crée le tableau
            self.__tableau = ttk.Treeview(self.__fen)
            self.__tableau["columns"]=self.get_attribut()
            #On remplit le nom des colonnes et on redimensionne les colonnes
            for i in range(len(self.get_attribut())):
                self.__tableau.column(self.get_attribut()[i], width=200)
                self.__tableau.heading(self.get_attribut()[i], text=self.get_attribut()[i])                 
            self.__tableau['show'] = 'headings'
            #On affiche tout verticalement
            self.__tableau.configure(height=len(self.__donnees))
            #On ajuste la scrollbar
            self.__tableau.configure(yscrollcommand=self.__scrollbar.set)
            self.__tableau.pack()
            
            if(len(self.__donnees)):
                for don in self.__donnees:
                    self.__tableau.insert('', 'end', values=don)
            else:
                print("Aucune données")
        
        except sqlite3.OperationError as err:
            if not self.__sqlite :
                print("La connection avec le fichier SQL a échoué")
            else:
                print("Il y a une erreur dans la requête SQL")
        finally:
            if self.__sqlite:
                self.__sqlite.close()

if __name__ == '__main__' :
    mon_appli = Interface()