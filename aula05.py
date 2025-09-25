from pymongo import MongoClient

# Conectar ao MongoDB Atlas
uri = "mongodb+srv://heytornascimento_db_user:emacDX4rqMWAtgos@cluster0.zezstqk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# Acessar o banco de dados
db = client["db_faculdade"]

# Acessar (ou criar automaticamente) a coleção
collection = db["FaculdadeSenac"]

# Documento a ser inserido
documento = [{
    "nome": "João",
    "idade": 18,
    "ano": 2023,
    "genero": "",
    "altura": 1.70
},

{
    "id_produto": "p3213",
    "produto:":"computador",
    "fabricante": "acer",
    "datavalidade": 18,
    "ano": 2023,
},


{
    "id_postagem": "21321",
    "data": 18,
    "horario": 2023,
    "conteudo": "conteudo",
},

{
    "id_evento": "casadeheyt1233",
    "nome": "Hackathon 2023",
    "data_inicio": "2023-10-10",
    "ano": 2023,
},

{
    "isbn": "978-3-16-148410-0",
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "ano_publicacao": 1954,
        "genero": "Fantasia",
        "disponivel": True,
        "quantidade": 5
}

]

# Inserir o documento
result = collection.insert_many(documento)