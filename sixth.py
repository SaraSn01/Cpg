import sys
import requests
import re


def download_url_and_get_all_hrefs(url):
    response = requests.get(url)
    html = response.text
    href = re.findall(r'href=["\'](.*?)["\']', html)
    if response.status_code == 200:
        return href
    

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        href = download_url_and_get_all_hrefs(url)
        print(href)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")