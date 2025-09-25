from pymongo import MongoClient

# Conectar ao MongoDB Atlas
uri = "mongodb+srv://heytornascimento_db_user:emacDX4rqMWAtgos@cluster0.zezstqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# Acessar o banco de dados
db = client["db_faculdade"]

# Acessar (ou criar automaticamente) a coleção
collection = db["alunas"]

# Documento a ser inserido
documento = {
    "nome": "João",
    "idade": 18,
    "ano": 2023,
    "genero": "",
    "altura": 1.70
}

# Inserir o documento
result = collection.insert_one(documento)

# Mostrar o ID do documento inserido
print("✅ Documento inserido com ID:", result.inserted_id)
