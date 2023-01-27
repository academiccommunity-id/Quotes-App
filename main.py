import json
import requests
from bs4 import BeautifulSoup

url: str = "https://quotes.toscrape.com/"


headers: dict = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

def get_quotes(url: str):
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        soup: BeautifulSoup = BeautifulSoup(res.text, "html.parser")

        # proses scraping
        contents = soup.find_all("div", attrs={"class": "quote"})
        quote_list: list = []
        for content in contents:
            quote = content.find("span", attrs={"class": "text"}).text.strip()
            author = content.find("small", attrs={"class": "author"}).text.strip()

            data_dict: dict = {
                "quote": quote,
                "quote by": author,
            }
            quote_list.append(data_dict)

        # proses pengolahan data
        with open("quote.json", "w+") as f:
            json.dump(quote_list, f)

        print("Data Berhasil di Generate")
if __name__ == "__main__":
    get_quotes(url)

