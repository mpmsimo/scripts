#/usr/bin/python
#sitemap_parse_search.py - Searches locks and combos for matching entries.
#msimo - 11/02/2014

from bs4 import BeautifulSoup
import urllib2, re

#Create a list of scrapable URL's from sitemap.xml or slsitemap.txt
site_list = []

#Search contents listed below
word_list = ["Python", "Michael Simo"]

#Other global variables... Bad! 
count = 0

#extract correct URL's from sitemap.xml // ONE TIME USE
def read_sitemap():
	filename = "sitemap.xml"
	fo = open(filename, "r+")
	lines = fo.readlines()
	for line in lines:
		line = line.strip()
		
		if line.startswith("<loc>"):
			try:
				line = line.replace("beta.", "")
			except: 
				pass
			line = line[5:]
			line = line[:-6]
			site_list.append(line)
			#print "Added %s to array!" % line
			print line
	fo.close()

#read URL's extracted from sitemap.xml as well as ones I've added. // Replaces read_sitemap
def read_file(filename):
	fo = open(filename, "r+")
	lines = fo.readlines()
	for line in lines:
		line = line.strip()
		if line.startswith("http://"):
			site_list.append(line)
			#print "Added %s to array!" % line
	fo.close()
	print "Number of websites: %d" % len(site_list)

#Returns tree format
def get_tree(url):
	source = urllib2.urlopen(url)
	tree = BeautifulSoup(source)
	#print tree
	return tree

#search for lowercase strings, see main for loop all items in site_list converted to lowercase
def match_text(tree):
	match = tree.get_text()
	match = tree.find_all(text=re.compile(r'\b%s\b' % '\\b|\\b'.join(word_list), flags=re.IGNORECASE))
	if len(match) == 0:
		pass
		#print "No matching items found in %s" % site_list[count]
		#print match
	else:
		print ("\nFound %d matches for: %s" % (len(match), site_list[count]))
		print match

for __name__ == "__main__":
	read_file("lac.txt")
	for item in site_list:
		tree = get_tree(item)
		match_text(tree)
		count += 1