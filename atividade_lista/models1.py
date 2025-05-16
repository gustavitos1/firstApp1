from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine('sqlite:///user.sqlite', echo=True)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False, unique=True)
    salario = Column(String, nullable=False)
    profissao = Column(String, nullable=False)

    def __repr__(self):
        return f'<User: {self.nome}, {self.salario}, {self.profissao}>'

    def save (self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        dados_user = {
            'id_user': self.id_user,
            'nome': self.nome,
            'salario': self.salario,
            'profissao': self.profissao
        }
        return dados_user

Base.metadata.create_all(engine)