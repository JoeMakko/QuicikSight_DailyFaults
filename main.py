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
buildingTypeBlockID = ''

organizationMain = '//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/button'
organizationEllipsis = '//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/div/div[2]/button'
organizationSearchField = '/html/body/div[7]/div[2]/ul/form/div/input'
organizationAllSites = '/html/body/div[7]/div[2]/ul/ul/span/div/div/div/label/input'
organizationKeySiteSelector = '/html/body/div[7]/div[2]/ul/ul/div/div/div/li/a/div/div/div/label/input'
organizationKeySite = 'aza5'
organizationBlockID = ''

equipmentTypeMain = '//*[@id="block-7e3b4118-46e9-4df5-af2e-46cbd2eef8d5"]/div/div/button'
equipmentTypeEllipsis = '//*[@id="block-7e3b4118-46e9-4df5-af2e-46cbd2eef8d5"]/div/div/div/div[2]/button'
equipmentTypeBlockID = ''

rmmMain = '//*[@id="block-61a0986b-5a66-4e4e-bc48-11c6ad9b7048"]/div/div/button'
rmmEllipsis = '//*[@id="block-61a0986b-5a66-4e4e-bc48-11c6ad9b7048"]/div/div/div/div[2]/button'
rmmBlockID = ''

criticalityMain = '//*[@id="block-c66be815-1336-4fa4-9058-b93589436ec0"]/div/div/button'
criticalityEllipsis = '//*[@id="block-c66be815-1336-4fa4-9058-b93589436ec0"]/div/div/div/div[2]/button'
criticalityBlockID = ''

oemMain = '//*[@id="block-6bac1e71-7c06-49d7-a4fc-99a6c99b1cb6"]/div/div/button'
oemEllipsis = '//*[@id="block-6bac1e71-7c06-49d7-a4fc-99a6c99b1cb6"]/div/div/div/div[2]/button'
oemBlockID = ''

hasAbnormalityMain = '//*[@id="block-2c8b708e-9464-4803-9ccf-9c240c0d3ffe"]/div/div/button'
hasAbnormalityEllipsis = '//*[@id="block-2c8b708e-9464-4803-9ccf-9c240c0d3ffe"]/div/div/div/div[2]/button'
hasAbnormalityBlockID = ''

descriptionMain = '//*[@id="block-9243388a-f655-466a-9c37-d783166108ad"]/div/div/button'
descriptionEllipsis = '//*[@id="block-9243388a-f655-466a-9c37-d783166108ad"]/div/div/div/div[2]/button'
descriptionBlockID = ''

equipmentIdMain = '//*[@id="block-67b3bf9a-a63a-4f02-9a3a-a18896b466d2"]/div/div/button'
equipmentIdEllipsis = '//*[@id="block-67b3bf9a-a63a-4f02-9a3a-a18896b466d2"]/div/div/div/div[2]/button'
equipmentIdBlockID = ''

areaMain = '//*[@id="block-c7189792-04ab-43a5-ae05-94042b8234ed"]/div/div/button'
areaEllipsis = '//*[@id="block-c7189792-04ab-43a5-ae05-94042b8234ed"]/div/div/div/div[2]/button'
areaBlockID = ''

subAreaMain = '//*[@id="block-275cf689-ae35-45d6-895e-22e31165a7d9"]/div/div/button'
subAreaEllipsis = '//*[@id="block-275cf689-ae35-45d6-895e-22e31165a7d9"]/div/div/div/div[2]/button'
subAreaBlockID = ''

locationMain = '//*[@id="block-b8ad9a7e-f493-4588-b686-e4bcdd8449ce"]/div/div/button'
locationEllipsis = '//*[@id="block-b8ad9a7e-f493-4588-b686-e4bcdd8449ce"]/div/div/div/div[2]/button'
locationBlockID = ''

startDateMain = '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]'
startDateEllipsis = '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[1]/div[2]/button'
startDateBlockID = ''

endDateMain = '//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[2]'
endDateEllipsis = '//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[1]/div[2]/button'
endDateBlockID = ''

yesterday = ''
tomorrow = ''

## Open chrome and initialize timeout on wait
def init_driver():
    s=Service('C:\Program Files (x86)\pyDrivers\chromedriver.exe')
    driver=webdriver.Chrome(service=s)
    driver.wait = WebDriverWait(driver, 30)
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
    driver.wait.until(EC.presence_of_element_located((By.XPATH, buildingTypeEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, equipmentTypeEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, rmmEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, criticalityEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, oemEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, hasAbnormalityEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, descriptionEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, equipmentIdEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, areaEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, subAreaEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, locationEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, startDateEllipsis)))
    driver.wait.until(EC.presence_of_element_located((By.XPATH, endDateEllipsis)))

def mainSelectorsLoad():

    while True:
        try:
            driver.wait.until(EC.presence_of_element_located((By.XPATH, buildingTypeMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, equipmentTypeMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, rmmMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, criticalityMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, oemMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, hasAbnormalityMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, descriptionMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, equipmentIdMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, areaMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, subAreaMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, locationMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, startDateMain)))
            driver.wait.until(EC.presence_of_element_located((By.XPATH, endDateMain)))
        except Exception:
            refreshBtn = driver.find_element(By.XPATH, 'sheet_control_sample_refresh')
            refreshBtn.click()
            print('CLICKED CLICKED CLICKED')
            continue
        else:
            break

def selectFaultsPage():
    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[7]')))
    faultsField = driver.find_element(By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/div/div[7]')
    faultsField.click()

def openControlsForm():
    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div/div/a/div')))
    controlFilter = driver.find_element(By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div/div/a/div')
    controlFilter.click()

def mainResetBtn():
    mainSelectorsLoad()
    mainResetBtn = driver.find_element(By.XPATH, '//*[@id="application-header"]/div/nav[2]/div/ul/div[1]/div[2]/button/div/span')
    mainResetBtn.click()
    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[2]/div/a/i')))
    reopenCF = driver.find_element(By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[2]/div/a/i')
    reopenCF.click()

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

        if elementValue == organizationKeySite:
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

    def siteAssign(self):
        mainSelectorsLoad()
        driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationMain)))
        organization = driver.find_element(By.XPATH, organizationMain)
        organization.click()
        driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationAllSites)))
        siteAll = driver.find_element(By.XPATH, organizationAllSites)
        siteAll.click()
        mainSelectorsLoad()
        driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationMain)))
        organization = driver.find_element(By.XPATH, organizationMain)
        organization.click()
        driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationSearchField)))
        searchField = driver.find_element(By.XPATH, organizationSearchField)
        searchField.click()
        searchField.send_keys(organizationKeySite)
        driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationKeySiteSelector)))
        keySiteSelect = driver.find_element(By.XPATH, organizationKeySiteSelector)
        keySiteSelect.click()
        mainSelectorsLoad()

def cfEvaluator():
    buildingType = selectorFilter(buildingTypeMain, buildingTypeEllipsis)
    organization = selectorFilter(organizationMain, organizationEllipsis)
    equipmentType = selectorFilter(equipmentTypeMain, equipmentTypeEllipsis)
    rmm = selectorFilter(rmmMain, rmmEllipsis)
    criticality = selectorFilter(criticalityMain, criticalityEllipsis)
    oem = selectorFilter(oemMain, oemEllipsis)
    hasAbnormality = selectorFilter(hasAbnormalityMain, hasAbnormalityEllipsis)
    description = selectorFilter(descriptionMain, descriptionEllipsis)
    equipmentId = selectorFilter(equipmentIdMain, equipmentIdEllipsis)
    area = selectorFilter(areaMain, areaEllipsis)
    subArea = selectorFilter(subAreaMain, subAreaEllipsis)
    location = selectorFilter(locationMain, locationEllipsis)

    if buildingType.fieldValuator() & organization.fieldValuator() & equipmentType.fieldValuator() & rmm.fieldValuator() & criticality.fieldValuator() & oem.fieldValuator() & hasAbnormality.fieldValuator() & description.fieldValuator() & equipmentId.fieldValuator() & area.fieldValuator() & subArea.fieldValuator() & location.fieldValuator():
        return True
    else:
        return False

def keySiteAssign():
    driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationMain)))
    organization = selectorFilter(organizationMain, organizationEllipsis)
    organization.siteValuator()
    organization.siteAssign()

def yesterday():
    today = datetime.date.today()
    tDelta = datetime.timedelta(days=1)

    todayLess1 = (today - tDelta)

    yester_Year = todayLess1.year
    yester_Month = todayLess1.month
    yester_Day = todayLess1.day

    _yesterday = (str(yester_Year) + '/' + str(yester_Month) + '/' + str(yester_Day))
    return _yesterday

def tomorrow():
    today = datetime.date.today()
    tDelta = datetime.timedelta(days=1)

    todayPlus1 = (today + tDelta)

    tomorrow_Year = todayPlus1.year
    tomorrow_Month = todayPlus1.month
    tomorrow_Day = todayPlus1.day

    _tomorrow = (str(tomorrow_Year) + '/' + str(tomorrow_Month) + '/' + str(tomorrow_Day))
    return _tomorrow

def loadMain():
    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="application-content"]/div/div/div[2]/div[1]/div[2]/div/div[1]/div')))

## Call main load
driver = init_driver()
get_data(driver)
login(driver)

### Run main page execution ###
while True:

    ## Load expected elements
    loadMain()
    selectFaultsPage()
    openControlsForm()

    ## Check controls fields and assign key site
    if not cfEvaluator():
        mainResetBtn()
        keySiteAssign()
    else:
        keySiteAssign()

    driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]/input')))
    startDate = driver.find_element(By.XPATH, '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]/input')
    startLabel = driver.find_element(By.XPATH,'//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]/input' )
    startDate.clear()
    time.sleep(0.5)
    startDate.send_keys(yesterday())
    startLabel.click()
    # '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]/input'
    # '//*[@id="SHEET_CONTROL-2a5005ce-f4d9-4cad-89bb-fbb808604088"]/span'


    # driver.wait.until(EC.presence_of_element_located((By.XPATH, buildingTypeMain)))
    # buildingType = selectorFilter(buildingTypeMain, buildingTypeEllipsis)
    # print(buildingType.fieldValuator())
    # if not buildingType.fieldValuator():
    #     buildingType.reset()
    #
    # driver.wait.until(EC.presence_of_element_located((By.XPATH, organizationMain)))
    # organization = selectorFilter(organizationMain, organizationEllipsis)
    # print(organization.siteValuator())
    # if not organization.siteValuator():
    #     organization.reset()
    #     organization.siteAssign()
    #
    # driver.wait.until(EC.presence_of_element_located((By.XPATH, equipmentTypeMain)))
    # equipmentType = selectorFilter(equipmentTypeMain, equipmentTypeEllipsis)
    # print(equipmentType.fieldValuator())
    # if not equipmentType.fieldValuator():
    #     equipmentType.reset()
    #
    # driver.wait.until(EC.presence_of_element_located((By.XPATH, rmmMain)))
    # rmm = selectorFilter(rmmMain, rmmEllipsis)
    # print(rmm.fieldValuator())
    # if not rmm.fieldValuator():
    #     rmm.reset()


    break

print('out of loop') #debug