import tkinter as tk
import os
from requests import get
from json import loads
from shutil import copyfileobj
import time

class EnterDecklistGUI:
    def __init__(self):

        self.root = tk.Tk()

        
        self.decklistName = tk.Label(self.root, text="Decklist Name: ", font=("Arial", 20))
        self.decklistName.pack(padx=15, pady=15)

        self.deckName = tk.Text(self.root, height=1, width=30)
        self.deckName.pack(padx=15)

        self.enterDecklist = tk.Label(self.root, text="Enter your decklist", font=("Arial", 20))
        self.enterDecklist.pack(padx=15, pady=15)

        self.decklist = tk.Text(self.root, height=10, width=30)
        self.decklist.pack(padx=15)

        self.button = tk.Button(self.root, text="Submit",command=self.save_decklist)
        self.button.pack(padx=15, pady=15)

        self.root.mainloop()

    def save_decklist(self):
        with open(f"{self.deckName.get('1.0', tk.END).strip()}.txt", "w") as f: 
            f.write(self.decklist.get("1.0",tk.END))
        global deckName
        deckName = self.deckName.get("1.0", tk.END).strip()
        self.createDeckImages()

    def pullCardImage(self, cardName):
 
        # Load the card data from Scryfall
        self.card = loads(get(f"https://api.scryfall.com/cards/named?exact={cardName}").text)
 
        # Get the image URL
        self.img_url = self.card['image_uris']['png']
 
        # Save the image
        with open(f"{self.deckName.get('1.0', tk.END).strip()}/{cardName}.png", 'wb') as out_file:
            copyfileobj(get(self.img_url, stream = True).raw, out_file)
    
    def createDeckImages(self):
        os.mkdir(f"{self.deckName.get('1.0', tk.END).strip()}")
        with open(f"{self.deckName.get('1.0', tk.END).strip()}.txt", "r") as f:
            for line in f:
                if (line.strip() != "Deck" and line.strip() != "Sideboard" and line.strip() != "\n"):
                    line = line.translate(str.maketrans('', '','0123456789'))
                    self.pullCardImage(line.strip())
                    time.sleep(0.05)
        # self.createDecklist()
        self.startMulliganGUI()
    
    def startMulliganGUI(self):
        self.root.destroy()
        MulliganGUI(deckName)
    
class MulliganGUI:
    def __init__(self, deckName):
        self.deckName = deckName

        self.root = tk.Tk()
        self.decklistName = tk.Label(self.root, text="Decklist Name: ", font=("Arial", 20))
        self.decklistName.pack(padx=15, pady=15)
        self.button = tk.Button(self.root, text="Random Card",command=self.printRandomCard)
        self.button.pack(padx=15, pady=15)

        self.deck = []
        self.createDecklist()

        self.root.mainloop()


    
    def createDecklist(self):
        with open(f"{self.deckName}.txt", "r") as f:
            for line in f:
                if (line != "Deck" and line != "Sideboard" and line != "\n"):
                    quantity = line.split(" ")[0]
                    quantity = int(quantity)
                    for i in range(quantity):
                        line = line.translate(str.maketrans('', '','0123456789'))
                        self.deck.append(line.strip())
        print(self.deck)
        

        
    def printRandomCard(self):
        self.card = self.deck.pop()
        self.cardName = tk.Label(self.root, text=self.card, font=("Arial", 20))
        self.cardName.pack(padx=15, pady=15)
        self.cardImage = tk.PhotoImage(file=f"./{self.deckName}/{self.card}.png")
        self.cardImageLabel = tk.Label(self.root, image=self.cardImage)
        self.cardImageLabel.pack(padx=15, pady=15)          

    


EnterDecklistGUI()