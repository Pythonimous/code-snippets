from utils import *
from tqdm import tqdm
from urllib3.exceptions import ProtocolError, NewConnectionError
from selenium.common.exceptions import InvalidArgumentException

if __name__ == "__main__":
    with open('non-images.txt', 'r') as non_img_file:
        urls = [u for u in non_img_file.read().split('\n') if u]
    non_img_file.close()

    log, psw = (input('Login? '), input('Password? '))

    driver = start_driver(log, psw)

    towrite = open('for_manual_download', 'a')

    actual_non_images = []

    for url in tqdm(urls):
        try:
            link = links_exist(driver, url)
            if link:
                towrite.write(f'{link}\n')
        except (ConnectionRefusedError, ProtocolError, NewConnectionError):
            restart_driver(log, psw)
            link = links_exist(driver, url)
            if link:
                towrite.write(f'{link}\n')
        except (AttributeError, InvalidArgumentException):
            towrite.write(f'{url}\n')

    driver.quit()
    towrite.close()
