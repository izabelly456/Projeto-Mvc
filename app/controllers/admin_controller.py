from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario


from app.auth import get_admin, hash_password

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

templates = Jinja2Templates(directory="app/templates")

#listar todos usuarios 
@router.get("/")
def listar_usuarios(
    request: Request,
    db: Session = Depends(get_db),
    admin = Depends(get_admin), # Bloqueia quem nao é admin
):
    # pegar todos os usuarios do banco de dados
    usuarios = db.query(Usuario).order_by(Usuario.nome).all()

    return templates.TemplateResponse(
        request,
        "usuarios/index.html",
        {
            "request": request,
            "admin": admin, 
            "usuarios": usuarios
        }
    )