import os
import sys

def get_song_name_from_music_path(filename):
    path, filename = os.path.split(filename)
    filename = filename[:-4]
    return filename

def get_genre_name_from_music_path(filename):
    rest_path, _ = os.path.split(filename)
    genre = os.path.split(rest_path)[1]
    return genre

def read_result_file(path):
    f = open(path, 'r')
    lines = f.readlines()
    f.close()
    genre = lines[0].split()[0] # Genre muss erstes Wort in erster Zeile sein
    title = lines[0].split()[-1] # Name/Bezeichner des Songs als letztes in erster Zeile
    lines.pop(0)
    lines = list(map(get_genre_name_from_music_path, lines))

    evaluate(lines, genre, title)


g = {
    0: "PopRock",
    1: "Classical",
    2: "Jazz",
    3: "Blues",
    4: "Latin",
    5: "Country",
    6: "Electronic",
    7: "Rap",
    8: "Folk"
    }
orders = {  g[0]: [g[0], g[6], g[8], g[4], g[2], g[3], g[5], g[1], g[7]],
            g[1]: [g[1], g[2], g[6], g[8], g[3], g[4], g[0], g[7], g[5]],
            g[2]: [g[2], g[3], g[4], g[0], g[6], g[8], g[1], g[7], g[5]],
            g[3]: [g[3], g[2], g[0], g[6], g[5], g[8], g[7], g[4], g[1]],
            g[4]: [g[4], g[0], g[2], g[6], g[8], g[7], g[3], g[1], g[5]],
            g[5]: [g[5], g[8], g[0], g[3], g[2], g[4], g[7], g[6], g[1]],
            g[6]: [g[6], g[0], g[2], g[7], g[4], g[3], g[8], g[1], g[5]],
            g[7]: [g[7], g[0], g[6], g[2], g[4], g[3], g[5], g[8], g[1]],
            g[8]: [g[8], g[5], g[0], g[3], g[2], g[1], g[6], g[7], g[4]]
          }

songs_per_genre = 20
def evaluate(lines, genre, title):
    aggr_distances = 0
    relevant_order = orders[genre]
    for i in range(len(lines)):
        genre_index = relevant_order.index(lines[i])
        distance = 0
        if i < genre_index * songs_per_genre:
            distance = genre_index * songs_per_genre - i
        elif i > (genre_index + 1) * songs_per_genre:
            distance = i - (genre_index + 1) * songs_per_genre
        # falls Genre in gewünschtem Gebiet ist, bleibt Distanz bei 0
        aggr_distances += distance
        # print("i = " + str(i) + ": " + lines[i] + " has distance " + str(distance))
    print(title + " (" + genre + ")")
    print("Aggregierte Distanzen: " + str(aggr_distances))
        

read_result_file(sys.argv[1])
