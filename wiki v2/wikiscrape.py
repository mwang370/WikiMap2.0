import re
import urllib.request
import json
import random

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
    for x in random.sample(range(0, len(links)), 9): 
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
    
    return results
             
#def search(topic): 
#    query = wikipedia.search(topic)[0]
#    pg = wikipedia.page(query)
#    return pg.url
#    
#def generate(url): 
#    if url[0] == '/': 
#        url = 'https://en.wikipedia.org' + url 
#    request = urllib.request.urlopen(url)
#    html = request.read()
#    text = html.decode()
#    soup = BeautifulSoup(text)
#    
#    title = soup.title.string
#    i = title.find(' - Wikipedia')
#    title = title[:i]
#    
#    intro = soup.p
#    links = []
#    topics = []
#    for link in intro.find_all('a'): 
#        x = link.get('href')
#        if x[0:6] == '/wiki/':
#            topic = x[6:]
#            topic = topic.replace("_", " ")
#            links.append(x)
#            topics.append(topic)
#    
#    return links, topics, title
#    
#def wikiLinks(topic, num): 
#    if topic[0] != '/': 
#        topic = search(topic)
#    links, topics, title = generate(topic)
#    
#    if num == 1:
#        list1 = []
#        for t in topics:
#            list1.append({"name": t})
#        return {"name": title, "children": list1}
#        
#    else: 
#        list1 = []
#        for i in range(len(topics)):
#            try:
#                list1.append(wikiLinks(links[i], num-1))
#            except:
#                pass
#        return {"name": title, "children": list1}
#        
#    
#            
    
    