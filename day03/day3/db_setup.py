from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine
from employee import Base
# Step 3: Setup database connection
engine = create_engine('sqlite:///employees_db.sqlite', echo=True)
# Step 4: Create table
Base.metadata.create_all(engine)
# Step 5: Create session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
