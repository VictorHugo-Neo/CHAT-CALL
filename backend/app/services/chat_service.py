from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

def get_ia_response(pergunta: str):
    llm = OllamaLLM(model="mistral")
    prompt  = PromptTemplate.from_template("Usuário: {pergunta}\nIA:")
    chain = prompt | llm 

    print("chatbot deepseek iniciado")
    print("Digite sua pergunta ou 'sair' para encerrar.")

    while True: 
        pergunta = input("Você: ")
        if pergunta.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando o chatbot. Até logo!")
            break
        resposta = chain.invoke({"pergunta": pergunta})
        print(f"IA: {resposta}\n")
    

