

from sqlalchemy import Column, Integer, String;
from database import Base;


class Register(Base):
    __tablename__="register";
    customer_id=Column(Integer,primary_key=True,autoincrement=True)
    full_name=Column(String)
    email=Column(String)
    mobile=Column(String)
    address=Column(String)
    city=Column(String)
    state=Column(String)
    pincode=Column(String)

class pet_Health_Demo(Base):
    __tablename__="pet_health_tab";
    pet_id=Column(Integer,primary_key=True,autoincrement=True)
    vaccination_name=Column(String)
    vaccination_date=Column(String)
    nexts_due_date=Column(String)
    vet_name=Column(String)
    health_notes=Column(String)

class petregistration_Demo(Base):

    __tablename__="pet_register_tab";
    pet_id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String)
    pet_category=Column(String)
    breed=Column(String)
    age=Column(String)
    color=Column(String)
    weight=Column(String)
    arrival_date=Column(String)
    health_status=Column(String)
    pet_description=Column(String)



class petadoption_Demo(Base):
    __tablename__ = "pet_adopt_tab"

    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    sale_date = Column(String)
    customer_search = Column(String)
    pet_search = Column(String)
    payment_method = Column(String)
    total_amount = Column(String)
    discount = Column(String)
    final_amount = Column(String)
    remarks = Column(String)