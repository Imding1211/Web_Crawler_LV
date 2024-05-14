# -*- coding: utf-8 -*-
"""
Created on Fri May  3 00:19:18 2024

@author: a0986
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import os

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

url = 'https://fr.louisvuitton.com/fra-fr/produits/sac-side-trunk-mm-h27-nvprod5280038v/M25160'
url = 'https://fr.louisvuitton.com/fra-fr/produits/sac-side-trunk-mm-monogram-reverse-canvas-nvprod5400003v/M47202'
url = 'https://kr.louisvuitton.com/kor-kr/products/side-trunk-mm-crocodilien-mat-nvprod4650092v/N83000'

screen_shot_img(url)
