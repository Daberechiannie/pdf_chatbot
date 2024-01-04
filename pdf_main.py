from pdf_body import Chatbot

def main(pdf_file_path ):
        chatbot = Chatbot(pdf_file_path )
        while True:
            query = input("You: ")  

            if query.lower() in ['quit', 'exit']:

                break  

            result = chatbot.chain({"question": query, "chat_history": chatbot.chat_history})

            answer = result['answer']

            print(f"Bot: {answer}")

            chatbot.chat_history.append((query, answer))


if __name__ == "__main__":
    pdf_file_path = r"C:\Users\USER\Downloads\paul.pdf"

    # chat = Chatbot(pdf_file_path)

    main(pdf_file_path )
