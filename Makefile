run:
	@uvicorn main:app --reload 

create-migrations:
	@PYTHONPATH=$$PYTHONPATH:$$(pwd) alembic revision --autogenerate -m "$(msg)"

run-migrations:
	@PYTHONPATH=$$PYTHONPATH:$$(pwd) alembic upgrade head