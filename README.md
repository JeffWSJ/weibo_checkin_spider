# weibo_checkin_spider
It can get any places' weibo checkin number
1.在http://www.poi86.com/poi/amap/city/530100.html
获取昆明各POI点的经纬度，由于微博使用的是高德地图，而高德地图使用的是火星坐标，因此只需用爬虫获取各POI点的火星坐标即可。
2.利用微博API:place/nearby/pois可以获得某坐标附近的微博POI点的poiid
3.利用微博API:place/pois/show可以获得该poi点的微博签到人数


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/Jackeriss/weibo_checkin_spider/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

