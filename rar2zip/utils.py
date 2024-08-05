"""Utility functions and classes for rar2zip"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Represents the settings obtained via environment variables"""
    out_dir: str = "/tmp/rar2zip_storage"
