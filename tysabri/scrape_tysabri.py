import urllib
import re
import json
import mechanize

list_of_states = open("states.txt").read()
list_of_states = list_of_states.split("\n")


myfile = open("./infusion_centers/infusion_centers.txt", "w+")
myfile.close()

for state in list_of_states:
	url = "http://www.tysabrihcp.com/findinfusions?zipCode=&radiusCode=true&radius=&state=true&stateCode=" + state
	br = mechanize.Browser()
	htmltext = br.open(url)
	data = json.load(htmltext)
	infusion_sites = data["infusionsDTO"]["infusionSites"]
	for site in infusion_sites:
		site = site
		myfile = open("./infusion_centers/infusion_centers.txt", "a")
		myfile.write(str(site)+"\n")
	myfile.close()