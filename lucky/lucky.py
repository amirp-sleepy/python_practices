#! python3
# This program search in Google and open the five first 
# results in the five tabs.

import sys, bs4, requests, webbrowser

def main():
    print("Googeling...")

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
    }
    query = (" ").join(sys.argv[1:])
    res = requests.get("https://www.google.com/search?q=" + query, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    results = soup.select("div.main a")

    num_open = min(5, len(results))

    for i in range(num_open):
        a_tag = results[i]
        link = a_tag.get("href")
        webbrowser.open_new_tab(link)


main()