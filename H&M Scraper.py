# !conda install selenium
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date, datetime
from IPython.display import display, HTML
from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# https://www2.hm.com/robots.txt

####################################################################################################

def make_initial_request(initial_search_url, ua):

    initial_request = requests.get(
        initial_search_url',
        headers={'User-Agent': ua}
    )

    ir_status_code = initial_request.status_code
    print(f"Status Code: {ir_status_code}")

    initial_request_soup = BeautifulSoup(initial_request.text, 'html.parser')
    initial_request_soup_type = type(initial_request_soup)
    print(f"Soup Type: {initial_request_soup_type}")

    return ir_status_code

####################################################################################################

def get_item_urls():

    url_request = requests.get(next_initial_search_url, headers=headers)
    url_request_soup = BeautifulSoup(url_request.text, 'html.parser')
    urls = url_request_soup.findAll('a')
    section_urls = ['https://www2.hm.com' + url.get('href','') for url in urls
                    if 'Toggle submenu for the' in url.get('data-deparment-toggle-text','')
                    and 'deparment' in url.get('data-deparment-toggle-text','')
                    and 'Go to' in url.get('data-goto-text','')
                    and 'home' in url.get('data-goto-text','')]
    section_url_list = list(dict.fromkeys(section_urls))

    print(f'''{len(section_url_list)} section urls:
    {section_url_list}
    ''')

    section_url_list.remove('https://www2.hm.com/en_gb/ladies.html')
    section_url_list.remove('https://www2.hm.com/en_gb/divided.html')
    section_url_list.remove('https://www2.hm.com/en_gb/kids.html')
    section_url_list.remove('https://www2.hm.com/en_gb/home.html')
    section_url_list.remove('https://www2.hm.com/en_gb/sale.html')
    section_url_list.remove('https://www2.hm.com/en_gb/sustainability.html')

    print(f'''{len(section_url_list)} section urls:
    {section_url_list}''')

    ####################################################################################################

    item_urls_list_total = []
    urls_lol = []

    for section_url in section_url_list[0:1]:
        section_url_request = requests.get(section_url, headers=headers)
        section_url_request_soup = BeautifulSoup(section_url_request.text, 'html.parser')
        section_url_request_soup_a = section_url_request_soup.findAll('a')
        dept_urls_list = ['https://www2.hm.com' + dept_url.get('href','') for dept_url in section_url_request_soup_a
                          if 'link' in dept_url.get('class','')
                          and 'menuitem' in dept_url.get('role','')]
        dept_urls_list += list(dict.fromkeys(dept_urls_list))
        print('')
        print(f'''{len(dept_urls_list)} department urls in {section_url} section
        ''')
        sleep(1)

        for dept_url in dept_urls_list[0:1]:
            print(dept_url)
            products_count_request = requests.get(dept_url, headers=headers)
            products_count_request_soup = BeautifulSoup(products_count_request.text, 'html.parser')
            products_count_request_soup_a = products_count_request_soup.findAll('div')
            products_count = [count.text for count in products_count_request_soup_a
                              if 'filter-pagination' in count.get('class','')]
            sleep(0.5)

            try:
                products_count_str = products_count[0]
                products_count_value =  [int(s) for s in products_count_str.split() if s.isdigit()]
                products_count_num = int(products_count_value[0])
            except:
                products_count_num = 1

            item_spots = ((products_count_num // 36) + 1) * 36

            print(f'''{products_count_num}:{item_spots} item spots occupied''')

            page_no_suffix = '?sort=stock&image-size=small&image=model&offset=0&page-size=' + str(item_spots)
            dept_url_page = dept_url + page_no_suffix
            print(dept_url_page)
            dept_url_request = requests.get(dept_url_page, headers=headers)
            dept_url_request_soup = BeautifulSoup(dept_url_request.text, 'html.parser')
            dept_url_request_soup_a = dept_url_request_soup.findAll('a')
            item_urls_list = [item_url.get('href','') for item_url in dept_url_request_soup_a
                              if 'link' in item_url.get('class','')
                              and 'productpage.' in item_url.get('href','')]
            item_urls_list = list(dict.fromkeys(item_urls_list))
            item_urls_list_new = ['https://www2.hm.com' + url for url in item_urls_list]
            item_urls_list_total += item_urls_list_new

            for item_url_new in item_urls_list_new:

                record = {
                    'section_url'   : section_url,
                    'dept_url'      : dept_url,
                    'dept_url_page' : dept_url_page,
                    'item_url'      : item_url_new
                }

                urls_lol.append(record)

            sleep(0.05)
            print(f'''{len(urls_lol)} item urls scraped''')

    urls_df_filepath = 'D:/Yourdrobe/hm_urls_df.csv'

    urls_df = pd.DataFrame(urls_lol)

    urls_df.to_csv(urls_df_filepath, index=False)
    print(f'Written to {urls_df_filepath}')
    display(HTML(urls_df.head(200).to_html()))

    return urls_lol

####################################################################################################

def get_item_data(urls_lol):

    item_data = []

    for urls in urls_lol[0:5]:

        item_url = urls['item_url'].replace('https://www2.hm.com','')

        item_url_request = requests.get(urls['item_url'], headers=headers)
        item_url_request_soup = BeautifulSoup(item_url_request.text, 'html.parser')

        html_h1 = item_url_request_soup.findAll('h1')
    #     print(html_h1)
    #     itemnumber_list = [url.get('data-itemnumber','') for url in html_div if len(url.get('data-itemnumber','')) == 6]
    #     itemnumber = itemnumber_list[0]
    #     itemno = itemnumber[:3] + '-' + itemnumber[3:]

    #     html_article = item_url_request_soup.findAll('article')

    #     id_list = [url.get('id','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     id_ = id_list[0]

    #     styleid_list = [url.get('data-styleid','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     styleid = styleid_list[0]

    #     targetitem_list = [url.get('data-targetitem','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     targetitem = targetitem_list[0]

    #     stylenumber_list = [url.get('data-stylenumber','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     stylenumber = stylenumber_list[0]

        itemname_list = [url.text for url in html_h1 if 'primary' in url.get('class','')
                                                    and 'product-item-headline' in url.get('class','')]
    #     print(itemname_list)
        itemname = itemname_list[0].strip()

    #     department_list = [url.get('data-department','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     department = department_list[0]

        html_a = item_url_request_soup.findAll('a')
        colour_list = [url.get('data-color','') for url in html_a if url.get('href','') == item_url]
        colour = colour_list[1]

    #     for entry in colour_list:
    #         if len(entry) > 0:
    #             colour = entry
    #             break

    #     brand_list = [url.get('data-brand','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     brand = brand_list[0]

    #     category_list = [url.get('data-category','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     category = category_list[0]

    #     class_list = [url.get('class','') for url in html_article if url.get('data-targetitem','') == itemno]
    #     class_ = class_list[0]

    #     html_option = item_url_request_soup.findAll('option')

        html_span = item_url_request_soup.findAll('span')
        price_list = [url.text for url in html_span if 'price-value' in url.get('class','')]
        price = price_list[0].strip()

        record = {
            'section_url'   : urls['section_url'],
            'dept_url'      : urls['dept_url'],
            'dept_url_page' : urls['dept_url_page'],
            'item_url'      : urls['item_url'],
            'item_name'     : itemname,
            'colour'        : colour,
            'price'         : price,
        }

        item_data.append(record)
        print(record)
        sleep(5)

    item_data_df = pd.DataFrame(item_data)

    item_data_df.to_csv('D:/Yourdrobe/H&M.csv', index=False)
    print('Written to D:/Yourdrobe/H&M.csv')
    display(HTML(item_data_df.head(200).to_html()))

    return item_data_df

initial_search_url = 'https://www2.hm.com/en_gb/index.html'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

ir_status_code = make_initial_request(initial_search_url, ua)
urls_lol = get_item_urls()
item_data_df = get_item_data(urls_lol)
