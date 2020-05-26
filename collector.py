import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# *(Not important) TODO: if wait too long, refresh the driver
SLEEP_TIME = 0
PAR_SLEEP_TIME = 0
FILE_NAME = "auction.csv"
HTML = "https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.23.10753e1f1cgkra&auction_source=0" \
       "&city=&province=&st_param=-1&auction_start_seg=-1"

### Driver set up
desired_capabilities = DesiredCapabilities.CHROME
desired_capabilities["pageLoadStrategy"] = "none"
driver1 = webdriver.Chrome(desired_capabilities=desired_capabilities)
driver1.get(HTML)
wait = WebDriverWait(driver1, 20)
wait.until(EC.presence_of_element_located((By.XPATH, '//em[@class="count"]')))
print("found")
driver1.execute_script("window.stop();")


### Function designed
def get_auction_num() -> int:
    """

    *** Single operator ***

    :return:
    """
    auction_num = driver1.find_element_by_xpath('//em[@class="count"]').text

    return int(auction_num)


def click_type(index_: int) -> None:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="sf-filter J_Filter"]')))
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    if index_ == -1:
        type_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[0]  # Checked
        type_.find_element_by_tag_name("a").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//em[@class="count"]')))
        # print("type found")
        driver1.execute_script("window.stop();")

    else:
        types_ = select_filter_.find_elements_by_xpath('//ul[@class="condition"]')[0].find_elements_by_tag_name(
            "em")  # Checked
        types_[index_].click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//em[@class="count"]')))
        # print("type found")
        driver1.execute_script("window.stop();")


def click_location(index_: int) -> None:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="sf-filter J_Filter"]')))
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    if index_ == -1:
        location_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[1]  # Checked
        location_.find_element_by_tag_name("a").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//em[@class="count"]')))
        # print("location found")
        driver1.execute_script("window.stop();")

    else:
        locations_ = select_filter_.find_elements_by_xpath('//ul[@class="condition"]')[1]
        li_ = locations_.find_elements_by_xpath('//li[@class ="triggle"]')
        li_[index_].click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//em[@class="count"]')))
        # print("location found")
        driver1.execute_script("window.stop();")


def click_status(index_: int) -> None:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="sf-filter J_Filter"]')))
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    if index_ == -1:
        status_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[2]  # Checked
        status_.find_element_by_tag_name("a").click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//em[@class="count"]')))
        # print("status found")
        driver1.execute_script("window.stop();")

    else:
        status_ = select_filter_.find_elements_by_xpath('//ul[@class="condition"]')[-1].find_elements_by_tag_name(
            "em")  # Checked
        status_[index_].click()
        wait.until(EC.presence_of_element_located((By.XPATH, '//em[@class="count"]')))
        # print("status found")
        driver1.execute_script("window.stop();")


def click_back_type() -> None:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="sf-filter J_Filter"]')))
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    type_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[0]  # Checked
    type_.find_element_by_tag_name("a").click()
    time.sleep(SLEEP_TIME)


def click_back_location() -> None:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="sf-filter J_Filter"]')))
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    location_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[1]  # Checked
    location_.find_element_by_tag_name("a").click()
    time.sleep(SLEEP_TIME)


def click_back_status() -> None:
    wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="sf-filter J_Filter"]')))
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    status_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[2]  # Checked
    status_.find_element_by_tag_name("a").click()
    time.sleep(SLEEP_TIME)


### Open the csv file
f = open(FILE_NAME, "w", encoding="utf8")
f.write("Type, Location, Status, Num" + "\n")

# Due to the design of the web, each click will cause refresh thus needing to find the link again.
select_filter = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
types, locations = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[:2]
status = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[-1]

types_num = len(types.find_elements_by_tag_name("em"))
locations_num = len(locations.find_elements_by_xpath('//li[@class ="triggle"]'))
status_num = len(status.find_elements_by_tag_name("em"))

### Data collection
for i in range(1, types_num):
    click_type(i)
    for j in range(-1, locations_num):
        click_location(j)
        time.sleep(PAR_SLEEP_TIME)
        for k in range(-1, status_num):
            click_status(k)

            select_filter = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
            types, locations = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[:2]
            status = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[-1]

            if i == -1:
                type_str = "不限,"
            else:
                type_str = types.find_elements_by_tag_name('li')[i].find_element_by_tag_name("a").text + ","
            if j == -1:
                location_str = "不限,"
            else:
                full_str = locations.find_element_by_xpath('//li[@class="triggle unfold "]').find_element_by_tag_name(
                    "a").text
                location_str = full_str[:full_str.find("\n")] + ","
            if k == -1:
                status_str = "不限,"
            else:
                status_str = status.find_elements_by_tag_name('li')[k].find_element_by_tag_name("a").text + ","

            print(type_str + location_str + status_str + str(get_auction_num()))
            f.write(type_str + location_str + status_str + str(get_auction_num()) + "\n")
        click_back_location()
        time.sleep(PAR_SLEEP_TIME)
        click_back_status()
        time.sleep(PAR_SLEEP_TIME)
    # click_back_type()

f.close()

if __name__ == "__main__":
    pass
