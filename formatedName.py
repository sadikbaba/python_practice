# Write a function called city_country() that takes in the name
# of a city and its country. The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value that’s returned.


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


city1 = city_country("santiago", "chile")
city2 = city_country("lagos", "nigeria")
city3 = city_country("tokyo", "japan")

print(city1)
print(city2)
print(city3,'\n')



# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the album information correctly.
# Add an optional parameter to make_album() that allows you to store the number of tracks on an album.
# If the calling line includes a value for the number of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.


def make_album(artist_name, album_title, num_tracks=None):
    album = {"artist_name": artist_name.title(), "album_title": album_title.title()}
    if num_tracks is not None:
        album["num_tracks"] = num_tracks
    return album


new_album1 = make_album("Adele", "25")
new_album2 = make_album("Ed Sheeran", "Divide", 12)

print(new_album1)
print(new_album2)

# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, num_tracks=None):
    album = {"artist_name": artist_name.title(), "album_title": album_title.title()}
    if num_tracks is not None:
        album["num_tracks"] = num_tracks
    return album    


while True:
    print("\nPlease enter the album's artist and title (or 'q' to quit):")
    artist = input("Artist: ")
    if artist.lower() == 'q':
        break
    title = input("Title: ")
    if title.lower() == 'q':
        break
    num_tracks_input = input("Number of tracks (optional): ")
    num_tracks = int(num_tracks_input) if num_tracks_input.isdigit() else None

    album_info = make_album(artist, title, num_tracks)
    print(album_info)