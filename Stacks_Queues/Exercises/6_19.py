#C6-19
from classes import *

def is_HTML_matched(html): #expects a str
    '''returns true iff all HTML tags are matched (tags are the delimiters)'''

    S = ArrayStack() #tracks opening tags
    start = 0
    while True:
        print(S)
        i = html.find('<', start) #returns index of first occurence of char from index=start
        if i== -1: #not found in str 
            break
        j = html.find('>', i)
        if j == -1:
            return False
        tag = html[i:j+1] #may contain attributes if opening tag
        if tag[1] != '/': #if it is opening tag
            S.push(tag)
        else: #if it is closing tag, perform check
            tag_name = tag[2:-1]
            print(tag_name)
            if not tag_name in S.pop()[1:-1].split():
                return False
        start = j #shifts starting point of next .find() operation to the right

    return True






