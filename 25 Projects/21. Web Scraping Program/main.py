import requests
from bs4 import BeautifulSoup as bs

github_input = input("Enter the GitHub username: ")
url = f'https://github.com/{github_input}'
r = requests.get(url)

soup = bs(r.content, 'html.parser')
profile_image = soup.find('img', class_='avatar avatar-user width-full border color-bg-default')['src']
print(f"Profile Image URL: {profile_image}")