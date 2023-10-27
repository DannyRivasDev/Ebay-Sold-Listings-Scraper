# Ebay-Sold-Listings-Scraper

## Description

This Python script allows you to scrape sold listings from eBay based on a user-provided search item. It utilizes the `requests` library to send HTTP requests to eBay's search page and `BeautifulSoup` for parsing the HTML content.

## Usage

1. **Input**: The user is prompted to input the eBay item they want to search for. For example, if the user wants to search for "nintendo switch oled", they can input that.
   
2. **Processing**: The script formats the input for the URL query, making sure it is in the format expected by eBay's search parameters. For example, spaces are replaced with `+` to create a valid URL.

3. **File Handling**: It opens a file named "Sold_listings.txt" in write mode to store the scraped data.

4. **Scraping Process**:
   - The script iterates through a specified range of pages (in this example, 3 pages starting from page 1).
   - For each page, it sends a request to eBay's search page using the formatted URL.
   - It then parses the HTML content using BeautifulSoup to extract relevant information from the sold listings, including title, price, date, and link.

5. **Data Writing**:
   - The extracted information is written to the file in a structured format (Title, Price, Date, Link).

6. **Price Formatting**:
   - The script handles price formatting by removing the dollar sign ($) and, if applicable, calculating the average for price ranges.

7. **Data Analysis**:
   - The script creates a list of unique prices and, if any prices are found, calculates the highest, lowest, and average prices.

8. **Output**:
   - The script writes the highest, lowest, and average prices to the file, and also prints them to the console.

9. **File Closing**:
   - Finally, the file is closed.

## Notes

- Make sure to have the necessary libraries (`requests` and `BeautifulSoup`) installed in your Python environment.
- This script is set to scrape data from three pages. You can adjust the range as needed.
- The script assumes a maximum price of $500 for the price range.

## Disclaimer

Please be aware that web scraping may be subject to legal and ethical considerations. Ensure you have the appropriate permissions and adhere to eBay's terms of service and policies before using this script. Use it responsibly and for personal use only.
