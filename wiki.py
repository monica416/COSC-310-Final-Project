"""
Installation:

pip install Wikipedia-API
"""
import wikipediaapi as w

## Get Summary ##
"""
Gets the a summary from the wikipedia page.
Only returns the first 1000 characters.
"""
def getSummary(page):
    summary = page.summary[0:1000]

    return summary

## Get URL ##
"""
Returns the url of the wikipedia page being talked about
"""
def getUrl(page):
    url = page.fullurl

    return url

## Get Text ##
"""
Returns the entire text from the wikipedia page
"""
def getText(page):
    text = page.text
    
    return text

## Gets Page ##
"""
Returns the entire page attribute from the wikipedia page being searched for
"""
def getPage(t): 
    x = w.Wikipedia('en')
    page = x.page(t)
    
    return page

## Get Sections ##
"""
Returns the sections of the wikipedia page
"""
def getSections(page):
    sections = page.sections

    return sections

## Get Title ##
"""
Returns the title of the wikipedia page
"""
def getTitle(page):
    title = page.title

    return title

## Get Categories ##
"""
Returns the categories from the wikipedia page
"""
def getCategories(page):
    categories = page.categories
    
    return categories

## Main func ##
"""
This is the function that is first called from the other classes. 

Takes the user input including what the user wants to know, find the wikipedia page (if it exists) and 
    outputs the relevant info for the user. 
"""
def wikiInfo(topic):
    try:
        ans = input("IMDBot: Would you like some Wikipedia informaiton on this?      ")
        
        if (ans.lower()[0] == 'y'):
            print("IMDBot: Ok, let me see if i can find a the Wikipedia page...")
            if (getPage(topic).exists()):
                print("IMDBot: A page has been found! What would you like to know from the Wikipedia page,", getTitle(getPage(topic)), "?")
                info_wanted = input("      (Title, summary, sections, categories, or entire text):      ")

                if (info_wanted.lower().__contains__("title")):
                    title = getTitle(getPage(topic))
                    print("IMDBot: Here is the title of the Wikipedia page: \n", title)

                    print("\nIMDBot: To learn more visit the Wikipedia page here: ", getUrl(getPage(topic)))

                elif (info_wanted.lower().__contains__("summary")):
                    summary = getSummary(getPage(topic))
                    print("IMDBot: Here is a summary of the Wikipedia Page: \n")
                    print(summary + "...")

                    print("\nIMDBot: To learn more visit the Wikipedia page here: ", getUrl(getPage(topic)))

                elif (info_wanted.lower().__contains__("sections")):
                    sections = getSections(getPage(topic))
                    print("IMDBot: Here are the sections of the Wikipedia page: \n")
                    for s in sections:
                        print(s.sections)
                    
                    print("\nIMDBot: To learn more visit the Wikipedia page here: ", getUrl(getPage(topic)))
                
                elif (info_wanted.lower().__contains__("categories")):
                    categories = getCategories(getPage(topic))
                    print("IMDBot: Ok, here are the categories of the Wikipedia page: \n")
                    for title in sorted(categories.keys()):
                        print("%s: %s" % (title, categories[title]))
                    
                    print("\nIMDBot: To learn more visit the Wikipedia page here: ", getUrl(getPage(topic)))
                
                elif (info_wanted.lower().__contains__("text")) or (info_wanted.lower().__contains__("entire")):
                    print("IMDBot: Here is the informaiton: \n")
                    print(getText(getPage(topic)))

                    print("\nIMDBot: To learn more visit the Wikipedia page here: ", getUrl(getPage(topic)))
                
                else:
                    print("IMDBot: Sorry, the Wikipedia page does not have any information about", info_wanted)
            else:
                print("IMDBot: Sorry, there is no Wikipedia page on ", topic)
        else:
            pass
    except:
        print("IMDBot: Sorry, i'm not quite sure how to help with that yet")

## --- For Testing and Debugging --- ##
#title = "The Avengers"

#wikiInfo(title + " (film)")