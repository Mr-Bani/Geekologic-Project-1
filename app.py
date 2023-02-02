import requests
import csv




# url_to_data_api : "https://www.delino.com/restaurant/data/dey-fried-chicken-motahari"
# url_to_menu_api : https://www.delino.com/restaurant/menu/e695c5db-f227-4450-ba84-d6a47371b0d5

# Some url as a sample to test codes
url_restaurants = [
    "https://www.delino.com/restaurant/kfs",
    "https://www.delino.com/restaurant/food-company",
    "https://www.delino.com/restaurant/gelatohouse",
    "https://www.delino.com/restaurant/visland",
    "https://www.delino.com/restaurant/seyedmehdi",
    "https://www.delino.com/restaurant/cafenafas",
    "https://www.delino.com/restaurant/dey-fried-chicken-motahari",
    "https://www.delino.com/restaurant/morshedcheloy",
    "https://www.delino.com/restaurant/seyedmehdi",
    "https://www.delino.com/restaurant/cafenafas",
    "https://www.delino.com/restaurant/dey-fried-chicken-motahari",
    "https://www.delino.com/restaurant/morshedcheloy",
    "https://www.delino.com/restaurant/gelatohouse",
    "https://www.delino.com/restaurant/visland",
    "https://www.delino.com/restaurant/heeva",
    "https://www.delino.com/restaurant/khoroos",
    "https://www.delino.com/restaurant/pizzahot-sohrevardi",
    "https://www.delino.com/restaurant/shemroon",
    "https://www.delino.com/restaurant/dar_be_dar",
    "https://www.delino.com/restaurant/burgerzoghali-zafar"
]

# Define a url as a base url 
base_url = "https://www.delino.com/restaurant/"

# Define a array to store menu url 
url_menu_restaurants = []

# Two global array to store all record and data, use for store in csv file
data_to_csv_rows = []
menu_to_csv_rows = []


# Get all data from Delino API for every restaurant
for i in range(len(url_restaurants)) :
    url_split =  url_restaurants[i].split("https://www.delino.com/restaurant/")

    # Create url for every restaurant and get data in json format
    url_to_data_api = base_url + "data/" + url_split[1]
    data_payload = requests.get(url_to_data_api)
    data_json = data_payload.json()
    
    # Create menu url of every restaurant
    url_to_menu_api = base_url + "menu/" + data_json['id']
    url_menu_restaurants.append(url_to_menu_api)

    # Define a dictionary to store fetched data from api
    data_row = {}

    # Store fetched data in dictionary
    data_row['id'] = data_json['id']
    data_row['domain'] = data_json['domain']
    data_row['name'] = data_json['name']
    data_row['online'] = data_json['online']
    data_row['offlineText'] = data_json['offlineText']
    data_row['branch'] = data_json['branch']
    data_row['address'] = data_json['address']
    data_row['address'] = data_json['address']
    data_row['logo'] = data_json['logo']
    data_row['cover'] = data_json['cover']
    data_row['discount'] = data_json['discount']
    data_row['newDiscount'] = data_json['newDiscount']
    data_row['mealTime'] = data_json['mealTime']
    data_row['brand'] = data_json['brand']
    data_row['lat'] = data_json['lat']
    data_row['lng'] = data_json['lng']
    data_row['fullAddress'] = data_json['fullAddress']
    data_row['compactMenu'] = data_json['compactMenu']
    data_row['about'] = data_json['about']
    data_row['deliveryTime'] = data_json['deliveryTime']
    data_row['inRamadan'] = data_json['inRamadan']
    data_row['serviceOnRamadan'] = data_json['serviceOnRamadan']
    data_row['restaurantType'] = data_json['restaurantType']
    data_row['rate'] = data_json['rate']
    data_row['rateCount'] = data_json['rateCount']
    data_row['priceRate'] = data_json['priceRate']
    data_row['reviewCount'] = data_json['reviewCount']
    data_row['deliveryDuration'] = data_json['deliveryDuration']
    data_row['cookingDuration'] = data_json['cookingDuration']
    data_row['areaId'] = data_json['areaId']
    data_row['cityId'] = data_json['cityId']
    data_row['complexTypeId'] = data_json['complexTypeId']

    # Store all data in a list to write in csv file
    data_to_csv_rows.append(data_row)



# Fetch menu data from api
for i in range(len(url_menu_restaurants)) :

    # Create url menu for every restaurant and get menu data in json format
    menu_payload = requests.get(url_menu_restaurants[i])
    menu_json_ = menu_payload.json()

    # Split restaurant id from urls to store in csv file
    restaurant_id =  url_menu_restaurants[i].split("https://www.delino.com/restaurant/menu/")

    menu_json = []
    menu_rows = []

    # Take categories data
    for item in menu_json_['categories'] :
        menu_json.append(item)

    # Get general data about category
    for i in range(len(menu_json)):
        menu_row = {}

        menu_row['id'] = menu_json[i]['id']
        menu_row['restaurant_id'] = restaurant_id[1]
        menu_row['title'] = menu_json[i]['title']
        menu_row['logo'] = menu_json[i]['logo']
        menu_row['cover'] = menu_json[i]['cover']
        menu_row['compact'] = menu_json[i]['compact']
        menu_row['forRamadan'] = menu_json[i]['forRamadan']
        menu_row['forHalfReady'] = menu_json[i]['forHalfReady']
        menu_row['index'] = menu_json[i]['index']
        menu_row['isActive'] = menu_json[i]['isActive']
        menu_row['type'] = menu_json[i]['type']

        # Get sub in category, It's contain some data about food and others
        menu_row_sub = menu_json[i]['sub']

        menu_row['sub_id'] = menu_row_sub[0]['id']
        menu_row['sub_title'] = menu_row_sub[0]['title']
        menu_row['sub_description'] = menu_row_sub[0]['description']
        menu_row['sub_img'] = menu_row_sub[0]['img']
        menu_row['sub_priceLabel'] = menu_row_sub[0]['priceLabel']
        menu_row['sub_index'] = menu_row_sub[0]['index']

        # Get foods data, It's in sub item
        menu_row_sub_food = menu_row_sub[0]['food']

        menu_food_row = {}

        for i in range(len(menu_row_sub_food)) :

            menu_food_row['sub_food_img'] = menu_row_sub_food[i]['img'] 
            menu_food_row['sub_food_id'] = menu_row_sub_food[i]['id'] 
            menu_food_row['sub_food_archive'] = menu_row_sub_food[i]['archive'] 
            menu_food_row['sub_food_ingredient'] = menu_row_sub_food[i]['ingredient'] 
            menu_food_row['sub_food_title'] = menu_row_sub_food[i]['title'] 
            menu_food_row['sub_food_stock'] = menu_row_sub_food[i]['stock'] 
            menu_food_row['sub_food_available'] = menu_row_sub_food[i]['available'] 
            menu_food_row['sub_food_unavailableText'] = menu_row_sub_food[i]['unavailableText'] 
            menu_food_row['sub_food_price'] = menu_row_sub_food[i]['price'] 
            menu_food_row['sub_food_discount'] = menu_row_sub_food[i]['discount'] 
            menu_food_row['sub_food_discountPercentage'] = menu_row_sub_food[i]['discountPercentage'] 
            menu_food_row['sub_food_index'] = menu_row_sub_food[i]['index'] 
            menu_food_row['sub_food_foodTag'] = menu_row_sub_food[i]['foodTag'] 
            menu_food_row['sub_food_saleOnRamadan'] = menu_row_sub_food[i]['saleOnRamadan'] 
            menu_food_row['sub_food_saleOnBreakfast'] = menu_row_sub_food[i]['saleOnBreakfast'] 
            menu_food_row['sub_food_saleOnNoon'] = menu_row_sub_food[i]['saleOnNoon'] 
            menu_food_row['sub_food_saleOnNight'] = menu_row_sub_food[i]['saleOnNight'] 
            menu_food_row['sub_food_saturday'] = menu_row_sub_food[i]['saturday'] 
            menu_food_row['sub_food_sunday'] = menu_row_sub_food[i]['sunday'] 
            menu_food_row['sub_food_monday'] = menu_row_sub_food[i]['monday'] 
            menu_food_row['sub_food_tuesday'] = menu_row_sub_food[i]['tuesday'] 
            menu_food_row['sub_food_wedensday'] = menu_row_sub_food[i]['wedensday'] 
            menu_food_row['sub_food_thursday'] = menu_row_sub_food[i]['thursday'] 
            menu_food_row['sub_food_friday'] = menu_row_sub_food[i]['friday'] 
            menu_food_row['sub_food_delinoRecommendation'] = menu_row_sub_food[i]['delinoRecommendation'] 
            menu_food_row['sub_food_halfReady'] = menu_row_sub_food[i]['halfReady'] 
            menu_food_row['sub_food_pickupOnly'] = menu_row_sub_food[i]['pickupOnly'] 

            # Join general data from category with every food that exist in category and add restaurant id for identification
            row_to_csv = {**menu_row , **menu_food_row}
            menu_to_csv_rows.append(row_to_csv)

# Create data header
data_headers = [
    "id","domain","name","online","offlineText", "branch","address","logo","cover","discount","newDiscount","mealTime","brand","lat","lng","fullAddress",
    "compactMenu","about","deliveryTime","inRamadan","serviceOnRamadan","restaurantType","rate","rateCount","priceRate","reviewCount","deliveryDuration",
    "cookingDuration","areaId","cityId","complexTypeId"
    ]

# Create menu header
menu_headers = ["id","restaurant_id","title", "logo","cover","compact","forRamadan","forHalfReady","index","isActive","type","sub_id" , 
                "sub_id","sub_title", "sub_description","sub_img","sub_priceLabel","sub_index","sub_food_id","sub_food_img","sub_food_archive","sub_food_ingredient",
                "sub_food_title","sub_food_stock", "sub_food_available","sub_food_unavailableText","sub_food_price","sub_food_discount","sub_food_discountPercentage",
                "sub_food_index","sub_food_foodTag", "sub_food_saleOnRamadan","sub_food_saleOnBreakfast","sub_food_saleOnNoon","sub_food_saleOnNight",
                "sub_food_saturday","sub_food_sunday", "sub_food_monday","sub_food_tuesday","sub_food_wedensday","sub_food_thursday",
                "sub_food_thursday","sub_food_friday", "sub_food_delinoRecommendation", "sub_food_halfReady","sub_food_pickupOnly"
                ]

# CSV file name
csv_data = "delino_api_data_csv.csv"
csv_menu = "delino_api_menu_csv.csv"


# Write data in csv file 

with open(csv_data , 'w', newline='', encoding="utf-8") as f :
    writer = csv.DictWriter(f, data_headers)
    writer.writeheader()
    for data_row in data_to_csv_rows :
        writer.writerow(data_row)

with open(csv_menu , 'w', newline='', encoding="utf-8") as f :
    writer = csv.DictWriter(f, menu_headers)
    writer.writeheader()
    for menu_row in menu_to_csv_rows :
        writer.writerow(menu_row)