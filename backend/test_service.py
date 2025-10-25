import sys
import os
print("Teste")

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
try:
    from app.services.chat_service import git_ia_response
    print("Importação bem-sucedida.")
    pergunta_teste = "Qual é a capital da França?"
    print(f"Pergunta de teste: {pergunta_teste}")
    resposta = git_ia_response(pergunta_teste)
    print("Resposta: ",resposta)
except ImportError as e:
    print("Detalhes: ",e)
except Exception as e: 
    print("Erro: ",e)
    