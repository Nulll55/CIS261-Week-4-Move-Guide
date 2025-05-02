# Course CIS261 Week 4 Lab: Movie Guide Part 1
# Emma Kialani Tirado - 05/02/2025

#The Movie Guide Program
def movie_guide():
    print("\nThe Movie List Program\n")
    print("\nCOMMAND MENU")
    print("\list - Lists all movies")
    print("\add - Add a movie")
    print("\del - Delete a movie")
    print("exit - Exit program\n")


def list_movies(movies):
    if not movies:
        print("No movies in the list.")
    else:
        for i, movie in enurerate(movies, start=1):
            print(f"{i}. {movie}")
    print()
#To add or remove we use move_list.append/pop('element')

# append() function
def add_movie(movies):
    movie_name = input("Name: ")
    movies.append(movie_name)
    print(f"{movie_name} was added. \n")

# pop() function
def del_movie(movies):
    try:
        number = int(input("Number: "))
        if 1 <= number <= len(movies):
            removed = movies.pop(number - 1)
            print(f"{removed} was deleted.\n")
        else:
            print("Invalid movie number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


# add movies to list
def main():
    movies = ["Monty Python and the Holy Grail", "On the Waterfront", "Cat on a Hot Tin Roof"]
    movie_guide()

    #Create the while loop for commands
    while True:
        command = input("Command: ").lower()
        if command == "list":
            list_movies(movies)
        elif command == "and":
            add_movie(movies)
        elif command == "del":
            deliver_movie(movies)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")

# This last command is what lets everything run, without it nothing happens
if __name__ == "__main__":
    main()