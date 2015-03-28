#!/usr/bin/env python

import web
import helpers.web_browser as tricks
#~ import helpers.metadisk_connect as metadisk_connect

urls = (
  '/', 'index',
  '/index/', 'index',
  "/what/", "what",
  "/apps/", "apps"
)


#~ Open a Web Browser
browser_tricks = tricks.browser_tricks()
browser_tricks.open_browser()

#~ mdc = metadisk_connect.download_image()


#~ render = web.template.render('static/dashboard/')

class index:	
	
    def GET(self):			
        # redirect to the static file ...
        raise web.seeother('static/dashboard/index.html')
        
class what:
	
	def GET(self):
		
		return 'Hello, World!'
		
class apps:
	def GET(apps):
		raise web.seeother('/static/dashboard/app.html')


app = web.application(urls, globals())


if __name__ == "__main__": app.run()






