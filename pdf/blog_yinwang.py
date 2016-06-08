# https://github.com/JazzCore/python-pdfkit

import pdfkit
import re
import urllib2

blog_url = "http://www.yinwang.org/"

pattern_get_str = "(?<=\<a href=\")(http:[^\"]*)\">(.*)</a>"
pattern_get = re.compile(pattern_get_str,re.UNICODE)

pattern_sub_str = "[^\w]"
pattern_sub = re.compile(pattern_sub_str,re.UNICODE)

response = urllib2.urlopen(blog_url)
content  = response.read()
content  = content.decode('utf-8')

result  = re.findall(pattern_get,content)

index = 1
for item in result[::-1]:
	pdfurl  = item[0]
	if not 'blog-cn' in pdfurl:
		continue
	pdfname = item[1]
	pdfurl = pdfurl.encode('utf-8')

	# replace all characters that is invalid for file name
	pdfname = re.sub(pattern_sub,"_",pdfname) 
	pdfname = "%03d"%index+"_"+pdfname+".pdf"
	print "url: " + pdfurl
	print "filename: "+ pdfname
	pdfurl = pdfurl.encode('utf8')
	pdfkit.from_url(pdfurl,pdfname)
	index+=1