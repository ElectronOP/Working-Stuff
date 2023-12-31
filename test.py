from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="The Atom", page_icon=":bulb:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#----------CSS Style---------

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

# -----LOAD ASSETS-----

lottie_coding = load_lottieurl("https://lottie.host/40b45951-80d4-4574-8172-af41ca65cbb3/fwBENUBuhN.json")
Image11 = Image.open("image11.jpg")
Dowload = Image.open("download.jpg")
Rap = Image.open("Image1234.jpeg")

#--------HEADER SECTION ---------
with st.container():
    st.subheader("Hi, Electron this side")
    st.title("Im ElectronOP")
    st.write("I love Playing Games Especially, Minecraft and Gta Series")
    st.write("[Checkout my Discord  Server >](https://discord.gg/89yhvWse)")

# ---WHAT I DO---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """ 
           I Play games like:
           - Minecraft
           - Gta 5
           - Gta San Andreas
           - Gta Vice city
           - Far Cry 3
          
           If you want to contact me, my Discord is given above
           
           """
        )
    with right_column:
        st_lottie(lottie_coding)

#---- HOW DO I PLAY MINECRAFT ----

with st.container():
    st.write("---")
    st.write("Minecraft Multiplayer")
    st.header("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
         st.image(Dowload)
    with text_column:
         st.subheader("Aternos is good for playing Minecraft multiplayer for free")
         st.write(
            """
            Contact me and i will teach you how to play Minecraft in aternos
            its a super good game and playing multiplayer makes it even more fun
            try it
            """
         )

with st.container():
    st.write("---")
    st.write("About Me")
    st.header("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
         st.image(Image11)
    with text_column:
         st.subheader("ElectronOP: The Legend")
         st.write(
            """
            Im ElectronOP, one of Minecraft Legends i love playing Minecraft and listening to Eminem
            I listen Rap songs and write rap rhymes
            Heres my profile pic.
            """
         )

#------ my Rap verses -------

with st.container(): 
    st.write("---") 
    st.write("My Rap Verses") 
    st.header("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(Rap)
    with text_column:
         st.subheader("Rap Legend") 
         st.write( 
             """ 
             I love writing Rap verses.
So far I have written 2 Verses
Btw, I will Repeat
- Will The Real Slim Shady......

             """
)



#--------- Contact ----------

with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("")


contact_form = """
<form action="https://formsubmit.co/nikhiliron285@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" bgcolor="blue" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message Here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

left_column, right_column = st.columns(2)
with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
        st.empty()
        
st.balloons()

tab1, tab2 = st.tabs(["Lol", "1"])

with tab1:
     tab1.write("Hi")
     tab1.header("heyy")
with tab2:
     tab2.write("Hello")
 

#------ button function --------

    
toggle = st.toggle("Brain")
if toggle:
    st.write('on')

