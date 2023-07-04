import tkinter as tk
from tkinter import filedialog
import os
from scipy.io import arff
import subprocess
import shutil
import numpy as np
from gui import App
import customtkinter
from PIL import Image
import time
from threading import Thread


amuse_workspace = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/'
amuse_proc_features_path = amuse_workspace + 'Processed_Features'


def start_amuse():
        subprocess.call(['sh', './amuseStartLoop.sh'])

# ------------------- Hilfsfunktionen ------------------- #

# Gibt einfach nur Dateinamen/letzten Teil des Pfades zurück
def get_song_name(filename):
	return os.path.split(filename)[1]

# Gibt Genre eines Songs aus Datenbank zurück (anhand der Ordnerstruktur)
def get_genre(filename):
        return os.path.split(os.path.split(os.path.split(filename)[0])[0])[1]

# Gibt Pfad der Processing-Datei des User-Songs zurück
def get_processing_path():
        music_path = '/Scratch/Musikinformatik/'
        user_path = user_song_path
        if user_song_path.startswith(music_path):
                user_path = '/' + user_path     [len(music_path):]
        print(user_path)
        print(amuse_proc_features_path + user_path[:-4] + '/' + get_song_name(user_path)[:-4] + processing_suffix_user)
        return amuse_proc_features_path + user_path[:-4] + '/' + get_song_name(user_path)[:-4] + processing_suffix_user

# Gibt zurück, ob Processing-Datei des User-Songs existiert
def user_proc_done():
        return os.path.exists(get_processing_path())


# Starte User-Song-Verarbeitung, Vergleich der Songs und Darstellung der Ergebnisse
def start(song_path, app):
        global app_ref
        app_ref = app
        
        global processing_suffix
        global processing_suffix_user
        processing_suffix = '_1-9__0[true_true]__-1ms_-1ms_proc08.arff'
        processing_suffix_user = '_1-9__0[true_true]__-1ms_-1ms_proc08.arff'

        global user_song_path
        user_song_path = song_path
        # Falls User-Song-Pfad nicht existiert
        if user_song_path == '' or not os.path.exists(user_song_path):
                tk.messagebox.showwarning('Ungültiger Pfad', message='Es wurde keine Datei angegeben oder die angegebene Datei existiert nicht...')
                return

        # Welche Elemente der Feature-Vektoren/welche Songfenster sollen verglichen werden?
        array_elements = [0] # Bei Fenstergröße -1 beinhaltet das Array nur ein Array (bei mehreren Fenstern dann entsprechend auswählen)
        
        # User-Song processen - irrelevante Fenster löschen (user_song_vector enthält nicht mehr die drei letzten Elemente)
        user_song_vector = process_user_song(array_elements)
        
        # Distanz des user_songs zu allen anderen Songs berechnen
        all_distances = compare_all_songs(user_song_vector, array_elements)

        display_result(all_distances)


# Processe user_song und gebe Feature-Vektor zurück
def process_user_song(array_elements):
	# Vergleichs-Song Features extrahieren
        templates = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/arff_templates/'
        tasks = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/tasks_dir/'
        infos = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/arff_infos/'

        extraction_list = []
        
        # Lösche letzte Zeile der FileList, damit diese durch User-Song-Pfad ersetzt werden kann
        extraction_file_list = open(infos + 'FileList.arff', 'r')
        extraction_list = extraction_file_list.readlines()[:-1]
        extraction_file_list.close()
        
        extraction_list.append('1, \'' + user_song_path + '\'')
        
        extraction_file_list = open(infos + 'FileList.arff', 'w')
        for line in extraction_list:
                extraction_file_list.write(line)
        extraction_file_list.close()
        

        # Falls Processing-File schon existiert, muss Amuse garnicht gestartet werden
        new_processing = False
        if not user_proc_done():
                new_processing = True
                thread = Thread(target = start_amuse)
                thread.start()
                print("Started Amuse")
                
                shutil.copyfile(templates + 'taskExtraction', tasks + 'taskExtraction')
                shutil.copyfile(templates + 'taskProcessing', tasks + 'taskProcessing')
        
        while(not user_proc_done()):
                time.sleep(3)

        # Falls Amuse nicht gestartet wurde, muss es auch nicht beendet werden
        if new_processing:
                shutil.copyfile('/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/stop_loop', tasks + 'stop_loop')
		
        user_proc, meta = arff.loadarff(get_processing_path())
        # user_proc = array([(x1, y1, z1, 'milliseconds', 0, <firstwindowend>), ..., (xn, yn, zn, 'milliseconds', <lastwindowstart>, <lastwindowend>)], types)
        print(user_proc)
        return raw_arff_to_vector(user_proc, array_elements)


# Gebe Liste von Tupeln (Song-Pfad, Distanz) zurück
# z.B. [("Jazz/xyz.wav", 0.35), ("Blues/abc.wav", 0.2)]
# Song-Vektoren liegen alle als NumPy-Arrays vor (die letzten 3 "unnötigen" Zeilen sind schon entfernt)
def compare_all_songs(user_song, array_elements):
        # berechne Distanz für alle vorliegenden Songs
        song_names, song_data = load_processings(array_elements)	

        distances = []
        total_distances = 0
        for i in range(len(song_data)):
                distance = compare_song(user_song, song_data[i])
                total_distances += distance
                distances.append((song_names[i], distance))
        print("====================================================================================")
        print("Gesamtdistanzen: " + str(total_distances))
        print("====================================================================================")
        distances = sorted(distances, key = lambda tup: tup[1])
        return distances


# Gebe Distanz zwischen song1 und song2 zurück (song1 und song2 sind jeweils noch "vollständige" Vektoren)
# hier kann noch Auswahl bestimmter Fenster o.Ä. vorgenommen werden (die letzten 3 "unnötigen" Zeilen wurden schon entfernt)
def compare_song(song1, song2):
        # NumPy-Arrays können mit Arrays indiziert werden (z.B. arr[[1, 2, 3]]), um Indizes 1, 2, 3 zu erhalten
        return np.linalg.norm(song1 - song2)

# Lädt vorhandene Processings der Musik aus der "Datenbank" in Array
def load_processings(array_elements):
        path = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/Processed_Features/Genres-Datensatz-15s/'

        files = [] # enthält am Ende Pfade zu allen Processing-Files der verglichenen Songs
        for genre in os.listdir(path):
	        genre_path = os.path.join(path, genre)
	        for song_folder in os.listdir(genre_path):
                        song_path = os.path.join(genre_path, song_folder, song_folder + processing_suffix)
                        if os.path.exists(song_path):
                                files.append(song_path)
        
        data = []
        for arff_file in files:
                processed_feature, meta = arff.loadarff(arff_file)
                processed_feature = raw_arff_to_vector(processed_feature, array_elements)
                data.append(processed_feature)
	        
        return (files, data)

# Behalte nur die gewünschten Songfenster und Array aus Arrays flatten
def raw_arff_to_vector(raw_content, array_elements):
        # tolist entfernt den letzten ndtype-Teil
        raw_content = raw_content.tolist()
        # entferne die letzten drei Werte aus jedem Tupel
        raw_content = [tup[:-3] for tup in raw_content]
        # ich will aber immernoch mit Array indizieren können
        raw_content = np.array(raw_content) 
        # user_proc ist jetzt Array aus Arrays; jedes innere Array ist ein Songfenster
        raw_content = raw_content[array_elements]
        # Arrays aus Arrays flatten, damit wir nur noch einen Vektor haben
        raw_content = raw_content.flatten()
        
        return raw_content

# Ergebnisse in GUI darstellen
def display_result(result_list):
        music_path = '/Scratch/Musikinformatik/Genres-Datensatz-15s/'
        song_paths = []
        song_names = []
        interprets = []
        genres = []
        distances = []
        for distance in result_list:
                song_path = os.path.split(distance[0])[0]
                rest, song_name = os.path.split(song_path)
                genre_name = os.path.split(rest)[1]
                full_path = os.path.join(music_path, genre_name, song_name + ".wav")
                # print(distance[0], ':', distance[1])
                # print(full_path)
                song_paths.append(full_path)
                if len(song_name.split('-')) > 1:
                        song_names.append(song_name.split('-')[1])
                        interprets.append(song_name.split('-')[0])
                else:
                        song_names.append(song_name)
                        interprets.append(song_name)
                genres.append(genre_name)
                distances.append(distance[1])
                
        result_file = open('/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/results/' + str(time.time()), 'w')
        result_file.write(processing_suffix + ' ' + user_song_path + '\n')
        for path in song_paths:
                result_file.write(path + '\n')
        result_file.close()
        
        list_size = 50
        result_dict = {'song_paths': song_paths[:list_size], 'song_names': song_names[:list_size], 'interprets': interprets[:list_size], 'genres': genres[:list_size], 'distances': distances[:list_size]}
        app_ref.load_songs_from_playlist(result_dict)
