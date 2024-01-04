import os
import PyPDF2
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from api_key import API_KEY
import json


os.environ["OPENAI_API_KEY"] = API_KEY

client = OpenAI(
  api_key=API_KEY
)

class Chatbot:
    def __init__(self, pdf_file_path):

        with open(pdf_file_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            pdf_text = ""

            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_text += page.extract_text()

        self.openai_instance = OpenAI(api_key=API_KEY)
        self.embeddings = OpenAIEmbeddings()
        self.text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        self.texts = self.text_splitter.split_text(pdf_text)
        self.docsearch = Chroma.from_texts(self.texts, self.embeddings)
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=ChatOpenAI(model="gpt-3.5-turbo-1106"),
            retriever=self.docsearch.as_retriever(search_kwargs={"k": 1}),
        )
        self.chat_history = []

    