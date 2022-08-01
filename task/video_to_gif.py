from moviepy.editor import VideoFileClip
import os


def make_gif(url: str) -> str:
    videoClip = VideoFileClip(url)
    number_of_gif = 1
    filename = 'TikTok-example-{0}.gif'.format(number_of_gif)
    while os.path.exists(filename):
        number_of_gif += 1
        filename = 'TikTok-example-{0}.gif'.format(number_of_gif)
        continue
    videoClip.write_gif(filename, program='ffmpeg', fps=20)
    return print(os.path.abspath(filename))


if __name__ == '__main__':
    make_gif('https://v16-webapp.tiktok.com/be817b1a194ea09547a1cf61c41b2284/62e87720/video/tos/useast2a/tos-useast2a-ve-0068c002/617349ce4b7f4fe4ab712fe5b195ad38/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=3000&bt=1500&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZDfoKwe2Ni50yl7Gb&mime_type=video_mp4&qs=0&rc=NzwzN2c5ZjQ2O2Y1ZGdkNEBpM3FlZzo2OTYzdzMzNTczM0BgXi8uYWAtXzExXjIuLS1fYSNuMC41NWVwbmBfLS1jMTZzcw%3D%3D&l=202208011859360102171351381356A833')
