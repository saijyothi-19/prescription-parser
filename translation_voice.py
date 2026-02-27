import json

with open("input.json", "r") as f:
    data = json.load(f)
import json
from googletrans import Translator
from gtts import gTTS



# Step 1: Generate simple English explanation
def generate_explanation(data):
    explanation = (
        f"Take {data['medicine']} {data['dosage']} "
        f"{data['frequency']} for {data['duration']}."
    )
    return explanation

# Step 2: Translate
def translate_text(text, target_lang):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text

# Step 3: Generate audio
def generate_audio(text, filename, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)

# Run pipeline
english_text = generate_explanation(data)
telugu_text = translate_text(english_text, "te")
hindi_text = translate_text(english_text, "hi")

generate_audio(english_text, "english_audio.mp3", "en")
generate_audio(telugu_text, "telugu_audio.mp3", "te")
generate_audio(hindi_text, "hindi_audio.mp3", "hi")

output = {
    "english_explanation": english_text,
    "telugu_text": telugu_text,
    "hindi_text": hindi_text,
    "audio_files": {
        "english": "english_audio.mp3",
        "telugu": "telugu_audio.mp3",
        "hindi": "hindi_audio.mp3"
    }
}

print(json.dumps(output, indent=4, ensure_ascii=False))