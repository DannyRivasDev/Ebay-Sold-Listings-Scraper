from bs4 import BeautifulSoup
import requests
import re

# search_link = input("Input the ebay link: ")

# Link: https://www.ebay.com/sch/i.html?_nkw=gameboy+advance+console&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1&_pgn=1

price_list = []
f = open("Sold_listings.txt", "w")
for i in range(5)[1:]:
    url = f"https://www.ebay.com/sch/i.html?_nkw=gameboy+advance+console&_sop=13&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={i}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    page = doc.find(class_ = "srp-results srp-list clearfix")

    listings = page.find_all("li", class_ = "s-item s-item__pl-on-bottom")


    for item in listings:
        title= item.find(class_ = "s-item__title").string
        price = item.find(class_ = "s-item__price").string
        date = item.find(class_ = "POSITIVE").string
        link = item.find(class_ = "s-item__link")['href'].split("?")[0]
        
        f.write(f"Title: {title}\n")
        f.write(f"Price: {price}\n")
        f.write(f"Date: {date}\n")
        f.write(f"Link: {link}\n")
        f.write("---\n")

        print("Title:", title)
        print("Price:", price)
        print("Date:", date)
        print("Link:", link)
        print("---")

        if price != None:
            price = price[1:]
            price = price.replace(",", "")
            if float(price) < 200:
                price_list.append(float(price))

# print(price_list)
price_list = list(set(price_list))
f.write(f"Highest Price: {max(price_list)}\n")
f.write(f"Lowest Price: {min(price_list)}\n")
f.write(f"Average Price: {round(sum(price_list) / len(price_list), 2)}\n")

print("Highest Price:", max(price_list))
print("Lowest Price:", min(price_list))
print("Average Price:", round(sum(price_list) / len(price_list), 2))

f.close()