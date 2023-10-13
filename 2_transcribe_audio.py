import whisper

model = whisper.load_model("base")

audio_path = "./data/sample.mp3"
result = model.transcribe(audio_path)

with open("./data/sample.txt", "w") as f:
    f.write(result["text"])

print(result["text"][0:100], "...")
