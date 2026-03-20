# Shanana — Virtual AI Voice Assistant

![Shanana banner](assets/shanana-banner.svg)

Shanana is a Python-based voice assistant that can:
- Wake up on “shanana” (and a few similar phrases)
- Read AI-related news headlines
- Open YouTube / Google in your browser
- Answer general questions using Groq (LLM)

## How It Works

Shanana runs in two modes:

1. **Sleep mode (waiting)**
   - Listens to the microphone using `SpeechRecognition`
   - When it hears a wake phrase (like `shanana`, `hey shanana`, `wake up`), it switches to active mode

2. **Active mode (commands)**
   - Listens again for your command and then:
     - `news` → fetches headlines from NewsAPI and speaks the first 5
     - `youtube` → opens YouTube
     - `google` → opens Google
     - `sleep` / `mute` → goes back to sleep mode
     - `shutdown` → exits the program
     - anything else → sends the request to Groq and speaks the response

Text-to-speech is done with `pyttsx3` and speech-to-text is done with Google Speech Recognition via `SpeechRecognition`.

## Setup

### 1) Install dependencies

Create a virtual environment and install:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requiremnts.txt
```

> Note: `PyAudio` may require system dependencies (like PortAudio) depending on your OS.

### 2) Add environment variables

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_key_here
NEWS_API_KEY=your_newsapi_key_here
```

## Run

```bash
python3 main.py
```

Say “shanana” to wake it up, then try: “news”, “youtube”, “google”, or ask any question.

## Notes

- On macOS the TTS driver is set to `nsss` in `main.py`. If you run on Windows/Linux, you may need to adjust the `pyttsx3` driver.
- Make sure your terminal/app has microphone permissions enabled.
