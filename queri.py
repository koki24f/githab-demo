
from baza import engine, Users, Products
from sqlalchemy.orm import Session
from sqlalchemy import select

#session = Session(engine)
#.....
#session.close()

# with Session(engine) as session:
#     # user = Users(name="Ana", email="ana@example.com") # INSERT INTO User (name,email) VALUES ("Ana", "ana@example.com");
#     # session.add(user)
#     # session.commit()
#     for i in range(5):
#         ime = input("Vnesi Ime: ")
#         email = input("Vnesi email: ")
#         user = Users(name=ime, email=email)
#         session.add(user)
#         session.commit()

# users_list = []
# for i in range(5):
#     user_dict = {}
#     user_dict["ime"] = input("Vnesi Ime: ")
#     user_dict["email"] = input("Vnesi email: ")
#     users_list.append(user_dict)
#     #[{"ime":"Ana", "email":"ana@example.com"},......]

# with Session(engine) as session:
#     for u in users_list:
#         user = Users(name=u["ime"], email=u['email'])
#         session.add(user)
#         session.commit()
    


with Session(engine) as session:
    users_select = select(Users)
    users = session.scalars(users_select).all()
    #print(users[0].name)
    for user in users:
        print(f"{user.id}. {user.name} - {user.email}")