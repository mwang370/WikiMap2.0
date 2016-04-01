import re
import urllib.request
import json
import random
import unicodedata

def topic_search(topic):
    topic = topic.strip()
    topic = topic.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + topic
    response = urllib.request.urlopen(url)
    html = response.read()
    text = html.decode()
    
    title = re.findall('<title>([^<]+)</title>', text)
    title = title[0]
    i = title.find(' - Wikipedia')
    title = title[:i]
    
    topics = links(text)
            
    return json.dumps({"name": title, "children": topics})

def links(text): 
    pat = 'href="/wiki/([^"]+)"'
    links = re.findall(pat, text)
    
    results = []
    for x in random.sample(range(0, len(links)), 10): 
        topic = links[x]
        topic = topic.replace('_', ' ')
        if '#' in topic: 
            i = topic.find('#')
            topic = topic[:i]
        if 'Category:' in topic: 
            i = topic.find(':')
            topic = topic[i+1:]
        if 'Wikipedia:' not in topic and 'Help:' not in topic and 'Special:' not in topic and 'Template:' not in topic and 'File:' not in topic and 'Portal:' not in topic: 
            results.append(topic)
    
    return results[0:5]
             
    
