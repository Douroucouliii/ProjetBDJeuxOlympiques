DROP TABLE IF EXISTS Pays CASCADE;
CREATE TABLE Pays(
    Nom_Pays VARCHAR(50),
    PRIMARY KEY(Nom_Pays)
);

DROP TABLE IF EXISTS Participants CASCADE;
CREATE TABLE Participants(
    Prenom_Participants VARCHAR(15),
    Nom_Participants VARCHAR(30),
    Date_Naissance_Participants CHAR(4),
    Nb_Medaille_Bronze_Participants INT,
    Nb_Medaille_Argent_Participants INT,
    Nb_Medaille_Or_Participants INT,
	Nom_Pays VARCHAR(50),
    Nom_Epreuve VARCHAR(500),
    PRIMARY KEY(Nom_Participants),
    FOREIGN KEY(Nom_Pays) REFERENCES Pays(Nom_Pays),
    FOREIGN KEY(Nom_Epreuve) REFERENCES Epreuve(Nom_Epreuve)
);

DROP TABLE IF EXISTS Sport CASCADE;
CREATE TABLE Sport(
    Nom_Sport VARCHAR(50),
    PRIMARY KEY(Nom_Sport)
);

DROP TABLE IF EXISTS Dates CASCADE;
CREATE TABLE Dates (
    ID_Date SERIAL,
    Jour DATE,
    PRIMARY KEY(ID_Date)
);

DROP TABLE IF EXISTS Epreuve CASCADE;
CREATE TABLE Epreuve(
    Nom_Epreuve VARCHAR(500),
	ID_Date SERIAL,
	Nom_Sport VARCHAR(50),
    PRIMARY KEY(Nom_Epreuve),
    FOREIGN KEY(ID_Date) REFERENCES Dates(ID_Date),
    FOREIGN KEY(Nom_Sport) REFERENCES Sport(Nom_Sport)
);

DROP TABLE IF EXISTS Transport_en_commun CASCADE;
CREATE TABLE Transport_en_commun(
    Nom_Transport VARCHAR(100),
    PRIMARY KEY(Nom_Transport)
);

DROP TABLE IF EXISTS Sites CASCADE;
CREATE TABLE Sites(
    Nom_Sites VARCHAR(100),
    Capacite_Spectateur_Sites INT,
    Adresse_Sites VARCHAR(75),
	ID_Date SERIAL,
    Nom_Transport VARCHAR(100),
    PRIMARY KEY(Nom_Sites),
    FOREIGN KEY(ID_Date) REFERENCES Dates(ID_Date)
    FOREIGN KEY(Nom_Transport) REFERENCES Transport_en_commun(Nom_Transport)
);