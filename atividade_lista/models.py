from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine('sqlite:///books.sqlite', echo=True)
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
Session = sessionmaker(bind=engine)
session = Session()

class Livro(Base):
    __tablename__ = 'livros'

    id_livro = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False, unique=True)
    autor = Column(String, nullable=False)
    categoria = Column(String, nullable=False)
    descricao = Column(String, nullable=False)

    def __repr__(self):
        return f'<Livro: {self.titulo}, {self.autor}, {self.categoria}, {self.descricao}>'

    def save (self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

    def serialize(self):
        try:
            dados = {
                "titulo": self.titulo,
                "autor": self.autor,
                "descricao": self.descricao,
                "categoria": self.categoria,
            }
            return dados
        except Exception as e:
            print(f"Erro ao serializar o livro: {e}")
            return None

Base.metadata.create_all(engine)
