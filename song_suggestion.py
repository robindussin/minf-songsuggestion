import tkinter as tk
from tkinter import filedialog


amuse_path = '/home/robin/AMUSE/amuse/'
amuse_workspace = '/home/robin/amuse_workspace/'
proc_features_path = amuse_workspace + 'Processed_Features/'

user_song_vector = []

processed_feature_suffix = ''

setup_gui()

def open_file_dialog():
	file_path = filedialog.askopenfilename()
	path_entry.delete(0, tk.END)
	path_entry.insert(tk.END, file_path)
	
	

def start():
	user_song_path = path_entry.get()
	user_song_vector = process_user_song(user_song_path)
	all_distances = compare_all_songs()
	
	pass
	
	
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

	
def setup_gui():
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




