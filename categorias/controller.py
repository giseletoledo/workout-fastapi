from fastapi import APIRouter, Body, status
from categorias.schemas import CategoriaIn

from contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/', 
    summary='Criar uma nova Categoria',
    status_code=status.HTTP_201_CREATED,
)
async def post(
    db_session: DatabaseDependency, 
    categoria_in: CategoriaIn = Body(...)
):
    pass