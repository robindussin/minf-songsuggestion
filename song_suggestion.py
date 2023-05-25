import tkinter as tk
from tkinter import filedialog
import os
from scipy.io import arff
import subprocess


amuse_path = '/home/robin/AMUSE/amuse/'
amuse_workspace = '/home/robin/amuse_workspace/'
proc_features_path = amuse_workspace + 'Processed_Features/'

user_song_vector = []

processed_feature_suffix = ''


def open_file_dialog():
	file_path = filedialog.askopenfilename()
	path_entry.delete(0, tk.END)
	path_entry.insert(tk.END, file_path)
	
	

def start():
	# user_song processen
	user_song_path = path_entry.get()
	if user_song_path == '' or not os.path.exists(user_song_path):
		tk.messagebox.showwarning('Ungültiger Pfad', message='Es wurde keine Datei angegeben oder die angegebene Datei existiert nicht...')
		return
	user_song_vector = process_user_song(user_song_path)
	
	# Distanz des user_songs zu allen anderen Songs berechnen
	all_distances = compare_all_songs()
	
	display_results(all_distances)
	
	
# Processe user_song und gebe Feature-Vektor zurück
def process_user_song():
	# Vergleichs-Song Features extrahieren
	
	# Vergleichs-Song Features processen
	pass
	
	
# Gebe Liste von Tupeln (Song-Pfad, Distanz) zurück
# z.B. [("Jazz/xyz.wav", 0.35), ("Blues/abc.wav", 0.2)]
def compare_all_songs():
	# berechne Distanz für alle vorliegenden Songs
	
	# sortiere Liste nach Distanzen
	pass
	
	
# Gebe Distanz zwischen Song in path und user_song zurück
def compare_song(path):
	pass
	
	
def display_result(result_list):
	pass

	
	
# GUI Setup
root = tk.Tk(className="Song Suggestions")
root.geometry("600x400")

select_song_button = tk.Button(root, text="Select a song you like", command=open_file_dialog)
select_song_button.pack()

path_entry = tk.Entry(root)
path_entry.pack()

button_start = tk.Button(root, text="Start", command=start)
button_start.pack()

listbox = tk.Listbox(root)
listbox.pack()

root.mainloop()


subprocess.call(['sh', './amuseStartLoop.sh'])

