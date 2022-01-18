import requests, time
from bs4 import BeautifulSoup


# Offer status in last check (if its True, game is on offer but if its on False, game is not in offer)
last_check = False

while True:
    # Get Game Steam page
    page = requests.get("https://store.steampowered.com/app/227300/Euro_Truck_Simulator_2/")

    # Make page data a readable data
    soup = BeautifulSoup(page.content, "html.parser")

    # Find needed data

    # final_price and original_price returns a price data and you can use them for your notify
    # For using this data just add a .text on everywhere you want to use them
    final_price = soup.find("div", {"class":"discount_final_price"})
    original_price = soup.find("div", {"class":"discount_original_price"})
    discount = soup.find("div", {"class":"discount_pct"}).text
    
    # If can find anything like discount or final price (game is on offer) and last_check is game on out of offer
    if final_price and original_price and last_check == False:
        print(f"Game is on offer with {discount}")
        last_check = True # set game is on offer

    # If cant find anything like discount or final price (game is out of offer) and last_check is game on offer
    elif not final_price and last_check == True:
        print(f"Game is out of soffer")
        last_check = False # set game is out of offer

    time.sleep(120) # check this page every 120 seconds (2mins)