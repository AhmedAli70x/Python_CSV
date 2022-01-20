
import csv


def movie_details(movies_list, movie_id):
    specific_movie = []
    for movie in movies_list:
        if int(movie[0]) == movie_id:
            specific_movie.append(movie)
    return(specific_movie)           
        

def movie_specif_year(movies_list, movie_year):
    year_movies = []
    for movie in movies_list:
        if movie_year == int(movie[3]):
            # print(movie[3])
            year_movies.append(movie)
    return year_movies
       

def movie_star_actor(movies_list, actor_name):
    movie_actor_list = []
    for movie in movies_list:
        actors = movie[6].split(", ")
        #make a list of movies for the this actor
        if actor_name in actors:
            movie_actor_list.append(movie)
    return(movie_actor_list) #Retunr movies for this actor

def top_movies(movies_list, moview_country):
    top_five = []
    top_rate = 0 
    
    for movie in movies_list:
        #compare country names in lowecase
        if moview_country.lower() ==  movie[7].lower():
            top_csv = float(movie[8])
            if top_csv > top_rate: 
                top_rate = top_csv
                if top_rate not in top_five:
                    top_five.append(movie) # append the top rated movie
            
    top_five = top_five[-3:]  # select the top 3 movies 
    return(top_five)  #return the top rated movies in the selected country
    


