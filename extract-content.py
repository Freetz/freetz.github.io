#!/usr/bin/env python3

import os
import sys
import subprocess
from bs4 import BeautifulSoup
from progress.bar import Bar

pages = []
titleList = []

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


# Create a list of all pages to convert
for path, subdirs, files in os.walk("wiki"):
	for name in files:
		if not "?" in name and not ".." in name and ".html" in name:
			pages.append(os.path.join(path, name))

# Also convert the toplevel index.html
pages.append("index.html")

# Progress bar
numPages = len(pages)
bar = Bar('Converting pages', max=numPages)

# Actual extraction
for count, page in enumerate(pages):
	pageFile = open(page, "r")
	pageSoup = BeautifulSoup(pageFile, 'html.parser')
	for div in pageSoup.find_all("div", {'class':'wiki-toc'}):
		div.decompose()

	pageFile.close()

	content = pageSoup.find(id="content")

	titleList.append(title)

	contentPage = open(page + ".content", "w")
	if not type(content) is None:
		contentPage.write(str(content))

	contentPage.close()

	subprocess.call(["pandoc", "-f", "html-header_attributes-link_attributes-native_spans-native_divs", "-t", "rst", page + ".content", "-o", page.replace(".html", ".rst")])
	subprocess.call(["sed", "-i", "/^:::/ d", page.replace(".html", ".rst")])

	os.remove(page + ".content")
	bar.next()

bar.finish()

for i in titleList:
	print("   " + "wiki/" + i)
