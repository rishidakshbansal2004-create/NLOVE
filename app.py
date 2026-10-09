import streamlit as st
import os

# ==============================================================================
# CONFIGURATION & PERSONALIZATION DICTIONARY
# (Easily customize any text, names, dates, or messages here)
# ==============================================================================
CONFIG = {
    # Names & Nicknames
    "her_name": "Nandani",
    "his_name": "Rishi",
    "nickname": "Puchu",
    
    # Audio Settings
    "audio_file": "assets/la_vie_en_rose.wav",
    "audio_title": "La Vie En Rose 🌹 (Our Song)",
    
    # Section 1: Gentle Welcome
    "welcome": {
        "eyebrow": "A quiet message for someone irreplaceable...",
        "greeting": "Hey Puchu, I made something for you...",
        "subtitle": "It comes straight from my heart. Take a deep breath, and open it when you're ready.",
        "button_text": "Open with Love 💌",
        "quote": "“Some hearts are meant to find their way back to each other.”"
    },
    
    # Section 2: My Apology
    "apology": {
        "title": "A Sincere Letter to My Nandani",
        "subtitle": "Owning every mistake. No excuses, no deflecting, just honest truth.",
        "salutation": "My Dearest Nandani (My Puchu),",
        "paragraphs": [
            "Being apart from you has made every single day feel quiet, empty, and painfully clear. It forced me to look straight in the mirror, and what I saw was how much I hurt the person who deserved only my gentlest care.",
            "I want to say this with complete honesty and without hiding behind a single excuse: <strong>I was wrong. Deeply, truly wrong.</strong>",
            "<strong>I ignored you.</strong> When you reached out for my presence, for comfort, or just to talk, I allowed silence to linger. No one who loves someone should ever make them feel unseen or unheard. Making you feel ignored is something I will regret for the rest of my life.",
            "<strong>I didn't pay attention to you.</strong> I failed to notice what you were going through, your quiet emotions, and the little details that matter. You deserved my undivided presence and my watchful care, and instead, I let other things distract me.",
            "<strong>I disrespected you.</strong> And for that, my heart breaks every time I think about it. Respect is not an optional luxury in love; it is the sacred bedrock. You deserved to be honored, lifted up, and treated with pure tenderness at all times. I failed to protect your dignity, and there is no excuse in the world for that.",
            "I am not writing this to justify anything or ask you to magically wipe away the pain. I broke your trust, and the blame is entirely mine.",
            "You are my Puchu. You deserved someone who treated you like royalty and made you feel utterly safe. I am deeply, genuinely sorry for failing to be that man."
        ],
        "signature": "With remorse and all my heart,\nRishi",
        "button_next": "Turn the Page: What I've Learned 🕊️"
    },
    
    # Section 3: What I've Learned
    "lessons_intro": {
        "title": "What This Distance Has Taught Me",
        "subtitle": "Real change doesn't start with words—it starts with understanding what went wrong.",
        "instruction": "Tap each card to read what I have learned deep in my heart:"
    },
    "lessons": [
        {
            "id": 1,
            "title": "I will never ignore you again",
            "summary": "Silence is never strength. Being present is how love breathes.",
            "detail": "Walking away or letting your messages sit in silence was weak of me. I've learned that holding space for you—answering you, showing up, and staying by your side through every feeling—is what a real partner does. You will never have to speak into an empty void again.",
            "icon": "💬"
        },
        {
            "id": 2,
            "title": "I will give you my full attention",
            "summary": "When you speak, the entire world can wait.",
            "detail": "No more divided attention, no half-listening, no scrolling or being mentally elsewhere. When my Nandani speaks, she gets my full focus, my eyes, and my whole heart. Every story you tell and every feeling you express is important.",
            "icon": "👁️"
        },
        {
            "id": 3,
            "title": "I will respect you always",
            "summary": "Respect is unconditional, in calm and in storms.",
            "detail": "Respect isn't just something to give when things are easy. It's how I speak to you when tensions rise, how I honor your boundaries, and how I protect your feelings. I will treat you with unwavering dignity and softness forever.",
            "icon": "🛡️"
        },
        {
            "id": 4,
            "title": "You are my first priority, not an afterthought",
            "summary": "You don't fit into my schedule; my life is built around cherishing you.",
            "detail": "I became complacent, and that was unforgivable. Never again will you wonder where you stand with me. You are my first priority in the morning, during the day, and at night. You are my first choice in every decision.",
            "icon": "👑"
        },
        {
            "id": 5,
            "title": "I'll listen first, understand always",
            "summary": "I leave my ego outside our door.",
            "detail": "I've learned to stop defending myself and instead listen with an open heart. If you hurt, my only goal is to understand, hold your hand, and make things right. Your feelings are always valid.",
            "icon": "🕊️"
        }
    ],
    
    # Section 4: My Promises
    "promises_intro": {
        "title": "My Sacred Promises to You",
        "subtitle": "These aren't just empty words. These are the vows I commit to living by every day.",
        "instruction": "Tap the heart on each promise to seal it in our hearts:"
    },
    "promises": [
        {
            "id": 0,
            "text": "To treat you like my baby, my own little girl—cherished, protected, and endlessly adored.",
            "tag": "Cherish & Protect"
        },
        {
            "id": 1,
            "text": "To make you my absolute first priority, every single day, with no hesitations.",
            "tag": "First Priority"
        },
        {
            "id": 2,
            "text": "To never leave you on seen or make you feel unattended or forgotten.",
            "tag": "Presence"
        },
        {
            "id": 3,
            "text": "To communicate with patience, transparency, and warmth, leaving all ego behind.",
            "tag": "Honest Communication"
        },
        {
            "id": 4,
            "text": "To honor and respect your thoughts, your boundaries, and your dignity unconditionally.",
            "tag": "Unwavering Respect"
        },
        {
            "id": 5,
            "text": "To give you all my love—pure, undivided, and fiercely devoted to your happiness.",
            "tag": "Undivided Love"
        },
        {
            "id": 6,
            "text": "To hold you through every storm and never let you feel lonely while you are with me.",
            "tag": "Forever By Your Side"
        }
    ],
    
    # Section 5: Something Fun (Breaking the Tension)
    "fun": {
        "title": "A Little Smile for Puchu 😊",
        "subtitle": "Because amidst the seriousness, I miss that bright, adorable smile of yours more than anything in the world.",
        "slider_question": "On a scale of 0% to 100%, how much do you think Rishi missed you?",
        "fun_facts": [
            "📈 Scientific Report: System overflow! Missing Puchu exceeded 999,999,999% (Broke the meter!).",
            "📱 Phone Glance Count: Approximately 420 times a day checking for a text from 'My Puchu'.",
            "🧸 Cuddle Deficit: Reached hazardous levels. Emergency cuddles recommended.",
            "🥺 Cutest Girl Award: Still 100% undisputed winner: Nandani."
        ],
        "coupons": [
            {"title": "Forehead Kisses", "desc": "Valid for lifetime unlimited gentle forehead kisses whenever you need reassurance.", "icon": "💋"},
            {"title": "Instant Priority Reply", "desc": "Guarantees Rishi drops everything to answer Puchu's calls or texts.", "icon": "⚡"},
            {"title": "Baby Girl Treatment", "desc": "To be babied, spoiled, pampered, and tucked in with all the warmth.", "icon": "🎀"},
            {"title": "Cuddle Shield", "desc": "A safe warm embrace that protects against all bad days and stresses.", "icon": "🧸"}
        ]
    },
    
    # Section 6: The Question
    "question": {
        "eyebrow": "From the bottom of my soul...",
        "title": "Nandani, my Puchu...",
        "message": (
            "I don't just want to go back to how things were. I want us to be so much better, gentler, and more devoted than before.<br><br>"
            "I want to make you feel like my baby, my own little girl—cherished, protected, and truly loved. "
            "From now on, you get all my love and you will always be my first priority."
        ),
        "the_big_ask": "Will you give me another chance and be my girlfriend again? 💕",
        "btn_yes": "Yes, I will be your girlfriend again! 💖",
        "btn_time": "I need a little more time 🥺",
        "time_response": {
            "title": "Take all the time you need, Puchu. 🌸",
            "content": (
                "I respect your heart completely. You were hurt, and healing takes its own sweet time.<br><br>"
                "I will be right here, waiting patiently with an open heart. I will keep earning your trust day by day through actions, not just words.<br><br>"
                "You never have to rush. Your comfort, your peace, and your feelings come first, always. I love you."
            )
        }
    },
    
    # Section 7: Celebration
    "celebration": {
        "eyebrow": "She said yes! 💕",
        "title": "To My Beautiful Nandani 💖",
        "quote": "“You are my baby, my Puchu, and you will always come first.”",
        "letter": [
            "Thank you from the deepest place in my soul for giving us another chance.",
            "I promise you that I will never let you down again. You will always be my baby girl—cherished, safe, protected, and showered with unconditional love every single day.",
            "This isn't just a restart; this is our fresh beginning, built on genuine respect, undivided attention, and eternal love.",
            "I love you more than words could ever describe, Puchu."
        ],
        "certificate_title": "Official Vow of Devotion 💍",
        "certificate_body": "This certifies that Nandani is Rishi's first priority, cherished baby girl, and true love for now and all eternity.",
        "signature": "Forever yours,<br>Rishi 💕"
    }
}

# ==============================================================================
# STREAMLIT PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title=f"For My Nandani 💕 | A Message from Rishi",
    page_icon="💌",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# HELPER: BULLETPROOF HTML RENDERER
# (Ensures CommonMark Markdown never misinterprets lines as code blocks)
# ==============================================================================
def render_html(html_str: str):
    """
    Strips leading and trailing indentation from each line, ensuring Markdown
    never interprets lines as indented code blocks (<pre><code>).
    """
    cleaned_lines = [line.strip() for line in html_str.strip().split("\n") if line.strip() != ""]
    st.markdown("\n".join(cleaned_lines), unsafe_allow_html=True)

# ==============================================================================
# INITIALIZE SESSION STATE
# ==============================================================================
if "step" not in st.session_state:
    st.session_state.step = 1
if "sealed_promises" not in st.session_state:
    st.session_state.sealed_promises = set()
if "revealed_lessons" not in st.session_state:
    st.session_state.revealed_lessons = set([0])
if "decision" not in st.session_state:
    st.session_state.decision = None
if "miss_slider_val" not in st.session_state:
    st.session_state.miss_slider_val = 50
if "miss_calculated" not in st.session_state:
    st.session_state.miss_calculated = False
if "claimed_coupons" not in st.session_state:
    st.session_state.claimed_coupons = set()
if "audio_enabled" not in st.session_state:
    st.session_state.audio_enabled = True

def go_to_step(step_num: int):
    st.session_state.step = step_num
    st.rerun()

def seal_promise(pid: int):
    st.session_state.sealed_promises.add(pid)
    st.rerun()

def toggle_lesson(lid: int):
    if lid in st.session_state.revealed_lessons:
        st.session_state.revealed_lessons.remove(lid)
    else:
        st.session_state.revealed_lessons.add(lid)
    st.rerun()

def claim_coupon(c_idx: int):
    st.session_state.claimed_coupons.add(c_idx)
    st.rerun()

# ==============================================================================
# CUSTOM CSS & FLOATING PARTICLES INJECTION
# ==============================================================================
CUSTOM_CSS = """
<style>
/* Import Romantic Google Fonts */
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Great+Vibes&family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,700;1,400&display=swap');

/* Clean up Streamlit Default Chrome */
#MainMenu { visibility: hidden !important; display: none !important; }
header { visibility: hidden !important; display: none !important; }
footer { visibility: hidden !important; display: none !important; }
.stDeployButton { display: none !important; }
[data-testid="stToolbar"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
[data-testid="stStatusWidget"] { display: none !important; }

/* Global App Styling */
.stApp {
    background: linear-gradient(145deg, #fff2f5 0%, #fde2e8 35%, #ffd6e0 70%, #ffccd5 100%) !important;
    background-attachment: fixed !important;
    font-family: 'Poppins', sans-serif !important;
    color: #3d1a24 !important;
}

/* App Container - Responsive & Mobile First */
.block-container {
    max-width: 660px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 4rem !important;
    padding-left: 1.1rem !important;
    padding-right: 1.1rem !important;
    margin: 0 auto !important;
}

/* Floating Petals and Hearts Background */
.petals-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.floating-item {
    position: absolute;
    bottom: -60px;
    font-size: 1.4rem;
    opacity: 0.6;
    animation: floatUp 13s infinite linear;
    user-select: none;
}
.floating-item:nth-child(1) { left: 8%; animation-duration: 11s; animation-delay: 0s; font-size: 1.2rem; }
.floating-item:nth-child(2) { left: 22%; animation-duration: 14s; animation-delay: 2s; font-size: 1.6rem; }
.floating-item:nth-child(3) { left: 38%; animation-duration: 12s; animation-delay: 4s; font-size: 1.1rem; }
.floating-item:nth-child(4) { left: 54%; animation-duration: 16s; animation-delay: 1s; font-size: 1.5rem; }
.floating-item:nth-child(5) { left: 68%; animation-duration: 13s; animation-delay: 3s; font-size: 1.3rem; }
.floating-item:nth-child(6) { left: 82%; animation-duration: 15s; animation-delay: 5s; font-size: 1.7rem; }
.floating-item:nth-child(7) { left: 93%; animation-duration: 12s; animation-delay: 2.5s; font-size: 1.2rem; }

@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0deg) scale(0.8);
        opacity: 0;
    }
    15% {
        opacity: 0.65;
    }
    85% {
        opacity: 0.65;
    }
    100% {
        transform: translateY(-110vh) rotate(360deg) scale(1.15);
        opacity: 0;
    }
}

/* Smooth Fade In for section transitions */
.fade-in {
    animation: romanticFadeIn 0.85s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes romanticFadeIn {
    0% {
        opacity: 0;
        transform: translateY(16px) scale(0.99);
    }
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

/* Romantic Glassmorphism Card */
.romantic-card {
    background: rgba(255, 255, 255, 0.82);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border: 1.5px solid rgba(255, 255, 255, 0.95);
    border-radius: 28px;
    padding: 2.2rem 1.8rem;
    box-shadow: 0 16px 40px -8px rgba(225, 77, 109, 0.16), 0 2px 6px rgba(0,0,0,0.03);
    margin-bottom: 1.4rem;
    position: relative;
    z-index: 1;
}

/* Letter Card Style with Warm Parchment Touch */
.letter-card {
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.94) 0%, rgba(255, 247, 248, 0.92) 100%);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border: 1.5px solid rgba(255, 225, 230, 0.9);
    border-radius: 24px;
    padding: 2.2rem 1.8rem;
    box-shadow: 0 18px 45px -10px rgba(201, 24, 74, 0.14);
    position: relative;
    z-index: 1;
}

/* Typography Classes */
.romantic-title {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(2.3rem, 7vw, 3.4rem);
    font-weight: 700;
    color: #c9184a;
    line-height: 1.25;
    margin-bottom: 0.5rem;
    text-align: center;
    text-shadow: 0 2px 8px rgba(201, 24, 74, 0.12);
}

.romantic-script {
    font-family: 'Dancing Script', cursive;
    font-size: clamp(1.7rem, 5.5vw, 2.3rem);
    color: #a4133c;
    line-height: 1.3;
}

.romantic-eyebrow {
    font-size: 0.85rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 2px;
    color: #ff4d6d;
    text-align: center;
    margin-bottom: 0.4rem;
}

.romantic-subtitle {
    font-size: 1.05rem;
    color: #6a3541;
    text-align: center;
    line-height: 1.5;
    margin-bottom: 1.5rem;
}

.letter-text {
    font-size: 1.02rem;
    line-height: 1.8;
    color: #421e27;
    margin-bottom: 1.1rem;
}

.wax-seal {
    width: 60px;
    height: 60px;
    background: radial-gradient(circle at 35% 35%, #ff4d6d, #a4133c);
    border-radius: 50%;
    margin: 0 auto 1.2rem auto;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 6px 16px rgba(164, 19, 60, 0.35), inset 0 -2px 4px rgba(0,0,0,0.2);
    border: 2px solid #ffd6e0;
    color: #fff;
    font-size: 1.7rem;
}

/* Heart Progress Tracker (Without word 'layer') */
.progress-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin-bottom: 1.4rem;
    padding: 0.6rem 1.2rem;
    background: rgba(255, 255, 255, 0.65);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    border-radius: 40px;
    border: 1px solid rgba(255, 255, 255, 0.8);
    width: fit-content;
    margin-left: auto;
    margin-right: auto;
}
.progress-heart {
    font-size: 1.2rem;
    transition: transform 0.3s ease;
}
.progress-heart.active {
    transform: scale(1.2);
    filter: drop-shadow(0 2px 5px rgba(255, 77, 109, 0.5));
}
.progress-label {
    font-size: 0.88rem;
    font-weight: 600;
    color: #8b324d;
    margin-left: 6px;
}

/* Interactive Cards (Lessons) */
.lesson-card {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    border: 1px solid rgba(255, 200, 215, 0.8);
    padding: 1.2rem 1.3rem;
    margin-bottom: 0.9rem;
    box-shadow: 0 6px 18px rgba(225, 112, 137, 0.08);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}
.lesson-header {
    display: flex;
    align-items: center;
    gap: 12px;
}
.lesson-icon {
    font-size: 1.6rem;
    background: #ffe5ec;
    border-radius: 14px;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.lesson-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: #800f2f;
    margin: 0;
}
.lesson-summary {
    font-size: 0.88rem;
    color: #6a3541;
    margin-top: 2px;
}
.lesson-detail {
    margin-top: 0.9rem;
    padding-top: 0.9rem;
    border-top: 1px dashed #ffb3c1;
    font-size: 0.96rem;
    line-height: 1.65;
    color: #49111c;
}

/* Promise Checklist Card */
.promise-row {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 18px;
    border: 1.5px solid rgba(255, 210, 222, 0.7);
    padding: 1.1rem 1.2rem;
    margin-bottom: 0.9rem;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    box-shadow: 0 4px 14px rgba(225, 77, 109, 0.06);
    transition: all 0.25s ease;
}
.promise-row.sealed {
    background: linear-gradient(135deg, #fff0f3 0%, #ffffff 100%);
    border-color: #ff4d6d;
    box-shadow: 0 6px 20px rgba(255, 77, 109, 0.15);
}
.promise-badge {
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 1px;
    padding: 2px 8px;
    border-radius: 8px;
    background: #ffe3e8;
    color: #a4133c;
    display: inline-block;
    margin-bottom: 4px;
}
.promise-text {
    font-size: 0.98rem;
    line-height: 1.55;
    color: #3b1822;
    margin: 0;
    font-weight: 500;
}

/* Coupons Grid */
.coupon-card {
    background: #ffffff;
    border: 2px dashed #ff758f;
    border-radius: 18px;
    padding: 1.1rem;
    text-align: center;
    box-shadow: 0 6px 16px rgba(255, 77, 109, 0.08);
    position: relative;
    overflow: hidden;
    margin-bottom: 0.8rem;
}
.coupon-title {
    font-weight: 700;
    color: #800f2f;
    font-size: 1.05rem;
    margin-top: 6px;
}
.coupon-desc {
    font-size: 0.84rem;
    color: #6a3541;
    margin-top: 4px;
    line-height: 1.4;
}

/* Big Re-Proposal Box */
.proposal-box {
    text-align: center;
    padding: 2.8rem 1.8rem;
    background: linear-gradient(160deg, rgba(255, 255, 255, 0.96) 0%, rgba(255, 240, 245, 0.94) 100%);
    border: 2px solid #ff758f;
    border-radius: 32px;
    box-shadow: 0 20px 50px -10px rgba(225, 77, 109, 0.28);
    position: relative;
    z-index: 1;
}
.ring-symbol {
    font-size: 3.5rem;
    margin-bottom: 0.5rem;
    animation: gentlePulse 2.4s infinite ease-in-out;
}
@keyframes gentlePulse {
    0%, 100% { transform: scale(1); filter: drop-shadow(0 4px 12px rgba(255, 77, 109, 0.3)); }
    50% { transform: scale(1.1); filter: drop-shadow(0 8px 24px rgba(255, 77, 109, 0.6)); }
}

/* Certificate of Devotion */
.certificate {
    background: #ffffff;
    border: 3px double #d4af37;
    border-radius: 24px;
    padding: 2.2rem 1.8rem;
    text-align: center;
    box-shadow: 0 14px 35px rgba(212, 175, 55, 0.18);
    margin: 1.5rem 0;
    position: relative;
}
.certificate-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: #a4133c;
    letter-spacing: 1px;
}

/* Style All Streamlit Buttons */
div[data-testid="stButton"] button {
    width: 100% !important;
    border-radius: 50px !important;
    padding: 0.75rem 1.6rem !important;
    font-size: 1.02rem !important;
    font-weight: 600 !important;
    font-family: 'Poppins', sans-serif !important;
    border: none !important;
    background: linear-gradient(135deg, #ff4d6d 0%, #ff758f 100%) !important;
    color: white !important;
    box-shadow: 0 8px 22px rgba(255, 77, 109, 0.32) !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    cursor: pointer !important;
}
div[data-testid="stButton"] button:hover {
    transform: translateY(-2px) scale(1.01) !important;
    box-shadow: 0 12px 28px rgba(255, 77, 109, 0.45) !important;
    color: white !important;
}
div[data-testid="stButton"] button:active {
    transform: scale(0.98) !important;
}

/* Secondary Button Style */
div[data-testid="stButton"] button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.85) !important;
    color: #8b324d !important;
    border: 1.5px solid #ffccd5 !important;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.04) !important;
}
div[data-testid="stButton"] button[kind="secondary"]:hover {
    background: #fff0f3 !important;
    color: #a4133c !important;
    border-color: #ff758f !important;
}

/* Responsive Font Sizing */
@media (max-width: 480px) {
    .romantic-card { padding: 1.6rem 1.2rem; border-radius: 22px; }
    .letter-card { padding: 1.6rem 1.2rem; border-radius: 20px; }
    .proposal-box { padding: 2rem 1.2rem; }
    .letter-text { font-size: 0.96rem; line-height: 1.7; }
}
</style>

<!-- Floating Petals & Hearts Background Overlay -->
<div class="petals-bg">
    <div class="floating-item">🌸</div>
    <div class="floating-item">💖</div>
    <div class="floating-item">✨</div>
    <div class="floating-item">🌸</div>
    <div class="floating-item">💕</div>
    <div class="floating-item">🌷</div>
    <div class="floating-item">💖</div>
</div>
"""
render_html(CUSTOM_CSS)

# ==============================================================================
# AUDIO PLAYER & MUSIC CONTROLLER
# ==============================================================================
audio_target = CONFIG.get("audio_file", "assets/la_vie_en_rose.wav")
if not os.path.exists(audio_target) and os.path.exists("la_vie_en_rose.wav"):
    audio_target = "la_vie_en_rose.wav"

with st.container():
    col_audio_left, col_audio_right = st.columns([3, 1])
    with col_audio_left:
        render_html(f"""
        <div style="font-size: 0.88rem; color: #8b324d; font-weight: 600; display: flex; align-items: center; gap: 6px; padding: 4px 0;">
            <span>🌹</span> <span>{CONFIG['audio_title']}</span>
        </div>
        """)
    with col_audio_right:
        music_toggle_label = "Mute 🔇" if st.session_state.audio_enabled else "Play 🎶"
        if st.button(music_toggle_label, key="toggle_music_btn", help="Play/Pause background song"):
            st.session_state.audio_enabled = not st.session_state.audio_enabled
            st.rerun()

    if st.session_state.audio_enabled and os.path.exists(audio_target):
        st.audio(audio_target, format="audio/wav", loop=True)

# ==============================================================================
# PROGRESS INDICATOR (Without mentioning 'layer')
# ==============================================================================
TOTAL_STEPS = 7
current_step = st.session_state.step

step_titles = [
    "A Quiet Welcome 🌸",
    "From My Heart 🕊️",
    "What I've Learned ✨",
    "My Promises to You 💍",
    "A Little Smile 😊",
    "The Question 💕",
    "Our Beginning 💖"
]

hearts_html = ""
for i in range(1, TOTAL_STEPS + 1):
    if i <= current_step:
        hearts_html += '<span class="progress-heart active">💖</span>'
    else:
        hearts_html += '<span class="progress-heart" style="opacity: 0.35;">🤍</span>'

render_html(f"""
<div class="progress-container">
    {hearts_html}
    <span class="progress-label">{step_titles[current_step - 1]}</span>
</div>
""")

# Back Navigation (Allowed between step 2 and 6)
if 1 < current_step < 7:
    col_nav_back, col_nav_space = st.columns([1, 2])
    with col_nav_back:
        if st.button("← Previous Page", key="btn_global_back"):
            go_to_step(current_step - 1)

# ==============================================================================
# SECTION 1: GENTLE WELCOME
# ==============================================================================
if current_step == 1:
    render_html(f"""
    <div class="fade-in">
        <div class="romantic-card" style="text-align: center; padding-top: 3rem; padding-bottom: 2.8rem;">
            <div class="wax-seal">💌</div>
            <div class="romantic-eyebrow">{CONFIG['welcome']['eyebrow']}</div>
            <h1 class="romantic-title">{CONFIG['welcome']['greeting']}</h1>
            <p class="romantic-subtitle" style="font-size: 1.15rem; max-width: 480px; margin: 0 auto 1.8rem auto;">
                {CONFIG['welcome']['subtitle']}
            </p>
            <div style="font-family: 'Dancing Script', cursive; font-size: 1.4rem; color: #a4133c; margin-bottom: 2rem;">
                {CONFIG['welcome']['quote']}
            </div>
        </div>
    </div>
    """)
    
    col_w_l, col_w_m, col_w_r = st.columns([1, 4, 1])
    with col_w_m:
        if st.button(CONFIG['welcome']['button_text'], key="btn_open_step1"):
            go_to_step(2)

# ==============================================================================
# SECTION 2: MY APOLOGY
# ==============================================================================
elif current_step == 2:
    apology = CONFIG['apology']
    paragraphs_html = "".join([f'<p class="letter-text">{p}</p>' for p in apology['paragraphs']])
    
    render_html(f"""
    <div class="fade-in">
        <div class="letter-card">
            <div class="wax-seal" style="background: radial-gradient(circle at 35% 35%, #e63946, #9b111e);">🕊️</div>
            <div class="romantic-eyebrow">From Rishi's Heart</div>
            <h2 class="romantic-title" style="font-size: 2.4rem;">{apology['title']}</h2>
            <div class="romantic-subtitle" style="margin-bottom: 1.8rem;">{apology['subtitle']}</div>
            
            <div style="font-family: 'Dancing Script', cursive; font-size: 1.6rem; color: #a4133c; margin-bottom: 1.2rem; font-weight: 700;">
                {apology['salutation']}
            </div>
            
            {paragraphs_html}
            
            <div style="text-align: right; margin-top: 2rem; border-top: 1px dashed #ffb3c1; padding-top: 1.2rem;">
                <div style="font-family: 'Dancing Script', cursive; font-size: 1.8rem; color: #800f2f; font-weight: 700; white-space: pre-line;">
                    {apology['signature']}
                </div>
            </div>
        </div>
    </div>
    """)
    
    col_a_l, col_a_m, col_a_r = st.columns([1, 4, 1])
    with col_a_m:
        if st.button(apology['button_next'], key="btn_next_step2"):
            go_to_step(3)

# ==============================================================================
# SECTION 3: WHAT I'VE LEARNED
# ==============================================================================
elif current_step == 3:
    intro = CONFIG['lessons_intro']
    lessons = CONFIG['lessons']
    
    render_html(f"""
    <div class="fade-in">
        <div class="romantic-card" style="padding-bottom: 1.2rem;">
            <div class="romantic-eyebrow">Growth & Realization</div>
            <h2 class="romantic-title" style="font-size: 2.4rem;">{intro['title']}</h2>
            <p class="romantic-subtitle">{intro['subtitle']}</p>
            <p style="text-align: center; font-size: 0.9rem; color: #a4133c; font-weight: 600; margin-bottom: 1rem;">
                {intro['instruction']}
            </p>
        </div>
    </div>
    """)
    
    for idx, item in enumerate(lessons):
        is_open = idx in st.session_state.revealed_lessons
        detail_html = f'<div class="lesson-detail">{item["detail"]}</div>' if is_open else ""
        button_label = "Hide reflection ✕" if is_open else f"Read reflection {item['icon']}"
        
        render_html(f"""
        <div class="lesson-card">
            <div class="lesson-header">
                <div class="lesson-icon">{item['icon']}</div>
                <div style="flex-grow: 1;">
                    <div class="lesson-title">{idx + 1}. {item['title']}</div>
                    <div class="lesson-summary">{item['summary']}</div>
                </div>
            </div>
            {detail_html}
        </div>
        """)
        
        col_btn_l, col_btn_r = st.columns([2, 1])
        with col_btn_r:
            if st.button(button_label, key=f"btn_lesson_{idx}"):
                toggle_lesson(idx)
        st.write("")
        
    st.markdown("<br>", unsafe_allow_html=True)
    col_l3_l, col_l3_m, col_l3_r = st.columns([1, 4, 1])
    with col_l3_m:
        if st.button("See My Promises to You 💍", key="btn_next_step3"):
            go_to_step(4)

# ==============================================================================
# SECTION 4: MY PROMISES (Interactive Heart Sealing)
# ==============================================================================
elif current_step == 4:
    intro = CONFIG['promises_intro']
    promises = CONFIG['promises']
    sealed_count = len(st.session_state.sealed_promises)
    total_promises = len(promises)
    
    render_html(f"""
    <div class="fade-in">
        <div class="romantic-card">
            <div class="romantic-eyebrow">Unconditional Commitment</div>
            <h2 class="romantic-title" style="font-size: 2.4rem;">{intro['title']}</h2>
            <p class="romantic-subtitle">{intro['subtitle']}</p>
            <div style="text-align: center; margin-bottom: 0.8rem;">
                <span style="background: #ffe3e8; color: #a4133c; font-weight: 700; padding: 4px 14px; border-radius: 20px; font-size: 0.9rem;">
                    Sealed: {sealed_count} of {total_promises} Promises 💖
                </span>
            </div>
            <p style="text-align: center; font-size: 0.88rem; color: #6a3541; margin-top: 6px;">
                {intro['instruction']}
            </p>
        </div>
    </div>
    """)
    
    for item in promises:
        pid = item['id']
        is_sealed = pid in st.session_state.sealed_promises
        status_icon = "💖🔒" if is_sealed else "🤍"
        row_class = "promise-row sealed" if is_sealed else "promise-row"
        
        render_html(f"""
        <div class="{row_class}">
            <div style="font-size: 1.5rem; flex-shrink: 0; margin-top: 2px;">{status_icon}</div>
            <div style="flex-grow: 1;">
                <span class="promise-badge">{item['tag']}</span>
                <p class="promise-text">{item['text']}</p>
            </div>
        </div>
        """)
        
        col_p_l, col_p_r = st.columns([2, 1])
        with col_p_r:
            if not is_sealed:
                if st.button("Seal with Love 💕", key=f"btn_seal_{pid}"):
                    seal_promise(pid)
            else:
                render_html('<div style="text-align: right; font-size: 0.84rem; color: #ff4d6d; font-weight: 600; padding: 6px 0;">Sealed Forever ✨</div>')
        st.write("")
        
    if sealed_count == total_promises:
        render_html("""
        <div style="background: linear-gradient(135deg, #ffe5ec 0%, #ffccd5 100%); border-radius: 20px; padding: 1.2rem; text-align: center; border: 1.5px solid #ff758f; margin: 1.2rem 0; box-shadow: 0 8px 24px rgba(255, 77, 109, 0.2);">
            <div style="font-size: 1.8rem; margin-bottom: 4px;">🔐✨</div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 1.6rem; color: #800f2f; font-weight: 700;">
                All 7 Promises Sealed in Rishi's Heart Forever
            </div>
            <div style="font-size: 0.92rem; color: #49111c; margin-top: 4px;">
                You are my baby girl, and these are my sacred vows to you.
            </div>
        </div>
        """)
    else:
        col_all_l, col_all_r = st.columns([1, 1])
        with col_all_r:
            if st.button("Seal All 7 Promises 💕", key="btn_seal_all"):
                st.session_state.sealed_promises = set(range(total_promises))
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    col_l4_l, col_l4_m, col_l4_r = st.columns([1, 4, 1])
    with col_l4_m:
        if st.button("A Little Smile for You Next 😊", key="btn_next_step4"):
            go_to_step(5)

# ==============================================================================
# SECTION 5: SOMETHING FUN (Miss-O-Meter & Cute Coupons)
# ==============================================================================
elif current_step == 5:
    fun = CONFIG['fun']
    render_html(f"""
    <div class="fade-in">
        <div class="romantic-card">
            <div class="romantic-eyebrow">A Sweet Breather</div>
            <h2 class="romantic-title" style="font-size: 2.3rem;">{fun['title']}</h2>
            <p class="romantic-subtitle">{fun['subtitle']}</p>
        </div>
        <div class="romantic-card" style="border: 2px dashed #ff8fa3; background: #fffcfd;">
            <div style="text-align: center; font-size: 2rem; margin-bottom: 0.2rem;">📏💖</div>
            <h3 style="text-align: center; color: #800f2f; font-weight: 700; margin-bottom: 0.5rem;">
                The Official "Puchu Miss-O-Meter"
            </h3>
            <p style="text-align: center; font-size: 0.95rem; color: #6a3541; margin-bottom: 1.2rem;">
                {fun['slider_question']}
            </p>
        </div>
    </div>
    """)
    
    user_slider = st.slider(
        label="Select a percentage:",
        min_value=0,
        max_value=100,
        value=st.session_state.miss_slider_val,
        step=5,
        key="slider_miss",
        help="Slide to test how much Rishi missed you!"
    )
    st.session_state.miss_slider_val = user_slider
    
    col_calc_l, col_calc_m, col_calc_r = st.columns([1, 2, 1])
    with col_calc_m:
        if st.button("Calculate Exact Truth 🔍", key="btn_calc_miss"):
            st.session_state.miss_calculated = True
            st.rerun()
            
    if st.session_state.miss_calculated or user_slider > 0:
        facts_html = "".join([
            f'<div style="background: rgba(255, 255, 255, 0.85); border-radius: 14px; padding: 0.75rem 1rem; margin-bottom: 0.5rem; border-left: 4px solid #ff4d6d; font-size: 0.92rem; color: #4a1525;">{fact}</div>'
            for fact in fun['fun_facts']
        ])
        
        render_html(f"""
        <div style="background: linear-gradient(135deg, #fff0f3, #ffe3e8); border-radius: 20px; padding: 1.4rem; border: 2px solid #ff4d6d; text-align: center; margin: 1.2rem 0; box-shadow: 0 10px 28px rgba(255, 77, 109, 0.2);">
            <div style="font-size: 2.2rem; animation: gentlePulse 2s infinite ease-in-out;">⚠️📈💥</div>
            <div style="font-family: 'Poppins', sans-serif; font-size: 1.3rem; font-weight: 800; color: #c9184a; margin-top: 6px;">
                CRITICAL OVERFLOW ERROR: SCALE BROKEN!
            </div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 2.2rem; color: #800f2f; font-weight: 700; margin: 6px 0;">
                Rishi Missed Puchu: ∞% (Infinity!)
            </div>
            <div style="font-size: 0.95rem; color: #590d22; line-height: 1.6; max-width: 480px; margin: 0 auto;">
                The meter cannot compute your selected percentage because the actual amount is mathematically boundless. Every hour felt like 47 years without you.
            </div>
        </div>
        <div style="margin: 1rem 0;">
            {facts_html}
        </div>
        """)

    # Puchu's Special Coupon Book
    render_html("""
    <div style="text-align: center; margin-top: 1.5rem; margin-bottom: 1.2rem;">
        <div class="romantic-eyebrow">Lifetime Guarantee</div>
        <h3 style="color: #800f2f; font-weight: 700; margin-bottom: 4px;">Puchu's Unconditional Perks 🎟️</h3>
        <p style="font-size: 0.9rem; color: #6a3541;">Tap to claim any of these whenever you wish:</p>
    </div>
    """)
    
    col_c1, col_c2 = st.columns(2)
    for idx, cp in enumerate(fun['coupons']):
        target_col = col_c1 if idx % 2 == 0 else col_c2
        is_claimed = idx in st.session_state.claimed_coupons
        with target_col:
            claim_text = "✅ Claimed by Puchu" if is_claimed else "✨ Ready to Redeem"
            render_html(f"""
            <div class="coupon-card">
                <div style="font-size: 2rem;">{cp['icon']}</div>
                <div class="coupon-title">{cp['title']}</div>
                <div class="coupon-desc">{cp['desc']}</div>
                <div style="font-size: 0.76rem; color: #ff4d6d; margin-top: 6px; font-weight: 600;">
                    {claim_text}
                </div>
            </div>
            """)
            if not is_claimed:
                if st.button(f"Claim {cp['icon']}", key=f"btn_claim_{idx}"):
                    claim_coupon(idx)
            st.write("")

    st.markdown("<br>", unsafe_allow_html=True)
    col_l5_l, col_l5_m, col_l5_r = st.columns([1, 4, 1])
    with col_l5_m:
        if st.button("Now, The Most Important Page... 💌", key="btn_next_step5"):
            go_to_step(6)

# ==============================================================================
# SECTION 6: THE QUESTION (The Re-Proposal)
# ==============================================================================
elif current_step == 6:
    q = CONFIG['question']
    render_html(f"""
    <div class="fade-in">
        <div class="proposal-box">
            <div class="ring-symbol">💍</div>
            <div class="romantic-eyebrow">{q['eyebrow']}</div>
            <h1 class="romantic-title" style="font-size: 2.9rem; margin-bottom: 1.2rem;">
                {q['title']}
            </h1>
            
            <div style="font-size: 1.08rem; line-height: 1.8; color: #49111c; max-width: 520px; margin: 0 auto 1.4rem auto;">
                {q['message']}
            </div>
            
            <div style="border-top: 2px dashed #ffb3c1; border-bottom: 2px dashed #ffb3c1; padding: 1.5rem 0; margin: 1.8rem 0;">
                <div style="font-family: 'Dancing Script', cursive; font-size: clamp(1.9rem, 6vw, 2.7rem); color: #c9184a; font-weight: 700; line-height: 1.3;">
                    {q['the_big_ask']}
                </div>
            </div>
            
            <p style="font-size: 0.92rem; color: #8b324d; font-style: italic;">
                There is no pressure, Puchu. Only love, respect, and the honest truth.
            </p>
        </div>
    </div>
    """)
    
    col_yes, col_time = st.columns([1.2, 1])
    with col_yes:
        if st.button(q['btn_yes'], key="btn_proposal_yes"):
            st.session_state.decision = "yes"
            st.balloons()
            go_to_step(7)
            
    with col_time:
        if st.button(q['btn_time'], key="btn_proposal_time", type="secondary"):
            st.session_state.decision = "need_time"
            st.rerun()

    if st.session_state.decision == "need_time":
        time_info = q['time_response']
        render_html(f"""
        <div style="background: rgba(255, 255, 255, 0.94); border-radius: 24px; padding: 2rem 1.6rem; border: 1.5px solid #ffccd5; margin-top: 1.8rem; box-shadow: 0 12px 35px rgba(225, 112, 137, 0.15); text-align: center;">
            <div style="font-size: 2.2rem; margin-bottom: 0.4rem;">🌸🤍</div>
            <h3 style="font-family: 'Dancing Script', cursive; font-size: 2.2rem; color: #800f2f; margin-bottom: 0.8rem;">
                {time_info['title']}
            </h3>
            <div style="font-size: 1rem; line-height: 1.75; color: #4a1525; max-width: 500px; margin: 0 auto;">
                {time_info['content']}
            </div>
            <div style="margin-top: 1.6rem; padding-top: 1rem; border-top: 1px dashed #ffb3c1; font-size: 0.88rem; color: #8b324d;">
                You can come back to this anytime. My heart is not going anywhere.
            </div>
        </div>
        """)
        
        col_re_l, col_re_m, col_re_r = st.columns([1, 2, 1])
        with col_re_m:
            if st.button("Re-read the letter 🕊️", key="btn_reread_letter"):
                go_to_step(2)

# ==============================================================================
# SECTION 7: CELEBRATION (After "Yes")
# ==============================================================================
elif current_step == 7:
    cel = CONFIG['celebration']
    paragraphs_cel_html = "".join([f'<p class="letter-text">{p}</p>' for p in cel['letter']])
    
    render_html(f"""
    <div class="fade-in">
        <div class="romantic-card" style="text-align: center; border: 2px solid #ff4d6d; background: linear-gradient(180deg, #ffffff 0%, #fff0f3 100%);">
            <div style="font-size: 3rem; margin-bottom: 0.3rem;">🎉💖🕊️</div>
            <div class="romantic-eyebrow">{cel['eyebrow']}</div>
            <h1 class="romantic-title" style="font-size: 2.8rem; margin-bottom: 0.8rem;">{cel['title']}</h1>
            
            <div style="font-family: 'Dancing Script', cursive; font-size: 1.65rem; color: #a4133c; margin: 1rem 0 1.6rem 0; font-weight: 700;">
                {cel['quote']}
            </div>
            
            <div style="text-align: left; background: rgba(255, 255, 255, 0.7); border-radius: 18px; padding: 1.5rem; border: 1px solid #ffd6e0; margin-bottom: 1.5rem;">
                {paragraphs_cel_html}
            </div>
            
            <div class="certificate">
                <div style="font-size: 1.8rem; margin-bottom: 0.2rem;">✨📜✨</div>
                <div class="certificate-title">{cel['certificate_title']}</div>
                <p style="font-size: 0.95rem; color: #590d22; line-height: 1.6; margin: 0.8rem 0;">
                    {cel['certificate_body']}
                </p>
                <div style="font-size: 0.82rem; color: #8b324d; font-weight: 600; text-transform: uppercase; letter-spacing: 1px;">
                    Date: Our Fresh Beginning & Forever
                </div>
            </div>
            
            <div style="text-align: right; margin-top: 1.4rem;">
                <div style="font-family: 'Dancing Script', cursive; font-size: 2rem; color: #800f2f; font-weight: 700;">
                    {cel['signature']}
                </div>
            </div>
        </div>
    </div>
    """)
    
    col_c_l, col_c_m, col_c_r = st.columns([1, 2, 1])
    with col_c_m:
        if st.button("Release Celebratory Balloons 🎈", key="btn_more_balloons"):
            st.balloons()

# ==============================================================================
# FOOTER / WATERMARK
# ==============================================================================
render_html(f"""
<div style="text-align: center; margin-top: 3.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255, 182, 193, 0.4); font-size: 0.85rem; color: #9c4a60;">
    <span>Built with all of Rishi's love for Nandani (Puchu) 💕</span>
</div>
""")
