# grabheader.py
# description: header analysis for ftw core
# author: @semprix

import sys, urllib2, time

from colors import *

def grabheader():
	print "[**] Starting header analysis"
	response = urllib2.urlopen('http://' + sys.argv[1])

	# Server header settings

	grabserver = response.info().getheader('server')
	print " [+] Grabbing web server version"
	if grabserver is None:
		printout('  >> Failed to get header value *not vulnerable*', RED)
	else:
		printout('  >> ' + grabserver, GREEN)

	grabplatform = response.info().getheader('x-powered-by')
	print " [+] Grabbing platform "
	if grabplatform is None:
		printout('  >> No response from server', RED)
	else:
		printout('  >> ' + grabplatform, GREEN)

	grabcontent = response.info().getheader('content-type')
	print " [+] Grabbing content type "
	if grabcontent is None:
		printout('  >> Failed to get header value *not vulnerable*', RED)
	else:
		printout('  >> ' + grabcontent , GREEN)

	 # Server header security settings
	
	 # Check if this is an SSL port

	if sys.argv[2] == '443':
		print " [+] Grabbing SSL header settings "
		printout('  >>  SSL Checks go here', WHITE)

	else:
		print "[!] Target not using SSL, proceed with http..."
		time.sleep(3)

	grabframeopt = response.info().getheader('x-frame-options')
	print " [+] Grabbing x-frame-options "
	if grabframeopt is None:
		printout('  >>  No x-frame-options *vulnerability to click-jacking is possible*', RED)
	else:
		printout('  >> ' + grabframeopt, GREEN)
	
	grabxssprotect = response.info().getheader('x-xss-protection')
	print " [+] Grabbing x-xss-protection "
	if grabframeopt is None:
		printout('  >> No XSS protection *vulnerability to XSS is possible*', RED)
	else:
		printout('  >> ' + grabframeopt, GREEN)
	
	grabxcontent = response.info().getheader('x-content-type-options')
	print " [+] Grabbing x-content-type-options"
	if grabxcontent is None:
		printout('  >> No x-content-type-options *vulnerability to MIME sniffing is possible*', RED)
 	else:
		printout('  >> ' + grabxcontent, GREEN)

 	response.close()  
	print'[*] Header analysis finishing....'
 	time.sleep(3)


