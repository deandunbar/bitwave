#!/usr/bin/env python



import webbrowser
new = 2 # open in a new tab, if possible

class browser_tricks:
	
	#~ new = 2 # open in a new tab, if possible
	
	def open_browser(self,url):
		#~ return render.index()
        # redirect to the static file ...
		print("Opening the web browser")
		webbrowser.open(url,new=new)






