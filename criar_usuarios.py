# popular o banco de dados com usarios admin 

from app.database import Session 
from app.models.usuario import Usuario
from app.auth import hash_password

USUARIOS = [
    {
        "nome": "Admin",
        "email": "admin@teste.com",
        "senha": "admin123",
        "role": "admin",
    },
    {
        "nome": " Izabelly",
        "email": "adminizabelly@teste.com",
        "senha": "admin123",
        "role": "admin",
    },
]
def criar_usuarios():
    db = Session()
    try:
        for user in USUARIOS:
            existente = db.query(Usuario).filter_by(email=user["email"]).first()
            if existente:
                print(f"esse e-mail {user['email']} já esta cadastrado no db")
            else:
                novo_usuario = Usuario(
                    nome=user["nome"],
                    email=user["email"],
                    senha_hash=hash_password(user["senha"]),
                    role=user["role"]
                )
                db.add(novo_usuario)
                print(f"Usuário cadastrado com sucesso: {user['nome']}")
        db.commit()


    except Exception as erro:
        db.rollback()
        print(f"Erro ao criar usuários: {erro}")
    finally:
        db.close()

criar_usuarios()

