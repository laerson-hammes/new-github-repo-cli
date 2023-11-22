from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import requests
import argparse
import os


load_dotenv(
    dotenv_path=".env",
    verbose=True
)

USERNAME = str(os.environ.get('USERNAME'))
TOKEN = str(os.environ.get('TOKEN'))
URL = "https://api.github.com/user/repos"


def post(options):
    response = requests.post(
        URL,
        auth=HTTPBasicAuth(USERNAME, TOKEN),
        json=vars(options)
    )
    if response.status_code == 201:
        print("Repository has been created...")
    else:
        print("Error...")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", type=str, dest="name", help="The name of the repository.")
    parser.add_argument("-d", "--description", type=str, default="", dest="description", help="A short description of the repository.")
    parser.add_argument("-p", "--private", type=bool, default=False, dest="private", help="Whether the repository is private.")
    parser.add_argument("-ai", "--auto-init", type=bool, default=True, dest="auto_init", help="Whether the repository is initialized with a minimal README.")
    parser.add_argument("-gi", "--gitignore", type=str, default="Python", dest="gitignore_template", help="The desired language or platform to apply to the .gitignore.")
    parser.add_argument("-l", "--license", type=str, default="", dest="license_template", help="The license keyword of the open source license for this repository.")

    options: argparse.Namespace = parser.parse_args()
    if not options.name:
        options.name = input("Repository name: ")
    post(options)


if __name__ == "__main__":
    main()