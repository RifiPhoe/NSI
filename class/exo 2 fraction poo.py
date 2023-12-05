class Date:
    def __init__(self,jour,mois,annee):
        self.jour = jour
        self.mois = mois
        self.annee = annee
        if jour <1 or jour >31:
            raise ValueError("")
        elif mois<1 or mois>12:
            raise ValueError("")

    def __str__(self):
        mois = ["janvier","fevrier","mars","avril","mai","juin","juillet","aout","septembre","octobre","novembre","decembre"]
        return "{} {} {}".format(self.jour,mois[self.mois -1],self.annee)

    '''def __lt__(self,date):
        if self.annee < date.annee:
            return True
        elif self.annee==date.annee:
            if self.mois < date.mois:
                return True
            #elif self.mois==date.mois:
           # if self.jour < date.jour:
               # return True
            else:
            return False'''
    def __lt__(self, d):
        inferieur=False
        if self.annee<d.annee or (self.annee==d.annee and self.mois<d.mois) or (self.mois==d.mois and self.jour<d.jour):
            inferieur=True

        return inferieur






date1=Date(8,6,2006)
date2=Date(25,6,2006)

if (date1<date2):
    print(date1,"strictement inferieure a",date2,".")
else:
    print("La premiere date est superieure.")


