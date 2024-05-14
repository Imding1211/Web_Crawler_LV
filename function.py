# -*- coding: utf-8 -*-
"""
Created on Fri May  3 00:19:18 2024

@author: a0986
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import openpyxl
import os

#=============================================================================#

def get_info(url):
    
    home_page = '/'.join(url.split('/')[0:3])
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    html = driver.page_source
    
    driver.quit()
    
    soup = BeautifulSoup(html, "lxml")
    
    products_id_url_element = soup.select('a.lv-smart-link.lv-product-card__url')
    products_price_element = soup.select('span.notranslate')
    
    products_id    = []
    products_name  = []
    products_price = []
    products_url   = []
    
    for product_id_url_element, product_price_element in zip(products_id_url_element, products_price_element):
        
        product_id = product_id_url_element["href"].split('/')[-1]
        products_id.append(product_id)
        
        product_name = product_id_url_element.text.replace('\n','').strip()
        products_name.append(product_name)
        
        product_price = product_price_element.text
        products_price.append(product_price)
        
        product_url = home_page + product_id_url_element["href"]
        products_url.append(product_url)
        
        screen_shot_img(product_url)
        
        print(product_id, product_name, product_price, product_url)
        
    return products_id, products_name, products_price, products_url

#=============================================================================#

def screen_shot_img(url):
    
    product_id = url.split('/')[-1]
    path = './Side Trunk/'+product_id
    
    if not os.path.exists(path):
        
        os.mkdir(path)
    
        driver = webdriver.Chrome()
        driver.get(url)
    
        html = driver.page_source
    
        driver.quit()
    
        soup = BeautifulSoup(html, "lxml")
    
        products_img_element = soup.select('div.lv-product-page-header__media img')
        
        n = 0
        
        for product_img_element in products_img_element:
            
            n += 1
            
            try:
                img_url = product_img_element['srcset'].split(',')[0]
                
            except:
                try:
                    img_url = product_img_element['data-srcset'].split(',')[0]
                    
                except:
                    break
            
            screen_shot_driver = webdriver.Chrome()
            screen_shot_driver.implicitly_wait(3)
            screen_shot_driver.get(img_url)
            screen_shot_driver.save_screenshot(path + '/' + product_id +'-' + str(n) + '.png')
            screen_shot_driver.quit()
            
            print(f'Screen shot image {product_id}-{n}.')
    
    else:
        print(f'Image {product_id} already exist.')

#=============================================================================#

def convert_dict(product_data, country, products_id, products_name, products_price, products_url):

    for product_id, product_name, product_price, product_url in zip(products_id, products_name, products_price, products_url):
        
        if product_id not in product_data:
            product_data[product_id] = {}
            
        if country not in product_data[product_id]:
            product_data[product_id][country] = {}
        
        product_data[product_id][country]['Name']  = product_name
        product_data[product_id][country]['Price'] = product_price
        product_data[product_id][country]['url']   = product_url
            
    return product_data

#=============================================================================#

def ouput_excel(product_data, countrys, heads, excel_name):
    
    workbook = openpyxl.Workbook()
    
    sheet = workbook.worksheets[0]
    
    for index, head in enumerate(heads):
        sheet.cell(1, index+1).value = head
            
    for index, product_id in enumerate(product_data.keys()):
        
        sheet.cell(index+2, 1).value = product_id
        
        sheet.cell(index+2, 9).value = '、'.join(list(product_data[product_id]))
        
        for i, country in enumerate(countrys):
            
            if product_data[product_id].get(country) is not None:
                
                product_first_country = list(product_data[product_id])[0]
                
                sheet.cell(index+2, 2).value = product_data[product_id][product_first_country]['Name']
                
                sheet.cell(index+2, i+10).value = product_data[product_id][country]['Price']
                
                sheet.cell(index+2, i+10).hyperlink = product_data[product_id][country]['url']
                sheet.cell(index+2, i+10).style = "Hyperlink"
    
    workbook.save(excel_name)
    
#=============================================================================#

if __name__ == '__main__':
    
    urls = ['https://tw.louisvuitton.com/zht-tw/search/Side%20Trunk',
            'https://jp.louisvuitton.com/jpn-jp/search/Side%20Trunk',
            'https://kr.louisvuitton.com/kor-kr/search/Side%20Trunk',
            'https://hk.louisvuitton.com/eng-hk/search/Side%20Trunk',
            'https://fr.louisvuitton.com/fra-fr/rechercher/Side%20Trunk',]
        
    countrys = ['Taiwan', 'Japan', 'Korean', 'Hong Kong', 'France']
    
    heads = ['商品編號', '名稱', '圖片一', '圖片二', '圖片三', '圖片四', '圖片五', '圖片六', '有販售國家', '台灣', '日本', '韓國', '香港', '法國']
    
    product_data = {}
    
    for url, country in zip(urls, countrys):
        
        print(f'{country} start~')
        
        products_id, products_name, products_price, products_url = get_info(url)
        
        product_data = convert_dict(product_data, country, products_id, products_name, products_price, products_url)
        
        print(f'{country} done!!')
        
    ouput_excel(product_data, countrys, heads, 'lv side trunk.xlsx')