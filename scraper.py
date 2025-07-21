import requests
from bs4 import BeautifulSoup
import csv

def scrape_books(url):
    """
    Scrapes book titles, prices, and ratings from 'books.toscrape.com'.

    Args:
        url (str): The URL of the website to scrape.

    Returns:
        list: A list of lists, where each inner list contains the
              title, price, and rating of a book. Returns None on failure.
    """
    try:
        response = requests.get(url, timeout=10)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all book containers on the page
    articles = soup.find_all('article', class_='product_pod')

    scraped_data = []

    for book in articles:
        # Extract title from the 'a' tag's title attribute
        title = book.h3.a['title']

        # Extract price from the element with the 'price_color' class
        price = book.find('p', class_='price_color').get_text()

        # Extract star rating from the 'p' tag's class attribute
        rating_class = book.find('p', class_='star-rating')['class']
        # The rating is the second class in the list (e.g., ['star-rating', 'Three'])
        rating = f"{rating_class[1]} out of Five"

        scraped_data.append([title, price, rating])

    return scraped_data

def save_to_csv(data, filename="books.csv"):
    """
    Saves the scraped data to a CSV file.

    Args:
        data (list): The list of book data to save.
        filename (str): The name of the output CSV file.
    """
    if not data:
        print("No data to save.")
        return

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(['Title', 'Price', 'Rating'])
            # Write all the book data
            writer.writerows(data)
        print(f"Data successfully saved to {filename} ✅")
    except IOError as e:
        print(f"Error writing to file: {e}")

# --- Main execution ---
if __name__ == "__main__":
    TARGET_URL = 'http://books.toscrape.com/'
    book_data = scrape_books(TARGET_URL)

    if book_data:
        save_to_csv(book_data)
