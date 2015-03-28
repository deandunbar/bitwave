#!/usr/bin/env python

import web
import helpers.web_browser as tricks

urls = (
  '/', 'index'
)


#~ Open a Web Browser
browser_tricks = tricks.browser_tricks()
browser_tricks.open_browser()


#~ render = web.template.render('static/dashboard/')

class index:
	
	
	
    def GET(self):
		#~ return render.index()
        # redirect to the static file ...
        raise web.seeother('static/dashboard/index.html')


app = web.application(urls, globals())


if __name__ == "__main__": app.run()






