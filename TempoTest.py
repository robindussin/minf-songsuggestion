import librosa

# Pfad zur Audiodatei des Songs
audio_path = 'C:/Studium/Fachprojekt/2.Teilprojekt/Musik/Ageing_hippie_groove_syndicate-Blues_for_Ben.wav'

# Laden der Audiodatei
audio_data, sr1 = librosa.load(audio_path)

# Extrahieren des Tempo des Songs
tempo, beat_frames = librosa.beat.beat_track(y=audio_data, sr=sr1, hop_length=512)

# Ausgabe des Tempos
print("Tempo:", tempo)
