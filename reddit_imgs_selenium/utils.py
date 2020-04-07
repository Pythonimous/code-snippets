from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from urllib import request
import os
import requests
import time

options = Options()
ua = UserAgent()
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')

sess = requests.Session()


def reddit_login(driver, log, psw):
    driver.get('https://www.reddit.com/login/')
    login = driver.find_element_by_id('loginUsername')
    login.send_keys(log)
    password = driver.find_element_by_id('loginPassword')
    password.send_keys(psw)
    driver.find_element_by_class_name('AnimatedForm__submitButton').click()
    time.sleep(10)


def start_driver(log='Login', psw='Password'):
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", options=options)
    reddit_login(driver, log, psw)
    return driver


def restart_driver(driver, log='Login', psw='Password'):
    driver.quit()
    time.sleep(10)
    return start_driver(log, psw)


def get_soup(driver, url):
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup


def find_repost(soup):
    if 'Crossposted' in soup.text:
        url = soup.findAll('a', {'data-click-id': 'timestamp'})[-1].get('href')
        return url


def find_image(soup):
    post_content = soup.find('div', {'data-test-id': 'post-content'})
    links = [a.get('href') for a in post_content.findAll('a')]
    best_link = [link for link in links if link.split('.')[-1] in ('jpg', 'jpeg', 'png')]
    if best_link:
        return best_link[0]
    else:
        return ''


def get_image(driver, url):
    soup = get_soup(driver, url)
    repost = find_repost(soup)
    if repost:
        url = repost
        soup = get_soup(driver, url)
    non_image = ''
    image = find_image(soup)
    if not image:
        non_image = url
    return image, non_image


def add_to_files(driver, url, images, fails):
    image, non_image = get_image(driver, url)
    images.write(f'{image}\n')
    fails.write(f'{non_image}\n')


def get_starting_point(urls):
    starting_point = input('What link to start from? ')
    try:
        starting_point = int(starting_point)
    except ValueError:
        starting_point = 0
        print('incorrect, reverting to 0')
    if (starting_point >= len(urls)) or (starting_point < 0):
        starting_point = 0
        print('incorrect, reverting to 0')
    return starting_point


def links_exist(driver, url):
    soup = get_soup(driver, url)
    post_content = soup.find('div', {'data-test-id': 'post-content'})
    links = [u for u in [a.get('href') for a in post_content.findAll('a')] if (u != url and u[:4] == 'http')]
    if links:
        link = links[0]
    else:
        link = ''
    return link


def handle_duplicates(filename):
    with open(filename, 'r') as f:
        links = [link for link in f.read().split('\n') if link]
    f.close()

    unique_links = []
    for link in links:
        if link not in unique_links:
            unique_links.append(link)
    with open(filename, 'w') as f:
        f.write('\n'.join(unique_links))
    f.close()


def retrieve_images(filename):
    if not os.path.exists('images'):
        os.makedirs('images')

    with open(filename, 'r') as image_file:
        links = [link for link in image_file.read().split('\n') if link]
    image_file.close()

    starting_point = int(input('what was the last number? ')) + 1

    for num, link in enumerate(links):
        file_type = link.split(".")[-1]
        img_name = f'images/{num + starting_point}.{file_type}'
        request.urlretrieve(link, img_name)
