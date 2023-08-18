from selenium import webdriver
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
options.add_argument("start-maximized")
options.add_argument("--headless")
# options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--safebrowsing-disable-download-protection")
options.add_argument("safebrowsing-disable-extension-blacklist")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

df_sale = pd.read_excel("Centaline_sale_lease.xlsx", sheet_name="Sale")
df_lease = pd.read_excel("Centaline_sale_lease.xlsx", sheet_name="Lease")
new_data_sale = []
new_data_lease = []

d = date.today() + timedelta(days=1)
print(d)
new_data_sale.append(d)
new_data_lease.append(d)

#Sequence: All sale, sale_3m, ..., sale_30m, sale_200ft, ..., sale_500ft)
driver = webdriver.Chrome('/usr/bin/chromedriver', options = options)
sale_links = ["https://hk.centanet.com/findproperty/list/buy", "https://hk.centanet.com/findproperty/list/buy?q=33e606ccc2",
"https://hk.centanet.com/findproperty/list/buy?q=33e60561e5", "https://hk.centanet.com/findproperty/list/buy?q=33e60576e2",
"https://hk.centanet.com/findproperty/list/buy?q=33e6055b97", "https://hk.centanet.com/findproperty/list/buy?q=33e61790c0",
"https://hk.centanet.com/findproperty/list/buy?q=33e6178d32", "https://hk.centanet.com/findproperty/list/buy?q=33e63a2626",
"https://hk.centanet.com/findproperty/list/buy?q=33e6178b2a", "https://hk.centanet.com/findproperty/list/buy?q=3511ff5d6d",
"https://hk.centanet.com/findproperty/list/buy?q=33ea2887d9", "https://hk.centanet.com/findproperty/list/buy?q=482827712b",
"https://hk.centanet.com/findproperty/list/buy?q=33e92a8639", "https://hk.centanet.com/findproperty/list/buy?q=33e7629114",
"https://hk.centanet.com/findproperty/list/buy?q=33e92a817b", "https://hk.centanet.com/findproperty/list/buy?q=33e7627d5a"]
for link in sale_links:
  sale = get_data(link)
  print(sale)
  store_sale(sale)
lease = get_data("https://hk.centanet.com/findproperty/list/rent")
print(lease)
store_lease(lease)
driver.quit()

df_sale.loc[len(df_sale)] = new_data_sale
df_lease.loc[len(df_lease)] = new_data_lease
df_sale['日期'] = pd.to_datetime(df_sale['日期'])
df_sale['日期'] = df_sale['日期'].dt.strftime('%Y-%m-%d')
df_lease['日期'] = pd.to_datetime(df_lease['日期'])
df_lease['日期'] = df_lease['日期'].dt.strftime('%Y-%m-%d')
print(df_sale)
with pd.ExcelWriter("Centaline_sale_lease.xlsx") as writer:
  df_sale.to_excel(writer, sheet_name="Sale", index=False)
  df_lease.to_excel(writer, sheet_name="Lease", index=False)
