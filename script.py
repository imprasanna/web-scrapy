import requests
from bs4 import BeautifulSoup
import argparse

def scrape_url(url, tag):
    try:
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        if response.status_code != 200:
            print(f'Error {response.status_code}: Unable to fetch the URL. Status code: {response.status_code}')
            return

        elements = soup.find_all(tag)

        if not elements:
            print(f'No elements found with the tag <{tag}>.')
            return

        for index, element in enumerate(elements, start=1):
            print(f'{index}. {element.get_text(strip=True)}')

    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occured: {http_err}')

    except requests.exceptions.Timeout:
        print('Request timed out. The server took too long to respond.')

    except requests.exceptions.RequestException as req_err:
        print(f'Request error occured: {req_err}')

    except Exception as err:
        print(f'An error occured: {err}')

def main():
    parser = argparse.ArgumentParser(
        description='Scrape a webpage for specific HTML tags.',
        epilog='Example usage:\npython script.py -u https://example.com -t h2\npython script.py -t h2 -u https://example.com'
    )

    parser = argparse.ArgumentParser(description='Scrape a webpage for specific HTML tags.')
    parser.add_argument('-u','--url', type=str, help='The URL of the webpage to scrape.')
    parser.add_argument('-t','--tag', type=str, help='The HTML tag to search for (e.g., h2, p).')
    
    args = parser.parse_args()
    
    scrape_url(args.url, args.tag)


if __name__ == "__main__":
    main()

