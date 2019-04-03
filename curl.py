import re
import requests

def get_cookies(Cookie):
	return dict(line.split("=", 1) for line in Cookie.split("; "))

def curlgo(curl):
	#单引号转双引号
	curl=curl.replace("'",'"')

	#提取请求头
	tou =re.findall(r'-H \"(.*?)\"',curl)     
	#转换为字典  清掉空格         
	headers = dict([line.replace(" ","").split(":",1) for line in tou])

	#提取Cookie，删除请求头中的Cookie
	kee=headers.keys()
	if 'Cookie' in kee:
		Cookie = get_cookies(headers['Cookie'])
		headers.pop('Cookie')
	elif 'cookie' in kee:
		Cookie = get_cookies(headers['Cookie'.lower()])
		headers.pop('Cookie'.lower())

	#提取POST数据
	data =re.findall(r'-d "(.*?)"',curl)     

	#提取url
	n=len(curl)
	for x in range(n):
		if curl[x]=='h'and curl[x+1]=='t' and curl[x+2]=='t' and curl[x+3]=='p' and curl[x-1]=='"':
			url=''
			if '-H' not in curl[x-4:x-1] :
				for i in range(n-x):
					if curl[x+i]=='"' or curl[x+i]=="'" :
						break
					else:
						url=url+curl[x+i]


	#判断是POST还是GET
	if 'POST' in curl:	
		response = requests.post(url, headers=headers,cookies=Cookie,data=data[0])
	else:
		response = requests.get(url, headers=headers,cookies=Cookie)

	response.encoding = 'utf-8'
	print(response.text)




	print("\n\n=====================================上面是响应信息=====================================================================\n\n")
	print("\n\n=====================================下面是请求头的信息=====================================================================\n\n")
	print("url=============",url)
	print("headers=========",headers)
	print("Cookie==========",Cookie)
	print("data============",data)



if __name__ == '__main__':

	#单引号
	curl='curl "https://www.hao123.com/" -H "Connection: keep-alive" -H "Cache-Control: max-age=0" -H "Upgrade-Insecure-Requests: 1" -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" -H "DNT: 1" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" -H "Accept-Encoding: gzip, deflate, br" -H "Accept-Language: zh-CN,zh;q=0.9" -H "Cookie: BAIDUID=93A0DF2F98D4078ADE3556BE685E0D06:FG=1; BID=6C9F62FEB36133FA7742432163B4793B:FG=1; FLASHID=983B359CCB2F17A5E987AE0A7E36ABBD:FG=1; Hm_lvt_22661fc940aadd927d385f4a67892bc3=1539883693; narrow=0; HAOSTOKEN=5fe883792c7e5b14ad16fac27aff00997a1efb768b35a3f723b9cae95ec2e4bd; BDUSS=FUUTBLN1Nrd2FHOG1KZUZKWDZtQ1daOFRCaHZ2TWNwZXlxa2J6eFY1RjRGcmhjQVFBQUFBJCQAAAAAAAAAAAEAAAAZuXUTRE5GUUZSAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHiJkFx4iZBcMU; hword=24; hz=0; s_ht_pageid=9; v_pg=s_102; Hm_lvt_0703cfc0023d60b244e06b5cacfef877=1553486109,1553883932,1554055217; nonUnion=1; Hm_lvt_48c57cebc84275afcff127cd20c37e4b=1554156310; Hm_lpvt_48c57cebc84275afcff127cd20c37e4b=1554156752; ft=1; hword=3; org=1; Hm_lpvt_0703cfc0023d60b244e06b5cacfef877=1554257841; tnwhiteft=XzFYUBclcMPGIANCmytknWnBQaFYTzclnHRdPjcdP161rgY" --compressed'
	curlgo(curl)


