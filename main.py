import tkinter as tk

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



MyGUI()