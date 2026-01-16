from fastapi import APIRouter, Body, status
from categorias.schemas import CategoriaIn, CategoriaOut
from categorias.models import CategoriaModel
from fastapi import HTTPException
from uuid import UUID
from sqlalchemy import select

from contrib.dependencies import DatabaseDependency

router = APIRouter()

@router.post(
    '/', 
    summary='Criar uma nova Categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut
)
async def post(
    db_session: DatabaseDependency, 
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:
    categoria_model = CategoriaModel(**categoria_in.model_dump())

    db_session.add(categoria_model)
    await db_session.commit()
    await db_session.refresh(categoria_model)

    return CategoriaOut(
        id=categoria_model.id,
        nome=categoria_model.nome
    )

@router.get(
    '/', 
    summary='Listar todas as Categorias',
    status_code=status.HTTP_200_OK,
    response_model=list[CategoriaOut]
)
async def get_all(
    db_session: DatabaseDependency
) -> list[CategoriaOut]:
    result = await db_session.execute(select(CategoriaModel))
    categorias = result.scalars().all()

    return [
        CategoriaOut(id=c.id, nome=c.nome)
        for c in categorias
    ]

@router.get(
    '/{id}',
    summary='Consulta uma Categoria pelo id',
    status_code=status.HTTP_200_OK,
    response_model=CategoriaOut,
)
async def query_id(
    id: UUID,
    db_session: DatabaseDependency,
) -> CategoriaOut:
    result = await db_session.execute(
        select(CategoriaModel).filter_by(id=id)
    )
    categoria = result.scalars().first()

    return categoria

