from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

video_path = "./data/sample.mp4"
audio_path = "./data/sample.mp3"

ffmpeg_extract_audio(video_path, audio_path)