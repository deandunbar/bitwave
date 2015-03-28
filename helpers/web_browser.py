#!/usr/bin/env python



import webbrowser
new = 1 # open in a new tab, if possible

class browser_tricks:
	default_url = "http://localhost:8080"
	#~ new = 2 # open in a new tab, if possible
	
	def open_browser(self):
		#~ return render.index()
        # redirect to the static file ...
		print("Opening the web browser")
		webbrowser.open(self.default_url,new=new)






