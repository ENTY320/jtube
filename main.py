from pytube import Playlist
import os
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

def download_audio_playlist(url):
    playlist = Playlist(url)


    output_path = os.getcwd()

    for video in playlist.videos:
        try:
            #print(f"Downloading audio from {video.title}...")
            audio_stream = video.streams.filter(only_audio=True).first()

            if audio_stream:
                audio_stream.download(output_path)
                # Rename the downloaded file to match the video title with '.mp3' extension
                original_filename = audio_stream.default_filename
                new_filename = f"{video.title}.mp3"
                os.rename(os.path.join(output_path, original_filename), os.path.join(output_path, new_filename))
                #print(f"Audio from {video.title} downloaded successfully as {new_filename}!")
            else:
                #print(f"No audio stream found for {video.title}.")
                pass
        except:
            pass


kivy.require("1.9.0")

class jtube(App):
    def build(self):
        return BoxLayout()
    def text(self):
        print(f"ok")

    def dw(self):
        texts = self.root.ids.link.text
        print(f"button ok {texts}")


jtube = jtube()
jtube.run()
   # download_audio_playlist(playlist_url)