import requests
import json
import csv

data=[] # final data
d={} # every resturant value
menu_dict={}
i=0 # every resturant key in dictionary

with open('restaurant_links.txt', 'r') as f: #text file containing the URLS
    for url in f:
        res_url = url.rstrip('\n')
        response = requests.get(res_url)
        text = json.dumps(response.json(), sort_keys=False, indent=4) # create a formatted string of the Python JSON object
        info=json.loads(text)
        menu_url = 'https://www.delino.com/restaurant/menu/'+info['id']
        menu_response = requests.get(menu_url)
        menu_text = json.dumps(menu_response.json(), sort_keys=False, indent=4)
        menu_info=json.loads(menu_text)
        menu_data=[]
        for i in range(0,len(menu_info['categories'])):
            for j in range(0,len(menu_info['categories'][i]['sub'])):
                for z in range(0,len(menu_info['categories'][i]['sub'][j]['food'])):
                    title=menu_info['categories'][i]['sub'][j]['food'][z]['title']
                    price=menu_info['categories'][i]['sub'][j]['food'][z]['price']
                    ingredient=menu_info['categories'][i]['sub'][j]['food'][z]['ingredient'].strip()
                    menu_dict[i+1*j+1*z+1]={'title':title, 'price':price,'ingredient':ingredient}
                    menu_data.append(menu_dict[i+1*j+1*z+1])
        d[i]={'id':info['id'],'name':info['name'],'cityId':info['cityId'],'address':info['address'],
           'rate':info['rate'],'fullAddress':info['fullAddress'],'rateCount':info['rateCount'],
           'deliveryDuration':info['deliveryDuration'],'typeId':info['complexTypeId'],'menu':menu_data}
        data.append(d[i])
        i+=1
        
# save data to csv file
csv_data = "delino_api_data_csv.csv"
data_headers = [
    "id","name","cityId","address","rate","fullAddress","rateCount","deliveryDuration","typeId","menu"
]

with open(csv_data , 'w', newline='', encoding="utf-8") as ff :
    writer = csv.DictWriter(ff, data_headers)
    writer.writeheader()
    writer.writerows(data)
