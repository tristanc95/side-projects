#!/usr/bin/env python
#!import items
import time
import tkinter as tk
from tkinter import *
from tkinter import Toplevel, simpledialog
from tkinter.messagebox import askquestion
from pywinauto import application

app = application.Application()

Root = tk.Tk()
Root.withdraw()

def get_link_first():
    YT_LINK = simpledialog.askstring(title="YouTube Link", prompt="Please enter the YouTube Link you want to download")
    if YT_LINK == 'None':
        quit
    else:
        LinkLength = len(YT_LINK)
        global thelink
        thelink = str(YT_LINK)
        

    if LinkLength == 0:    
        Goofed = tk.messagebox.showerror(title="No Link Included!", message="Please enter a full YouTube Link.")
        if Goofed == 'Cancel':
            quit
        else:
            get_link_first()
    
    if LinkLength > 40:
        link_format()
    else:
        GoofedAgain = tk.messagebox.showerror(title="Not Long Enough.", message="Please enter a full YouTube Link.")
        if GoofedAgain == 'Cancel':
            quit
        else:
            get_link_first()

def link_format():
    L_FORMAT = simpledialog.askstring(title="Type Of Link", prompt="What type of YouTube link is this? C for Channel, P for Playlist, V for Video")
    if L_FORMAT == 'C' or L_FORMAT =='c':
        channel_download_first()
    elif L_FORMAT == 'P' or L_FORMAT =='p':
        playlist_download_first()
    elif L_FORMAT == 'V' or L_FORMAT =='v':
        video_download_first()
    else:
        Incorrect_Format = tk.messagebox.showerror(title="Not a right format!", message="Please enter one of the 3 letters above only.")
        link_format()

def video_download_first():
    app.start('C:\Program Files\ConEmu\ConEmu64.exe')
    time.sleep(1.5)
    app.ConEmu.type_keys("cd {VK_SPACE} D:youtube-dl ~")
    time.sleep(1)
    app.ConEmu.type_keys("D: ~")
    time.sleep(1)
    app.ConEmu.type_keys("yt-dlp {VK_SPACE} -f {VK_SPACE} bestaudio[ext=m4a]{+}bestvideo[ext=mp4] {VK_SPACE}")
    app.ConEmu.type_keys(thelink)
    time.sleep(1.5)
    app.ConEmu.type_keys("~")
    time.sleep(3)
    continuing_or_closing()

def playlist_download_first():
    app.start('C:\Program Files\ConEmu\ConEmu64.exe')
    time.sleep(1.5)
    app.ConEmu.type_keys("cd {VK_SPACE} D:youtube-dl ~")
    time.sleep(1)
    app.ConEmu.type_keys("D: ~")
    time.sleep(1)
    app.ConEmu.type_keys("yt-dlp {VK_SPACE} -f {VK_SPACE} bestvideo[ext=mp4]{+}bestaudio {VK_SPACE} -o {VK_SPACE} {%}{(}playlist{)}s/{%}{(}playlist_index{)}s.{%}{(}title{)}s.{%}{(}ext{)}s {VK_SPACE}")
    app.ConEmu.type_keys(thelink)
    time.sleep(1.5)
    app.ConEmu.type_keys("~")
    time.sleep(30)
    continuing_or_closing()

def channel_download_first():
    app.start('C:\Program Files\ConEmu\ConEmu64.exe')
    time.sleep(1.5)
    app.ConEmu.type_keys("cd {VK_SPACE} D:youtube-dl ~")
    time.sleep(1)
    app.ConEmu.type_keys("D: ~")
    time.sleep(1)
    app.ConEmu.type_keys("yt-dlp {VK_SPACE} -f {VK_SPACE} bestvideo[ext=mp4]{+}bestaudio {VK_SPACE} --embed-thumbnail {VK_SPACE} --embed-metadata {VK_SPACE} -o {VK_SPACE} {%}(channel)s/{%}(title)s.{%}(ext)s {VK_SPACE}")
    app.ConEmu.type_keys(thelink)
    time.sleep(1.5)
    app.ConEmu.type_keys("~")
    time.sleep(30)
    continuing_or_closing()

def get_link_second():
    YT_LINK = simpledialog.askstring(title="YouTube Link", prompt="Please enter the YouTube Link you want to download")
    if YT_LINK == 'None':
        quit
    else:
        LinkLength = len(YT_LINK)
        global thelink
        thelink = str(YT_LINK)
        

    if LinkLength == 0:    
        Goofed = tk.messagebox.showerror(title="No Link Included!", message="Please enter a full YouTube Link.")
        if Goofed == 'Cancel':
            quit
        else:
            get_link_second()
    
    if LinkLength > 40:
        link_format_two()
    else:
        GoofedAgain = tk.messagebox.showerror(title="Not Long Enough.", message="Please enter a full YouTube Link.")
        if GoofedAgain == 'Cancel':
            quit
        else:
            get_link_second()

def link_format_two():
    L_FORMAT = simpledialog.askstring(title="Type Of Link", prompt="What type of YouTube link is this? C for Channel, P for Playlist, V for Video")
    if L_FORMAT == 'C' or L_FORMAT =='c':
        channel_download_continue()
    elif L_FORMAT == 'P' or L_FORMAT =='p':
        playlist_download_continue()
    elif L_FORMAT == 'V' or L_FORMAT =='v':
        video_download_continue()
    else:
        Incorrect_Format = tk.messagebox.showerror(title="Not a right format!", message="Please enter one of the 3 letters above only.")
        link_format_two()

def channel_download_continue():
    app.ConEmu.type_keys("yt-dlp {VK_SPACE} -f {VK_SPACE} bestvideo[ext=mp4]{+}bestaudio {VK_SPACE} --embed-thumbnail {VK_SPACE} --embed-metadata {VK_SPACE} -o {VK_SPACE} {%}(channel)s/{%}(title)s.{%}(ext)s")
    app.ConEmu.type_keys(thelink)
    time.sleep(1.5)
    app.ConEmu.type_keys("~")
    time.sleep(30)
    continuing_or_closing()

def playlist_download_continue():
    app.ConEmu.type_keys("yt-dlp {VK_SPACE} -f {VK_SPACE} bestaudio {VK_SPACE} -o {VK_SPACE} {%}(playlist)s/{%}(playlist_index)s.{%}(title)s.{%}(ext)s {VK_SPACE}")
    app.ConEmu.type_keys(thelink)
    time.sleep(1.5)
    app.ConEmu.type_keys("~")
    time.sleep(30)
    continuing_or_closing()

def video_download_continue():
    app.ConEmu.type_keys("yt-dlp {VK_SPACE} -f {VK_SPACE} bestaudio[ext=m4a]{+}bestvideo[ext=mp4] {VK_SPACE}")
    app.ConEmu.type_keys(thelink)
    time.sleep(1.5)
    app.ConEmu.type_keys("~")
    time.sleep(5)
    continuing_or_closing()

def continuing_or_closing():
    answer = askquestion("Another Link?", "Do you have another link to download?")
    if answer == 'yes':
        get_link_second()
    elif answer == 'no':
        tk.messagebox.showinfo(title="All done then!", message="Good Bye!")
        quit
get_link_first()
continuing_or_closing()