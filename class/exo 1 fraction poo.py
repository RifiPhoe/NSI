#EXERCICE 1
class Fraction:
    """
    une fraction
    """
    def __init__(self,num,denom):
        self.num = num
        self.denom = denom
        if denom<=0:
            raise ValueError("")

    def __str__(self):
        if self.denom==1:
            return "{}".format(self.num)
        else:
            return "{}/{}".format(self.num,self.denom)

    def __eq__(self,fraction):
        #return fraction == self.__str__()
        if self.num == fraction.num and self.denom == fraction.denom :
            return True
        else:
            return False

    def __lt__(self,fraction):
        if (self.num / self.denom) < (fraction.num / fraction.denom):
            return True
        else:
            return False

    def __add__(self,fraction):
        numerateur=0
        denominateur=0
        if self.denom!=fraction.denom:
            numerateur=self.num*fraction.denom+fraction.num*self.denom
            denominateur=self.denom*fraction.denom
            resultat=Fraction(numerateur,denominateur)
        else:
            numerateur=self.num+fraction.num
            denominateur=self.denom
            resultat=Fraction(numerateur,denominateur)
        return resultat

    def __mul__(self,fraction):
        return "{}/{}".format(self.num*fraction.num, self.denom*fraction.denom)




fraction1=Fraction(1,5)
fraction2=Fraction(2,6)
print(fraction1)
if(fraction1==fraction2):
    print("ce sont les deux mÃªme fractions")
else:
    print("les fractions sont diffÃ©rentes")
if(fraction1 < fraction2):
    print ("la fraction ",fraction1," est infÃ©rieure Ã  la fraction",fraction2)
else:
    print("la fraction ",fraction1," est supÃ©rieure Ã  la fraction",fraction2)
print (fraction1+fraction2)
print (fraction1*fraction2)