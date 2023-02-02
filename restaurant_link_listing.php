<?php
//Tinker away!

use Illuminate\Support\Facades\Http;

$city_array = [1, 1003, 1005, 1007, 1008, 1009, 1011, 1012, 1013, 1015, 1033];

$myfile = fopen("/home/alibayat73/restaurant_links.txt", "w");
foreach ($city_array as $city_id) {
    $restaurants = Http::get("https://www.delino.com/restaurant/search/?city_id=$city_id&limit=1200&_=1675354211861");
    $result = $restaurants->object()->result;
    foreach ($result as $restaurant) {
        $restaurant_domain_name = $restaurant->domain;
        fwrite($myfile, "\nhttps://www.delino.com/restaurant/data/$restaurant_domain_name");
    }
}
fclose($myfile);
