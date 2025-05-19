import os
from pprint import PrettyPrinter

from dotenv import load_dotenv
from requests import get

load_dotenv()

def main():
    print("Hello from currency-converter!")

    printer = PrettyPrinter()
    api_key=os.getenv("API_KEY")
    base_url=os.getenv("BASE_URL")

    endpoint = f"{base_url}{api_key}"
    data = get(endpoint).json()['data']

    data = list(data.items())
    data.sort()

    printer.pprint(data)
if __name__ == "__main__":
    main()
