from utils import *
from tqdm import tqdm
from urllib3.exceptions import ProtocolError, NewConnectionError

if __name__ == "__main__":
    with open('links.txt', 'r') as links_file:
        urls = links_file.read().split('\n')
    links_file.close()

    start = get_starting_point(urls)

    log, psw = (input('Login? '), input('Password? '))

    driver = start_driver(log, psw)

    images = open('images.txt', 'a')
    fails = open('non-images.txt', 'a')

    for url in tqdm(urls[start:]):
        try:
            add_to_files(driver, url, images, fails)
        except AttributeError:
            fails.write(f'{url}\n')
        except (ConnectionRefusedError, ProtocolError, NewConnectionError):
            restart_driver(log, psw)
            add_to_files(driver, url, images, fails)

    images.close()
    fails.close()
    driver.quit()

    handle_duplicates('images.txt')
    handle_duplicates('non-images.txt')