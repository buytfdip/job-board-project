from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.config import settings
from apis.version1.route_general_pages import general_pages_router
from db.session import engine  
from db.base import Base
from db.session import engine   #new
from db.base_class import Base  #new

def include_router(app):
	app.include_router(general_pages_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def create_tables():
	print('create tables')      
	Base.metadata.create_all(bind=engine)

	
def start_application():
	app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
	include_router(app)
	configure_static(app)
	create_tables()       
	return app

app = start_application()
