import requests
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import random
from time import sleep
import json

import os

import errors
import vars


def query_to_service(scrapping_data):
    """Function to call microservice"""
    base_url = vars.URLS.get('base_url')
    microservice_url = f'{base_url}/'

    if scrapping_data:
        response = requests.post(url=microservice_url, data=json.dumps(scrapping_data),
                                 headers={'Content-Type': 'application/json'})

        if response.status_code == 201:
            os.system(f'echo Scrapping data was saved successfully: {scrapping_data}')
        else:
            raise errors.UnexpectedErrorFromService('Failed save data')

    else:
        raise errors.DataNotFound('The scrapping provided invalid data')

    return True


def get_scrapper_products(driver):
    list_data = []
    score_param = 3
    try:
        while True:
            products = driver.find_elements(By.XPATH, f'//div[@class="thumbnail"]')
            for product in products:
                product_id = product.id
                product_score = product.find_elements(By.TAG_NAME, 'span')
                if len(product_score) <= score_param:
                    product_details = product.find_elements(By.TAG_NAME, 'h4')[1]
                    product_name = product_details.text
                    # product_details.click()
                    webdriver.ActionChains(driver).move_to_element(product_details).click(product_details).perform()
                    sleep(random.uniform(1.0, 2.0))

                    product_description = driver.find_element(By.XPATH, f'//p[@class="description"]').text
                    product_price = driver.find_element(By.XPATH, f'//h4[@class="pull-right price"]').text
                    product_reviews = driver.find_element(By.XPATH, f'//div[@class="ratings"]').text
                    dict_data = {'id': product_id,
                                 'name': product_name,
                                 'description': product_description,
                                 'reviews': product_reviews,
                                 'price': product_price
                                 }
                    list_data.append(dict_data)
                    sleep(random.uniform(1.0, 2.0))
                    driver.back()
                    sleep(random.uniform(1.0, 2.0))

            paginator = driver.find_element(By.XPATH, f'//a[@rel="next"]')
            paginator.click()

    except NoSuchElementException():
        pass

    return list_data


def scrapper():
    driver = webdriver.Chrome()
    site_var = vars.SITE_URL
    driver.get(site_var)
    os.system(f'echo Page already loaded')
    sleep(random.uniform(1.0, 2.0))

    return get_scrapper_products(driver)


if __name__ == '__main__':
    is_successful = None
    try:
        data = scrapper()
        is_successful = query_to_service(data)

    except errors.InvalidParameters as ex1:
        os.system(f'echo {ex1}')

    except errors.DataNotFound as ex2:
        os.system(f'echo Error while executing query_to_service: {ex2}')

    except errors.InvalidResponseData as ex3:
        os.system(f'echo Error while executing query_to_service: {ex3}')

    except errors.UnexpectedErrorFromService as ex4:
        os.system(f'echo Error running the service: {ex4}')

    except requests.exceptions.ConnectionError:
        os.system('echo Error calling the service: Failed to establish a new connection')

    except Exception as ex:
        os.system(f'echo An unexpected error has occurred: {ex}')
