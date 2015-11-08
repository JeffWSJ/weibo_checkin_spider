#coding=utf-8
import weibo
import json

APP_KEY = 'XXXXXXXXXXXXXX'#在新浪申请一个APP
APP_SECRET = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'
def run():
        client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)
        auth_url = client.get_authorize_url()
        print "auth_url : " + auth_url
        code = raw_input("input the retured code : ")
        r = client.request_access_token(code)
        client.set_access_token(r.access_token, r.expires_in)
        lat_long_file = open("poi.txt","r")
        cache = []#缓存以确保不重复
        for lines in lat_long_file:
                try:
                        checkin_num = 0
                        title = None
                        lat_long = lines.strip("\n").split(",")
                        longitude = lat_long[0]
                        latitude = lat_long[1]
                        poi_result = str(client.place.nearby.pois.get(lat=latitude,long=longitude))#返回附近多个poi点的信息
                        poi_list = eval(poi_result)
                        poi_string = json.dumps(poi_list)
                        poi_json = json.loads(poi_string)
                        for i in range(0,len(poi_json["pois"])):#把附近所有的poi点都遍历一遍
                                if poi_json["pois"][i]["poiid"] in cache:
                                        pass
                                else:
                                        poi_id = poi_json["pois"][i]["poiid"]
                                        cache.append(poi_id)
                                        checkin_result=str(client.place.pois.show.get(poiid=poi_id))
                                        checkin_list = eval(checkin_result)
                                        checkin_string = json.dumps(checkin_list)
                                        checkin_json = json.loads(checkin_string)
                                        checkin_num = checkin_json["checkin_num"]#签到数
                                        lon = checkin_json["lon"]#经度
                                        lat = checkin_json["lat"]#纬度
                                        title = checkin_json["title"]#地点名称
                                        if checkin_num !=0 and title != None:
                                                print "%s\t%s\t%s\t%s"%(lon,lat,checkin_num,title)
                except:
                        print "ERROR!!!!"

if __name__ == "__main__":
	run()
