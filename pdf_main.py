from pdf_body import Chatbot

if __name__ == "__main__":
    pdf_file_path = r"C:\Users\USER\Downloads\paul.pdf"

    chat = Chatbot(pdf_file_path)

    chat.main()
