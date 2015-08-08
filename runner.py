import json
import urllib2

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

drupal_site = "http://url.toyourdrupalsite.com"
data_path   = "/api/v1/resource" # returns array of objects containing nids
driver      = webdriver.Firefox()

def parse_nids_json(record):
    return str(record["nid"])

def login():
    driver.get(drupal_site + "/user")
    driver.find_element_by_id("edit-name").send_keys("your_username")
    driver.find_element_by_id("edit-pass").send_keys("your_password")

    return driver.find_element_by_id("edit-submit").submit()

request = json.load(urllib2.urlopen(drupal_site + data_path))
nids    = map(parse_nids_json, request)

login()

for nid in nids:
    url = drupal_site + "/node/" + nid + "/edit"
    driver.get(url)
    # Do stuff here like change fields and click the Save button

driver.quit()
