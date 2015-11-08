#coding=utf-8
import urllib2
poi_file=open("poi.txt","a")
for i in range(1,866):#五华区的poi点数据共11页
        url1="http://www.poi86.com/poi/amap/district/530102/"+str(i)+".html"#五华区的poi点数据的网址
        try:
                page1=urllib2.urlopen(url1)
        except:
                pass
        if page1:
                text1=page1.read()
                for j in range(0,50):#每页50条数据
                        if "<td><a href=" in text1 and "</a></td>" in text1:  
                                text1=text1[text1.index("<td><a href=")+1:]
                                text1_1=text1[text1.index("<td><a href=")+13:]
                                url2="http://www.poi86.com"+text1_1[:text1_1.index("html")+4]
                                try:
                                        page2=urllib2.urlopen(url2)
                                except:
                                        pass
                                if page2:
                                        text2=page2.read()
                                        if "火星坐标" in text2 and "百度坐标" in text2:
                                                text2=text2[text2.index("火星坐标"):text2.index("百度坐标")]
                                                if "</span>" in text2 and "</li>" in text2:
                                                        poi=text2[text2.index("</span>")+8:text2.index("</li>")]+"\n"
                                                        poi_file.write(poi)
        print i
poi_file.flush()
poi_file.close()
