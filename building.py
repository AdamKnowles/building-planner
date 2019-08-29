import datetime


class Building:

    def __init__(self, address, stories):
        self.designer = "Adam Knowles"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
       
    def constructor(self):
        self.date_constructed = datetime.datetime.now()

    def purchasher(self, owner):
        self.owner = owner

    def print_string(self):
        print(f'{self.address} was purchased by {self.owner}, has {self.stories} story, and was constructed on {self.date_constructed}')


baseball_stadium = Building("100 8th Street", 1)
baseball_stadium.purchasher("adam")
baseball_stadium.constructor()
baseball_stadium.print_string()

tennis_stadium = Building("200 8th Street", 2)
tennis_stadium.purchasher("joe")
tennis_stadium.constructor()
tennis_stadium.print_string()

football_stadium = Building("300 8th Street", 3)
football_stadium.purchasher("melanie")
football_stadium.constructor()
football_stadium.print_string()

track_stadium = Building("400 8th Street", 4)
track_stadium.purchasher("drew")
track_stadium.constructor()
track_stadium.print_string()

soccer_stadium = Building("500 8th Street", 5)
soccer_stadium.purchasher("sydney")
soccer_stadium.constructor()
soccer_stadium.print_string()





    

    

    