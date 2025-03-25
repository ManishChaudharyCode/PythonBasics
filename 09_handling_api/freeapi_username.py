import requests

def user_freeapi():
    url ="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()
    
    if data ["success"] and "data" in data:
        userData = data["data"]
        username = userData["login"]["username"]
        Gender = userData["gender"]
        Email = userData["email"]
        Password = userData["login"]["password"]
        country = userData["location"]["country"]
        city = userData["location"]["city"]  
        state = userData["location"]["state"]  
        return username, Gender, Email, Password,  country, city, state
    else:
        raise Exception("Failed fetch user the data")
    
    
def main():
    try:
        username, gender, email, password,  country, city, state = user_freeapi()
        print(f"Username: {username} \n Gender: {gender} \n Email: {email}\n Password: {password}  \n Country: {country} \n city: {city} \n state: {state}" )
        
    except Exception as e:
        print(str(e))  

if __name__ =="__main__":
    main()    
    
