# Filename: Movie Dictionary.py
# Author: Gracy Changirala
# Email address: GChangirala_GPS@nec.edu
# Description: Program that manages a dictionary of movies with their leading actors, allowing users to view, update, and search for movies and their corresponding stars.
# Last changed: 12-02-2024

# Program that manages a dictionary of movies with their leading actors, allowing users to view, update, and search for movies and their corresponding stars.

# Create a dictionary of movie names (the key) and the leading actor
movies_dict = {
    "Hi Nanna": "Nani",
    "Guntur Karam": "Mahesh Babu",
    "Eagle": "Ravi Teja",
    "Pindam": "Sriram",
    "Yatra": "Mammootty"
}

# Print the dictionary
print("Dictionary of movies and leading actors:")
print(movies_dict)

# Loop through printing key/value pairs
print("\nLooping through key/value pairs:")
for movie, actor in movies_dict.items():
    # Print each movie along with its leading actor
    print(f"Movie: {movie}, Actor: {actor}")

# Add a new entry
movies_dict["Baahubali"] = "Prabhas"

# Reprint
print("\nUpdated dictionary:")
print(movies_dict)

# Find a star by selecting the movie
selected_movie = input("Enter the movie name to find its leading actor: ")
if selected_movie in movies_dict:
    # If the movie is found in the dictionary, print its leading actor
    print(f"The leading actor in {selected_movie} is {movies_dict[selected_movie]}")
else:
    # If the movie is not found in the dictionary, inform the user
    print("Movie not found in the dictionary.")

# Description:
# The program starts by creating a dictionary named movies_dict where the keys are movie names and the values are the leading actors.
# It then prints out the dictionary to display all the movies and their leading actors.
# Next, it iterates over the dictionary using a for loop to print each movie name along with its leading actor.
# After that, it adds a new entry to the dictionary for the movie "Baahubali" with the leading actor Prabhas.
# It prints out the updated dictionary to show the addition of the new movie.
# Finally, it prompts the user to enter a movie name and then checks if the entered movie exists in the dictionary. If found, it prints out the leading actor for that movie; otherwise, it informs the user that the movie was not found in the dictionary.