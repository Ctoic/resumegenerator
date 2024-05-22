import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('sk-proj-Z8pp38lMYDv3kmHkCrS5T3BlbkFJ8Dk3RhDvrRqS1ffyAU51') or 'you-will-never-guess'
    MONGO_URI = os.environ.get('MONGO_URI')
    OPENAI_API_KEY = os.environ.get('sk-proj-Z8pp38lMYDv3kmHkCrS5T3BlbkFJ8Dk3RhDvrRqS1ffyAU51')
