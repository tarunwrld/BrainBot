from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import HuggingFaceHub
import os
import io
from PIL import Image
import time
import requests
import streamlit as st
import socket

os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACETOKEN1"]
API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACETOKEN2"]

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
API_URL2 = "https://api-inference.huggingface.co/models/segmind/SSD-1B"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


st.set_page_config(
    page_title="BrainBot",
    page_icon=":robot_face:",
    layout="wide",
         menu_items={
        'About': "# Under Construction"
    }
    )

def main():
    # Set up Streamlit page
    with st.sidebar:
        st.sidebar.title("Navigation")
        hide_st_style = """
                <style>
                MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                # header {visibility: hidden;}
                </style>
                """
        st.markdown(hide_st_style, unsafe_allow_html=True)
        
        page = st.sidebar.radio("", ("Home", "Pdf Chat", "ChatBot","Text-to-Image","Privacy Policy", "Text-to-Voice", "My Projects"))

    user = None  # Define the user variable outside the if block

    if page == "Home":
        with st.container(): 
            page_bg_img = '''
                <style>
                    [data-testid = "stAppViewContainer"] {
                    background-image: url("https://cdn.dribbble.com/userupload/4011847/file/original-791dcead9571116617ad7b449547e6fe.png?resize=1200x1200");
                    background-size: cover;
                    }
                    [data-testid = "stHeader"] {
                    background-color : rgba(0,0,0,0);
                    }
                    [data-testid = "stToolbar"] {
                    right: 2rem;
                    }
                    
                    [data-testid = "stSidebar"] {
                    background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9192cab2-667e-4641-920d-5ed6cd554c15/d8fzxcq-4399d43f-3685-43a1-bc74-0611ef2f055c.png/v1/fill/w_1024,h_1280,q_80,strp/purple___blue_gradient___custom_box_background_by_rnewls_d8fzxcq-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzkxOTJjYWIyLTY2N2UtNDY0MS05MjBkLTVlZDZjZDU1NGMxNVwvZDhmenhjcS00Mzk5ZDQzZi0zNjg1LTQzYTEtYmM3NC0wNjExZWYyZjA1NWMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.GClmvnk9czR3dcYxAAV56txGcrqwWVg-DEVwJmP2AF0");
                    background-size: cover;
                    }

                   # div[data-testid="column"]:nth-of-type(1)
                    # {
                    #     border:1px solid red;
                    # } 
                    div[data-testid="column"]:nth-of-type(2)
                    {
                        # border:0.5px;
                        text-align: end;
                    }
                    img {
                        max-width: 80%; /* Set the maximum width to 100% of the container */
                        # height: 0.1; /* Maintain the aspect ratio */
                    } 
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
            left_column, right_column = st.columns(2)
            with left_column:
                
                st.subheader("// BRAINBOT - UNLEASH THE POWER OF LLM")

                st.title("Introducing BrainBot!!")

                st.subheader('Your interactive hub for intelligent creativity Ask, explore, and discover with BrainBot, powered by :red[LLM]. Unlock a world of information at your fingertips. ')
                st.write(":red[Select a page from the sidebar to get started.]")
            with right_column:
                st.markdown("![Alt Text](https://media1.giphy.com/media/eljCVpMrhepUSgZaVP/giphy.gif)")
                # st.video("https://cdn.dribbble.com/users/32512/screenshots/16146992/media/d3a1d9da27f3434eef4349725050da2b.mp4",format="video/mp4", start_time=0)
                st.write("BrainBot Neural Network")
                st.toast('Welcome User!!')
                time.sleep(2)
                st.toast('Start Exploring From Sidebar')
                time.sleep(5)

        with st.container():
            st.divider()
        
    elif page == "Pdf Chat":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://www.paint-paper.co.uk/media/catalog/product/cache/89c20c7b531947a66725fa39b70debca/b/o/bo23001_2.jpg");
                background-size: cover;
                }
                [data-testid = "stHeader"] {
                background-color : rgba(0,0,0,0);
                }
                [data-testid = "stToolbar"] {
                right: 2rem;
                }
                [data-testid = "stFileUploadDropzone"] {
                background-image: url("https://img.freepik.com/free-photo/studio-background-concept-abstract-empty-light-gradient-purple-studio-room-background-product-plain-studio-background_1258-63900.jpg");
                background-size: cover;
                }

                [data-testid = "stSidebar"] {
                background-image: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw0PDQ0NDw0NDQ0NDQ0NDQ0NDQ8NDQ0NFREWFhUVFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDQ0NFQ0PFS0dFRkrLy0tKystKzcrKysrLS0rLSsrLSs3LSs3KzctKy0rKy03LS0tLTc3NysrLSsrKys3N//AABEIASwAqAMBIgACEQEDEQH/xAAZAAEBAQEBAQAAAAAAAAAAAAAAAQMCBAf/xAAhEAEBAAICAgMAAwAAAAAAAAAAAQIRAyExcUFRkRJhgf/EABcBAQEBAQAAAAAAAAAAAAAAAAABAgP/xAAZEQEBAQEBAQAAAAAAAAAAAAAAARExQRL/2gAMAwEAAhEDEQA/APsIDi6gAAAAACKAgAAAoAA4d1wAAAADQAQAAAAAAABBQEAAAFHEduAABQAGqKgyAAAAAAAAAAAAgqAOcnSZQVyAKACNQFRKFEAAAAAAAAAAAAEAoOLNX2OeTPfU/Xmu99+Utbker+U+5+jzCavy94DbmlCiAAAAAAAAAAACWgZXXbHLLZlltEakHOeO/boFYDXLDfv7GWtesB0cioqAAIAAAAAAAADLly+Hed1GKVZPQAaAAAAekFrTCAAgCAAAAAAAADLlvevpwW97EbAAAAAAelUVpgQoAACAIAAAADnO9V045PARkAjQAAAAAD1Io0ygUAABBUQAAAAHHLOnaZTcsCMAEaAAAAAAeoBplBUAAASqAgCAAAADHkmr7cts8dxijUAAAAAAeoBpkoAIKgFABAEAAAABhnO63Zcs7/wqxwAiqigAig9Qg0yVFQFABAAQBAAAAAZ83iNHPJOqUnWKpFRoAAAB6MLtWUuq1aZEUBFAEFQBFAQBAAAAB51M/NEaVFAQUB2648vhyKNA2KyAoIAAAAiogAAAAy5Z3HLTlnXplEanHQAAAOxUqjrjvw6ZTzGozQBQAAAAAQQAAAEsY+Lpu45MfkqxwJFRQAHZQUSu8L05phe/YlaAKgAAACKCAigIAAADHPHV/qo2s2xyx0jUqiSgNAFBFAd43cVnjdVqM1BUUAAAAEVEAAAABLNxQHns0razYmLrkBVAAK7wrgErQSVVQAAEAVFRAAAAAAAABwANAAAAGN7aMmmF6IlVAEAAAAAAAAAAAAf/2Q==")
                background-size: cover;
                }
                </style>
                '''

            st.markdown(page_bg_img, unsafe_allow_html=True)

            st.title("Chat with PDF 📚🗣️")
            user = st.file_uploader("Upload PDF file", type="pdf")
            docs = []  # Moved this line here

            try:
                # Check if a PDF file is uploaded
                if user is not None:
                    user_question = st.text_input("Ask questions")
                    st.button("Ask BrainBot")

                    # Extract the text from the PDF
                    pdf_reader = PdfReader(user)
                    text = ""
                    for page in pdf_reader.pages:
                        text += page.extract_text()

                    # Split text into chunks
                    text_splitter = CharacterTextSplitter(
                        separator="\n",
                        chunk_size=150,
                        chunk_overlap=35,
                        length_function=len
                    )
                    chunks = text_splitter.split_text(text)

                    # Get embedding model
                    repo_id = "sentence-transformers/all-MiniLM-L6-v2"
                    hf = HuggingFaceHubEmbeddings(repo_id=repo_id)
                    embeddings = hf
                    knowledge_base = FAISS.from_texts(chunks, embeddings)

                    # Create vector database
                    if user_question:
                        docs = knowledge_base.similarity_search(user_question)

                        llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 50}
                        )

                        chain = load_qa_chain(llm, chain_type="stuff")
                        generated_text = chain.run(input_documents=docs, question=user_question)
                        with st.chat_message("assistant"):
                            st.write(generated_text)
            except:
                st.error("Error, This error can be genrated from server side.// Recommended Action: Rerun the App //")


    elif page == "ChatBot":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://wallpapers.com/images/high/simple-zoom-background-xo95fqa3fnc1box0.webp");
                background-size: cover;
                }
                
                [data-testid = "stHeader"] {
                background-color : rgba(0,0,0,0);
                }

                [data-testid = "stToolbar"] {
                right: 2rem;
                }
                
                [data-testid = "stSidebar"] {
                background-image: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw0PDQ0NDw0NDQ0NDQ0NDQ0NDQ8NDQ0NFREWFhUVFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDQ0NFQ0PFS0dFRkrLy0tKystKzcrKysrLS0rLSsrLSs3LSs3KzctKy0rKy03LS0tLTc3NysrLSsrKys3N//AABEIASwAqAMBIgACEQEDEQH/xAAZAAEBAQEBAQAAAAAAAAAAAAAAAQMCBAf/xAAhEAEBAAICAgMAAwAAAAAAAAAAAQIRAyExcUFRkRJhgf/EABcBAQEBAQAAAAAAAAAAAAAAAAABAgP/xAAZEQEBAQEBAQAAAAAAAAAAAAAAARExQRL/2gAMAwEAAhEDEQA/APsIDi6gAAAAACKAgAAAoAA4d1wAAAADQAQAAAAAAABBQEAAAFHEduAABQAGqKgyAAAAAAAAAAAAgqAOcnSZQVyAKACNQFRKFEAAAAAAAAAAAAEAoOLNX2OeTPfU/Xmu99+Utbker+U+5+jzCavy94DbmlCiAAAAAAAAAAACWgZXXbHLLZlltEakHOeO/boFYDXLDfv7GWtesB0cioqAAIAAAAAAAADLly+Hed1GKVZPQAaAAAAekFrTCAAgCAAAAAAAADLlvevpwW97EbAAAAAAelUVpgQoAACAIAAAADnO9V045PARkAjQAAAAAD1Io0ygUAABBUQAAAAHHLOnaZTcsCMAEaAAAAAAeoBplBUAAASqAgCAAAADHkmr7cts8dxijUAAAAAAeoBpkoAIKgFABAEAAAABhnO63Zcs7/wqxwAiqigAig9Qg0yVFQFABAAQBAAAAAZ83iNHPJOqUnWKpFRoAAAB6MLtWUuq1aZEUBFAEFQBFAQBAAAAB51M/NEaVFAQUB2648vhyKNA2KyAoIAAAAiogAAAAy5Z3HLTlnXplEanHQAAAOxUqjrjvw6ZTzGozQBQAAAAAQQAAAEsY+Lpu45MfkqxwJFRQAHZQUSu8L05phe/YlaAKgAAACKCAigIAAADHPHV/qo2s2xyx0jUqiSgNAFBFAd43cVnjdVqM1BUUAAAAEVEAAAABLNxQHns0razYmLrkBVAAK7wrgErQSVVQAAEAVFRAAAAAAAABwANAAAAGN7aMmmF6IlVAEAAAAAAAAAAAAf/2Q==")
                background-size: cover;
                }
                </style>
                '''

            st.markdown(page_bg_img, unsafe_allow_html=True)

            st.title("Chat with BrainBot AI")

            st.markdown(""":red[**Your privacy is of paramount importance to us ensuring that we do not collect any user data.**]""")

            st.markdown(""":red[**BrainBot is in early faces so server might take some seconds to respond Tip:- Have a fast internet connection**]""")

            st.divider()

            def mod(question):
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = 'india-artistic.gl.at.ply.gg'
                port = 10010
                client_socket.connect((host, port))
            
                while True:
                    client_socket.sendall(question.encode('utf-8'))
                    data = client_socket.recv(1024)
                    response = data.decode('utf-8')
                    return response

            def lol(question):
                d = mod(question)
                for word in d:
                    yield word
                    time.sleep(0.02)
                    
            question = st.chat_input("Write Something Here: ")

            if question:
                ans = lol(question)
                with st.status("In Progress..."):
                    st.write("Loading Model")
                    time.sleep(5)
                    st.write("Searching for data...")
                    time.sleep(5)
                st.write("Assistant: ")
                with st.chat_message("user"):
                    st.write(question)
                with st.chat_message("assistant"):
                    st.write_stream(ans)
            else:
                st.write("Try Asking Who is Elbert Einstien, Where is Taj Mahal Located.. ")

                    # except:
                    #     st.error("Error, This error can be genrated from server side.// Recommended Action: Rerun the App //")

    elif page == "Text-to-Image":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://cdn.wallpapersafari.com/66/44/2XSkpV.jpg");
                background-size: cover;
                }
                [data-testid = "stHeader"] {
                background-color : rgba(0,0,0,0);
                }
                [data-testid = "stToolbar"] {
                right: 2rem;
                }
                
                [data-testid = "stSidebar"] {
                background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9192cab2-667e-4641-920d-5ed6cd554c15/d8fzxcq-4399d43f-3685-43a1-bc74-0611ef2f055c.png/v1/fill/w_1024,h_1280,q_80,strp/purple___blue_gradient___custom_box_background_by_rnewls_d8fzxcq-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzkxOTJjYWIyLTY2N2UtNDY0MS05MjBkLTVlZDZjZDU1NGMxNVwvZDhmenhjcS00Mzk5ZDQzZi0zNjg1LTQzYTEtYmM3NC0wNjExZWYyZjA1NWMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.GClmvnk9czR3dcYxAAV56txGcrqwWVg-DEVwJmP2AF0");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)

            left_column, right_column = st.columns(2)
            try:
                with left_column:

                    st.header("Text To Image Generator 👻")
                    st.title("Generate infinite versions of your creativity with BrainBot.")

                    inpu1 = st.text_input("Write Your Creation🖋️")
                    o = st.button("Create")
                    if o:
                        st.toast('Processing!!', icon='📈')

                    st.write(" ")
                    st.divider()
                    st.write("Try writing Cute Cat🐈")

                    st.write("""
                            
                        This is an AI Image Generator. It creates an image from scratch from a text description.

                        Yes, this is the one you've been waiting for. This text to image generator uses AI to understand your words and convert them to a unique image each time. Like magic.

                        This can be used to generate AI art, or for general silliness.

                        Don't expect the quality to be photorealistic, however. You would need a really really big AI to do that, and have you priced those lately?

                        If you can't think of something, try "Balloon in the shape of X" where X is something you wouldn't find in balloon form.""")

                with right_column:
                    st.title("Your Creation Output🙌")
                    st.write("It can take some while....")

                    if inpu1:
                        progress_text = "Operation in progress. Please wait.."
                        my_bar = st.progress(0, text=progress_text)

                        for percent_complete in range(100):
                            time.sleep(0.1)
                            my_bar.progress(percent_complete + 1, text=progress_text)
                        time.sleep(1)
                        # my_bar.empty()
                        def query(payload):
                            response = requests.post(API_URL2, headers=headers, json=payload)
                            return response.content
                        image_bytes = query({
                            "inputs": inpu1,
                        })
                        image = Image.open(io.BytesIO(image_bytes))
                        new_image = image.resize((600, 500))
                        st.image(new_image, caption = inpu1)
                        my_bar.empty()

                st.divider()
            except:
                st.error("Error, This error can be genrated from server side.// Recommended Action: Reload the App //")
                
            st.divider()

    elif page == "Privacy Policy":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9192cab2-667e-4641-920d-5ed6cd554c15/d8fzxcq-4399d43f-3685-43a1-bc74-0611ef2f055c.png/v1/fill/w_1024,h_1280,q_80,strp/purple___blue_gradient___custom_box_background_by_rnewls_d8fzxcq-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzkxOTJjYWIyLTY2N2UtNDY0MS05MjBkLTVlZDZjZDU1NGMxNVwvZDhmenhjcS00Mzk5ZDQzZi0zNjg1LTQzYTEtYmM3NC0wNjExZWYyZjA1NWMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.GClmvnk9czR3dcYxAAV56txGcrqwWVg-DEVwJmP2AF0");
                background-size: cover;
                }
                [data-testid = "stHeader"] {
                background-color : rgba(0,0,0,0);
                }
                [data-testid = "stToolbar"] {
                right: 2rem;
                }
                
                [data-testid = "stSidebar"] {
                background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9192cab2-667e-4641-920d-5ed6cd554c15/d8fzxcq-4399d43f-3685-43a1-bc74-0611ef2f055c.png/v1/fill/w_1024,h_1280,q_80,strp/purple___blue_gradient___custom_box_background_by_rnewls_d8fzxcq-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzkxOTJjYWIyLTY2N2UtNDY0MS05MjBkLTVlZDZjZDU1NGMxNVwvZDhmenhjcS00Mzk5ZDQzZi0zNjg1LTQzYTEtYmM3NC0wNjExZWYyZjA1NWMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.GClmvnk9czR3dcYxAAV56txGcrqwWVg-DEVwJmP2AF0");
                background-size: cover;
                }
                </style>
                '''

            st.markdown(page_bg_img, unsafe_allow_html=True)


            st.header("Privacy Policy 🛠️")

            # Add interactive settings options here
            st.write(
                """
                At "BraintBot", we take your privacy seriously. We understand the importance of your personal information and are committed to ensuring that your privacy is protected when you use our app. This privacy policy outlines how we collect, use, and protect your data. Please read this policy carefully to understand our practices regarding your personal data and how we treat it.

                1. ** No Collection of Personal Information:
                    We do not collect or store any personal information from our users. Your privacy is our priority, and we designed our app to function without the need for any personal data.

                2. ** No Storage of Information:
                    We do not store any information provided by our users. Whether it's your name, address, email, or any other personal details, we do not retain any of this information within our app or on our servers.

                3. ** Inaccurate Data Generated:
                    The data generated by our app may be inaccurate. We do not guarantee the accuracy of the information provided by our app. Users should use the data generated as a reference and verify its accuracy through other means if necessary.

                4.  Third-Party Services:
                    Our app may contain links to third-party websites or services. We are not responsible for the content or privacy practices of these websites or services. We recommend that you review the privacy policies of these third-party sites.

                5.  Children's Privacy:
                    Our app is not intended for children under the age of 13. We do not knowingly collect personal information from children under 13. If you believe we have collected personal information from a child under 13, please contact us, and we will promptly remove the information.

                6.  Changes to Privacy Policy:
                    We reserve the right to modify this privacy policy at any time. Any changes we make will be effective immediately upon notice, which we may provide by any means, including posting a revised version on our app. Your continued use of our app after such changes constitutes your acceptance of the new privacy policy.

                7.  Contact Us:
                    If you have any questions or concerns about our privacy policy or how we handle your personal data, please contact us at "gozochan31@gmail.com".

                By using "BrainBot", you agree to the terms and conditions of this privacy policy. We appreciate your trust in us and assure you that we are committed to protecting your privacy and providing you with the best possible user experience.

                """
            )

    elif page == "Text-to-Voice":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://wallpapers.com/images/high/404-error-page-background-viahrdp4d4angmr8.webp");
                background-size: cover;
                }
                [data-testid = "stHeader"] {
                background-color : rgba(0,0,0,0);
                }
                [data-testid = "stToolbar"] {
                right: 2rem;
                }
                
                [data-testid = "stSidebar"] {
                background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9192cab2-667e-4641-920d-5ed6cd554c15/d8fzxcq-4399d43f-3685-43a1-bc74-0611ef2f055c.png/v1/fill/w_1024,h_1280,q_80,strp/purple___blue_gradient___custom_box_background_by_rnewls_d8fzxcq-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzkxOTJjYWIyLTY2N2UtNDY0MS05MjBkLTVlZDZjZDU1NGMxNVwvZDhmenhjcS00Mzk5ZDQzZi0zNjg1LTQzYTEtYmM3NC0wNjExZWYyZjA1NWMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.GClmvnk9czR3dcYxAAV56txGcrqwWVg-DEVwJmP2AF0");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)
    elif page == "My Projects":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://wallpapers.com/images/high/404-error-page-background-viahrdp4d4angmr8.webp");
                background-size: cover;
                }
                [data-testid = "stHeader"] {
                background-color : rgba(0,0,0,0);
                }
                [data-testid = "stToolbar"] {
                right: 2rem;
                }
                
                [data-testid = "stSidebar"] {
                background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9192cab2-667e-4641-920d-5ed6cd554c15/d8fzxcq-4399d43f-3685-43a1-bc74-0611ef2f055c.png/v1/fill/w_1024,h_1280,q_80,strp/purple___blue_gradient___custom_box_background_by_rnewls_d8fzxcq-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzkxOTJjYWIyLTY2N2UtNDY0MS05MjBkLTVlZDZjZDU1NGMxNVwvZDhmenhjcS00Mzk5ZDQzZi0zNjg1LTQzYTEtYmM3NC0wNjExZWYyZjA1NWMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.GClmvnk9czR3dcYxAAV56txGcrqwWVg-DEVwJmP2AF0");
                background-size: cover;
                }
                </style>
                '''
            st.markdown(page_bg_img, unsafe_allow_html=True)



if __name__ == "__main__":
    main()
