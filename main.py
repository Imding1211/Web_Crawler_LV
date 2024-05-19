
from function import *

urls = ['https://tw.louisvuitton.com/zht-tw/search/Side%20Trunk',
        'https://jp.louisvuitton.com/jpn-jp/search/Side%20Trunk',
        'https://kr.louisvuitton.com/kor-kr/search/Side%20Trunk',
        'https://hk.louisvuitton.com/eng-hk/search/Side%20Trunk',
        'https://fr.louisvuitton.com/fra-fr/rechercher/Side%20Trunk',]
    
countrys = ['Taiwan', 'Japan', 'Korean', 'Hong Kong', 'France']

product_data = {}

for url, country in zip(urls, countrys):

    print(f'{country} start~')

    products_id, products_name, products_price, products_url = get_info(url)

    product_data = convert_dict(product_data, country, products_id, products_name, products_price, products_url)

    print(f'{country} done!!')

generate_html(product_data)

#ouput_excel(product_data, countrys, 'lv side trunk.xlsx')

#ouput_json(product_data, 'product_data.json')
