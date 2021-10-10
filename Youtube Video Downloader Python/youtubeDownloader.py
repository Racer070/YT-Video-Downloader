from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube 

Folder_Name = ""


def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")


def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again!!",fg="red")


    
    select.download(Folder_Name)
    ytdError.config(text="Download Completed!!")



root = Tk()
root.title("Youtube Video Downloader")
root.geometry("350x400") 
root.iconbitmap(r'./appIcon/youtube.ico')
root.columnconfigure(0,weight=1)


ytdLabel = Label(root,text="Please enter url here !",font=("jost",15))
ytdLabel.grid()


ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()


ytdError = Label(root,text="Error Msg",fg="green",font=("jost",10))
ytdError.grid()

saveLabel = Label(root,text="Save the Video File",font=("jost",15,"bold"))
saveLabel.grid()


saveEntry = Button(root,width=10,bg="blue",fg="white",text="Choose Path",command=openLocation)
saveEntry.grid()

locationError = Label(root,text="Error Msg of Path",fg="green",font=("jost",10))
locationError.grid()


ytdQuality = Label(root,text="Select video's quality",font=("jost",15))
ytdQuality.grid()

choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices)
ytdchoices.grid()

downloadbtn = Button(root,text="Donwload",width=10,bg="blue",fg="white",command=DownloadVideo)
downloadbtn.grid()


developerlabel = Label(root,text="Rahul G",font=("jost",15))
developerlabel.grid()
root.mainloop()