# FREE PUNJABI VDEO DOWNLOADER NO VIRUS
# START DAY 1/30/2024
# --------------------------------------------
# TODO: priority order
# audio downloader DONE
# goof way to bundle ffmpeg
# switch formats
# size of pyinstaller .exe (not much i can do)
# progress bar
# playlists
#-------------------------------------------
from os import path, walk
from yt_dlp import YoutubeDL, utils
import PySimpleGUI as sg
# from dataclasses import dataclass
# from datetime import timedelta
# from typing import Optional


def find_files(filename, search_path):
    result = []

# Walking top-down from the root
    for root, dir, files in walk(search_path):
        if filename in files:
            result.append(path.join(root, filename))
        return result


prog_loc = path.dirname(path.abspath(__file__))
ffm_loc = find_files('ffmpeg.exe', prog_loc)
print(ffm_loc)
print(path.realpath(ffm_loc[0]))


class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


# @dataclass
# class YTProgress:
#     """
#     The youtube_dl progress hook's information dictionary is weakly-typed. This
#     represents it as a convenience dataclass.
#     """
#
#     status: str
#     total_bytes: int
#     filename: str
#     downloaded_bytes: Optional[int] = None
#     elapsed: Optional[float] = None
#     tmpfilename: Optional[str] = None
#     eta: Optional[int] = None
#     speed: Optional[float] = None
#
#     @property
#     def is_finished(self) -> bool:
#         return self.status == 'finished'
#
#     @property
#     def elapsed_delta(self) -> timedelta:
#         return timedelta(seconds=round(self.elapsed))
#
#     @property
#     def eta_delta(self) -> timedelta:
#         return self.elapsed_delta + timedelta(seconds=self.eta)
#
#     def __str__(self):
#         if self.is_finished:
#             # Many of the members will be None if we're finished, so just
#             # return the status.
#             return self.status


vid_opt = {
    'format': 'mp4',
    'logger': MyLogger()
}
aud_opt = {
    'format': 'm4a/bestaudio/best',
    'logger': MyLogger(),
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'ffmpeg_location': ffm_loc[0],
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }]
}
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Rohans Super awesome video downloader')],
            [sg.Text('Youtube URL'), sg.InputText()],
            [sg.Button('Video'), sg.Button('Audio'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, URLS_dict = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    URLS = URLS_dict[0]
    if event == 'Video':
        with YoutubeDL(vid_opt) as yt:
            try:
                yt.download(URLS)
                sg.popup('Done!')
            except utils.DownloadError:
                sg.popup('Enter a youtube url')
    if event == 'Audio':
        with YoutubeDL(aud_opt) as yt:
            try:
                yt.download(URLS)
                sg.popup('Done!')
            except utils.DownloadError:
                sg.popup('Enter a youtube url')


window.close()

