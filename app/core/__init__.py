"""
Core application components.

This module provides:
 - Configuration management
 - Database connection
 - Logging setup
 """
from app.core.config import get_settings, settings

__all__ = ['get_settings', 'settings']
