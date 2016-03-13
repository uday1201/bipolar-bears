from bs4 import BeautifulSoup
from django.shortcuts import render
import nltk
import re
import sys
import urllib
import urllib2
from .models import getda, getForm

# Create your views here.


def show(request):
	m = {}
	form = getForm(request.POST or None, request.FILES or None)
	if request.method == 'POST':
		if form.is_valid():
			instance = form.save(commit=False)
			m = processLanguage(instance.a)
		context = {
			"form" : form,
			"m" : m,
		}
		return render(request, "base.html", context)
	else:
		m = {}
		context = {
			"form" : form,
			"m" : m,
		}
		return render(request, "base.html", context)





##let the fun begin!##
def processLanguage(x):
	data = {'sl':'hi','tl':'en','text':x} 
	querystring = urllib.urlencode(data)
	request = urllib2.Request('http://www.translate.google.com' + '?' + querystring )

	request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11')
	opener = urllib2.build_opener()
	feeddata = opener.open(request).read()
	#print feeddata
	soup = BeautifulSoup(feeddata,"lxml")
	contentArray = soup.find('span', id="result_box").get_text()
	#print request.get_method()
	try:
	    tokenized = nltk.word_tokenize(contentArray)
	    tagged = nltk.pos_tag(tokenized)
	    return tagged

	    #namedEnt = nltk.ne_chunk(tagged)
	    #namedEnt.draw()

	except Exception, e:
	    return str(e)
        