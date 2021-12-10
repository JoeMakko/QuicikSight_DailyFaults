### Boneyard ###

# organization.printer('//*[@id="block-792432fe-8b58-4d55-9162-76529c593d30"]/div/div/button')

# driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="block-792432fe-8b58-4d55-9162-76529c593d30"]/div/div/button')))
# buildingTypeHTML = driver.find_element(By.XPATH, '//*[@id="block-792432fe-8b58-4d55-9162-76529c593d30"]/div/div/button').get_attribute('title')
# print(buildingTypeHTML)
#
# driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/button')))
# elementValue = driver.find_element(By.XPATH, '//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/button').get_attribute('title')
# elementName = driver.find_element(By.XPATH, '//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/button').get_attribute('data-automation-context')
# print(elementName)
# print(elementValue)

# selectorFilter(buildingType, buildingTypeEllipsis)
## copied from organization > copy > outer html:
## print(<div class="dropdown-title ellipsis flex-grow" data-automation-id="dropdown_caret">ABE2</div>)
## use to search the code below for 'all' - then if not reset it

## building type reset
# selectorFilter(buildingType, buildingTypeEllipsis,
#
# ## organization reset
# ellipsisElementsLoad()
# organizationEllipsis = driver.find_element_by_xpath('//*[@id="block-ccbe5567-76a4-406e-91c3-1a86b95c454d"]/div/div/div/div[2]/button')
# organizationEllipsis.click()
# time.sleep(0.25)
# organizationReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# organizationReset.click()
#
# ## equipment type
# ellipsisElementsLoad()
# equipmentTypeEllipsis = driver.find_element_by_xpath('//*[@id="block-7e3b4118-46e9-4df5-af2e-46cbd2eef8d5"]/div/div/div/div[2]/button')
# equipmentTypeEllipsis.click()
# time.sleep(0.25)
# equipmentTypeReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# equipmentTypeReset.click()
#
# ## rmm
# ellipsisElementsLoad()
# rmmEllipsis = driver.find_element_by_xpath('//*[@id="block-61a0986b-5a66-4e4e-bc48-11c6ad9b7048"]/div/div/div/div[2]/button')
# rmmEllipsis.click()
# time.sleep(0.25)
# rmmReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# rmmReset.click()
#
# ## criticality reset
# ellipsisElementsLoad()
# criticalityEllipsis = driver.find_element_by_xpath('//*[@id="block-c66be815-1336-4fa4-9058-b93589436ec0"]/div/div/div/div[2]/button')
# criticalityEllipsis.click()
# time.sleep(0.25)
# criticalityReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# criticalityReset.click()
#
# ## oem reset
# ellipsisElementsLoad()
# oemEllipsis = driver.find_element_by_xpath('//*[@id="block-6bac1e71-7c06-49d7-a4fc-99a6c99b1cb6"]/div/div/div/div[2]/button')
# oemEllipsis.click()
# time.sleep(0.25)
# oemReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# oemReset.click()
#
# ## has abnormality reset
# ellipsisElementsLoad()
# hasAbnormalityEllipsis = driver.find_element_by_xpath('//*[@id="block-2c8b708e-9464-4803-9ccf-9c240c0d3ffe"]/div/div/div/div[2]/button')
# hasAbnormalityEllipsis.click()
# time.sleep(0.25)
# hasAbnormalityReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# hasAbnormalityReset.click()
#
# ## description
# ellipsisElementsLoad()
# descriptionEllipsis = driver.find_element_by_xpath('//*[@id="block-9243388a-f655-466a-9c37-d783166108ad"]/div/div/div/div[2]/button')
# descriptionEllipsis.click()
# time.sleep(0.25)
# descriptionReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# descriptionReset.click()
#
# ## equipment ID
# ellipsisElementsLoad()
# equipmentIdEllipsis = driver.find_element_by_xpath('//*[@id="block-67b3bf9a-a63a-4f02-9a3a-a18896b466d2"]/div/div/div/div[2]/button')
# equipmentIdEllipsis.click()
# time.sleep(0.25)
# equipmentIdReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# equipmentIdReset.click()
#
# ## area
# ellipsisElementsLoad()
# areaEllipsis = driver.find_element_by_xpath('//*[@id="block-c7189792-04ab-43a5-ae05-94042b8234ed"]/div/div/div/div[2]/button')
# areaEllipsis.click()
# time.sleep(0.25)
# areaReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# areaReset.click()
#
# ## subArea
# ellipsisElementsLoad()
# subAreaEllipsis = driver.find_element_by_xpath('//*[@id="block-275cf689-ae35-45d6-895e-22e31165a7d9"]/div/div/div/div[2]/button')
# subAreaEllipsis.click()
# time.sleep(0.25)
# subAreaReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# subAreaReset.click()
#
# ## location =
# ellipsisElementsLoad()
# locationEllipsis = driver.find_element_by_xpath('//*[@id="block-b8ad9a7e-f493-4588-b686-e4bcdd8449ce"]/div/div/div/div[2]/button')
# locationEllipsis.click()
# time.sleep(0.25)
# locationReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li[1]/a')
# locationReset.click()
#
# ## start date reset
# ellipsisElementsLoad()
# startDateEllipsis = driver.find_element_by_xpath('//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[1]/div[2]/button')
# startDateEllipsis.click()
# time.sleep(0.25)
# startDateReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li/a')
# startDateReset.click()
#
# ## end date reset
# ellipsisElementsLoad()
# endDateEllipsis = driver.find_element_by_xpath('//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[1]/div[2]/button')
# endDateEllipsis.click()
# time.sleep(0.25)
# endDateReset = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/li/a')
# endDateReset.click()

### Set filter params ###

# ## organization
# driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[1]/div[2]/button')))
# organization = driver.find_element_by_xpath('//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[1]/div[2]/button')
# organization.click()
# time.sleep(0.5)
# organizationAll = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/span/div/div/div/label/input')
# siteAll.click()
# time.sleep(0.5)
# searchField = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/form/div/input')
# searchField.send_keys('aza5')
# time.sleep(1)
# siteAza5 = driver.find_element_by_xpath('/html/body/div[7]/div[2]/ul/ul/div/div/div/li/a/div/div/div/label/span ')
# siteAza5.click()
# time.sleep(1)
# site.click()
#
# ## start date
# driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]/input')))
# startDate = driver.find_element_by_xpath('//*[@id="block-2c65d635-7ccc-46e5-989d-29fd6eab8b71"]/div/div/div[2]/input')
# startLabel = driver.find_element_by_xpath('//*[@id="SHEET_CONTROL-2a5005ce-f4d9-4cad-89bb-fbb808604088"]/span')
# startDate.clear()
# time.sleep(0.5)
# startDate.send_keys(yesterday)
# startLabel.click()
#
# ## end date
# driver.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[2]/input')))
# startDate = driver.find_element_by_xpath('//*[@id="block-4888b434-d0f6-4310-908a-b18944003caf"]/div/div/div[2]/input')
# startLabel = driver.find_element_by_xpath('//*[@id="SHEET_CONTROL-f32ffda7-f808-4c17-9d3f-540baa9efb74"]/span')
# startDate.clear()
# time.sleep(0.5)
# startDate.send_keys(tomorrow)
# startLabel.click()

## end while