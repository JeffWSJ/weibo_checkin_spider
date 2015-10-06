#coding=utf-8
import urllib2
for i in range(1,866,10):
	url1="http://www.poi86.com/poi/amap/district/530114/"+str(i)+".html"
	try:
		page1=urllib2.urlopen(url1)
	except:
		pass
	if page1:
		text1=page1.read()
		if "<td>" in text1 and "</td>" in text1:
			text1=text1[text1.index("<td>"):text1.index("</td>")]
			if "a href=" in text1:
				url2="http://www.poi86.com"+text1[text1.index("a href=")+8:text1.index("html")+4]
				try:
					page2=urllib2.urlopen(url2)
				except:
					pass
				if page2:
					text2=page2.read()
					if "火星坐标" in text2 and "百度坐标" in text2:
						text2=text2[text2.index("火星坐标"):text2.index("百度坐标")]
						if "</span>" in text2 and "</li>" in text2:
							poi=text2[text2.index("</span>")+8:text2.index("</li>")]
							print poi
