# 🎙️ Voice Assistant

![Voice Assistant Banner](assets/banner.png)  

[![Python Version](https://img.shields.io/badge/python-3.12-blue?logo=python)](https://www.python.org/) 
[![GitHub stars](https://img.shields.io/github/stars/yPrashanth1984-sudo/voice-assistant?style=social)](https://github.com/yPrashanth1984-sudo/voice-assistant/stargazers)

An **AI-powered Voice Assistant** built in Python that understands **natural English commands** and helps you automate tasks with voice.  

---

## ✨ Features

| Feature | Description | Emoji |
|---------|-------------|-------|
| Voice Recognition | Understands spoken commands | 🗣️ |
| Speech Output | Talks back to you | 🔊 |
| Open Websites | Launch websites with voice | 🌐 |
| Run Apps | Launch applications | 💻 |
| Tell Time & Date | Current time/date information | ⏰ |
| Custom Commands | Add your own commands | 🛠️ |



---

## 🛠️ Installation

<details>
<summary>Click to expand installation steps</summary>

1. **Install dependencies**
```bash
pip install -r requirements.txt
2.Download Vosk model
Place it in the models/ directory:

# Example: small English model
# https://alphacephei.com/vosk/models


3.Verify models directory
Ensure your models/ folder contains the downloaded Vosk model files. For example:

models/
└─ vosk-model-small-en-us-0.15/


4.Run the assistant

python main.py
