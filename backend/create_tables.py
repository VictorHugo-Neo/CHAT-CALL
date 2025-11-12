import sys
import os
from sqlalchemy.exc import OperationalError

# Adiciona a pasta 'backend' ao path para encontrar 'app'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

try:
    from app.core.database import engine, Base
    # Importe todos os seus modelos aqui!
    from app.models import chat 

    print("Conectando ao banco de dados para criar tabelas...")
    
    # Este comando cria todas as tabelas (que herdam de Base)
    Base.metadata.create_all(bind=engine)
    
    print("[SUCESSO] Tabelas criadas (ou já existentes)!")

except OperationalError as e:
    print("\n[FALHA] Não foi possível conectar ao banco.")
    print("Verifique a DATABASE_URL no .env e se o Postgres está rodando.")
    print(f"Detalhe: {e}")
except ImportError as e:
    print(f"\n[FALHA] Erro de importação. Verifique os paths.")
    print(f"Detalhe: {e}")