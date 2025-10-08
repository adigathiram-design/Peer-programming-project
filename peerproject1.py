class User:            #creates a user class for user information
    def __init__(self, username, birth):
        self.username = username
        self.birth = birth

class Artist:#creates an artist class for artist information as well as formating purposes
    def __init__(self, name, length, singer, genre=None):
        self.name = name
        self.length = length
        self.singer = singer
        self.genre = genre

def preferences():#function to get user preferences
    fav_artist = input("Enter your favorite artist: ")
    fav_genre = input("Enter your favorite genre: ")
    print(f"Favorite Artist: {fav_artist}, Favorite Genre: {fav_genre}")
    return fav_artist, fav_genre

# Read artist data safely incase it doesnt exist it wont run with an error
try:
    with open("savedlibary.txt") as file:#file name and file needs to be created
        data = [line.strip().split(",") for line in file]#splitting the file
        data = [Artist(name, length, singer, genre) for name, length, singer, genre in data]#branding each item into its specified catgeory
except FileNotFoundError:
    print("No saved library found. Starting with an empty one.")
    data = []

# Get user info
name = input("Enter your name: ")#simple user details
birth = input("Enter your date of birth: ")
user = User(name, birth)

# Get preferences
fav_artist, fav_genre = preferences()
optionA = input("Would you like to see your songs sorted A-Z? (Yes/No): ").strip()
if data and optionA.lower()=="yes":
    song_titles = sorted([artist.name for artist in data])#reads artists name from data
    print("\nSongs in your library (A–Z):")
    for title in song_titles:#loops in order to print out all the possible titles in the file
        print(f" - {title}")
else:
    print("\nNo songs in your library yet.")#checks when there is nothing put in

# Ask for confirmation
while True:#this could be made better with functions
    question = input("Are you sure about your preferences? (yes/no): ").strip().lower()
    if question == "yes":break
    elif question == "no":fav_artist, fav_genre = preferences()
    else:
        print("Please answer with 'yes' or 'no'.")
