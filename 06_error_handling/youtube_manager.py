import json 

def load_data():
    try:
        with open('youtube.text', 'r') as file:
           test = json.load(file)
           print(type(test))
           return test
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.text', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print('*' * 0)
    if(len(videos)):
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['name']}, duration: {video['time']} description: {video['description']} videoType: {video['videoType']}")
    else: print("No videos available!")
    print("\n")
    print('*' * 0)


def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    description = input("Enter video description: ")
    videoType = input("Private or Public: ")
    videos.append({'name': name, 'time': time, 'description':description,"videoType":videoType})
    save_data_helper(videos)

def update_video(videos ):
    list_all_videos(videos)
    index = int(input("Enter the video number update: "))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the new video time: ")
        videos[index-1] = {'name': name, 'time': time }
        save_data_helper(videos)
    else:
        print("Invaid index selected ")    
l

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1 <= index < len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else: 
        print("Invaid video index selected  ")  

def delete_all(videos):
    for i in range(0,len(videos)):
        print("i:",videos[i-1])
        del videos[i-1]
        save_data_helper(videos)




def main():
    videos = load_data( )
    while True:
        print("\n youtube manager | choose an option")
        print("1. List all youtube videos: ")
        print("2. Add a youtube video: ")
        print("3. Update a youtube video: ")
        print("4. Delete a youtube video: ")
        print("5. Delete all youtube video: ")
        print("6. Exit app")
        choice = input("Inter the choice: ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                delete_all(videos)
            case '6':
                break
            case _:
                print("Invaid choice")

if __name__ == "__main__":  
    main()                  
                
