from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[3]
"""Normalized root directory of the project."""

DATA_DIR = (ROOT_DIR / "data").resolve()
"""Normalized data directory path."""

CLIENTS_DIR = (DATA_DIR / "clients").resolve()
"""Normalized clients directory path."""

SCRIPTS_DIR = (DATA_DIR / "scripts").resolve()
"""Normalized scripts directory path."""

LIBRARY_DIR = (DATA_DIR / "lib").resolve()
"""Normalized library directory path."""
