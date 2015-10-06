#coding=utf-8
import weibo,glob
import json

APP_KEY = '3445172026'
APP_SECRET = '577a0175b54ee77ed70d191348f116a6'
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'
def run():
        client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)
        auth_url = client.get_authorize_url()
        print "auth_url : " + auth_url
        code = raw_input("input the retured code : ")
        r = client.request_access_token(code)
        client.set_access_token(r.access_token, r.expires_in)
        lat_long_file = open("poi.txt","r")
        i = 0
        cache = []
        for i in range (303):
                try:
                        checkin_num = 0
                        title = None
                        lat_long = lat_long_file.readline().strip("\n").split(",")
                        longitude = lat_long[0]
                        latitude = lat_long[1]
                        poi_result = str(client.place.nearby.pois.get(lat=latitude,long=longitude))
                        poi_list = eval(poi_result)
                        poi_string = json.dumps(poi_list)
                        poi_json = json.loads(poi_string)
                        if poi_json["pois"][0]["poiid"] in cache:
                                pass
                        else:
                                poi_id = poi_json["pois"][0]["poiid"]
                                cache.append(poi_id)
                                checkin_result=str(client.place.pois.show.get(poiid=poi_id))
                                checkin_list = eval(checkin_result)
                                checkin_string = json.dumps(checkin_list)
                                checkin_json = json.loads(checkin_string)
                                checkin_num = checkin_json["checkin_user_num"]
                                title = checkin_json["title"]
                                if checkin_num !=0 and title != None:
                                        print "%s\t%s\t%s\t%s"%(longitude,latitude,checkin_num,title)
                except:
                        pass

if __name__ == "__main__":
	run()
