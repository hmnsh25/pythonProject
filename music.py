import numpy as np
import tensorflow as tf
import moviepy
from moviepy.editor import AudioFileClip
import pygame
import pygame.sndarray as sndarray

# Define the genres and their corresponding indices
genres = ['pop', 'rock', 'jazz', 'electronic']
genre_indices = {genre: i for i, genre in enumerate(genres)}

# Load pre-trained model weights
model = tf.keras.models.load_model('music_generator_model.h5')

def generate_music(genre, duration=30):
    # Validate the requested genre
    if genre not in genres:
        return "Invalid genre. Please choose from: " + ", ".join(genres)

    # Generate random input for the model
    random_input = np.random.rand(1, duration, len(genres))
    genre_index = genre_indices[genre]
    random_input[:, :, genre_index] = 1.0

    # Generate music using the model
    generated_music = model.predict(random_input)[0]

    return generated_music

def save_as_mp4(music_array, filename):
    # Convert the music array to a WAV file
    pygame.mixer.init(channels=1, frequency=44100, size=-16)
    sound = sndarray.make_sound((music_array * (2**15 - 1)).astype(np.int16))
    sound.export(filename, format='wav')

    # Load the WAV file using moviepy
    audio_clip = AudioFileClip(filename)

    # Create a blank video clip with the same duration as the audio
    video_clip = moviepy.VideoClip(lambda t: [0, 0, 0], duration=audio_clip.duration)

    # Set the audio of the video clip to the generated music
    video_clip = video_clip.set_audio(audio_clip)

    # Write the video clip to an mp4 file
    video_clip.write_videofile(filename[:-4] + '.mp4', codec='libx264')

# Usage example
requested_genre = 'pop'
generated_music = generate_music(requested_genre)
save_as_mp4(generated_music, 'generated_music')
