#! python3
# This program downloads the last N comics from 
# the XKCD webcomic.

import requests, os, bs4, sys

os.makedirs("./comics", exist_ok=True)

def main():

    comic_count = get_int()

    page_link = "https://xkcd.com"

    print("Downloading...")

    for i in range(comic_count):
        print(f"\rdownload comic{i + 1}...  {(i + 1) / comic_count:.2%}", end="")
        
        res = get_response(page_link)

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        image = soup.select_one("#comic img")
        
        if not image :
            print(f"\nNo image found for page {page_link}, skipping...")
        else:

            image_link = image.get("src")
            if not image_link.startswith("http"):
                image_link = "https:" + image_link

            image_res = get_response(image_link)
            image_ext = image_link.split(".")[-1]

            with open(f"./comics/comic{i + 1}.{image_ext}", "wb") as current_comic:
                for chunk in image_res.iter_content(100000):
                    current_comic.write(chunk)

        prev = soup.select_one("a[rel='prev']")
        page_link = "https://xkcd.com" + prev.get("href")

    print("\nDone!")


def get_int():
    for _ in range(10):
        try:
            count = int(input("Enter the number of comics:"))
            if count > 0:
                return count
            else:
                continue

        except ValueError:
            print("The count should be an integer!")
            continue
    
    sys.exit("Too many invalid inputs.")


def get_response(url):
    try: 
        res = requests.get(url)
        res.raise_for_status()
        return res
    except Exception as err:
        sys.exit(str(err))

main()
