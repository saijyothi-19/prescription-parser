import json
from googletrans import Translator
from gtts import gTTS


def generate_explanation(data):
    explanation = (
        f"Take {data['dosage']} mg of {data['medicine']} "
        f"{data['frequency']} times daily "
        f"for {data['duration']} days."
    )
    return explanation


def translate_text(text, target_lang):
    translator = Translator()
    translated = translator.translate(text, dest=target_lang)
    return translated.text


def generate_audio(text, filename, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save(filename)


def process_prescription(data):

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

    return output


if __name__ == "__main__":
    with open("input.json", "r") as f:
        data = json.load(f)

    result = process_prescription(data)
    print(json.dumps(result, indent=4, ensure_ascii=False))