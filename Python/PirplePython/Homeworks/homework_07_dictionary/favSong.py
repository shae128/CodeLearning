# Creating favourite song dictionary
FavSong = {
    "OriginaleName": "Ghatar",
    "EnglishName": "Train",
    "Artist": "Mohsen Chavoshi",
    "Lyrics": "Hossein Safa",
    "Gener": "Pop Rock",
    "Album": "White Flag",
    "Year": 2012,
    "Duration": 214,
    "ArtistWiki": "https://en.wikipedia.org/wiki/Mohsen_Chavoshi",
    "SpotifyLink": "https://open.spotify.com/track/7mJQdh0nzN6YfOFiWTcu6R?si=Y4hFEqc9SjCwx43_CnpD8A"
}


# Define a function to print out a dictionary
def DictToPrint(dct):
    for key in dct:
        print(key, " : ", dct[key])


# To check key,value pair in the dictionary
def favSong(key, val):
    if key in FavSong and FavSong[key] == val:
        print("+" * 88)
        print(f"Bravoooooooo!!! Now check informations about {FavSong['EnglishName']} song by {FavSong['Artist']}")
        print("+" * 88)
        DictToPrint(FavSong)
        return True
    else:
        print("-" * 88)
        print("OOOOOOPS!!! but don\'t worry,", f"Now check informations about {FavSong['EnglishName']} song by {FavSong['Artist']} ")
        print("-" * 88)
        DictToPrint(FavSong)
        return False


# check input
try:
    SongKey = input("Please enter the key: ")
    SongKey = int(SongKey)
except ValueError:
    pass


# check input
try:
    SongVal = input(f"Please enter {SongKey} Value : ")
    SongVal = int(SongVal)
except ValueError:
    pass

# call function
favSong(SongKey, SongVal)
