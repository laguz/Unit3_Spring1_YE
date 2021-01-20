class Polo():

    #attributes of Polos 
    #polo(color, size, brand)
    
    def __init__(self, color, size, brand):
        self.color = color
        self.size = size
        self.brand = brand

    #methos for polos
    def fold(self):
        print("Please fold the Polo shirt")

if __name__=="__main__":
    polo1 = Polo(color="Pink", size="S", brand='RL')
    polo1.fold()
    print(polo1.color)

    # polo2 = Polo(color="Red", size="S", brand='RL')
    # print(polo2.color)
    

    # df = pd.DataFrame("") #df is the class
    # df.apply() # this is a function of intance of the class "dataframe"
    # df.columns #This is attribute of the dataframe