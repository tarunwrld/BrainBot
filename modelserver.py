from ctransformers import AutoModelForCausalLM
import socket
import threading

def model(message):
    llm = AutoModelForCausalLM.from_pretrained("C:\\Users\\hp\\TarunCode\\Python\\streamlit\\falcon-7b-instruct.bin",
                                    model_type ="falcon",
                                    temperature=0.3,
                                    local_files_only=True
                                )
    

    generated_words = ""
    for words in llm(message, stream=True, reset=True):
        generated_words += words
    return generated_words

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        message = data.decode('utf-8')
        print(f"Received message: {message}")
        compile = model(message)
        response = "Server has compiled your response: " + compile
        client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 8080
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
