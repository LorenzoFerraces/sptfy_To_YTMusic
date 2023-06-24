import spotipy
from spotipy.oauth2 import SpotifyClientCredentials 
from object_spotipy import aux_Spotipy as objsp
import time

#spotify app authentication
client_id = 'ID'
client_secret = "Secret" 

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager) 

#aux object init
aux = objsp('ID', "Secret", sp)

#spotify playlist url
# mejunje = "https://open.spotify.com/playlist/6DaFmf4BQVBRAonTp749vW?si=2b2c3e7b19af4357"


#writing txt's
txt_genres = open('genres.txt', 'w')
txt_dates = open('dates.txt', 'w')

    


if __name__ == '__main__':
    try:
        playlist = input("URL de la playlist: ")
        cantidad = int(input("Cantidad de canciones a contar: "))
        lista = aux.tracklist(playlist, cantidad)
        valores = lista.values()
    except:
        print("parametros incorrectos")
    results = aux.get_Playlist_Data(valores)
    txt_dates.write("name; artist; date" + '\n')
    txt_genres.write("name; artist; genre" + '\n')
    for num, result in enumerate(results):
        try:
            #descartar resultados erroneos
            if result[0] == 's':
                continue
            #quitar ";" de nombre de canciones
            song_name = result[0].replace(';',' ')
            artist = result[1]
            genres = result[2]
            release_date = result[3]
            txt_dates.write(song_name + '; ' + artist + '; ' +  release_date + '\n')
            for genre in genres:
                txt_genres.write(song_name + '; ' + artist + '; ' + str(genre) + '\n')
        except:
            print("write error with number " + str(num))

    
