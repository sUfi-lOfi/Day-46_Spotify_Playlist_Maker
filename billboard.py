import datetime as dt
import requests
from bs4 import BeautifulSoup
class BillBoard:
    def __init__(self):
        self.url = "https://www.billboard.com/charts/hot-100/"
        self.http_header = {
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0"
}
    def fetch_songs(self,date):
        try:
            http_request = requests.get(self.url+date+'/',headers=self.http_header)
            http_response = http_request.text
        except:
            print("Endpoint not reachable!!")
        else:
                soup = BeautifulSoup(http_response,"lxml")
                names_of_songs = soup.select("ul li ul li h3")
                print([n.getText().strip() for n in names_of_songs])




