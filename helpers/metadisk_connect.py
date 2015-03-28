#!/usr/bin/env python


import requests
import shutil
from PIL import Image   

class metadisk_connect:
	
	
	#~ metadisk_server = 'http://node1.metadisk.org/api/'
	#~ download_command = 'download/'

	def __init__(self):
	    self.metadisk_server = 'http://node1.metadisk.org/api/'
	    self.download_command = 'download/'
	    
		
	def download_image(self,file_hash):
		download_url = self.metadisk_server +  self.download_command + file_hash
		print download_url
		response = requests.get(download_url, stream=True)
		with open('img.png', 'wb') as out_file:
		    shutil.copyfileobj(response.raw, out_file)
		del response
		img = Image.open("img.png")
		img.show() 
		
		
	def show_image(self,image_response):
		with open('img.png', 'wb') as out_file:
		    shutil.copyfileobj(image_response.raw, out_file)
		del image_response
		img = Image.open("img.png")
		img.show() 
		
	def download_file(self,file_hash):
		download_url = self.metadisk_server +  self.download_command + file_hash
		print "now downloading " + download_url
		response = requests.get(download_url, stream=True)
		return response
		
	def run_script(self,script_hash):
		print "running script"
		

		
	#~ def install(self, file_hash):
		
		



mdc = metadisk_connect()
#~ mdc.download_image("164e70faf4e2ff2ce00734e4088b617dd0dbb211c4a93914b9a45614ae2c48c3?key=6b47bc31bc959558018781f509881e417f290e60cb6beea00fdb7b2ce1464cba&token=ZHwaAZ6YzmZ5ONOa")
#~ raw_img = mdc.download_file("164e70faf4e2ff2ce00734e4088b617dd0dbb211c4a93914b9a45614ae2c48c3?key=6b47bc31bc959558018781f509881e417f290e60cb6beea00fdb7b2ce1464cba&token=ZHwaAZ6YzmZ5ONOa")
raw_img = mdc.download_file("9ecae2ac2906026c0ac5a212c47b0c9d78ce0f5d002e484251a166977bcb5e59?key=45d34e5f8bc58f2717b19f7ad6284f11c39a1b3ebe1689bb481b9aa36fccef72")
#~ raw_img = mdc.download_file("69b5a46c06e89370f1fbd0ae49ed985a8281f48baaf2170ef2adccf988504ade?key=cfca8f9521d0fda48ff3d781687eb4cbacefb5e259150374fe26f78a14c78055")


image_showed = mdc.show_image(raw_img)



#~ mdc.download_image("a83f7f0e29d856ff57cf2a459f093240ba991aaf6700474ba8247cdd6b6130c2?key=23b64716bff5ff91484944960a435c70fabf196fd2f000a1c35bd3ac5f73ab34")
                                                   #~ 


#~ url = 'http://node1.metadisk.org/api/download/164e70faf4e2ff2ce00734e4088b617dd0dbb211c4a93914b9a45614ae2c48c3?key=6b47bc31bc959558018781f509881e417f290e60cb6beea00fdb7b2ce1464cba&token=ZHwaAZ6YzmZ5ONOa'
#~ response = requests.get(url, stream=True)
#~ with open('img.png', 'wb') as out_file:
    #~ shutil.copyfileobj(response.raw, out_file)
#~ del response
#~ 
#~ 
#~ img = Image.open("img.png")
#~ img.show() 
#~ 

