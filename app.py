from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub
import os
import requests
import streamlit as st

os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACETOKEN1"]
API_TOKEN = os.environ["HUGGINGFACEHUB_API_TOKEN"] = st.secrets["HUGGINGFACETOKEN2"]

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-v0.1"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


st.set_page_config(
    page_title="BrainBot",
    page_icon=":robot_face:",
    layout="wide"
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
        
        page = st.sidebar.radio("", ("Home", "Pdf Chat", "ChatBot","Privacy Policy", "Text-Bomber", "Text-to-Voice", "My Projects"))

    user = None  # Define the user variable outside the if block

    if page == "Home":
        with st.container():    
            page_bg_img = '''
                <style>
                    [data-testid = "stAppViewContainer"] {
                    # background-image: url("https://cdn.dribbble.com/userupload/9493524/file/original-191d685dc9e50c38cbb4f7363a7c714e.jpg?resize=1200x713");
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

        with st.container():
            st.divider()
        
    elif page == "Pdf Chat":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                # background-image: url("https://cdn.dribbble.com/users/1766465/screenshots/14502878/media/ba92064dd5bac7f0eadf35e515df14b5.png?resize=1000x750&vertical=center");
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
                background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/9192cab2-667e-4641-920d-5ed6cd554c15/d8fzxcq-4399d43f-3685-43a1-bc74-0611ef2f055c.png/v1/fill/w_1024,h_1280,q_80,strp/purple___blue_gradient___custom_box_background_by_rnewls_d8fzxcq-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI4MCIsInBhdGgiOiJcL2ZcLzkxOTJjYWIyLTY2N2UtNDY0MS05MjBkLTVlZDZjZDU1NGMxNVwvZDhmenhjcS00Mzk5ZDQzZi0zNjg1LTQzYTEtYmM3NC0wNjExZWYyZjA1NWMucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.GClmvnk9czR3dcYxAAV56txGcrqwWVg-DEVwJmP2AF0");
                background-size: cover;
                }
                </style>
                '''

            st.markdown(page_bg_img, unsafe_allow_html=True)

            st.title("Chat with PDF 📚🗣️")
            user = st.file_uploader("Upload PDF file", type="pdf")
            docs = []  # Moved this line here

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


    elif page == "ChatBot":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://cdn.dribbble.com/userupload/9624904/file/still-cb16e7cce808be23a2bfa8661007485b.png?resize=450x338&vertical=center");
                background-size: cover;
                }
                
                [data-testid = "stHeader"] {
                background-color : rgba(0,0,0,0);
                }

                [data-testid = "textInputRootElement"] {
                background-image: url("https://img.freepik.com/free-photo/studio-background-concept-abstract-empty-light-gradient-purple-studio-room-background-product-plain-studio-background_1258-63900.jpg");
                background-size: cover;
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

            # repo_id = "mistralai/Mistral-7B-v0.1" 
            repo_id = "openchat/openchat_3.5"
            st.title("Chat with BrainBot AI")
            st.markdown(""":red[**The BrainBot Ai is in early stages, can generete short inaccurate responses**]""")
            question = st.text_input("Write Something Here: ")
            st.button("Ask BrainBot")
            if question:
                if st.button:
                    template = """Question: {question}

                            Answer: Lets think step by step I'm a smart assistant My work is to provide efficient answer My name is BrainBot developed by Mr. Tarun"""

                    prompt = PromptTemplate(template=template, input_variables=["question"])
                    llm = HuggingFaceHub(
                        repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_length": 5000}
                    )
                    llm_chain = LLMChain(prompt=prompt, llm=llm)

                    generated_text = llm_chain.run(question)
                    with st.chat_message("user"):
                        st.write(generated_text)
                else:
                    st.warning("Oops! Something went wrong. Please try again.")


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

    elif page == "Text-Bomber":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://cdn.dribbble.com/users/2560227/screenshots/5288424/media/bb5367c566d7af6bd2dac446f3baebd6.png?resize=1000x750&vertical=center");
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
    elif page == "Text-to-Voice":
        with st.container():
            page_bg_img = '''
                <style>
                [data-testid = "stAppViewContainer"] {
                background-image: url("https://cdn.dribbble.com/users/2560227/screenshots/5288424/media/bb5367c566d7af6bd2dac446f3baebd6.png?resize=1000x750&vertical=center");
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
                background-image: url("https://blog.thomasnet.com/hs-fs/hubfs/shutterstock_774749455.jpg?width=900&name=shutterstock_774749455.jpg");
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

