import pytube
import tkinter as tk
import yt_downloader
import insta_downloader
import fb_downloader

def renderScreen():
    plat_options = ["Youtube", "Instagram", "Facebook", "Twitter", "Reddit"]
    quality_options = ["Highest", "Lowest", "Audio"]

    root = tk.Tk()
    root.geometry("500x600")
    root.title("Video Downloader")
    root.columnconfigure(0, weight = 1)

    platform_label = tk.Label(root, text = "Choose Platform", font = ("jost", 15), pady = 15)
    platform_label.grid()
    variable = tk.StringVar(root)
    variable.set(plat_options[0])
    plat_select = tk.OptionMenu(root, variable, *plat_options)
    plat_select.grid()

    url_label = tk.Label(root, text = "Paste URL", font = ("jost", 15), pady = 15)
    url_label.grid()
    url = tk.StringVar()
    url_entry = tk.Entry(root, width = 40, borderwidth = 5, textvariable = url)
    url_entry.grid(ipadx = 15)
    url_error = tk.Label(root, text = "URL Error", fg = "red", font = ("jost", 10), pady = 5)
    url_error.grid()

    loc_label = tk.Label(root, text = "Save Location", font = ("jost", 15), pady = 10)
    loc_label.grid()
    loc = tk.StringVar()
    loc_entry = tk.Entry(root, width = 30, borderwidth = 5, textvariable = loc)
    loc_entry.grid(ipadx = 15)
    loc_error = tk.Label(root, text = "Directory Error", fg = "red", font = ("jost", 10), pady = 5)
    loc_error.grid()
    loc_button = tk.Button(root, text = "Select Directory", bg = "green", fg = "white")
    loc_button.grid()

    down_label = tk.Label(root, text = "Select Download Quality", font = ("jost", 8), pady = 15)
    down_label.grid()
    variable = tk.StringVar(root)
    variable.set(quality_options[0])
    down_select = tk.OptionMenu(root, variable, *quality_options)
    down_select.grid()

    temp = tk.Label(text = "", pady = 15)
    temp.grid()
    download = tk.Button(root, text = "Download", font = ("jost", 20), bg = "red", fg = "white")
    download.grid()

    root.mainloop()

renderScreen()