from __future__ import unicode_literals
import youtube_dl

# importing the module

################# download videos upto any quality ################
# from pytube import YouTube
# yt = YouTube('https://www.youtube.com/watch?v=wK4VPM-0ssU')
# yt.streams[-4].download()
# # for i in yt.streams:
# #     pprint.pprint(i)
# print('done')


################ download mp3 from YouTube ,, just pass in URL as argument#########################
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # filenames = sys.argv[1:]
        # print(filenames)
        ydl.download(['https://www.youtube.com/watch?v=WC5FdFlUcl0','https://www.youtube.com/watch?v=YnzgdBAKyJo'])