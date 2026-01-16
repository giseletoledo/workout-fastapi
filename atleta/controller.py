from fastapi import APIRouter
from fastapi import Body, status
from uuid import uuid4
from atleta.schemas import AtletaIn, AtletaOut
from atleta.models import AtletaModel

from contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/', 
    summary='Criar um novo atleta',
    status_code=status.HTTP_201_CREATED,
    response_model=AtletaOut
)
async def post(
    db_session: DatabaseDependency, 
    atleta_in: AtletaIn = Body(...)
):
    pass