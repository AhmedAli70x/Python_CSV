

#display movies list
def view_movies(mylist):
    for movie in mylist:  
        name = movie[1]
        duration = movie[2]
        year = movie[3]
        genre = movie[4]
        director = movie[5]
        actors = movie[6]
        country = movie[7]
        print(f"Movie Name: {name}")
        print(f"Movie Duration: {duration}")
        print(f"Production Year: {year}")
        print(f"Movie Duration: {genre}")
        print(f"Movie director: {director}")
        print(f"Movie actors: {actors}")
        print(f"Movie Country: {country}")
        print()

def no_movie_detail():
    print("No movies with this id available to display")

def no_movie_year():
    print("No movies at this year available to display")

def no_movie_actor():
    print("No movies for this actor available to display")
    
def no_movie_country():
    print("No top movies in this country available to display")
    
#Function to display to get the file name from user
def open_CSV_file():
    
    file_path= input("Please enter the file path or file name: ")
    print("-----------------")
    return file_path

#Function to display basic information about the CSV file
def basic_information(info, db_name):
    number_of_records = len(list(info))
    print(f"Welcom to {db_name}")
    print(f"The loaded number of records is {number_of_records}")

#Function to display options for the user
def user_option():
    option = int(input("""
    Pleas enter one of the following options:
    -----------------------------------------

    1. Retrieve the details for a specific movie
    2. Retrieve the details for movies released in a specific year
    3. Retrieve the details for movies that star a particular actor
    4. Retrieve the top movies by rating for a specific country
    5. Pie chart for the movies rating.
    6. Exit the program
    """))
    return option


def movie_id():
    while True:
        try: 
            movie_id = int(input("Please Enter the movie id: "))
            return movie_id
        except:
            print("Invalid movie id, try again")

def year_movie():
    while True:
        try:
            movie_year = int(input("Please Enter the production year: "))
            
            return movie_year
        except:
            print("Invalid input. Try again")


def movie_actor():
    actor = input("Enter the actor name: ")
    actor = actor.strip(" ")  # remove additional spaces
    return actor

def movie_country():
    country = input("Please Enter the country movie: ")
    country = country.strip(" ") # remove additional spaces
    return country


if __name__ == "manin":
    open_CSV_file()