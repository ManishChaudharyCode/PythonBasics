import requests

def fatchCatch():
    url = "https://api.freeapi.app/api/v1/public/youtube/videos/EQwmQLU1S6I"
    respose = requests.get(url)
    Data = respose.json()
    
    
    if Data ["success"] and "data" in Data:
        userdata = Data["data"]
        Userid = userdata["video"]["items"]["id"]
        title = userdata["channel"]["info"]["title"]
        videoCount = userdata["channel"]["statistics"]["videoCount"]
        subscriberCount = userdata["channel"]["statistics"]["subscriberCount"]
        return Userid, title, subscriberCount, videoCount

    else:
        raise Exception("failed fatch youtube id")
    
def main():
   try:
       userid, title, subscriberCount, videoCount = fatchCatch()
       print(f"id: {userid} \n title:{title}  \n subscriberCount: {subscriberCount} \n videoCount: {videoCount}")
   except Exception as e:
       print(str(e))   
        
if __name__ == "__main__":
    main()        
                