import tkinter as tk
import os
from requests import get
from json import loads
from shutil import copyfileobj
import time

class MyGUI:
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
        self.createDeckImages()

    def pullCardImage(self, cardName):
 
        # Load the card data from Scryfall
        self.card = loads(get(f"https://api.scryfall.com/cards/search?q={cardName}").text)
 
        # Get the image URL
        self.img_url = self.card['data'][0]['image_uris']['png']
 
        # Save the image
        with open(f"{self.deckName.get('1.0', tk.END).strip()}/{cardName}.png", 'wb') as out_file:
            copyfileobj(get(self.img_url, stream = True).raw, out_file)
    
    def createDeckImages(self):
        os.mkdir(f"{self.deckName.get('1.0', tk.END).strip()}")
        with open(f"{self.deckName.get('1.0', tk.END).strip()}.txt", "r") as f:
            for line in f:
                if (line != "Deck" and line != "Sideboard" and line != "\n"):
                    line = line.translate(str.maketrans('', '', '0123456789'))
                    self.pullCardImage(line.strip())
                    time.sleep(0.05)
                else:
                    continue
        # self.createDecklist()
    
    # def createDecklist(self):
    #     with open(f"{self.deckName.get('1.0', tk.END).strip()}.txt", "r") as f:
    #         with open(f"{xself.deckName.get('1.0', tk.END).strip()}_decklist.txt", "w") as f2:
    #             for line in f:
    #                 f2.write(line.strip() + "\n")
    #     self.createDecklistImage()

    # def createDecklistImage(self):
    #     with open(f"{self.deckName.get('1.0', tk.END).strip()}_decklist.txt", "r") as f:
    #         with open(f"{self.deckName.get('1.0', tk.END).strip()}_decklist.png", "w") as f2:
    #             for line in f:
    #                 f2.write(line.strip() + "\n")
        


MyGUI()