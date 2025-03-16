import sqlite3

conn = sqlite3.connect("youtu_video.db")  # Corrected file name to .db for consistency

cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def listVideos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def addVideo(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?, ?)", (name, time))
    conn.commit()

def updateVideo(videoId, newName, newTime):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (newName, newTime, videoId))
    conn.commit()

def deleteVideo(videoId):
    cursor.execute("DELETE FROM videos WHERE id = ?", (videoId,))
    conn.commit()

def main():
    while True:
        print("\nYouTube Manager App with DB:")
        print("1. List YouTube videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")
        choice = input("Enter your choice: ")  
        
        if choice == '1':
            listVideos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            addVideo(name, time)
        elif choice == '3':
            try:
                videoId = int(input("Enter the video ID to update: "))  
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                updateVideo(videoId, name, time)
            except ValueError:
                print("Invalid ID input. Please enter a valid integer.")
        elif choice == '4':
            try:
                videoId = int(input("Enter the video ID to delete: "))  
                deleteVideo(videoId)
            except ValueError:
                print("Invalid ID input. Please enter a valid integer.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")
    
    conn.close()

if __name__ == "__main__":
    main()
