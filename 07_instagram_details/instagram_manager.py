import json

def load_data():
    try:
        with open('instagram.text', 'r') as file:
            test = json.load(file)
            print(type(test))
            return test
    except FileNotFoundError:
        return []

def save_data_helper(users):
    with open('instagram.text', 'w') as file:
        json.dump(users, file)

def allData(users):
    if len(users):
        for index, user in enumerate(users, start=1):
            print(f"{index}. {user['name']}")
    else:
        print("No users available!")

def addUser(users):
    name = input("Enter name: ")
    age = input("Enter age: ")
    followers = input("Enter followers: ")
    following = input("Enter following: ")
    videoType = input("reel or story: ")
    isAddStory = int(input("Want to add story press 1: "))
    isAddReel = int(input("Want to add reel press 1: "))
    stories = []
    reels = []
    if isAddStory == 1:
        storyCount = int(input("Enter the number of stories you want to add?: "))
        for i in range(storyCount):
            title = input("Enter story title: ")
            date = input("Enter story date: ")
            viewed = input("Enter story isViewed: ")
            stories.append({
                "title": title,
                "date": date,
                "viewed": viewed
            })
    if isAddReel == 1:
        reelCount = int(input("Enter the number of reels you want to add?: "))
        for i in range(reelCount):
            title = input("Enter reel title: ")
            date = input("Enter reel date: ")
            viewed = input("Enter reel isViewed: ")
            reels.append({
                "title": title,
                "date": date,
                "viewed": viewed
            })
    users.append({
        "name": name,
        "age": age,
        "followers": followers,
        "following": following,
        "videotype": videoType,
        "stories": stories,
        "reels": reels
    })
    save_data_helper(users)

def updateUser(users):
    allData(users)
    index = int(input("Enter story or reel number to update: "))
    
    if 1 <= index <= len(users):
        user = users[index-1]
        name = input(f"Enter the name ({user['name']}): ") or user['name']
        age = input(f"Enter the age ({user['age']}): ") or user['age']
        followers = input(f"Enter followers ({user['followers']}): ") or user['followers']
        following = input(f"Enter following ({user['following']}): ") or user['following']
        videotype = input(f"Enter videotype (story/reel) ({user['videotype']}): ") or user['videotype']
        
        user.update({
            'name': name,
            'age': age,
            'followers': followers,
            'following': following,
            'videotype': videotype
        })
        
        save_data_helper(users)

def deleteStory(users):
    for index, user in enumerate(users, start=1):
        if user['videotype'] == "story":
            print(f"{index}. {user['name']} - Story")
    
    index = int(input("Enter the story number to delete: "))
    if 1 <= index <= len(users) and users[index-1]['videotype'] == "story":
        users.pop(index-1)
        save_data_helper(users)
        print("Story deleted successfully!")
    else:
        print("Invalid story number!")

def deleteReel(users):
    for index, user in enumerate(users, start=1):
        if user['videotype'] == "reel":
            print(f"{index}. {user['name']} - Reel")
    
    index = int(input("Enter the reel number to delete: "))
    if 1 <= index <= len(users) and users[index-1]['videotype'] == "reel":
        users.pop(index-1)
        save_data_helper(users)
        print("Reel deleted successfully!")
    else:
        print("Invalid reel number!")

def allDelete(users):
    users.clear()
    save_data_helper(users)
    print("All data deleted successfully!")

def getUserDetails(users):
    name = input("Enter the name of the user: ")
    found = False
    for user in users:
        if user['name'] == name:
            print(f"Name: {user['name']}, Age: {user['age']}, Followers: {user['followers']}, Following: {user['following']}")
            found = True
            break
    if not found:
        print("User not found!")

def main():
    users = load_data()
    print("Users: ", users)

    while True:
        print("\nInstagram manager | Choose an option:")
        print("1. All Instagram users")
        print("2. Add username, Instagram reels and stories")
        print("3. Update username, Instagram reels and stories")
        print("4. Delete Instagram story")
        print("5. Delete Instagram reel")
        print("6. Delete all Instagram reels and stories")
        print("7. Get details of a specific user")
        print("8. Get reels of a specific user")
        print("9. Get stories of a specific user")
        choice = input("Enter your choice: ")

        if choice == '1':
            allData(users)
        elif choice == '2':
            addUser(users)
        elif choice == '3':
            updateUser(users)
        elif choice == '4':
            deleteStory(users)
        elif choice == '5':
            deleteReel(users)
        elif choice == '6':
            allDelete(users)
        elif choice == '7':
            getUserDetails(users)
        elif choice == '8':
            pass  # You can add functionality for getting reels here.
        elif choice == '9':
            pass  # You can add functionality for getting stories here.
        else:
            print("Invalid choice!")

main()
