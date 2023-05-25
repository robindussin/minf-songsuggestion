from scipy.io import arff
import numpy as np

path = '/home/robin/amuse_workspace/Processed_Features/Genres-Datensatz-15s/'
file1 = 'Blues/Ageing_hippie_groove_syndicate-Blues_for_Ben/Ageing_hippie_groove_syndicate-Blues_for_Ben_1-9-8[true_false_false]__0[true_true]__15000ms_2500ms_WS15000.arff'
file2 = 'Blues/Alan_Fox_and_The_Shooters_Band-Your_Fault/Alan_Fox_and_The_Shooters_Band-Your_Fault_1-9-8[true_false_false]__0[true_true]__15000ms_2500ms_WS15000.arff'

file3 = 'Jazz/Ann_Alee-Infant_Holy_Infant_Lowly/Ann_Alee-Infant_Holy_Infant_Lowly_1-9-8[true_false_false]__0[true_true]__15000ms_2500ms_WS15000.arff'

data1, meta1 = arff.loadarff(path + file1)
data2, meta2 = arff.loadarff(path + file2)
data3, meta3 = arff.loadarff(path + file3)


data1 = list(data1[0])[:-3]
data2 = list(data2[0])[:-3]
data3 = list(data3[0])[:-3]

vec1 = np.array(data1)
vec2 = np.array(data2)
vec3 = np.array(data3)

distanceBlues = np.linalg.norm(vec1 - vec2)
distanceJazz1 = np.linalg.norm(vec1 - vec3)
distanceJazz2 = np.linalg.norm(vec2 - vec3)

print("distance of blues1 - blues2: " + str(distanceBlues))
print("distance of blues1 - jazz: " + str(distanceJazz1))
print("distance of blues2 - jazz: " + str(distanceJazz2))









