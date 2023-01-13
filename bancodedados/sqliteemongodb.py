from sqlalchemy import ForeignKey, Column, Integer, String, create_engine, inspect, select
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, nullable=False)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = Column(String(20))

    conta = relationship(
        "conta", back_populates="cliente"
    )

    def __repr__(self):
        return f"User(id={self.id}, id={self.nome}, id={self.cpf}, id={self.endereco},)"


class conta(Base):
    __tablename__ = "conta"

    id_conta = Column(Integer, primary_key=True)
    tipo_conta = Column(String)
    agencia = Column(String)
    num = Column(Integer)
    saldo = Column(String)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship(
        "cliente", back_populates="conta"
    )

    def __repr__(self):
        return f"User(id={self.id}, tipo={self.tipo}, agencia={self.agencia}, num={self.num}, saldo={self.saldo},)"

print(cliente.__tablename__)
print(conta.__tablename__)

engine = create_engine("sqlite://")

Base.metadata.create_all(engine)

inspector_engine = inspect(engine)
print(inspector_engine.has_table("cliente"))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)

with Session(engine) as session:
    lua = cliente(
        nome='lua silva',
        cpf='34798670989',
        endereco='rua francisco'
    )

    sol = cliente(
        nome='sol souza',
        cpf='34798670989',
        endereco='rua america',
    )

    session.add_all([lua, sol])

    session.commit()

stmt = select(cliente).where(cliente.nome.in_(['lua', 'sol']))
print('Recuperando usuários a partir de condição de filtragem')




