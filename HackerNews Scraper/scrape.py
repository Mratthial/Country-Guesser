# Tutorial from zero to hero python udemy course for Hacker News Webscraping.

import requests 
from bs4 import BeautifulSoup
import pprint 

# Beautiful soup allows us to scrape the HMTL Data.
# Requests lets us download that data.
# pprint is pretty print, built in to python to make it neat.

#get the stuff from this website
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# we got the data.  There is a LOT of information.  We want to remove info we don't need, like stories with >100 upvote points.
# beautiful soup will PARSE this. It will convert the string into something we can ue
    # the html parser can parse xml too.  We want the HTML, not XML.  We set this to the variable.  
    # We are calling this soup.
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, "html.parser")

# We can print anything we want from this page.  
# We can print all the div objects on this page!
    # find_all('div')

# We can print all the links too!  
#   find_all('a')
    # Use 'a" (which is the a tags, the links)

# Use select function to use css selectors.  We can use the class, id, etc.
    # we can use '.' and then select what class we want!
    # we can use '#' which is the ID.

# we will use .titleline to get the title and the link of the stories.
# print(soup.select('.titleline')[1])

links = soup.select('.titleline > a')
links2 = soup2.select('.titleline > a')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

# make a function for hackernews list.
# we will enumerate through all to get the links and votes.
# we want the href (the links) for the sites
# we want the vote points too.  sometimes, pages have 0 points,
    # it causes an error since the list length of votes is less than the titles.
    # to prevent, use the if len(vote) part 
def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse = True)

        # when sorting dictionaries, we can give it a lambda and sort the key we want.
        # without it, we get the error.  we can't compare lists to dictionaries.  
            # now we are using the list  in votes

def create_custom_hn(links, subtext):
    hn = []
    for index, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn) 

pprint.pprint(create_custom_hn(mega_links,mega_subtext))