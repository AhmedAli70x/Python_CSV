import csv

import  user_interface  
import process
import csv_visual

def data_loading(file_dir = None):
    while True:
        try:
            if not file_dir:
                path = user_interface.open_CSV_file()
            else:
                path = file_dir
            with open(path, encoding="utf-8") as file:
                    read_csv = csv.reader(file)
                    header = next(read_csv)
                    csv_list = list(read_csv)
                    user_interface.basic_information(csv_list, path)
                    return csv_list
        except:
            print("No file with this name, try again")
            
def run_csv():   
    try:
        csv_data =  data_loading()
        while csv_data:
            selected_option = 0
            while selected_option is not True:
                try:
                    selected_option = user_interface.user_option()
                    if 7 > selected_option > 0:
                        break
                except:
                    print("Sorry, not avalid number. Try again! ")
            if selected_option == 1:
                movie_id = user_interface.movie_id()
                movie_detail = process.movie_details(csv_data, movie_id)
                if movie_detail:
                    user_interface.view_movies(movie_detail)
                else:
                    user_interface.no_movie_detail()

            elif selected_option == 2:
                input_year = user_interface.year_movie()
                year_movies = process.movie_specif_year(csv_data, input_year)
                if year_movies:
                    user_interface.view_movies(year_movies)
                else:
                    user_interface.no_movie_year()

            # elif selected_option == 3:
            #     input_actor = user_interface.movie_actor()
            #     actor_movies = process.movie_star_actor(csv_data, input_actor)
            #     if actor_movies:
            #         user_interface.view_movies(actor_movies)
            #     else:
            #         user_interface.no_movie_actor()

            # elif selected_option == 4:
            #     input_country = user_interface.movie_country()
            #     top_rated_movies = process.top_movies(csv_data, input_country)
            #     if top_rated_movies:
            #         user_interface.view_movies(top_rated_movies)
            #     else:
            #         user_interface.no_movie_country()

            # elif selected_option == 5:
            #     csv_visual.csv_visualise(csv_data)
            #     pass

            # elif selected_option == 6:
            #     quit()

    except SyntaxError:
        print("No file with this name")
   

if __name__ == "__main__":
    run_csv()
 


