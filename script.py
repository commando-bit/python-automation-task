import requests
from bs4::BeautifulSoup import BeautifulSoup  # यदि BeautifulSoup प्रयोग गर्ने भए
# वा एउटा सामान्य वेब स्क्र्यापिङ वा डेटा तान्ने टेम्प्लेट:

def simple_scraper():
    # एउटा टेस्ट वेबसाइटको URL
    url = "http://quotes.toscrape.com/"
    
    print(f"Connecting to {url}...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully connected!")
            # यहाँ डेटा पार्से गर्ने वा स्क्र्याप गर्ने कोड लेखिन्छ
            print("Page content fetched successfully.")
        else:
            print("Failed to connect to the website.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    simple_scraper()