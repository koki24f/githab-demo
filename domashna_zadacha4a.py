from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


engine = create_engine("sqlite:///baza.db")

print("Connection created successfully!")








engine = create_engine("sqlite:///baza.db")

print("Connection created successfully!")


# Base class
class Base(DeclarativeBase):
    pass


# Employees table
class Employees(Base):
    __tablename__ = "Employees"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))


# Create table
Base.metadata.create_all(engine)


# Add new employees
def add_user():

    number = int(input("How many employees do you want to add? "))

    with Session(engine) as session:

        for i in range(number):

            print(f"\nEnter details for employee {i + 1}")

            name = input("Enter name: ")
            email = input("Enter email: ")

            new_employee = Employees(
                name=name,
                email=email
            )

            session.add(new_employee)

        session.commit()

    print(f"\n{number} employee(s) added successfully!")


# View all employees
def view_users():

    with Session(engine) as session:

        employees = session.query(Employees).all()

        if employees:

            print("\n------ Employees List ------")
            print(f"{'ID':<5}{'NAME':<15}{'email':<15}")

            print("-" * 40)

            for employee in employees:

                print(f"{employee.id:<5}{employee.name:<15}{employee.email:<15}")
                print()
                


# Delete employee
def delete_employee():

    with Session(engine) as session:

        employees = session.query(Employees).all()

        if employees:

            print("\n------ Employees List ------")
            print("-" * 40)

            for employee in employees:

                print(
                    f"ID: {employee.id} | "
                    f"Name: {employee.name} | "
                    f"Email: {employee.email}"
                )

            print("-" * 40)

            employee_id = int(
                input("Enter the ID of the employee to delete: ")
            )

            employee = session.query(Employees).filter_by(id=employee_id).first()

            if employee:

                session.delete(employee)
                session.commit()

                print("Employee deleted successfully!")

            else:
                print("Employee not found!")

        else:
            print("No employees found!")


# Main program menu
while True:

    print("\nChoose an option:")
    print("1. Add new user")
    print("2. View all users")
    print("3. Delete an employee")
    print("4. Exit")

    choice = input("Enter choice: ")


    if choice == "1":

        add_user()


    elif choice == "2":

        view_users()


    elif choice == "3":

        delete_employee()


    elif choice == "4":

        print("Goodbye!")
        break


    else:

        print("Invalid choice!")


def employee1():
    while True:

        print("Choose an option:")
        print("1. Add new employee")
        print("2. View all employees")
        print("3. Delete an employee")
        print("4. Exit")

        choice = input("Enter your choice: ")