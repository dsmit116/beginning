#GCS Logic Engine
import os
import html
import datetime 
import calendar
import sqlite3
from sqlite3 import Error
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("patientintake.html")
if __name__ == "__main__":
    app.run(debug=True)

def user_info():
    username=input("Create a username:")
    name_first=input("Enter your first name")
    name_last=input("Enter your last name")
    password=input("Create a 7-15 character password:")
    primary_email= input("Enter a preferred contact email:")
    phone_number= input("Enter a preferred contact number:")
    
def insert_record(conn,first_name, last_name,
                  id_number, pt_fname,
                  pt_lname, pt_gcs,
                  injury_severity, email, birthdate):

    try:

        sql_insert = """
        INSERT INTO gcstracker
        (first_name, last_name, id_number,
         pt_fname, pt_lname, pt_gcs,
         injury_severity, email, birthdate)

        VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)
        """

        conn.execute(sql_insert,
        (
            first_name,
            last_name,
            id_number,
            pt_fname,
            pt_lname,
            pt_gcs,
            injury_severity,
            email, birthdate
        ))

        conn.commit()

        print(f"User '{first_name} {last_name}' added successfully.")

    except Error as e:
        print(f"Error inserting user: {e}")   
    
def scaling_eyes():
    print("1: No Response")
    print("2: Open to Pain")
    print("3: Open to Verbal")
    print("4:Open Voluntarily")
    print("Determine the score of Eyes Response (1-4)")
    eye_score = int(input("Enter the observed score:"))
    if 1 <= eye_score <= 4:
        return eye_score
    else:
        print("Error. Enter value from correct range (1-4)")
        return 0 
def scaling_talking():
    print("1: No Response")
    print("2: Incomprehensible sounds")
    print("3: Use of inappropriate Words")
    print("4:Confused")
    print("5: Alert and Oriented to Person, Place, Event")
    print("Determine the score of Verbal Response (1-5)")
    verbal_score = int(input("Enter the observed score:"))
    if 1 <= verbal_score <= 5:
            return verbal_score
    else:
            print("Error. Enter value from correct range (1-5)")
            return 0
def scaling_moving():
    print("1: No Response") 
    print("2: Decorticate Posturing")
    print("3: Decerebrate Posturing")
    print("4:Withdraws from Pain")
    print("5: Localizes Pain")
    print("6: Obeys Commands")
    print("Determine the score of Motor Response (1-6)")
    motor_score= int(input("Enter the observed score:"))
    if 1 <= motor_score <= 6:
       return motor_score
    else:
        print("Error. Enter value from correct range (1-6)")
        return 0
def gcs_total():
    e = scaling_eyes()
    v= scaling_talking()
    m = scaling_moving()
    total = e + v + m
    print(f"\n -- Total GCS Score: {total}---")
    if 3<= total <=8:
        injury_severity = "SEVERE"
    elif 9<= total<= 12:
        injury_severity = "MODERATE"
    else:
        injury_severity= "MILD"
        print("Injury Severity:", injury_severity)
        
    return injury_severity,total
def interface():
    print( "_" *30)
    print( "Glasgow Coma Scale Identifier")
    print( "_" *30)
    print("Press enter to continue...")

def profile_info():
    fname=input("Enter first name of patient:") 
    lname= input("Enter last name of patient:")
    print("Full name:", fname, lname)
    print("Press Enter to proceed...")
def full_doc():
    
    first_name = input("First Name:").strip()
    last_name = input("Last Name:").strip()
    
    id_number = int(input("Enter your ID number:"))
    
    pt_fname = input("Patient First Name:").strip()
    pt_lname = input("Patient Last Name:").strip()
    
    birthdate = input("Enter birth date (Format MM/DD/YYYY):")
    
    pt_gcs,injury_severity = gcs_total()
   
    email = input("Email: ").strip()
    
    print("Information has been captured!")
    print("Press Enter to proceed...")
    return (first_name, last_name, id_number, pt_fname, pt_lname, pt_gcs, injury_severity, email, birthdate)

def intakeform():
    full_doc()
def gcs_document():
    gcs_total()
def program_run():
    while True:

        interface()

        print("Main Menu")
        print("=" * 30)
        print("1. Profile Information")
        print("2. Complete Patient Intake Form")
        print("3. Exit")
        
        try:
            choice = int(input("Enter your menu selection: "))
        except ValueError:
            print("Please enter a number.")
            continue
        match choice:

           
            case 1:
                profile_info()

            case 2:

                user_data = full_doc()
                (first_name,last_name,id_number,pt_fname,pt_lname, pt_gcs,injury_severity,email,birthdate) = user_data
                connection = sqlite3.connect(r"C:\Users\dejas\OneDrive\Desktop\Projects\Database\gcslogic.db")
                cursor = connection.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS gcstracker (first_name TEXT, last_name TEXT, id_number INTEGER, pt_fname TEXT, pt_lname TEXT, pt_gcs INTEGER, injury_severity TEXT, email TEXT, birthdate TEXT)""")
                connection.commit()
                data = [first_name,last_name,id_number,pt_fname,pt_lname, pt_gcs,injury_severity,email,birthdate]
                cursor.execute("INSERT INTO 'gcstracker' ('first_name','last_name','id_number','pt_fname','pt_lname', 'pt_gcs','injury_severity','email', 'birthdate') VALUES (?,?,?,?,?,?,?,?,?)""", data)
                connection.commit()
            case 3:
                print("Exiting program...")
                break
            case _:
                print("Invalid selection.")


if __name__ == "__main__":
    program_run()
    

