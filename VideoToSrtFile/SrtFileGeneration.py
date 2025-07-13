import whisper

def transcribe_to_srt(video_path):
    model = whisper.load_model("base")  # You can use 'tiny', 'base', 'small', 'medium', 'large'
    result = model.transcribe(video_path, task='transcribe', verbose=True)

    # Save SRT
    with open("output.srt", "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"], start=1):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()

            # Format time
            def format_time(seconds):
                h = int(seconds // 3600)
                m = int((seconds % 3600) // 60)
                s = seconds % 60
                return f"{h:02}:{m:02}:{s:06.3f}".replace('.', ',')

            f.write(f"{i}\n{format_time(start)} --> {format_time(end)}\n{text}\n\n")

    print("✅ Generated subtitles: output.srt")

# Usage
transcribe_to_srt("OpenNoteVideo.mp4")