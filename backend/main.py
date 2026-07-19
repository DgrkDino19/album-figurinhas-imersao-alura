from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Inicializa a aplicação FastAPI
app = FastAPI()

# 1. Configura o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Define caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# 3. Lista contendo as 30 figurinhas do álbum
# Deixamos ativas apenas as figurinhas cujas imagens existem na pasta (IDs de 1 a 29)
# A figurinha com ID 30 (Você) foi comentada pois sua imagem correspondente ainda não existe no diretório
figurinhas = [
    {"id": 1, "nome": "Alan Turing", "categoria": "IA", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "John McCarthy", "categoria": "IA", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Sam Altman", "categoria": "IA", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Geoffrey Hinton", "categoria": "IA", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Yann LeCun", "categoria": "IA", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Guido van Rossum", "categoria": "Python", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Tim Peters", "categoria": "Python", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Raymond Hettinger", "categoria": "Python", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Travis Oliphant", "categoria": "Python", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Wes McKinney", "categoria": "Python", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Edgar F. Codd", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Larry Ellison", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Michael Widenius", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Salvatore Sanfilippo", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Eliot Horowitz", "categoria": "Banco de Dados", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Linus Torvalds", "categoria": "Sistemas Operacionais", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Dennis Ritchie", "categoria": "Sistemas Operacionais", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Richard Stallman", "categoria": "Sistemas Operacionais", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Bill Gates", "categoria": "Sistemas Operacionais", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Steve Jobs", "categoria": "Sistemas Operacionais", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Paulo Silveira", "categoria": "Brasil", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Guilherme Silveira", "categoria": "Brasil", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Gustavo Guanabara", "categoria": "Brasil", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Maurício Aniche", "categoria": "Brasil", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Andre David", "categoria": "Brasil", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Guilherme Lima", "categoria": "Brasil", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Gi Space Coding", "categoria": "Brasil", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Vinicius Neves", "categoria": "Brasil", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Rafaela Ballerini", "categoria": "Brasil", "imagem_url": "/figurinhas/29/imagem"},
    # {"id": 30, "nome": "Você", "categoria": "Brasil", "imagem_url": "/figurinhas/30/imagem"}
]

# 4. Crie o endpoint GET "/figurinhas" que retorna a lista
@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas ativas
    return figurinhas

# 5. Crie o endpoint GET "/figurinhas/{id}/imagem"
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Usa glob para encontrar o arquivo com prefixo correspondente na pasta figurinhas/
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Retorna erro 404 se não encontrar nenhum arquivo
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
        
    # Retorna o arquivo encontrado
    return FileResponse(arquivos[0])