# Lyric Dreamer

This project uses LyricGenius (genius.com), DALLE-3, GPT-3.5-Turbo, and GPT-4 to generate images for "Lyric Image Videos".

It's unbelievably silly, and a good way to drive up your API costs.

# Installation
```bash
pip install -r requirements.txt
```

# Usage

Create a .env file with OPENAI_API_KEY and GENIUS_API_KEY defined

### Generate images using just the lyrics

python lyric-dreamer.py

### Generate images using GPT to enhance the image prompts

python lyric-dreamer-v2.py