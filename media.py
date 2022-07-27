
import streamlit as st
from PIL import Image
import pytube
from pytube import YouTube
import instaloader
from instaloader import Post
import requests
import urllib.request
import os
import re

st.title("Social Media Video Downloader")
st.text("By Copy-paste link")
#imgage=Image.open("C:/Users/hp/Downloads/Soc dow.jpg")
#nimgage=imgage.resize((800,200))
#st.image(nimgage)
st.text("By Copy-paste link")

def check_internet():
    cmd = os.system('ping google.com -w 4 > clear')
    if cmd == 0:
        st.write('Internet is connected Downloader is ready')
    else:
        st.write('Internet is not connected troublshoote the your Network connections')
check_internet()


rad=st.sidebar.radio("Social Media Video Downloader",["Instagram","Youtube","Facebook"])

def main():
    if rad =="Youtube":
        st.title("Youtube Downloader")
        #imge=Image.open("C:/Users/hp/Downloads/ytt.jpg")
        #nimge=imge.resize((800,400))
        #st.image(nimge)
        path = st.text_input('Enter URL of any youtube video')
        option = st.selectbox('Select type of download',('audio', 'highest_resolution', 'lowest_resolution'))
        matches = ['audio', 'highest_resolution', 'lowest_resolution']
        if st.button("download"):
            video_object =  YouTube(path)
            st.write("Title of Video: " + str(video_object.title))
            st.write("Number of Views: " + str(video_object.views))
            st.write("Length of Vide: " + str(video_object.length))
            st.write("Description: " + str(video_object.description))
            if option=='audio':
                video_object.streams.get_audio_only().download()
                #4.b64encode("if file is too large").decode()
            elif option=='highest_resolution':
                video_object.streams.get_highest_resolution().download()
            elif option=='lowest_resolution':
                video_object.streams.get_lowest_resolution().download()
        if st.button("view"):
            st.video(path)
            vid=  YouTube(path)
            st.write("Title of Video: " + str(vid.title))
            st.write("Number of Views: " + str(vid.views))
            st.write("Length of Vide: " + str(vid.length))
            st.write("Description: " + str(vid.description))
if rad=="Instagram":
    st.title("Instagram Downloader")
    #img=Image.open("C:/Users/hp/Downloads/inst dow.jpg")
    #nimg=img.resize((800,400))
    #st.image(nimg)
       
    i=instaloader.Instaloader()
    user=st.text_input("Enter instagram username:")
    if st.button("Download"):
        i.download_profile(user,profile_pic_only=True)

    


    url =st.text_input("Please enter Instagram Post URL: ")
    a=url[26:28]  
    b=url[26:27]
    c=url[26:30]
    # b='tv'
    if a=='tv':
        shorted_url=url[29:40]
        i = instaloader.Instaloader()
        post =Post.from_shortcode(i.context,shorted_url)
        if st.button("Download vdo"):
            i.download_post(post, target='download_post')
            
            
            #print(shorted_url)
    if b=='p':
        shorted_url=url[28:39]
        i = instaloader.Instaloader()
        post =Post.from_shortcode(i.context,shorted_url)    
        if st.button("Download post"):
            i.download_post(post, target='download_post')

    if c=='reel':
        shorted_url=url[31:42]
        i = instaloader.Instaloader()
        post =Post.from_shortcode(i.context,shorted_url)
        if st.button("Download Reel"):
            i.download_post(post, target='download_post')
    
#filedir = os.path.join('C:/Users/hp')
#ERASE_LINE = '\x1b[2K'
if rad=="Facebook":
    st.title("Facebook Downloader")
    link=st.text_input("Enter FB video url here")
# read the html of the link
    html=requests.get(link)
    opt = st.selectbox('Select Video Quality',('HD','SD'))
    matches = ['HD', 'SD']
    if opt=='HD':
        if st.button("download"):
            url=re.search('hd_src:"(.+?)"',html.text)[1]
        #url=re.search('sd_src:"(.+?)"',html.text)[1]
            urllib.request.urlretrieve(url,"Video.mp4")
            st.write("Downloaded")
            
    if opt=='SD':
        if st.button("download"):
            url=re.search('sd_src:"(.+?)"',html.text)[1]
        #url=re.search('sd_src:"(.+?)"',html.text)[1]
            urllib.request.urlretrieve(url,"Video.mp4")
            st.write("Downloaded")
        


if __name__ == '__main__':
	main()
