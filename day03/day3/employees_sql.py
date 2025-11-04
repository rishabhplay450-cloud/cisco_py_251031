from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Float, create_engine



# Step 1: Define Base
Base = declarative_base()


# Step 2: Define Employee model
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    job_title = Column(String(255), nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', job_title='{self.job_title}', salary={self.salary})>"


# Step 3: Setup database connection
engine = create_engine('sqlite:///employees_db.sqlite', echo=True)

# Step 4: Create table
Base.metadata.create_all(engine)

# Step 5: Create session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

"""
# Step 6: CRUD operation example (Create)
dravid = Employee(name='Dravid', job_title='Old Coach', salary=1200)
session.add(dravid)
session.commit()

jaiswal = Employee(name='Jaiswal', job_title='Young Coach', salary=1500)
session.add(jaiswal)
session.commit()

abhishek = Employee(name='Abhishek', job_title='Assistant Coach', salary=1000)
session.add(abhishek)
session.commit()

# Step 7: Verify
employees = session.query(Employee).all()
print(employees)

abhi=session.query(Employee).filter_by(name='Abhishek').first()
print(abhi)

abhishek.salary=1100
session.commit()
print(abhi)

"""

mahesh=Employee(name='Mahesh', job_title='Manager', salary=2000)
session.add(mahesh)
session.commit()

employees = session.query(Employee).all()
print(employees)
session.delete(mahesh)
session.commit()    





