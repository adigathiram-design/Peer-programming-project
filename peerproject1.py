class User:  # creates a user class for user information
    def __init__(self, username, birth):
        self.username = username
        self.birth = birth


class Artist:  # creates an artist class for artist information
    def __init__(self, name, length, singer, genre=None):
        self.name = name
        self.length = length  # in seconds or minutes depending on file data
        self.singer = singer
        self.genre = genre


def preferences():  # function to get user preferences
    fav_artist = input("Enter your favorite artist: ")
    fav_genre = input("Enter your favorite genre: ")
    print(f"Favorite Artist: {fav_artist}, Favorite Genre: {fav_genre}")
    return fav_artist, fav_genre


# Read artist data safely
try:
    with open("savedlibrary.txt") as file:
        data = [line.strip().split(",") for line in file]
        data = [Artist(name, length, singer, genre) for name, length, singer, genre in data]
except FileNotFoundError:
    print("No saved library found. Starting with an empty one.")
    data = []


# Get user info
name = input("Enter your name: ")
birth = input("Enter your date of birth: ")
user = User(name, birth)

# Get preferences
fav_artist, fav_genre = preferences()

optionA = input("Would you like to see your songs sorted A-Z? (Yes/No): ").strip()
if data and optionA.lower() == "yes":
    song_titles = sorted([artist.name for artist in data])
    print("\nSongs in your library (A–Z):")
    for title in song_titles:
        print(f" - {title}")
else:
    print("\nNo songs in your library yet.")

# Ask for confirmation
while True:
    question = input("Are you sure about your preferences? (yes/no): ").strip().lower()
    if question == "yes":
        break
    elif question == "no":
        fav_artist, fav_genre = preferences()
    else:
        print("Please answer with 'yes' or 'no'.")


# ========== PLACEHOLDER ==========
# Requirement 5 (Person 3):
# Functions for playlist generation based on time or genre will go here.
# Example: def create_playlist_by_time() or def create_playlist_by_genre()
# =================================


# ========== REQUIREMENT 6 ==========
# Export songs by a specific artist to a text file
def export_songs_by_artist(artist_name):
    """Exports all songs by the chosen artist into a new text file"""
    songs_by_artist = [song for song in data if song.singer.lower() == artist_name.lower()]

    if not songs_by_artist:
        print(f"No songs found for artist: {artist_name}")
        return

    filename = f"{artist_name}_songs.txt"
    with open(filename, "w") as file:
        for song in songs_by_artist:
            file.write(f"{song.name}, {song.length}, {song.genre}\n")

    print(f"Songs by {artist_name} have been exported to '{filename}'.")


# ========== REQUIREMENT 7 ==========
# Calculate average track length per genre
def average_track_length_by_genre():
    """Calculates and displays the average track length for each genre"""
    genre_lengths = {}

    for song in data:
        try:
            length = float(song.length)
        except ValueError:
            print(f"Skipping invalid length value for song: {song.name}")
            continue

        if song.genre:
            if song.genre not in genre_lengths:
                genre_lengths[song.genre] = []
            genre_lengths[song.genre].append(length)

    if not genre_lengths:
        print("No genre data available.")
        return

    print("Average track length by genre:")
    for genre, lengths in genre_lengths.items():
        avg_length = sum(lengths) / len(lengths)
        print(f" - {genre}: {avg_length:.2f} (mins)")


# Menu for user to access new functions
while True:
    print("Options:")
    print("1 - Export songs by artist")
    print("2 - Show average track length by genre")
    print("3 - Exit")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        artist_name = input("Enter the artist name to export: ")
        export_songs_by_artist(artist_name)
    elif choice == "2":
        average_track_length_by_genre()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
