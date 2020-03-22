from __future__ import unicode_literals
# import pandas as pd
import pprint
# # j=pd.read_json('response.json')
# d={"authenticationResultCode":"ValidCredentials","brandLogoUri":"http:\/\/dev.virtualearth.net\/Branding\/logo_powered_by.png","copyright":"Copyright © 2020 Microsoft and its suppliers. All rights reserved. This API cannot be accessed and the content and any results may not be used, reproduced or transmitted in any manner without express written permission from Microsoft Corporation.","resourceSets":[{"estimatedTotal":5,"resources":[{"__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1","bbox":[30.674499847109981,76.646701065443963,30.732440613095097,76.736523421860724],"name":"Mohali, India","point":{"type":"Point","coordinates":[30.703470230102539,76.691612243652344]},"address":{"adminDistrict":"PB","adminDistrict2":"Sahibzada Ajit Singh Nagar","countryRegion":"India","formattedAddress":"Mohali, India","locality":"Mohali"},"confidence":"High","entityType":"PopulatedPlace","geocodePoints":[{"type":"Point","coordinates":[30.703470230102539,76.691612243652344],"calculationMethod":"Rooftop","usageTypes":["Display"]}],"matchCodes":["Ambiguous"]},{"__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1","bbox":[30.661030151065059,76.675096303024546,30.718970917050175,76.7649061383817],"name":"Sahibzada Ajit Singh Nagar district","point":{"type":"Point","coordinates":[30.690000534057617,76.720001220703125]},"address":{"adminDistrict":"PB","adminDistrict2":"Sahibzada Ajit Singh Nagar district","countryRegion":"India","formattedAddress":"Sahibzada Ajit Singh Nagar district"},"confidence":"Low","entityType":"AdminDivision2","geocodePoints":[{"type":"Point","coordinates":[30.690000534057617,76.720001220703125],"calculationMethod":"Rooftop","usageTypes":["Display"]}],"matchCodes":["Ambiguous"]},{"__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1","bbox":[31.777267119465456,74.585158601087869,31.784992554606809,74.597275480943381],"name":"Mohali, India","point":{"type":"Point","coordinates":[31.781129837036133,74.591217041015625]},"address":{"adminDistrict":"PB","adminDistrict2":"Amritsar","countryRegion":"India","formattedAddress":"Mohali, India","locality":"Ajnala Sub-District"},"confidence":"Low","entityType":"Neighborhood","geocodePoints":[{"type":"Point","coordinates":[31.781129837036133,74.591217041015625],"calculationMethod":"Rooftop","usageTypes":["Display"]}],"matchCodes":["Ambiguous"]},{"__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1","bbox":[0.21346261363811167,15.450243174044267,0.27140337962322564,15.527498067410811],"name":"Mohali, Republic of the Congo","point":{"type":"Point","coordinates":[0.24243299663066864,15.488870620727539]},"address":{"countryRegion":"Republic of the Congo","formattedAddress":"Mohali, Republic of the Congo","locality":"Mohali"},"confidence":"Low","entityType":"PopulatedPlace","geocodePoints":[{"type":"Point","coordinates":[0.24243299663066864,15.488870620727539],"calculationMethod":"Rooftop","usageTypes":["Display"]}],"matchCodes":["Ambiguous"]},{"__type":"Location:http:\/\/schemas.microsoft.com\/search\/local\/ws\/rest\/v1","bbox":[21.977107665119753,75.98826631972679,21.984833100261106,75.999374061132585],"name":"Mohali, India","point":{"type":"Point","coordinates":[21.98097038269043,75.993820190429688]},"address":{"adminDistrict":"MP","adminDistrict2":"West Nimar","countryRegion":"India","formattedAddress":"Mohali, India","locality":"Bhikangaon"},"confidence":"Low","entityType":"Neighborhood","geocodePoints":[{"type":"Point","coordinates":[21.98097038269043,75.993820190429688],"calculationMethod":"Rooftop","usageTypes":["Display"]}],"matchCodes":["Ambiguous"]}]}],"statusCode":200,"statusDescription":"OK","traceId":"2855f95e2010496dbe012a23d87ce512|CO0000112B|0.0.0.1|Ref A: E48DD71DCDDB4BF1AE050A53688DEF79 Ref B: CO1EDGE1020 Ref C: 2020-03-20T18:40:45Z"}
# pprint.pprint(d['resourceSets'][0]['resources'][0]['geocodePoints'][0]['coordinates'])


# importing the module
# from pytube import YouTube
# yt = YouTube('https://www.youtube.com/watch?v=wK4VPM-0ssU')
# yt.streams[-4].download()
# # for i in yt.streams:
# #     pprint.pprint(i)
# print('done')


# from pydub import AudioSegment
# sound = AudioSegment.from_file("C://Users//ravi//PycharmProjects//untitled//New folder//Flesh and the Power It Holds")
# sound.export("C:/Users/ravi/PycharmProjects/untitled/New folder/Flesh and the Power It Holds", format="mp3", bitrate="192k")


import youtube_dl

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