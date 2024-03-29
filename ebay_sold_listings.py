from bs4 import BeautifulSoup
import requests

search_item = input("Input the eBay item: ")
search_item = search_item.split(" ")
search_item = ("+").join(search_item)

# Example item: nintendo switch oled

price_list = []
f = open("Sold_listings.txt", "w")
# The range of pages starting at page 1
for i in range(3)[1:]:
    url = f"https://www.ebay.com/sch/i.html?_nkw={search_item}&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1&_pgn={i}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")

    page = doc.find(class_="srp-results srp-list clearfix")

    listings = page.find_all("li", class_="s-item s-item__pl-on-bottom")

    for item in listings:
        title= item.find(class_ = "s-item__title").text
        price = item.find(class_ = "s-item__price").text
        date = item.find(class_ = "POSITIVE").string
        link = item.find(class_ = "s-item__link")['href'].split("?")[0]
        
        f.write(f"Title: {title}\n")
        f.write(f"Price: {price}\n")
        f.write(f"Date: {date}\n")
        f.write(f"Link: {link}\n")
        f.write("---\n")

        # print("Title:", title)
        # print("Price:", price)
        # print("Date:", date)
        # print("Link:", link)
        # print("---")

        if price != None:
            price = price.replace("$", "")
            if 'to' in price:
                price = sum([float(num) for num in price.split() if num != 'to']) / 2
                price = round(price, 2)
            # Max amount for the price range
            if float(price) < 500:
                price_list.append(float(price))

price_list = list(set(price_list))

if price_list:
    f.write(f"Highest Price: {max(price_list)}\n")
    f.write(f"Lowest Price: {min(price_list)}\n")
    f.write(f"Average Price: {round(sum(price_list) / len(price_list), 2)}\n")

    print("Highest Price:", max(price_list))
    print("Lowest Price:", min(price_list))
    print("Average Price:", round(sum(price_list) / len(price_list), 2))
else:
    print("No items found matching the criteria.")

f.close()
