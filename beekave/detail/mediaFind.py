from apiclient.discovery import build
import urllib.request


NAVER_CLIENT_ID = "ZGXdDH_nDH957xeoxgvF"
CLIENT_SECRET = "tlGan_kGMm"
YOUTUBE_DEVELOPER_KEY = "AIzaSyBr5r9HsE-IcLNkgyDGRwUgFZNogI626N8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def getNaverSearch(query):
    encText = urllib.parse.quote(query)

    url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",NAVER_CLIENT_ID)
    request.add_header("X-Naver-Client-Secret",CLIENT_SECRET)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        return response_body.decode('utf-8')
    else:
        print("Error Code:" + rescode)
        return 1



def youtube_search(title,titleen):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=YOUTUBE_DEVELOPER_KEY)
    if titleen:
       searchquery  =title + " 예고편 " + titleen + " trailer"
    else:
        searchquery = title + " 예고편 trailer"
    search_response = youtube.search().list(
        q=searchquery,
        part="id,snippet",
        maxResults="5"
    ).execute()
    titles = []
    videoID = []



    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            title = search_result["snippet"]["title"]
            titles.append(title)
            videoID.append(search_result["id"]["videoId"])


    return videoID[0]
