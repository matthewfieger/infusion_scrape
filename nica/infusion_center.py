import urllib
import re


infusion_center_file = open ("infusion_center_input.txt")
infusion_center_list = infusion_center_file.read()
infusion_center_list_split =  infusion_center_list.split("\n")

myfile = open("./infusion_center_output.txt", "w+")
myfile.close()

i=0
while i<77:

	url = "http://infusioncenter.net/ic/" +infusion_center_list_split[i]
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	
	
	regex_name = '<h1 class="entry-title">(.+?)</h1>'
	pattern_name = re.compile(regex_name)

	regex_contact = '<h2>Contact Info</h2>[\s]*<p>(.*)<br />[\s]*(.*)[\s]*<br /><a href="(.*)" title="(.*)">(.*)</a></p>'
	pattern_contact = re.compile(regex_contact)	
	
	regex_number = '<h2>Contact Info</h2>[\s]*<p>[\s]*(.*)[\s]*<br /></p>'
	pattern_number = re.compile(regex_number)	
	
	regex_location = '<h2>Location:</h2>[\s]*<div class="one-half first">[\s]*<p>(.*)<br />[\s]*(.*)[\s]*<br />[\s]*(.*)</p>[\s]*</div>'
	pattern_location = re.compile(regex_location)
	
	name = re.findall(pattern_name, htmltext)
	
	number = re.findall(pattern_number, htmltext)
	location = re.findall(pattern_location, htmltext)
	contact = re.findall(pattern_contact, htmltext)

# Open our file, with the append attribute
# Write each value to the file, delimit with ;, and add a line break after each iteration.

	myfile = open("./infusion_center_output.txt", "a")
	myfile.write(str(str(name)+";"+str(contact)+";"+str(number)+";"+str(location)+"\n"))
	myfile.close()

	i+=1
	
	
# http://infusioncenter.net/



