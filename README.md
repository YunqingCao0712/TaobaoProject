# TaoBao Project
A simple web scrapping project to collect auction number from [AliBaba](https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.19.59367ddapTeyuA&category=122406001&auction_source=0&st_param=-1&auction_start_seg=-1)
website in terms of types, locations and status.

## Set Up 
This is temporarily only adaptable for Google Chrome user. And to successfully
run the project, you may:
    
1. Get your google Chrome version from Google Chrome > ... > help(E) > about..(G).
2. Refer to [ChromeDriver - WebDriver for Chrome](https://chromedriver.chromium.org/downloads)
to download the ChromeDriver closed to your version in the directory of this project.
3. pip install selenium.
4. Run the [collector.py](collector.py).

* Note: for my convenience, this project has bundled with a chromedriver.exe at version 83.0.4103.61. If your
google Chrome is not the version as me, follow the step 2 to overwrite the chromedriver.exe.

## Potential Problems
Due to the property of [AliBaba](https://sf.taobao.com/item_list.htm?spm=a213w.7398504.filter.19.59367ddapTeyuA&category=122406001&auction_source=0&st_param=-1&auction_start_seg=-1) 
website designed structure, each auction number need at least one click to obtain. Therefore, to optimize this problem, 
this project use `wait.until` method to minimizing the collecting time.

However, due to the optimization operation and potentially unstable internet, one may occur web-element not found error.
To overcome this problem, this project temporally use `time.sleep` to wait for a while. By default, this project will 
wait for 2s for type selection only. In the future, we may formally fix this problem using `wait.until` covered by `try`
methods. 

For now, if any problems occurs above, adjust the default sleep time `SLEEP_TIME` in [collector](collector.py) to fit your
internet condition.  
