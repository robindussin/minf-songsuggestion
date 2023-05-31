from scipy.io import arff
import numpy as np
import os

def get_song_name(filename):
	path, filename = os.path.split(filename)
	filename = filename[:-len(processing_suffix)]
	return filename
	
	
path = '/home/fpss23/gruppe04/workspace_fachprojekt/amuse-workspace/Processed_Features/Genres-Datensatz/'
processing_suffix = '_1-9__0[true_true]__-1ms_-1ms_distanceTests04.arff'

files = []
for genre in os.listdir(path):
	genre_path = os.path.join(path, genre)
	for song_folder in os.listdir(genre_path):
		files.append(os.path.join(genre_path, song_folder, song_folder + processing_suffix))

for arff_file in files:
	assert os.path.exists(arff_file)

data = []
for arff_file in files:
	processed_feature, meta = arff.loadarff(arff_file)
	processed_feature = np.array(list(processed_feature[0])[:-3])
	data.append(processed_feature)

for index1, arff_file1 in enumerate(data):
	for index2, arff_file2 in enumerate(data):
		if index2 > index1:
			distanceEuklid = np.linalg.norm(arff_file1 - arff_file2)
			distanceManhatten = np.abs(arff_file1 - arff_file2).sum()
			distanceCosine = 1 - np.dot(arff_file1, arff_file2) / (np.linalg.norm(arff_file1) * np.linalg.norm(arff_file2))
			print(get_song_name(files[index1]), ' vs. ', get_song_name(files[index2]))
			print('\tEuklid:', str(distanceEuklid))
			print('\tManhatten:', str(distanceManhatten))
			print('\tCosinus:', str(distanceCosine))

"""
data1, meta1 = arff.loadarff(path + file1)
data2, meta2 = arff.loadarff(path + file2)
data3, meta3 = arff.loadarff(path + file3)


data1 = list(data1[0])[:-3]
data2 = list(data2[0])[:-3]
data3 = list(data3[0])[:-3]

vec1 = np.array(data1)
vec2 = np.array(data2)
vec3 = np.array(data3)

bluesJazz1 = np.linalg.norm(vec1 - vec2)
bluesJazz2 = np.linalg.norm(vec1 - vec3)
jazzJazz = np.linalg.norm(vec2 - vec3)

print("distance of Blues and Jazz1: " + str(bluesJazz1))
print("distance of Blues and Jazz2: " + str(bluesJazz2))
print("distance of Jazz1 and Jazz2: " + str(jazzJazz))


"""






