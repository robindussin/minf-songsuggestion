import librosa

# Pfad zur Audiodatei des Songs
audio_path = 'C:/Studium/Fachprojekt/2.Teilprojekt/Musik/Ageing_hippie_groove_syndicate-Blues_for_Ben.wav'

# Laden der Audiodatei
audio_data, sr = librosa.load(audio_path)

# Extrahieren der musikalischen Merkmale des Songs
features = librosa.feature.chroma_stft(y=audio_data, sr=sr)

# Berechnen des Durchschnitts der Merkmale über die Zeit
mean_features = features.mean(axis=1)

# Berechnen der Stimmung
valence = mean_features.mean()

# Ausgabe der Stimmung des Songs
print("Valenz (Stimmung):", valence)
