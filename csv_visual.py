import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation





def movie_rates(csv_movies):
    low_rating = []
    high_rating = []
    avg_rating  = []
    rate = 0
    for movie in csv_movies:
        rate = float(movie[8])
        # print(rate)
        if rate <= 3.0: 
            low_rating.append(rate)
        elif rate >= 7.0:
            high_rating.append(rate)
        else:
            avg_rating.append(rate)

    return [low_rating, avg_rating, high_rating]


def pie_anime(frames):
    
    
    labels = 'Low rating', 'Average Rating', 'High rating'
    colors = ['blue', 'cyan', 'red']
    ax1.axis('equal')
    low = 0
    avg = 0
    high = 0
    explode = (0, 0, 0.1)
    rating = movie_rates(movies)
    low += rating[0][frames]
    avg += rating[1][frames]
    high += rating[2][frames]
    rating_vis = [low, avg, high]

    ax1.pie(rating_vis, explode= explode, labels=labels, autopct='%1.1f%%', colors= colors, shadow=False, startangle=90)
    plt.gca()
    # plt.pause(100)
    # ax1.clear()

def csv_visualise(csv_movies):
    global movies
    global fig1
    global rating
    global low ,avg ,high
    global ax1
    movies =  csv_movies
    fig1, ax1 = plt.subplots()
    ani = FuncAnimation(fig1, pie_anime, frames= 1, interval =0.1, repeat=False)
    plt.show() 


if __name__ == "manin":
    pass
