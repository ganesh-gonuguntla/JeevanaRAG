"""Central configuration â€” loads environment variables and exposes application-wide constants."""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# â”€â”€ Load environment from project root .env file â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_ENV_PATH)

# â”€â”€ Sarvam AI (Indian language translation, transliteration, TTS, STT) â”€â”€â”€â”€â”€â”€â”€
SARVAM_API_KEY: str = os.getenv("SARVAM_API_KEY", "")

# â”€â”€ OpenAI (GPT-4o Vision for OCR, GPT-4o-mini for CRAG evaluation) â”€â”€â”€â”€â”€â”€â”€â”€â”€
OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

# â”€â”€ Google Gemini (fallback vision OCR and CRAG completeness scoring) â”€â”€â”€â”€â”€â”€â”€â”€
def _collect_gemini_api_keys() -> tuple[str, ...]:
    """Gather all configured Gemini API keys, deduplicating across sources."""
    keys: list[str] = []
    seen: set[str] = set()

    for env_name in ("GEMINI_API_KEY", "GEMINI_API_KEY_2", "GEMINI_API_KEY_3"):
        value = os.getenv(env_name, "").strip()
        if value and value not in seen:
            seen.add(value)
            keys.append(value)

    extra_keys = os.getenv("GEMINI_API_KEYS", "")
    for value in extra_keys.split(","):
        cleaned = value.strip()
        if cleaned and cleaned not in seen:
            seen.add(cleaned)
            keys.append(cleaned)

    return tuple(keys)


GEMINI_API_KEYS: tuple[str, ...] = _collect_gemini_api_keys()
GEMINI_API_KEY: str = GEMINI_API_KEYS[0] if GEMINI_API_KEYS else ""

# â”€â”€ Groq (Llama Vision and Text models as tertiary fallback) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

# â”€â”€ Google Cloud Vision (optional additional OCR path) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
GOOGLE_CLOUD_VISION_KEY: str = os.getenv("GOOGLE_CLOUD_VISION_KEY", "")

# â”€â”€ OpenFDA (supplementary drug lookup) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
OPENFDA_API_KEY: str = os.getenv("OPENFDA_API_KEY", "")

# â”€â”€ Neo4j Graph Database â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
NEO4J_URI: str = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER: str = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD: str = os.getenv("NEO4J_PASSWORD", "")

# â”€â”€ Application Defaults â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
DEFAULT_LANGUAGE: str = os.getenv("DEFAULT_LANGUAGE", "en")
LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

# â”€â”€ Supported Interface Languages â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
SUPPORTED_LANGUAGES: dict[str, str] = {
    "en": "English",
    "hi": "à¤¹à¤¿à¤¨à¥à¤¦à¥€",
    "ta": "à®¤à®®à®¿à®´à¯",
    "te": "à°¤à±†à°²à±à°—à±",
    "kn": "à²•à²¨à³à²¨à²¡",
    "ml": "à´®à´²à´¯à´¾à´³à´‚",
    "mr": "à¤®à¤°à¤¾à¤ à¥€",
    "bn": "à¦¬à¦¾à¦‚à¦²à¦¾",
    "gu": "àª—à«àªœàª°àª¾àª¤à«€",
    "pa": "à¨ªà©°à¨œà¨¾à¨¬à©€",
}

# â”€â”€ File System Paths â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
DATA_DIR: Path = Path(os.getenv("DATA_DIR", "/data"))
