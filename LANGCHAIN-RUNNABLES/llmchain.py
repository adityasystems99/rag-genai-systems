# =====================================================
# IMPORTS
# =====================================================

from langchain_openai import OpenAI

from langchain.prompts import PromptTemplate

from langchain.chains import LLMChain

from dotenv import load_dotenv

# =====================================================
# LOAD ENV VARIABLES
# =====================================================

load_dotenv()

# =====================================================
# CREATE