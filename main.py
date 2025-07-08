import datetime as dt
from spotify_config import Spotify
from billboard import BillBoard
# #-----------Date Validator-------------#
def input_date():
    date_today = dt.datetime.now()
    user_input = input("Enter the particular date you want the playlist of (YYYY-MM-DD) : ")
    try :
        user_date_object = dt.datetime.strptime(user_input,"%Y-%m-%d")
    except:
        print("Wrong date or format added.")
        input_date()
    else:
        if date_today.date() >= user_date_object.date():
            return user_date_object.strftime("%Y-%m-%d")
        else:
            print("You can't a date in future!!")
            input_date()
date = input_date()
#
billboard = BillBoard()
spotify = Spotify()
songs_title_list = billboard.fetch_songs(date)
print(songs_title_list)
spotify.create_playlist(date)
songs = spotify.search_songs(songs_title_list)
spotify.add_songs(songs)

