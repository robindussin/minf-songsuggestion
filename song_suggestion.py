import tkinter as tk
from tkinter import filedialog
import os
from scipy.io import arff
import subprocess
import shutil
import numpy as np


amuse_path = '/home/robin/AMUSE/amuse/'
amuse_workspace = '/home/robin/amuse_workspace/'
proc_features_path = amuse_workspace + 'Processed_Features/'

user_song_vector = []

processed_feature_suffix = ''

	
def start(song_path):

        global processing_suffix
        processing_suffix = '_1-9__0[true_true]__-1ms_-1ms_songsuggestion_processing.arff'

        # user_song processen
        global user_song_path
        user_song_path = song_path
        if user_song_path == '' or not os.path.exists(user_song_path):
                tk.messagebox.showwarning('Ungültiger Pfad', message='Es wurde keine Datei angegeben oder die angegebene Datei existiert nicht...')
                return
        user_song_vector = process_user_song()

        # Distanz des user_songs zu allen anderen Songs berechnen
        all_distances = compare_all_songs(user_song_vector)

        display_result(all_distances)
	
	
def get_song_name(filename):
	path, filename = os.path.split(filename)
	filename = filename[:-len(processing_suffix)]
	return filename

def get_song_name_ignore_suffix(filename):
	return os.path.split(filename)[1]
 
def get_genre(filename):
        return os.path.split(os.path.split(os.path.split(filename)[0])[0])[1]
	
# Processe user_song und gebe Feature-Vektor zurück
def process_user_song():
	# Vergleichs-Song Features extrahieren
        templates = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/arff_templates/'
        tasks = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/tasks_dir/'
        infos = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/minf-songsuggestion/arff_infos/'
        
        extraction_list = []
        extraction_file_list = open(infos + 'ExtractionTestFile.arff', 'r')
        extraction_list = extraction_file_list.readlines()[:-1]
        extraction_list.append('1, \'' + user_song_path + '\'')
        extraction_file_list.close()
        
        extraction_file_list = open(infos + 'ExtractionTestFile.arff', 'w')
        for line in extraction_list:
                extraction_file_list.write(line)
        extraction_file_list.close()
        
        processing_file_list = open(infos + 'ProcessingTestFile.arff', 'r')
        processing_list = processing_file_list.readlines()[:-1]
        processing_list.append('1, \'' + user_song_path + '\'')
        processing_file_list.close()
        
        processing_file_list = open(infos + 'ProcessingTestFile.arff', 'w')
        for line in processing_list:
                processing_file_list.write(line)
        processing_file_list.close()
        
        shutil.copyfile(templates + 'taskExtraction', tasks + 'taskExtraction')
        shutil.copyfile(templates + 'taskProcessing', tasks + 'taskProcessing')
        
        subprocess.call(['sh', './amuseStartLoop.sh'])
	
        user_proc, meta = arff.loadarff('/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/Processed_Features' + user_song_path[:-4] + '/' + get_song_name_ignore_suffix(user_song_path)[:-4] + processing_suffix)
        user_proc = np.array(list(user_proc[0])[:-3])
	
        return user_proc
	
	
# Gebe Liste von Tupeln (Song-Pfad, Distanz) zurück
# z.B. [("Jazz/xyz.wav", 0.35), ("Blues/abc.wav", 0.2)]
def compare_all_songs(user_song):
        # berechne Distanz für alle vorliegenden Songs
        song_names, song_data = load_processings()	

        distances = []

        for i in range(len(song_data)):
                distanceEuklid = np.linalg.norm(user_song - song_data[i])
                distances.append((get_genre(song_names[i]), get_song_name(song_names[i]), distanceEuklid))
        
        distances = sorted(distances, key = lambda tup: tup[2])
        return distances

def load_processings():
        	
        path = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/Processed_Features/Genres-Datensatz-15s/'

        files = []
        for genre in os.listdir(path):
	        genre_path = os.path.join(path, genre)
	        for song_folder in os.listdir(genre_path):
                        song_path = os.path.join(genre_path, song_folder, song_folder + processing_suffix)
                        if os.path.exists(song_path):
                                files.append(song_path)

        data = []
        for arff_file in files:
                processed_feature, meta = arff.loadarff(arff_file)
                processed_feature = np.array(list(processed_feature[0])[:-3])
                data.append(processed_feature)
	        
        return (files, data)

# Gebe Distanz zwischen Song in path und user_song zurück
def compare_song(path):
	pass


def display_result(result_list):
        for distance in result_list:
                print(distance[0], '-', distance[1], ':', str(distance[2]))


def generate_task_files():
	pass


