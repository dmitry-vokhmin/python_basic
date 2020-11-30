from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Homeworks import models

class DataBase:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine) #Что делает metadata ?
        self.maker = sessionmaker(bind=engine)

    def session(self, data, model_name):
        session = self.maker()
        session.add(model_name(**data))
        try:
            session.commit()
        except Exception as e:
            session.rollback()
        finally:
            session.close()

    def create_category(self, data, model_name):
        self.session(data, model_name)

    def create_product(self, data, model_name):
        self.session(data, model_name)

    def create_promo(self, data, model_name):
        self.session(data, model_name)