# 💌 For My Nandani (Puchu) — A Romantic Re-Proposal Web App

A single-page, multi-layered interactive web app built with **Streamlit & Custom CSS/HTML/JS** designed as a sincere, heartfelt, and romantic re-proposal from **Rishi** to his girlfriend **Nandani (Puchu)**.

---

## ✨ Features & Highlights

- **🌸 Soft Pink Romantic Aesthetic**:
  - Blush pink, baby pink, and rose color palette with smooth gradient backgrounds and glassmorphic cards.
  - Custom Google Fonts: *Dancing Script* for titles/signatures and *Poppins* for readable body text.
  - Floating cherry blossom petals and glowing pink hearts drifting softly in the background.
  - Fully responsive and mobile-optimized (touch targets, readable typography, cards tailored for phone screens).
  - Sidebar-free, immersive full-screen experience (Streamlit's default chrome is hidden).

- **💖 Narrative Architecture (`st.session_state`)**:
  - **Progress Indicator**: 7 glowing heart badges (`💖` / `🤍`) displaying the current chapter name.
  - **Chapter 1 – A Quiet Welcome**: Typewriter greeting *"Hey Puchu, I made something for you..."* with a wax-sealed envelope card and an *Open with Love 💌* button.
  - **Chapter 2 – From My Heart (My Apology)**: A sincere letter from Rishi owning mistakes with zero excuses (ignoring her, not paying attention to her, disrespecting her) and genuine remorse.
  - **Chapter 3 – What I've Learned**: Interactive reflection cards that expand to reveal the deep lessons Rishi learned from this separation.
  - **Chapter 4 – My Promises to You**: 7 sacred vows (treating her like his baby girl, making her first priority, never leaving her on seen, etc.) with interactive heart seals (`Seal with Love 💕` ➔ `Sealed Forever 💖🔒`).
  - **Chapter 5 – A Little Smile**: The *"Puchu Miss-O-Meter"* (which breaks the scale with an overflow calculation to infinity ♾️) plus redeemable perks/coupons (*Forehead Kisses*, *Instant Priority Reply*, *Baby Girl Treatment*).
  - **Chapter 6 – The Question**: The big ask: *"Nandani, my Puchu, will you give me another chance and be my girlfriend again? 💕"*
    - **`Yes 💖`**: Triggers celebratory balloons and takes her to the celebration.
    - **`I need a little more time 🥺`**: A 100% genuine, respectful response without any guilt-tripping (*"Take all the time in the world, Puchu. I'll be right here, and I'll keep earning it."*).
  - **Chapter 7 – Our Beginning (Celebration)**: Love letter ending from Rishi (*"You're my baby, my Puchu, and you'll always come first"*), an official vow certificate, and balloons.

- **🎵 Background Music**:
  - Configured with your audio: `assets/la_vie_en_rose.wav` (*La Vie En Rose 🌹*).
  - Includes a play/mute toggle button at the top.

- **⚙️ 100% Configurable**:
  - All text, names, promises, lessons, and messages are organized in a single `CONFIG` dictionary at the very top of `app.py`.

---

## 🚀 Running Locally

### 1. Requirements
- Python 3.9+
- Streamlit

### 2. Quick Setup
Open your terminal inside this folder:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will immediately open in your browser at `http://localhost:8501`.

---

## 🎵 How to Use Your Own Song

1. Place your MP3/WAV song file inside the `assets/` folder (e.g. `assets/our_song.mp3`).
2. Open `app.py` and update the top configuration:
   ```python
   CONFIG = {
       ...
       "audio_file": "assets/our_song.mp3",
       "audio_title": "Our Special Song 🎵",
       ...
   }
   ```
3. Save the file. Streamlit will instantly reload with your song!

---

## 🌐 How to Deploy for Free on Streamlit Community Cloud

Deploying online gives you a permanent, beautiful link (e.g., `https://for-my-puchu.streamlit.app`) that you can text or send to Nandani on WhatsApp/Instagram so she can open it on her phone.

### Step 1: Push to GitHub
1. Create a free account at [github.com](https://github.com).
2. Create a new repository (e.g., `for-nandani` or `love`).
3. In your terminal inside this directory, run:
   ```bash
   git init
   git add .
   git commit -m "Romantic Re-Proposal for Nandani"
   git branch -M main
   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/for-nandani.git
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud (100% Free)
1. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with GitHub.
2. Click **"New app"**.
3. Select your repository: `<YOUR_GITHUB_USERNAME>/for-nandani`.
4. Branch: `main`.
5. Main file path: `app.py`.
6. Click **"Deploy!"**.

Within 1–2 minutes, your website will be live with a shareable URL!

---

## 📝 Folder Structure

```
love/
├── app.py                     # Main interactive application & CONFIG
├── requirements.txt           # Python dependencies (streamlit)
├── README.md                  # Instructions for setup and deployment
├── .streamlit/
│   └── config.toml            # Custom romantic theme palette (pink & blush)
└── assets/
    └── romantic_melody.wav    # Gentle music-box audio sample
```
