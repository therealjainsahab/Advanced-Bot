import os
from dotenv import load_dotenv
from typing import Dict, Any

load_dotenv()

class Config:
    """Secure configuration management with validation"""
    
    # Telegram Bot Token (from your input)
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "8480838296:AAEoVE7D-7vIUbSm5VlvCb_92nuiqrGEe8o")
    
    # AI Service API Key (from your input)
    AI_SERVICE_KEY = os.getenv("AI_SERVICE_KEY", "287e27f48bca1e6ad2b1adf416e2f6a1")
    
    # Security validation
    @classmethod
    def validate_tokens(cls) -> Dict[str, bool]:
        """Validate all API tokens before startup"""
        validations = {
            "telegram_token_valid": len(cls.TELEGRAM_TOKEN) > 30 and ":" in cls.TELEGRAM_TOKEN,
            "ai_service_key_valid": len(cls.AI_SERVICE_KEY) == 32,  # Assuming 32-char key
        }
        
        if not all(validations.values()):
            raise ValueError(f"Token validation failed: {validations}")
        
        return validations
    
    # Database configuration
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///bot_data.db")
    
    # AI Service endpoints (future-proof)
    AI_SERVICES = {
        "openai": "https://api.openai.com/v1",
        "anthropic": "https://api.anthropic.com/v1",
        "cohere": "https://api.cohere.ai/v1",
        "stability": "https://api.stability.ai/v1",
        "huggingface": "https://api-inference.huggingface.co",
        "custom_ai_orchestrator": "https://orchestrator.ai/v3"
    }
    
    # Rate limiting
    RATE_LIMIT_PER_USER = 60  # requests per minute
    RATE_LIMIT_PER_CHAT = 300  # requests per minute
    
    # Monitoring
    SENTRY_DSN = os.getenv("SENTRY_DSN", "")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    
    # Deployment
    WEBHOOK_URL = os.getenv("WEBHOOK_URL", "")
    PORT = int(os.getenv("PORT", 8443))
