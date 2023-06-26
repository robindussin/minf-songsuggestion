import json
import sys

path = './arff_infos/Features.arff'

f = open('./allFeatures.arff', 'r')
data = f.read()
f.close()
as_dict = json.loads(data)

f = open(path, 'w')
meta = """@RELATION FeatureTable

@ATTRIBUTE 'Id' STRING
@ATTRIBUTE 'Description' STRING
@ATTRIBUTE 'ExtractorId' NUMERIC
@ATTRIBUTE 'WindowSize' NUMERIC
@ATTRIBUTE 'StepSize' NUMERIC
@ATTRIBUTE 'Dimensions' NUMERIC
@ATTRIBUTE 'FeatureType' {'WindowedNumeric'}

@DATA
"""
f.write(meta)
for feature in sys.argv[1:]:
    f.write(as_dict[feature] + '\n')

f.close()
    
