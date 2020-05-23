import time
from selenium import webdriver

# import os
# os.chdir('C:\\Users\\wangt\\Desktop\\PythonProjects\\TaoBao_Project')

HTML = "https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.23.10753e1f1cgkra&auction_source=0" \
       "&city=&province=&st_param=-1&auction_start_seg=-1"

driver1 = webdriver.Chrome()
driver1.get(HTML)

# Obtain the auction num
def get_auction_num() -> int:
    """

    *** Single operator ***

    :return:
    """
    target_row_ = driver1.find_element_by_xpath('//div[@class="sf-scroll-fixed"]')
    auction_num = target_row_.find_element_by_tag_name("em").text

    return int(auction_num)

def click_type(index_: int) -> None:
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    if index_ == -1:
        type_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[0]  # Checked
        type_.find_element_by_tag_name("a").click()
    else:
        types_ = select_filter_.find_elements_by_xpath('//ul[@class="condition"]')[0].find_elements_by_tag_name("em")  # Checked
        types_[index_].click()
    print("click type")

def click_location(index_: int) -> None:
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    if index_ == -1:
        location_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[1]  # Checked
        location_.find_element_by_tag_name("a").click()
    else:
        locations_ = select_filter_.find_elements_by_xpath('//ul[@class="condition"]')[1]
        li_ = locations_.find_elements_by_xpath('//li[@class ="triggle"]')
        li_[index_].click()
    print("click location")

def click_status(index_: int) -> None:
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    if index_ == -1:
        status_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[2]  # Checked
        status_.find_element_by_tag_name("a").click()
    else:
        status_ = select_filter_.find_elements_by_xpath('//ul[@class="condition"]')[-1].find_elements_by_tag_name("em")  # Checked
        status_[index_].click()
    print("click status")

def click_back_type() -> None:
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    type_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[0]  # Checked
    type_.find_element_by_tag_name("a").click()

def click_back_location() -> None:
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    location_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[1]  # Checked
    location_.find_element_by_tag_name("a").click()
    time.sleep(2)

def click_back_status() -> None:
    select_filter_ = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
    status_ = select_filter_.find_elements_by_xpath('//div[@class="unlimited"]')[2]  # Checked
    status_.find_element_by_tag_name("a").click()


f = open("test.csv", "w", encoding="utf8")
f.write("Type, Location, Status, Num")
# Due to the design of the web, each click will cause refresh thus needing to find the link again.
select_filter = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
types, locations = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[:2]
status = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[-1]

types_num = len(types.find_elements_by_tag_name("em"))
locations_num = len(locations.find_elements_by_xpath('//li[@class ="triggle"]'))
status_num = len(status.find_elements_by_tag_name("em"))

# ### 3 unlimited
# f.write("不限,不限,不限," + str(get_auction_num()) + "\n")
#
# ### 2 unlimited
# # Type
# for i in range(types_num):
#     click_type(i)
#     select_filter = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
#     types, locations, sub_locations, status = select_filter.find_elements_by_xpath('//ul[@class="condition"]')
#     type_str = types.find_element_by_tag_name('li').find_element_by_tag_name("a").text + ","
#     f.write(type_str + "不限,不限," + str(get_auction_num()) + "\n")
#
# # Location
# for j in range(locations_num):
#     click_location(j)
#     select_filter = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
#     types, locations, sub_locations, status = select_filter.find_elements_by_xpath('//ul[@class="condition"]')
#     full_str = locations.find_element_by_xpath('//li[@class="triggle unfold "]').find_element_by_tag_name("a").text
#     location_str = full_str[:full_str.find("\n")] + ","
#     f.write("不限," + location_str + "不限," + str(get_auction_num()) + "\n")
#
# # Status
# for k in range(status_num):
#     click_status(k)
#     select_filter = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
#     types, locations, sub_locations, status = select_filter.find_elements_by_xpath('//ul[@class="condition"]')
#     status_str = status.find_elements_by_tag_name('li')[k].find_element_by_tag_name("a").text + ","
#     f.write("不限,不限," + status_str + str(get_auction_num()) + "\n")
#
# # TODO: For 1 unlimited, replicate the similar code above

### 0 unlimited
for i in range(-1,types_num):
    click_type(i)
    for j in range(-1, locations_num):
        click_location(j)
        for k in range(-1, status_num):
            click_status(k)

            select_filter = driver1.find_element_by_xpath('//div[@class="sf-filter J_Filter"]')
            types, locations = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[:2]
            status = select_filter.find_elements_by_xpath('//ul[@class="condition"]')[-1]

            if i == -1:
                type_str = "不限,"
            else:
                type_str = types.find_element_by_tag_name('li').find_element_by_tag_name("a").text + ","
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
            # f.write(type_str + location_str + status_str + str(get_auction_num()) + "\n")

        click_back_location()
    # click_back_type()


if __name__ == "__main__":
    pass
