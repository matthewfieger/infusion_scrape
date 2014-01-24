import urllib
import re

# The urllib module provides a high-level interface for fetching data across the World Wide Web.
# The re documentation can be found here http://docs.python.org/2/library/re.html

myfile = open("./two_infuse.txt", "w+")
myfile.close()

# For some reason, the id for each infusion center goes from 7660 to 9449.
# Set up a while loop to iterate through this search space.

i=7660
while i<7700:

# Concatenate the url with our iterator variable.
# Open the url and write the html to text.  You must tell the urlopen function that http is the method.

	url = "http://www.2infuse.com/profile-ic/"+ str(i)
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()

# Assign regex for each entry we are looking for.
# Extract entry out of regex and assign to a new variable.
# (.+?) Matches any string of any repeating characters except a newline.  Putting it in parenthesis indicates a group.  It can be accessed later with \number, e.g. \1.

# Infusion Center Name
	regex_name = '<h1 class="fn org">(.+?)</h1>'
	pattern_name = re.compile(regex_name)

# Phone, [\s]* captures a bunch of \t after the phone number.
	regex_phone = '<span class="type">Tel:</span> (.+?)[\s]*</div>'
	pattern_phone = re.compile(regex_phone)

# Fax [\s]* captures a bunch of \t after the fax number.
	regex_fax = '<span class="type">Fax:</span> (.+?)[\s]*</div>'
	pattern_fax = re.compile(regex_fax)

# Address	
	regex_address = '<div class="street-address">(.+?)</div>'
	pattern_address = re.compile(regex_address)

# Locality
	regex_locality = '<span class="locality">(.+?)</span>'
	pattern_locality = re.compile(regex_locality)

# State / Region
	regex_state = '<abbr class="region" title="">(.+?)</abbr>'
	pattern_state = re.compile(regex_state)

# Postal Code
	regex_zip = '<span class="postal-code">(.+?)</span>'
	pattern_zip = re.compile(regex_zip)

# The last time the information was updated on the 2infuse website.
	regex_update = '<p class="last-updated">This site profile was last updated on (.+?)</p>'
	pattern_update = re.compile(regex_update)	
	
# Practice Affiliate Physicians, [\s]* captures a \n and a bunch of \t before the names.
	regex_physicians = '<li><strong>Practice-affiliated physicians:</strong>[\s]*(.+?)</li>'
	pattern_physicians = re.compile(regex_physicians)
	
# Affiliated Hospitals, [\s]* captures a \n and a bunch of \t before the names.
	regex_hospitals = '<li><strong>Hospital affiliations:</strong>[\s]*(.+?)</li>'
	pattern_hospitals = re.compile(regex_hospitals)

# Parse html to find regex we are looking for.
# Then compile the pattern into a new variable.
	
	name = re.findall(pattern_name, htmltext)
	phone = re.findall(pattern_phone, htmltext)
	fax = re.findall(pattern_fax, htmltext)
	address = re.findall(pattern_address, htmltext)
	locality = re.findall(pattern_locality, htmltext)
	state = re.findall(pattern_state, htmltext)
	zip = re.findall(pattern_zip, htmltext)
	update = re.findall(pattern_update, htmltext)
	physicians = re.findall(pattern_physicians, htmltext)
	hospitals = re.findall(pattern_hospitals, htmltext)

# Open our file, with the append attribute
# Write each value to the file, delimit with ;, and add a line break after each iteration.

	myfile = open("./two_infuse.txt", "a")
	myfile.write(str(str(name)+";"+str(phone)+";"+str(fax)+";"+str(address)+";"+str(locality)+";"+str(state)+";"+str(zip)+";"+str(update)+";"+str(physicians)+";"+str(hospitals)+"\n"))
	myfile.close()

# Iterate this super awesome loop
	i+=1