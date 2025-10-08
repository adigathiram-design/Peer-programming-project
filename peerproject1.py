class User:
    def __init__(self, username, birth):
        self.username = username
        self.birth = birth

class Artist:
    def __init__(self, name,length,singer, genre=None):
        self.name = name
        self.singer = singer
        self.genre = genre
        self.length = length

def preferences():
   
    FavArtist = input("Enter your favorite artist: ")
    FavGenre = input("Enter your favorite genre: ")
    print(f"Favorite Artist: {FavArtist}, Favorite Genre: {FavGenre}")


data = [line.strip().split(",") for line in open("savedlibary.txt")]
data = [Artist(name, genre,length,singer) for name, genre,length,singer in data]
   


Name = input("Enter your name: ")
Date = input("Enter your date of birth: ")
preferences()
uncertain = True
while uncertain:
    question = input("Are you sure about your preferences? (yes/no): ").strip().lower()
    if question == 'yes': uncertain = False
    elif question == 'no': preferences()
    else: print("Please answer with 'yes' or 'no'.")


