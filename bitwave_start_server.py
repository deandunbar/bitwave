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


class beginit:
	
	def __init__(self):
		app = web.application(urls, globals())
		#~ Open a Web Browser
		browser_tricks = tricks.browser_tricks()
		browser_tricks.open_browser()
		#fixes the error of not loading from the launcher
		app.run()

	#~ 
		if __name__ == "__main__": 
			app.run()


#~ server = beginit()




