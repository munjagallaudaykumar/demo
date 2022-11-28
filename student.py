import os
import csv
import pandas as pd

print("""
    ========================================================
            Coding Academy Student Management System                 
    ========================================================""")

def mobile_sms(totalMarks,status):
    from twilio.rest import Client
    import keys

    client = Client(keys.account_sid,keys.auth_token)

    #try:
    client.messages.create(from_=keys.from_number,
        to=keys.to_number,
        body='Welcome to Coding Academy,\n\nTotal Marks : {}\n\nStatus : {}'.format(totalMarks,status))
    #except Exception as e:
    #    pass
        #print("Unable to send unverified numbers need to purchase..") 

def whatsapp_sms(totalMarks,status):
    from twilio.rest import Client
    import keys

    client = Client(keys.account_sid,keys.auth_token)

    #from_whatsapp_number = 'whatsapp:+14155238886'
    #to_whatsapp_number = 'whatsapp:+917207366926'

    message = client.messages.create( 
        from_='whatsapp:+14155238886',  
        body='Welcome to Coding Academy,\n\nTotal Marks : {}\n\nStatus : {}'.format(totalMarks,status),      
        to='whatsapp:+917207366926'
        )


def studentRegister():
    df=""
    rollNumber = int(input("Enter the Roll Number:"))
    studentName = input("Enter Student Name:")
    className = input("Enter the Class Name:")
    phoneNumber = input("Enter the Phone Number:")
    emailId = input("Enter Email Id:")
    try:
        filename = 'school.xlsx'
        file = os.path.isfile(filename)
        if not file:
            print("File Not Exists")
        else:
            df = pd.read_excel('school.xlsx')
        df2 = pd.DataFrame()
        df_rollno = df.rollNumber.tolist()
        if rollNumber not in df_rollno:
            df2['rollNumber'] = [int(rollNumber)]
            df2['studentName']=[studentName]
            df2['className']=[className]
            df2['phoneNumber'] = [phoneNumber]
            df2['emailId'] = [emailId]
            df2['coding'] = 0
            df2['iot'] = 0
            df2['mc'] = 0
            df2['totalMarks'] = 0
            df = df.append(df2)
            df.to_excel('school.xlsx',index=False)
            print("RollNo : {} successfuly registered".format(rollNumber))
        else:
            print("RollNo already Exists!!")
    except Exception as e:
        print(e)


def getAllStudents():
    df = pd.read_excel('school.xlsx')
    records = df.to_dict(orient='records')
    if records:
        print(records)
    else:
        print("No records")

def searchStudent():
    rollNumber = int(input("Enter RollNo:"))
    df = pd.read_excel('school.xlsx')
    data_frame = df[df.rollNumber == rollNumber]
    df_rollno = data_frame.rollNumber.tolist()

    if rollNumber not in df_rollno:
        print("Roll Number Not Exists!!")
    else:
        result ={
            "rollNumber":data_frame.rollNumber.tolist()[0],
            "studentName":data_frame.studentName.tolist()[0],
            "className":data_frame.className.tolist()[0],
            "phoneNumber":data_frame.phoneNumber.tolist()[0],
            "emailId":data_frame.emailId.tolist()[0]
        }
        print(result)

def deleteStudent():
    
    rollNumber = int(input("Enter Student Roll Number:"))
    df = pd.read_excel("school.xlsx")
    df = df[df.rollNumber == rollNumber]
    df_rollno = df.rollNumber.tolist()
    if rollNumber not in df_rollno:
        print("Roll Number Not Exists!!")
    else:    
        df = pd.read_excel('school.xlsx')
        df.drop(df[df.rollNumber == rollNumber].index.tolist()[0], inplace = True)
        df.to_excel("school.xlsx", index = False)
        print("{} is successfuly deleted".format(rollNumber))

def getStudentResult():

    rollNumber = int(input("Enter the Roll Number:"))
    df = pd.read_excel('school.xlsx')
    data_frame = df[df.rollNumber == rollNumber]

    df_rollno = data_frame.rollNumber.tolist()

    if rollNumber not in df_rollno:
        print("Roll Number Not Exists!!")
    else:
        totalMarks = (data_frame.coding.tolist()[0]) + (data_frame.iot.tolist()[0]) + (data_frame.mc.tolist()[0])
        name = data_frame.studentName.tolist()[0]
        print("For 1. To send Phone\nFor 2. To send Whatsapp")
        send_option = int(input("Results Sent to Phone or Whatsapp:"))
        if send_option == 1:
            if totalMarks > 50 :
                status="{} Passed".format(name)
                print("{} Passed".format(name))
                #try:
                mobile_sms(totalMarks,status)
                print("Results sent to Phone")
                # except Exception as e:
                #     print(e)

                # except Exception as e:
                #     print("Sms not sent Due to Technical problem")
                
            elif totalMarks < 50:
                status="{} Failed".format(name)
                print("{} Failed".format(name))
                mobile_sms(totalMarks,status)
                print("Results sent to Phone")
        elif send_option == 2:
            if totalMarks > 50 :
                status="{} Passed".format(name)
                print("{} Passed".format(name))
                #try:
                whatsapp_sms(totalMarks,status)
                print("Results sent to Whatsapp")
                # except Exception as e:
                #     print(e)

                # except Exception as e:
                #     print("Sms not sent Due to Technical problem")
                
            elif totalMarks < 50:
                status="{} Failed".format(name)
                print("{} Failed".format(name))
                whatsapp_sms(totalMarks,status)
                print("Results sent to Whatsapp")
             


                        
while True:
    print("""
    1. View list of the students
    2. Add New Student
    3. Search Student
    4. Delete Student
    5. Get Result""")

    option = int(input("Select Your Option:"))

    if option == 1:
        getAllStudents()
    elif option == 2:
        studentRegister()
    elif option == 3:
        searchStudent()
    elif option == 4:
        deleteStudent()
    elif option == 5:
        getStudentResult()
        break
    else:
        print("Invalid Option")
            

