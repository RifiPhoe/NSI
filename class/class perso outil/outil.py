class Outil:
    def __init__(self,xp=8,masse=0,main=1):
        self.xp = xp
        self.masse = masse
        self.main = main

    def set_mains(self):
        if self.main >1:
            self.main -=1

    def get_masse(self):
        return self.masse

    def get_main(self):
        return self.main
