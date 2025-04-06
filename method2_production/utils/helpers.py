

import re
from typing import List, Dict, Optional
import logging

logger = logging.getLogger(__name__)

def format_phone(phone: str) -> str:
    """Normalize phone number to 10-digit format"""
    cleaned = re.sub(r'\D', '', phone)
    if len(cleaned) != 10:
        raise ValueError("Phone number must contain 10 digits")
    return cleaned

def validate_events_list(events: List[str], allowed_events: List[str]) -> List[str]:
    """Validate and normalize event names"""
    normalized = [e.strip().lower() for e in events]
    allowed = [a.lower() for a in allowed_events]
    
    invalid = [e for e in normalized if e not in allowed]
    if invalid:
        raise ValueError(f"Invalid events: {', '.join(invalid)}")
        
    return normalized

def mask_email(email: str) -> str:
    """Mask email for logging purposes"""
    if '@' not in email:
        return email
    name, domain = email.split('@', 1)
    return f"{name[:2]}***@{domain}"

def format_error_response(error: Exception) -> Dict:
    """Create standardized error response"""
    error_type = type(error).__name__
    return {
        "error": error_type,
        "details": str(error),
        "documentation": "https://api.example.com/docs/errors/" + error_type.lower()
    }

def log_error(error: Exception, context: Optional[Dict] = None):
    """Standard error logging with context"""
    error_info = {
        "error_type": type(error).__name__,
        "message": str(error),
        "context": context or {}
    }
    logger.error("Registration Error: %s", error_info)

def validate_indian_phone(phone: str) -> bool:
    """Validate Indian phone number format"""
    pattern = r'^(\+91[\-\s]?)?[6-9]\d{9}$'
    return re.match(pattern, phone) is not None

def sanitize_input(text: str) -> str:
    """Sanitize user input"""
    return text.strip().replace('\0', '')[:500]