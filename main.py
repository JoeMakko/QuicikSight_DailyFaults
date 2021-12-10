import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from __init__ import userID
# from selenium.webdriver import chrome
# import pyautogui as PAG

## Global Vars
user = userID

controlFilter = ''
faultsField = ''

buildingTypeMain = '//*[@id="block-792432fe-8b58-4d55-9162-76529c593d30"]/div/div/button'
buildingTypeEllipsis = '//*[@id="block-792432fe-8b58-4d55-9162-76529c593d30"]/div/div/div/div[2]/button'
buildingTypeReset = ''

organizationMain = '//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/button'
organizationEllipsis = '//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/div/div[2]/button'
organizationReset = ''

equipmentTypeMain = '//*[@id="block-7e3b4118-46e9-4df5-af2e-46cbd2eef8d5"]/div/div/button'
equipmentTypeEllipsis = '//*[@id="block-7e3b4118-46e9-4df5-af2e-46cbd2eef8d5"]/div/div/div/div[2]/button'
equipmentTypeReset = ''

rmmMain = '//*[@id="block-61a0986b-5a66-4e4e-bc48-11c6ad9b7048"]/div/div/button'
rmmEllipsis = '//*[@id="block-61a0986b-5a66-4e4e-bc48-11c6ad9b7048"]/div/div/div/div[2]/button'
rmmReset = ''

criticalityMain = '//*[@id="block-c66be815-1336-4fa4-9058-b93589436ec0"]/div/div/button'
criticalityEllipsis = '//*[@id="block-c66be815-1336-4fa4-9058-b93589436ec0"]/div/div/div/div[2]/button'
criticalityReset = ''

oemMain = '//*[@id="block-6bac1e71-7c06-49d7-a4fc-99a6c99b1cb6"]/div/div/button'
oemEllipsis = '//*[@id="block-6bac1e71-7c06-49d7-a4fc-99a6c99b1cb6"]/div/div/div/div[2]/button'
oemReset = ''

hasAbnormalityMain = '//*[@id="block-2c8b708e-9464-4803-9ccf-9c240c0d3ffe"]/div/div/button'
hasAbnormalityEllipsis = '//*[@id="block-2c8b708e-9464-4803-9ccf-9c240c0d3ffe"]/div/div/div/div[2]/button'
hasAbnormalityReset = ''

descriptionMain = '//*[@id="block-9243388a-f655-466a-9c37-d783166108ad"]/div/div/button'
descriptionEllipsis = '//*[@id="block-9243388a-f655-466a-9c37-d783166108ad"]/div/div/div/div[2]/button'
descriptionReset = ''

equipmentIdMain = '//*[@id="block-67b3bf9a-a63a-4f02-9a3a-a18896b466d2"]/div/div/button'
equipmentIdEllipsis = '//*[@id="block-67b3bf9a-a63a-4f02-9a3a-a18896b466d2"]/div/div/div/div[2]/button'
equipmentIdReset = ''

areaMain = '//*[@id="block-c7189792-04ab-43a5-ae05-94042b8234ed"]/div/div/button'
areaEllipsis = '//*[@id="block-c7189792-04ab-43a5-ae05-94042b8234ed"]/div/div/div/div[2]/button'
areaReset = ''

subAreaMain = '//*[@id="block-275cf689-ae35-45d6-895e-22e31165a7d9"]/div/div/button'
subAreaEllipsis = '//*[@id="block-275cf689-ae35-45d6-895e-22e31165a7d9"]/div/div/div/div[2]/button'
subAreaReset = ''

locationMain = '//*[@id="block-b8ad9a7e-f493-4588-b686-e4bcdd8449ce"]/div/div/button'
locationEllipsis = '//*[@id="block-b8ad9a7e-f493-4588-b686-e4bcdd8449ce"]/div/div/div/div[2]/button'
locationReset = ''

startDateMain = '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]'
startDateEllipsis = '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[1]/div[2]/button'
startDateReset = ''

endDateMain = '//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[2]'
endDateEllipsis = '//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[1]/div[2]/button'
endDateReset = ''

yesterday = ''
tomorrow = ''

## Open chrome and initialize timeout on wait
def init_driver():
    s=Service('C:\Program Files (x86)\pyDrivers\chromedriver.exe')
    driver=webdriver.Chrome(service=s)
    driver.wait = WebDriverWait(driver, 15)
    return driver

## Initialize anomalies site request
def get_data(driver):
    driver.get('https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/a11a3395-b08d-45b4-8d44-85cbede55cd6/sheets/a11a3395-b08d-45b4-8d44-85cbede55cd6_ccb742e2-3145-4f6e-a587-0493a7854ce1?#')
    driver.maximize_window()

## Check for login page (True) or return False
def login(driver):
    title = driver.title
    driver.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="account"]'))) ## Element 'by xpath' deprecated - need to find work around
    loginField = driver.find_element(By.XPATH, '//*[@id="account"]')
    continueButton = driver.find_element(By.XPATH, '//*[@id="continue"]')
    if title == 'QuickSight Sign-In':
        loginField.send_keys(user)
        time.sleep(0.5)  ##Debug only
        continueButton.click()
        return True
    else:
        return False

## wait for controls form ellipsis elements to populate
def ellipsisElementsLoad():
    driver.wait.until(EC.presence_of_element_located((By.XPATH, buildingTypeEllipsis))) # buildingTypeEllipsis
    driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationEllipsis))) # organizationEllipsis
    driver.wait.until(EC.presence_of_element_located((By.XPATH, equipmentTypeEllipsis))) # equipmentTypeEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, rmmEllipsis))) # rmmEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, criticalityEllipsis))) # criticalityEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, oemEllipsis))) # oemEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, hasAbnormalityEllipsis))) # hasAbnormalityEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, descriptionEllipsis))) # descriptionEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, equipmentIdEllipsis))) # equipmentIdEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, areaEllipsis))) # areaEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, subAreaEllipsis))) # subAreaEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, locationEllipsis))) # locationEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, startDateEllipsis))) # startDateEllipsis = ''
    driver.wait.until(EC.presence_of_element_located((By.XPATH, endDateEllipsis))) # endDateEllipsis = ''

class selectorFilter:

    def __init__(self, XPath, ellipsisXPath):
        self.ellipsisXPath = ellipsisXPath
        self.XPath = XPath

    def fieldValuator(self):
        driver.wait.until(EC.presence_of_element_located((By.XPATH, self.XPath)))
        elementValue = driver.find_element(By.XPATH, self.XPath).get_attribute('title')

        if elementValue == 'All':
            return True
        else:
            return False

    def siteValuator(self):
        driver.wait.until(EC.presence_of_element_located((By.XPATH, self.XPath)))
        elementValue = driver.find_element(By.XPATH, self.XPath).get_attribute('title')

        if elementValue == 'AZA5':
            return True
        else:
            return False

    def reset(self):
        ellipsisElementsLoad()
        ellipsis = driver.find_element(By.XPATH, self.ellipsisXPath)
        ellipsis.click()
        time.sleep(0.25)
        reset = driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/ul/ul/li[1]/a')
        reset.click()



## Call main load
driver = init_driver()
get_data(driver)
login(driver)

### Run main page execution ###

while True:
    ## wait for main page element to be loaded
    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div')))

    ## find yesterday and tomorrow
    today = datetime.date.today()
    tDelta = datetime.timedelta(days=1)

    todayLess1 = (today - tDelta)

    yester_Year = todayLess1.year
    yester_Month = todayLess1.month
    yester_Day = todayLess1.day

    yesterday = (str(yester_Year) + '/' + str(yester_Month) + '/' + str(yester_Day))

    todayPlus1 = (today + tDelta)

    tomorrow_Year = todayPlus1.year
    tomorrow_Month = todayPlus1.month
    tomorrow_Day = todayPlus1.day

    tomorrow = (str(tomorrow_Year) + '/' + str(tomorrow_Month) + '/' + str(tomorrow_Day))


        #### Nav main page ####

    ## select faults page
    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[7]')))
    faultsField = driver.find_element(By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[7]')
    faultsField.click()

    ## open controls form
    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div/div/a/div')))
    controlFilter = driver.find_element(By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div/div/a/div')
    controlFilter.click()

        ### reset all fields ###
    driver.wait.until(EC.presence_of_element_located((By.XPATH, buildingTypeMain)))
    buildingType = selectorFilter(buildingTypeMain, buildingTypeEllipsis)
    print(buildingType.fieldValuator())
    if not buildingType.fieldValuator():
        buildingType.reset()

    driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationMain)))
    organization = selectorFilter(organizationMain, organizationEllipsis)
    print(organization.siteValuator())
    if not organization.siteValuator():
        organization.reset()

    break

print('out of loop') #debug