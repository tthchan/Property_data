from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date, datetime, timedelta
import time




def get_data(url):
  driver.get(url)
  time.sleep(5)
  data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
  return data

def store_sale(data):  # Store scrapped sale data to the list as int
  if "," in data:
    data = data.replace(",","")
  else:
    pass
  new_data_sale.append(int(data))

def store_lease(data):  # Store scrapped lease data to the list as int
  if "," in data:
    data = data.replace(",","")
  else:
    pass
  new_data_lease.append(int(data))

#set webdriver
chrome_options = webdriver.chrome.options.Options()

prefs = {
'download.extensions_to_open': 'xml',
'safebrowsing.enabled': True
}
## Uncomment the below to let the program to run in background
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs',prefs)
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

df_sale = pd.read_excel("中原放盤.xlsx", sheet_name="賣盤")
df_lease = pd.read_excel("中原放盤.xlsx", sheet_name="租盤")
new_data_sale = []
new_data_lease = []

d = date.today() + timedelta(days=1)
print(d)
new_data_sale.append(d)
new_data_lease.append(d)

#Sequence: All sale, sale_1m, sale_1.01m-2m, ..., sale_20m_or_above, sale_0-200ft, ..., sale_1000ft_or_above, sale_studio, ..., sale_4rooms_or_more
sale_links = ["https://hk.centanet.com/findproperty/list/buy?q=3463167af7", "https://hk.centanet.com/findproperty/list/buy?q=9148d10403",
              "https://hk.centanet.com/findproperty/list/buy?q=767ee297f7", "https://hk.centanet.com/findproperty/list/buy?q=4955e55325", "https://hk.centanet.com/findproperty/list/buy?q=92adc6cb7b",
              "https://hk.centanet.com/findproperty/list/buy?q=90d18dcdd5", "https://hk.centanet.com/findproperty/list/buy?q=92adc715ad", "https://hk.centanet.com/findproperty/list/buy?q=92adc73a2f",
              "https://hk.centanet.com/findproperty/list/buy?q=92adc76092", "https://hk.centanet.com/findproperty/list/buy?q=92adc784b4", "https://hk.centanet.com/findproperty/list/buy?q=92adc845a9",
              "https://hk.centanet.com/findproperty/list/buy?q=92adc86a7b", "https://hk.centanet.com/findproperty/list/buy?q=92adc88fcd", "https://hk.centanet.com/findproperty/list/buy?q=92adc8b4b0",
              "https://hk.centanet.com/findproperty/list/buy?q=92adc8d9c2", "https://hk.centanet.com/findproperty/list/buy?q=92adc8fe8e", "https://hk.centanet.com/findproperty/list/buy?q=92adc9bfc9",
              "https://hk.centanet.com/findproperty/list/buy?q=92adc9e45f", "https://hk.centanet.com/findproperty/list/buy?q=92adca0a65", "https://hk.centanet.com/findproperty/list/buy?q=92adca2e6c",
              "https://hk.centanet.com/findproperty/list/buy?q=92ade3e0d5", "https://hk.centanet.com/findproperty/list/buy?q=33e92a8639", "https://hk.centanet.com/findproperty/list/buy?q=9180e7652f",
              "https://hk.centanet.com/findproperty/list/buy?q=9180e7d565", "https://hk.centanet.com/findproperty/list/buy?q=78d5b2bf97", "https://hk.centanet.com/findproperty/list/buy?q=9180e94802",
              "https://hk.centanet.com/findproperty/list/buy?q=9180eafc4c", "https://hk.centanet.com/findproperty/list/buy?q=9180eb41b9", "https://hk.centanet.com/findproperty/list/buy?q=9180ec697b",
              "https://hk.centanet.com/findproperty/list/buy?q=9180ecbf4d", "https://hk.centanet.com/findproperty/list/buy?q=a50effaa35", "https://hk.centanet.com/findproperty/list/buy?q=33e7b84607",
              "https://hk.centanet.com/findproperty/list/buy?q=33e6c3d6bb", "https://hk.centanet.com/findproperty/list/buy?q=33e5faa963", "https://hk.centanet.com/findproperty/list/buy?q=33e617873f",
              "https://hk.centanet.com/findproperty/list/buy?q=33e5ff0a96"]

#Sequence: All lease, lease_0-200ft, ..., lease_1000ft_or_above, lease_studio, ..., lease_4rooms_or_more
lease_links = ["https://hk.centanet.com/findproperty/list/rent?q=345cd78d03", "https://hk.centanet.com/findproperty/list/rent?q=a2f55a6ca7",
               "https://hk.centanet.com/findproperty/list/rent?q=a2f55a91e7", "https://hk.centanet.com/findproperty/list/rent?q=a2f55b529d", "https://hk.centanet.com/findproperty/list/rent?q=a2f55b778a",
               "https://hk.centanet.com/findproperty/list/rent?q=a2f55b9c42", "https://hk.centanet.com/findproperty/list/rent?q=a2f55bc147", "https://hk.centanet.com/findproperty/list/rent?q=a2f55be724",
               "https://hk.centanet.com/findproperty/list/rent?q=a2f55c0c51", "https://hk.centanet.com/findproperty/list/rent?q=a2f55c2400", "https://hk.centanet.com/findproperty/list/rent?q=33e6b19896",
               "https://hk.centanet.com/findproperty/list/rent?q=33e9c9c512", "https://hk.centanet.com/findproperty/list/rent?q=33e68e1b64", "https://hk.centanet.com/findproperty/list/rent?q=33e60b045b",
               "https://hk.centanet.com/findproperty/list/rent?q=33e604c9a4"]

#Sale
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
url = "https://hk.centanet.com/findproperty/list/buy"
driver.get(url)

data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
print(data)
store_sale(data)
time.sleep(3)

try:
  for price in range(100,2001,100):
      driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[5]/span/button/i').click()
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(price-99)
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[2]/div/input').send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[2]/div/input').send_keys(price)
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[2]/div/input').send_keys(Keys.ENTER)
      time.sleep(3)

      data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
      print(data)
      store_sale(data)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[5]/span/button/i').click()
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').clear()
  driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(2001)
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)
  time.sleep(3)
  data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
  print(data)
  store_sale(data)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[5]/span/button/i[1]').click()
  time.sleep(3)

  for size in range(200,1001,100):
      driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[6]/span/button/i').click()
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
      driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[1]/div/input').send_keys(size-99)
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[2]/div/input').send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
      driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[2]/div/input').send_keys(size)
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[2]/div/input').send_keys(Keys.ENTER)
      time.sleep(3)

      data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
      print(data)
      store_sale(data)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[6]/span/button/i').click()
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[1]/div/input').clear()
  driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[1]/div/input').send_keys(1001)
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/ul[2]/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)
  time.sleep(3)
  data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
  print(data)
  store_sale(data)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[6]/span/button/i[1]').click()
  time.sleep(3)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[7]/span/button/i').click()
  time.sleep(3)

  for fp in range(1,6):
      driver.find_element_by_xpath(f'/html/body/ul[3]/div[2]/div/label[{fp}]/span[1]/span').click()
      time.sleep(3)
      data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
      print(data)
      store_sale(data)

      driver.find_element_by_xpath(f'/html/body/ul[3]/div[2]/div/label[{fp}]/span[1]/span').click()
      time.sleep(3)

except:
  print("Using backup method for sale data")
  for link in sale_links[len(new_data_sale) - 2:]:
    sale = get_data(link)
    print(sale)
    store_sale(sale)

driver.quit()

#Lease
driver = webdriver.Chrome(ChromeDriverManager().install(), options = options)
url = "https://hk.centanet.com/findproperty/list/rent"
driver.get(url)

data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
print(data)
store_lease(data)
time.sleep(3)

try:
  for size in range(200,1001,100):
      driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[6]/span/button/i').click()
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(size-99)
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[2]/div/input').send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[2]/div/input').send_keys(size)
      time.sleep(3)
      driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[2]/div/input').send_keys(Keys.ENTER)
      time.sleep(3)

      data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
      print(data)
      store_lease(data)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[6]/span/button/i').click()
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').clear()
  driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(1001)
  time.sleep(3)
  driver.find_element_by_xpath('/html/body/ul/div[2]/div[2]/div[1]/div/input').send_keys(Keys.ENTER)
  time.sleep(3)
  data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
  print(data)
  store_lease(data)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[6]/span/button/i[1]').click()
  time.sleep(3)

  driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[3]/div/div[2]/div[1]/div[7]/span/button/i').click()
  time.sleep(3)

  for fp in range(1,6):
      driver.find_element_by_xpath(f'/html/body/ul[2]/div[2]/div/label[{fp}]/span[1]/span').click()
      time.sleep(3)
      data = driver.find_element_by_xpath('//*[@id="__layout"]/div/div[4]/div[6]/div/div[1]/div[1]/div/h2/span/span').text
      print(data)
      store_lease(data)

      driver.find_element_by_xpath(f'/html/body/ul[2]/div[2]/div/label[{fp}]/span[1]/span').click()
      time.sleep(3)

except:
  print("Using backup method for lease data")
  for link in lease_links[len(new_data_lease) - 2:]:
    lease = get_data(link)
    print(lease)
    store_lease(lease)

print(new_data_sale)
print(new_data_lease)

df_sale.loc[len(df_sale)] = new_data_sale
df_lease.loc[len(df_lease)] = new_data_lease
df_sale['日期'] = pd.to_datetime(df_sale['日期'])
df_sale['日期'] = df_sale['日期'].dt.strftime('%Y-%m-%d')
df_lease['日期'] = pd.to_datetime(df_lease['日期'])
df_lease['日期'] = df_lease['日期'].dt.strftime('%Y-%m-%d')

with pd.ExcelWriter("中原放盤.xlsx") as writer:
  df_sale.to_excel(writer, sheet_name="賣盤", index=False)
  df_lease.to_excel(writer, sheet_name="租盤", index=False)
