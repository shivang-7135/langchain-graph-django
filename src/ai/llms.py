from django.conf import settings
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI


def get_openai_api_key():
    # ApiKey.objects.get(provider='openai', org='CFE)
    return settings.OPENAI_API_KEY


def get_openai_model(model="mistral-medium-latest"):
    if model is None:
        model = "mistral-medium-latest"
    return ChatMistralAI(
        model=model,
        temperature=0,
        max_retries=2,
        api_key=get_openai_api_key(),
        base_url="https://api.mistral.ai/v1"
    )