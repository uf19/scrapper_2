from tkinter import *
import requests
import bs4
import uuid
from urllib.parse import urlparse

def scrappin():
    try:
        url = requests.get(URL.get())
        res = bs4.BeautifulSoup(url.text, "html.parser")

        # Get domain name from URL
        parsed_url = urlparse(URL.get())
        domain = parsed_url.netloc

        # Generate unique file names
        content_file_name = "Web_Text_" + domain + "_" + str(uuid.uuid4()) + ".txt"
        code_file_name = "Web_Code_" + domain + "_" + str(uuid.uuid4()) + ".txt"

        # Content file
        with open(content_file_name, "w") as content_file:
            for i in res.select('p'):
                content_file.write(i.getText())

        # Code file
        with open(code_file_name, "w") as code_file:
            code_file.write(str(res))

    except IOError:
        print("An error occurred while writing to the file:")
    except Exception:
        print("An unexpected error occurred:")


main_window = Tk()
main_window.title("Tool")

var = StringVar()
var.set("Website Scraper Tool")
label_of_web = Label(main_window, textvariable=var, bd=8, bg="purple", font=("Helvetica", 35))
label_of_web.grid(row=0, column=0, sticky="nsew") #Use sticky="nsew" to expand label in all directions
URL = StringVar()
entry = Entry(main_window, bd=5, font=7, textvariable=URL)
entry.grid(row=1, column=0, ipadx=100)

button = Button(main_window, text="Scrap it!", bd=5, command=scrappin)
button.grid(row=2, column=0, padx=8, pady=4)

main_window.grid_columnconfigure(0, weight=1)
main_window.grid_rowconfigure(0, weight=1)
main_window.grid_rowconfigure(1, weight=1)
main_window.grid_rowconfigure(2, weight=1)

main_window.mainloop()
