prompt = "\nEnter a movie you like: "
prompt += "\nEnter 'q' to end"

movies = ""

while movies != "q":
    movies = input(prompt)
    if movies != "q":
        print(f"\nlet me see if i can find {movies} for you")
