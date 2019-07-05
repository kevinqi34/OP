from bs4 import BeautifulSoup
import requests
import re

base_url = "https://www20.gogoanimes.tv/one-piece-dub-episode-"
episode_number = 1


def get_initial_page_contents():
    gogo_url = base_url + str(episode_number)
    page = requests.get(gogo_url)
    contents = page.content
    return contents


def get_first_video_host_link(page):
    soup = BeautifulSoup(page, "html.parser")
    return soup.find("iframe")["src"]

def get_second_page_contents(link):
    link = "http:" + link
    page = requests.get(link)
    contents = page.text
    return contents

def get_final_link(page):
    pattern = "sources:\[{file: \\'[^']*'"
    regex = re.compile(pattern)
    links = regex.findall(page)
    link = links[0]
    link = link[17:-1]
    print(link)



def main():
    gogo_contents = get_initial_page_contents()
    first_host = get_first_video_host_link(gogo_contents)
    video_host_contents = get_second_page_contents(first_host)
    get_final_link(video_host_contents)



if __name__ == "__main__":
    main()
