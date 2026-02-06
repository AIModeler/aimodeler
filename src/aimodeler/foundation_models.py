import os

def chatgpt_model:

  from openai import OpenAI
  import tiktoken

  client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

  LLM_MODEL = "gpt-4.1-nano"

  EMBED_MODEL = "text-embedding-3-small"

  TOKENIZER = tiktoken.encoding_for_model(EMBED_MODEL)
