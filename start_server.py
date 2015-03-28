#!/usr/bin/env python

import web
import helpers.web_browser as tricks

urls = (
  '/', 'index'
)

#~ render = web.template.render('static/dashboard/')

class index:
	
	
	
    def GET(self):
		#~ return render.index()
        # redirect to the static file ...
        raise web.seeother('static/dashboard/index.html')


#~ Open a Web Browser
browser_tricks = tricks.browser_tricks()
ran = browser_tricks.open_browser("http://localhost:8080")



app = web.application(urls, globals())

if __name__ == "__main__": app.run()


