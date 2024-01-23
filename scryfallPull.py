# Import required methods
from requests import get
from json import loads
from shutil import copyfileobj
 
# In this example, we're looking for "Vindicate"
search_query = 'Ragavan, Nimble Pilferer'
 
# Load the card data from Scryfall
card = loads(get(f"https://api.scryfall.com/cards/search?q={search_query}").text)
 
# Get the image URL
img_url = card['data'][0]['image_uris']['png']
 
# Save the image
with open('image.png', 'wb') as out_file:
    copyfileobj(get(img_url, stream = True).raw, out_file)