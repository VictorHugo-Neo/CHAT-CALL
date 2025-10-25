from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

llm = OllamaLLM(model="mistral")
prompt  = PromptTemplate.from_template("Usuário: {pergunta}\nIA:")
chain = prompt | llm 
def git_ia_response(user_question: str) -> str:
    try:
        print(f"INFO: Invocando a IA com: {user_question}")
        resposta = chain.invoke({"pergunta": user_question})
        return resposta
    except Exception as e:
        print(f"ERROR: Falha ao obter resposta da IA: {e}")
        return "Desculpe, ocorreu um erro ao processar sua solicitação."

