import wikipediaapi as w

## how to get a single page
x = w.Wikipedia('en')
page = x.page("The Avengers")
print(page)

## how to check if a wiki page exists
exists = page.exists()
print(exists)

## how to get page summary
title = page.title
print(title)

summary = page.summary[0:200]
print(summary)

## how to get the page URL
url = page.fullurl
curl = page.canonicalurl
print(url)
print(curl)

## How to get full text
text = page.text
#print(text)

## how to get page top sections
sections = page.sections
level = 0
for s in sections:
    #print(s.sections)
    pass

## How to get page categories
categories = page.categories
for title in sorted(categories.keys()):
    #print("%s: %s" % (title, categories[title]))
    pass

"""
BRAINSTORMING:
    - Create 3 fuctions:
        ~ get summary
        ~ get sections
        ~ get categories
        ~ Main func:
            > ask the user what type of info they want displayed or if they want the entire page displayed
            > do error checking first to see if the page exists
            > give the user the url to the wikipedia page if they wish to learn more about the topic
"""