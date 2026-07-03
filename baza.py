# # # #from sqlalchemy.orm
# # # #orm object relation maping
# # # from sqlalchemy.orm import declarative_base,Mapped,mapped_column


# # # class base (declarative_base)
# # #         pass
# # # class usser (base):
# # #         _table name_="usser table"
# # # idMapped        
    
# # from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# # from sqlalchemy import String, Integer, create_engine
# # engine=create_engine("sqlite///baza")
# # class Base(DeclarativeBase):
# #         pass

# # class Users(Base):
# #     __tablename__ = "users_table"
# #     id: Mapped[int] = mapped_column(primary_key=True)
# #     name: Mapped[str] = mapped_column(String(50))
# #     email: Mapped[str] = mapped_column(String(50))

# # class Products(Base):
# #       __tablename__ = "products"
# #     id: Mapped[int]=mapped_column(primary_key=True)
# #     product_name: Mapped[str] = mapped_column(String(50))
# #     quantity: Mapped[int] = mapped_column(Integer())
# #     price: Mapped[int] = mapped_column(Integer())   


# # Base.metabase

# # ORM = Object Relational Mapping
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# from sqlalchemy import String, Integer, create_engine

# engine = create_engine("sqlite:///baza.db")

# class Base(DeclarativeBase):
#         pass

# # CREATE TABLE users_table(
# #   id INT PRIMARY KEY,
# #   name VARCHAR(50) NOT NULL,
# #   email VARCHAR(50) NOT NULL)
# class Users(Base):
#     __tablename__ = "users_table"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(50))
#     email: Mapped[str] = mapped_column(String(50))

# class Products(Base):
#     __tablename__ = "products"
#     id: Mapped[int]=mapped_column(primary_key=True)
#     product_name: Mapped[str] = mapped_column(String(50))
#     quantity: Mapped[int] = mapped_column(Integer())
#     price: Mapped[int] = mapped_column(Integer())

# Base.metadata.create_all(engine)
# import os
# print(os.path.abspath("baza.db"))

# ORM = Object Relational Mapping
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Integer, create_engine

engine = create_engine("sqlite:///baza.db")

class Base(DeclarativeBase):
        pass

# CREATE TABLE users_table(
#   id INT PRIMARY KEY,
#   name VARCHAR(50) NOT NULL,
#   email VARCHAR(50) NOT NULL)
class Users(Base): 
    __tablename__ = "users_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))

class Products(Base):
    __tablename__ = "products"
    id: Mapped[int]=mapped_column(primary_key=True)
    product_name: Mapped[str] = mapped_column(String(50))
    quantity: Mapped[int] = mapped_column(Integer())
    price: Mapped[int] = mapped_column(Integer())

Base.metadata.create_all(engine)