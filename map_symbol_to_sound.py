"""
This script is just to extract the data. 

Its primary goal is to match the ipa symbol to its corresponding mp3 

Eg. mp3 = IPA110.mp3, symbol=/g/

Will need to extract tbody and then extract the gif name and the ipa mp3 name. 

The symbol is actually a gif image. The gif name has features relating to it so /f/ would be xx_pul_fri_lab01.gif for 
pulmonic fricative, and lab01 refers to it being the first symbol in the fricative row and being labial 

For easier mapping to convert this fri_01 to its relevant IPA directly 
"""
from bs4 import BeautifulSoup
import re

filepath = ""
soup = BeautifulSoup(open(filepath, encoding = "ISO-8859-1"), "html.parser")# opens local file

spans = list(soup.find_all("span"))
ipa_sound = r'id="(\w*)"'
ipa_img = r'img\/C_\d{2}_[a-z]*_([a-z]*_[a-z]*\d?\d?)\.gif'

ipa_sounds = []
ipa_imgs = []

for span in spans:
	span = str(span)

	m = re.search(ipa_sound, span)
	ma = re.search(ipa_img, span)

	ipa_sounds.append(m.group(1))
	try:
		ipa_imgs.append(ma.group(1))
	except AttributeError:
		# catch some name outliers
		ma5 = re.search(r'C_(\d{3}p\d{3}p\d{3})', span)
		ipa_imgs.append(ma5.group(1))


## mappings 
#map ipa imgs to their corresponding ipa ARPABET symbol 
with open('arpa_con.txt', 'r') as f:
	arpa = [line.replace('\n','') for line in f]

arpa = [[arp for arp in line.split()]for line in arpa]

arpa_dict = {k[2]:k[0] for k in arpa}

ipa_to_arpa = {}
just_arpa_things = []
for key in arpa_dict:
	if key in ipa_imgs:
		ipa_to_arpa[arpa_dict[key]] = key # maps ipa from norwegian site to arpa phoneset
		just_arpa_things.append(key)
	else:
		ipa_to_arpa[arpa_dict[key]] = "no"
		just_arpa_things.append("no")

print(ipa_to_arpa)



# map imgs to sounds 
# convert this to ARPAbet to mp3 filename 
ipa_dict = {k:ipa_sounds[idx] for idx, k in enumerate(ipa_imgs)} 


print(ipa_dict)


