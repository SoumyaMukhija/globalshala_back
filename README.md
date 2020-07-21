# globalshala_backend

# globalshala

In command prompt, run 


    git clone https://github.com/SoumyaMukhija/globalshala_front
    git clone https://github.com/SoumyaMukhija/globalshala_back
          
          
         
Once it has downloaded, go into the globalshala_back directory and run


     pip install -r requirements.txt
          

# Steps to run: 

1- Download ngrok from its website and put it in your PATH.

2- In a command prompt/terminal, run 

     ngrok http 5000

3- Copy the https://... link that pops up. DO NOT CLOSE THIS TERMINAL. 

4- Open the frontend directory. Navigate to src > utils > network_utils. Paste the https:// copied link in the BASE_URL variable. Save it and close.

5- Open a new terminal. Navigate to the backend directory from the terminal and run

     flask run 

6- Open a new terminal. Navigate to the frontend directory from the terminal and run 

     expo start
          
          
Scan the expo code from the website on your device on simulator. 
          

Dataset citations:

Mohan S Acharya, Asfia Armaan, Aneeta S Antony : A Comparison of Regression Models for Prediction of Graduate Admissions, IEEE International Conference on Computational Intelligence in Data Science 2019
