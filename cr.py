import streamlit as st
import mysql.connector 
import time
import numpy as np
from matplotlib import pyplot as plt
from time import sleep
from scipy.integrate import odeint
import control as ct 
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="41712629@#$Ss",
#     database="msd_2"
# )
# mycursor=mydb.cursor()
# print("Connection Established")


st.title("Mass Spring Damper System Continuous to Discrete Converter")
def main():

    option=st.sidebar.selectbox(" Menu",("Home","About"))
    if option == "Home":
        st.subheader('welcome to simple mass spring damper system')
    #     st.subheader("Register")
    #     usernames=st.text_input("Enter user name")
    #     email=st.text_input("Enter Email")
    #     password=st.text_input("Enter your password")
    #     if st.button("Create"):
    #         sql= "insert into users(name,email,password) values(%s,%s,%s)"
    #         val= (usernames,email,password)
    #         mycursor.execute(sql,val)
    #         mydb.commit()
           
    #         def fetch_users():
    #             mycursor.execute("select * from users")
    #             users = mycursor.fetchall()
    #             return users.items
    #         def get_user_emails():
    #             mycursor.execute("select * from users")
    #             users = mycursor.fetchall()
    #             emails = []
    #             for user in users.items:
    #                 emails.append(user['email'])
    #             return emails
    #         def get_usernames():
    #             mycursor.execute("select * from users")
    #             users = mycursor.fetchall()
    #             usernames = []
    #             for user in users.items:
    #                 usernames.append(user['email'])
    #             return usernames
    #         def validate_email(email):
    #             pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com
    #             if re.match(pattern, email):
    #                 return True
    #             return False
    #         def validate_username(username):
    #             pattern = "^[a-zA-Z0-9]*$"
    #             if re.match(pattern, username):
    #                 return True
    #             return False
    #         def sign_up():
    #             with st.form(key='signup', clear_on_submit=True):
    #                 st.subheader(':green[Sign Up]')
    #                 email = st.text_input(':blue[Email]', placeholder='Enter Your Email')
    #                 username = st.text_input(':blue[Username]', placeholder='Enter Your Username')
    #                 password1 = st.text_input(':blue[Password]', placeholder='Enter Your Password', type='password')
    #                 password2 = st.text_input(':blue[Confirm Password]', placeholder='Confirm Your Password', type='password')
    #                 if email:
    #                     if validate_email(email):
    #                         if email not in get_user_emails():
    #                             if validate_username(username):
    #                                 if username not in get_usernames():
    #                                     if len(username) >= 2:
    #                                         if len(password1) >= 6:
    #                                             if password1 == password2:
    #                                                     hashed_password = stauth.Hasher([password2]).generate()
    #                                                     insert_user(email, username, hashed_password[0])
    #                                                     st.success('Account created successfully!!')
    #                                                     st.balloons()
    #                                             else:
    #                                                 st.warning('Passwords Do Not Match')
    #                                         else:
    #                                             st.warning('Password is too Short')
    #                                     else:
    #                                         st.warning('Username Too short')
    #                                 else:
    #                                     st.warning('Username Already Exists')
    #                             else:
    #                                 st.warning('Invalid Username')
    #                         else:
    #                             st.warning('Email Already exists!!')
    #                     else:
    #                         st.warning('Invalid Email')
    #                 btn1, bt2, btn3, btn4, btn5 = st.columns(5)
    #                 with btn3:
    #                     st.form_submit_button('Sign Up')
    #         st.success("created")
        # def fetch_users():
        #     users = mydb.fetch()
        #     return users.items
        # def get_user_emails():
        #     users = mydb.fetch()
        #     emails = []
        #     for user in users.items:
        #         emails.append(user[''])
        #         return emails
        # def validate_email(email):
        #     pattern = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$" #tesQQ12@gmail.com
        #     if re.match(pattern, email):
        #         return True
        #     return False
        # try:
        #     users = fetch_users()
        #     emails = []
        #     usernames = []

        #     for user in users:
        #         emails.append(user['email'])
        #         usernames.append(user['username'])
        # except:
        #       st.success('input_parameters')
              #def input_parameters():
        st.header("input parameters")
        m  = st.text_input("Mass:","5")
        f = st.text_input("Force:","0")
        ks = st.text_input("Spring Constant:","0")
        d = st.text_input("Damper Constant:","0")
        ts= st.text_input("Sampling time:","0.001")
        ti = st.text_input("Starting time :","0")
        tf= st.text_input("Stopping time:","0")
        plot = st.selectbox("MSD:",["Continuous","Discrete"])
        #sleep(10)
                      

        if st.button("plot graph:"):
            if plot == "Continuous":

                x_init = [0 ,0]
                increment = 0.1
                t = np.arange(float(ti),float(tf)+1,increment)
                def mydiff(x, t): 
                    dx1dt = x[1]
                    dx2dt = (float(f) - float(d)*x[1] - float(ks)*x[0])/float(m)
                    dxdt = [dx1dt, dx2dt]
                    return dxdt

                    # Solve ODE
                x = odeint(mydiff, x_init, t)
                x1 = x[:,0]
                x2 = x[:,1]
                    # Plot the Results
                fig1 = plt.figure(figsize=(10, 5) ,dpi =100)
                plt.plot(t,x1, t,x2)
                plt.title('Continuous of mass spring damper system')
                plt.xlabel('Time (sec)')
                plt.ylabel('y(t)')
                plt.legend(["y(t)", "y'(t)"])
                plt.grid()
                plt.show()
                st.pyplot(fig1)
            if plot == "Discrete":
                N = ((float(tf)-float(ti))/float(ts)) # Simulation length
                x1 = np.zeros(int(N)+2)
                x2 = np.zeros(int(N)+2)
                x1[0] = 0 # Initial Position
                x2[0] = 0 # Initial Speed
                a11 = 1
                a12 = float(ts)
                a21 = -(float(ts)*float(ks))/float(m)
                a22 = 1 - (float(ts)* float(d))/float(m)
                b1 = 0
                b2 = float(ts)/float(m)
                      
                for k in range(int(N)+1):
                      x1[k+1] = a11 * x1[k] + a12 * x2[k] + b1 * float(f)
                      x2[k+1] = a21 * x1[k] + a22 * x2[k] + b2 * float(f)
                t = np.arange(float(ti),float(tf) +2*float(ts),float(ts))
                fig = plt.figure(figsize=(10, 5) ,dpi =100)
                plt.plot(t, x1,t,x2)
                plt.title('Discrete mass spring damper system')
                plt.xlabel('Time (sec)')
                plt.ylabel('y(t)')
                plt.legend(["y(t)", "y'(t)"])
                plt.grid()
                plt.show()

                # Display first graph in Streamlit
                st.pyplot(fig)
    
    if option =="About":
        st.subheader('MSD is basic in control system analysising and modeling')
        st.markdown('Created by: [Sena Alemu](https://github.com/sorisena)')
        st.markdown('Contact via mail: [seenaabaayee@gmail.com]')      
if __name__ == "__main__":
    main()