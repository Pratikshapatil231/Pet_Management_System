from flask import Flask,render_template,request;
from sqlalchemy.orm import Session;
from sqlalchemy import select;
from database import engine,Base;
from models import Register, pet_Health_Demo,petregistration_Demo,petadoption_Demo;

app=Flask(__name__);

Base.metadata.create_all(engine);


@app.route("/login")
def login():
    return render_template("login.html");

@app.route("/dashboard")
def dashboard():
     return render_template("dashboard.html");
   
@app.route("/pet_registration")
def pet_registratio():
     return render_template("pet_registration.html");

@app.route("/customer_registration")
def customer_registration():
     return render_template("customer_registration.html");

@app.route("/pet_ health")
def pet_health():
     return render_template("pet_ health.html");

@app.route("/petadoption")
def petadoptio():
     return render_template("petadoption.html");


@app.route("/login-data",methods=["POST"])
def loginData():
     email=request.form["email"];
     password=request.form["password"];
     
     return f'''email={email}
    
     password={password}
   ''';

@app.route("/register-user",methods=["POST"])
def Registers():
    data = request.form
    session=Session(engine);
    register=Register(
        full_name=data.get("full_name"),
        email=data.get("email"),
        mobile=data.get("mobile"),
        address=data.get("address"),
        city=data.get("city"),
        state=data.get("state"),
        pincode=data.get("pincode"),
    );

    session.add(register);
    session.commit();   
    session.close();
    return("User Register Successfully");

@app.route("/register-data")
def registerData():
    session = Session(engine)

    statement = select(Register)

    result = session.scalars(statement).all()

    session.close()

    return render_template(
        "users.html",
        users=result
    )

@app.route("/health_demo",methods=["POST"])
def add_pet_healths():
    data = request.form
    session=Session(engine);
    pet_health_tab = pet_Health_Demo(
    vaccination_name=data.get("vaccination_name"),
    vaccination_date=data.get("vaccination_date"),
    nexts_due_date=data.get("nexts_due_date"),
    vet_name=data.get("vet_name"),
    health_notes=data.get("health_notes")
)

    session.add(pet_health_tab);
    session.commit();   
    session.close();
    return("pet health daata add  Successfully");

@app.route("/healths")
def view_pet_healths():
    session = Session(engine)

    statement = select(pet_Health_Demo)

    result = session.scalars(statement).all()

    session.close()

    return render_template(
    "pet_health.html",
    healths=result
)




@app.route("/pet_register_demo",methods=["POST"])
def add_pet():
    data = request.form
    session=Session(engine);
    pet_register_tab = petregistration_Demo(
    pet_id=data.get("pet_id"),
    name=data.get("name"),
    pet_category=data.get("pet_category"),
    breed=data.get("breed"),
    age=data.get("age"),
    color=data.get("color"),
    weight=data.get("weight"),
    arrival_date=data.get("arrival_date"),
    health_status=data.get("health_status"),
    pet_description=data.get("pet_description")
)

    session.add(pet_register_tab);
    session.commit();   
    session.close();
    return("pet register Successfully");

@app.route("/pet_adoption_demo",methods=["POST"])
def adopt_pet():
    data = request.form
    session=Session(engine);

    pet_adopt_tab = petadoption_Demo(

    sale_id=data.get("sale_id"),
    sale_date=data.get("sale_date"),
    customer_search=data.get("customer_search"),
    pet_search=data.get("pet_search"),
    payment_method=data.get("payment_method"),
    total_amount=data.get("total_amount"),
    discount=data.get("discount"),
    final_amount=data.get("final_amount"),
    remarks=data.get("remarks")
)

    session.add(pet_adopt_tab);
    session.commit();   
    session.close();
    return("pet adopt Successfully");

@app.route("/petadopt")
def adopt_pets():
    session = Session(engine)

    statement = select(petadoption_Demo)

    result = session.scalars(statement).all()

    session.close()

    return render_template(
    "pet_register.html",
    healths=result
)
    

@app.route("/custregistration_demo", methods=["POST"])
def custregistration_demo():

    full_name = request.form["full_name"]
    email = request.form["email"]
    mobile = request.form["mobile"]
    address = request.form["address"]
    city = request.form["city"]
    state = request.form["state"]
    pincode = request.form["pincode"]

    active_status = request.form.get("active-status")


    

    return f"""
    <h2>Customer Registration Details</h2>

    full_name: {full_name}<br>
    Email : {email}<br>
    Mobile : {mobile}<br>
    Address : {address}<br>
    City : {city}<br>
    State : {state}<br>
    Pincode : {pincode}<br>
    Active Status : {active_status}<br>
    
    """

@app.route("/petregistration_demo", methods=["POST"])
def petregistration_demo():
    name = request.form["name"]
    pet_category = request.form["pet_category"]
    breed = request.form["breed"]
    gender = request.form["gender"]
    age = request.form["age"]
    color = request.form["color"]
    weight = request.form["weight"]
    arrival_date = request.form["arrival_date"]
    vaccinated = request.form.get("vaccinated")
    health_status = request.form["health_status"]
    pet_description = request.form["pet_description"]
    

   

    

    return f"""
    <h2>Pet Registration Details</h2>

    name : {name}
    pet_category : {pet_category}<br>
    Breed : {breed}<br>
    Gender : {gender}<br>
    Age : {age}<br>
    Color : {color}<br>
    Weight : {weight}<br>
    Arrival Date : {arrival_date}<br>
    Vaccinated : {vaccinated}<br>
    health_status : {health_status}<br>
    pet_description : {pet_description}<br>
    
    """

@app.route("/petadoption_demo", methods=["GET", "POST"])
def petadoption_demo():

    if request.method == "POST":
        sale_id = request.form["sale_id"]

        sale_date = request.form["sale-date"]
        customer_search = request.form["customer-search"]
        pet_search = request.form["pet-search"]
        payment_method = request.form["payment-method"]
        total_amount = request.form["total-amount"]
        discount = request.form["discount"]
        final_amount = request.form["final-amount"]
        agreement = request.form.get("agreement")
        remarks = request.form["remarks"]

        return f"""
        <h2>Pet Adoption / Sales Details</h2>

        Sale Date : {sale_date}<br>
        Customer : {customer_search}<br>
        Pet : {pet_search}<br>
        Payment Method : {payment_method}<br>
        Total Amount : ₹{total_amount}<br>
        Discount : ₹{discount}<br>
        Final Amount : ₹{final_amount}<br>
        Agreement Accepted : {agreement}<br>
        Remarks : {remarks}
        """
    

@app.route("/pet_health_demo", methods=["GET", "POST"])
def pet_health_demo():
    

    if request.method == "POST":
        

        
        vaccination_name = request.form["vaccination_name"]
        vaccination_date = request.form["vaccination_date"]
        nexts_due_date = request.form["nexts_due_date"]
        vet_name = request.form["vet_name"]
        reminder_enabled = request.form.get("reminder_enabled")
        health_notes = request.form["health_notes"]
        medical_report = request.form.get("medical_report")
       

        return f"""
        <h2>Pet Health Details</h2>


        Vaccination Name : {vaccination_name}<br>
        Vaccination Date : {vaccination_date}<br>
        Next Due Date : {nexts_due_date}<br>
        vet_name: {vet_name}<br>
        Reminder Enabled : {reminder_enabled}<br>
        Health Notes : {health_notes}<br>
        Medical Report : {medical_report}<br>
       
        """
    
    






   

if __name__=="__main__":
    app.run(debug=True)