from sqlalchemy import create_engine, String, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine("sqlite:///employees.db")


class Base(DeclarativeBase):
    pass

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    surname: Mapped[str] = mapped_column(String(50))
    position: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))



Base.metadata.create_all(engine)


def add_employee():
    with Session(engine) as session:

        while True:
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            position = input("Enter position: ")
            email =input("Entel email: ")

            employee = Employee (
                name=name,
                surname=surname,
                position=position,
                email=email
            )

            session.add(employee)

            choice = input("Do you want to add another employee? (y/n): ").lower()

            if choice != "y":
                break

        session.commit()
        print("\nEmployees added successfully!\n")


def view_employees():
    with Session(engine) as session:

        employees = session.query(Employee).all()

        if not employees:
            print("\nNo employees found.\n")
            return

        print("\n------ EMPLOYEES ------")
        print(f"{'ID':<5}{'NAME':<15}{'SURNAME':<15}{'POSITION'}{"email"}")

        for employee in employees:
            print(
                f"{employee.id:<5}{employee.name:<15}{employee.surname:<15}{employee.position}{employee.email}"
            )

        print()


def delete_employee():
    with Session(engine) as session:

        employees = session.query(Employee).all()

        if not employees:
            print("\nNo employees to delete.\n")
            return

        print("\nEmployees:")

        for employee in employees:
            print(f"{employee.id}. {employee.name} {employee.surname}{employee.email}")

        employee_id = int(input("\nEnter employee ID to delete: "))

        employee = session.get(Employee, employee_id)

        if employee:
            session.delete(employee)
            session.commit()
            print("Employee deleted successfully.\n")
        else:
            print("Employee not found.\n")


def employee1():
    while True:

        print("Choose an option:")
        print("1. Add new employee")
        print("2. View all employees")
        print("3. Delete an employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            delete_employee()

        elif choice == "4":
            print("exit")
            break

        else:
            print("Invalid option! Try again.\n")


employee1()