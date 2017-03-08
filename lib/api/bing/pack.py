import requests
import re
import Queue
import thread

def BingSearch(query,limit):
    ans = set()
    for i in range(1,limit,10):
        print i
        q = "https://www.bing.com/search?q=" + query + "&first=" + str(i)
        c = requests.get(q, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}).content
        p = re.compile(r'<a target="_blank" href="(.*?)"', re.S)
        l = re.findall(p, c)
        for each in l:
            if "?" in each:
                ans.add(each[:each.find('?')])
            elif each[-1] == '/':
                ans.add(each[:-1])
            else:
                ans.add(each)
    return ans
if __name__ == '__main__':
    BingSearch("inurl:indexSub.action",55)