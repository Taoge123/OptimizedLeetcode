
""
def teamFormation(score, team, m):
    # Write your code here
    left = 0
    right = len(score) - 1
    res = 0
    if team >= right:
        return sum(score)
    while left <= right:
        for i in range(m):

            maxi = max(maxi, score[i], score[right - i])
            res += maxi
            score.remove(maxi)

    return sum

score = [10, 20, 10, 15, 5, 30, 20]
team = 2
m = 3

print(teamFormation(score, team, m))



import requests
import json

def getMovieTitles(test):
    titles = []
    data = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(substr))
    response = json.loads(data.content.decode('utf-8'))
    for page in range(0, response["total_pages"]):
        page_response = requests.get("https://jsonmock.hackerrank.com/api/movies/search/?Title={}&amp;page={}".format(substr, page + 1))
        page_content = json.loads(page_response.content.decode('utf-8'))
        #print ('page_content', page_content, 'type(page_content)', type(page_content))
        for item in range(0, len(page_content["data"])):
             titles.append(str(page_content["data"][item]["Title"]))
    titles.sort()
    return titles
