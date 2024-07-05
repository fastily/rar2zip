"""Utility functions and classes for unrar_tool"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Represents the settings obtained via environment variables"""
    out_dir: str = "/tmp/unrar_tool_storage"
