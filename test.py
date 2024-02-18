import yt_dlp


def get_direct_link(video_url):
    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'quiet': True,
        'no_warnings': True,
        'outtmpl': '%(id)s.%(ext)s',
        'merge_output_format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)

    return info_dict


video_url = input()
print(get_direct_link(video_url))