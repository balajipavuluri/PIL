from time import sleep	
import streamlit as st	
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os	
from PIL import Image		
import sys



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)





def get_class_nd_click(x):
       
    y=str(x)    
    y='//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[{0}]/div'.format(x)
    try:
        sleep(1)
        cl= driver.find_element_by_xpath(y) #c_d[x])    
        cl.click()
    except:
        st.write("class link not available")
        img()

def join_class_nd_sound(x):
    try:    
        j=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/a')    
        j.click()   
        sleep(2)
        iframe = driver.find_element_by_xpath("//iframe[@id='frame']")  
        driver.switch_to.frame(iframe)  
        sleep(2)
        listen = driver.find_elements_by_tag_name("button") 
        for item in listen: 
            attrs = driver.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', item)    
            if 'aria-label' in attrs:   
                if attrs['aria-label'] == 'Listen only':    
                    item.click()    
                    sleep(5)   
                    img()   
                    break   
    except: 
        img()   
        st.write("క్లాస్ पूरा 🙌 :",x) 

def start(mail,passw):
    try:
                
        m_btn= driver.find_element_by_name('loginId')   
        m_btn.clear()   
        m_btn.send_keys(mail)   
        sleep(1)   
        p_btn=driver.find_element_by_name('password')   
        p_btn.clear()   
        p_btn.send_keys(passw)  
        sleep(1)   
        sub=driver.find_element_by_xpath('//button[text()="Submit"]')   
        sub.click() 
        sleep(1)   

           
        
        meet_path='/html/body/div[9]/div/div[1]/div/div/div[1]/div/div[2]/a'    
        meet = driver.find_element_by_xpath(meet_path)  
        meet.click()    

    except :
        img()
        st.write(' 🤯  vachindi ankunta 😔')
       



def img():	
    try:
        driver.save_screenshot("s.png")	
        image = Image.open('s.png')	
        st.image(image, caption='Image of class')	
        os.remove('s.png')	
    except:
        img()    

st.title(" I'll class join AVTA! 🙋" )	
with st.form(key="form1"):	
    mail=st.text_input("Enter mail")	
    passw=st.text_input("Enter passw", type="password")		
    #x=st.slider("class no",min_value=1,max_value=4)	
    class_link = st.selectbox(	
        'which class  you like to attend?',	
         ('class-1', 'class-2','class-3', 'class-4'))	
    
    	
 	
    submit=st.form_submit_button("click here")
    if submit:	
        #driver = webdriver.Chrome('C:/Users/balaji/Desktop/selenium/chromedriver.exe')	
        driver.maximize_window()	
        driver.get("https://rvrjcce.codetantra.com")	
        sleep(2)		
        l=driver.find_element_by_link_text("Log in")	
        l.click()	
        sleep(1)	
        
        start(mail,passw)

        sleep(1)

        get_class_nd_click(class_link[-1])
        sleep(1)

        join_class_nd_sound(class_link[-1])
        



        sleep(1)	
          	
       	

        
    else:	
       pass	
