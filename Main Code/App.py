from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import PyPDF2
import os
from draganddrop import *
import pygame


def adjustWindow(window):
    w = 900  # width for the window size
    h = 600  # height for the window size
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed
    window.resizable(False, False)    # disabling the resize option for the window
    window.configure(background='#013243')    # making the background white of the window

class PDF_Doc():
	def __init__(self,filename):
		try:

			self.filename=filename
			self.display=filename.split('/')[-1]
			self.pdf=load_pdf(filename)
			self.pages=self.pdf.getNumPages()
			self.start=1
			self.end=self.pages
		except AttributeError:
			pass
	def add_to_writer(self,writer):

	    for i in range(self.start-1,self.end):
	        writer.addPage(self.pdf.getPage(i))

def load_pdf(filename):
    try:
        f = open(filename, 'rb')
        return PyPDF2.PdfFileReader(f)
    except FileNotFoundError:
        pass

def load():
	pygame.mixer.music.load("Sound.mp3") #Loading File Into Mixer
	pygame.mixer.music.play() #Playing It In The Whole Device
	try:

		f = filedialog.askopenfilename(initialdir="/",title="Select A File",filetypes=(("pdf files", "*.pdf"),("all files", "*.*")))
		print(f)
		pdf= PDF_Doc(f)
		pdf_list.append(pdf)
		listbox.insert(END,pdf.display)
		print(pdf_list)
	except Exception as e:
		index=int(listbox.curselection()[0])
		# print(index)
		pdf_list.pop(index)
		# print(pdf_list)
		listbox.delete(ANCHOR)



def remove():
	global filename,pages,start,end,s1,s2,s3,s4
	pygame.mixer.music.load("Sound.mp3") #Loading File Into Mixer
	pygame.mixer.music.play() #Playing It In The Whole Device
	s1.delete(0, 'end')
	s2.delete(0, 'end')
	s3.delete(0, 'end')
	s4.delete(0, 'end')
	try:
		# print(pdf_list)
		index=int(listbox.curselection()[0])
		# print(index)
		pdf_list.pop(index)
		# print(pdf_list)
		listbox.delete(ANCHOR)
		# print(pdf_list)

	except IndexError:
		pass

def save_pdf():
	try:

		writer= PyPDF2.PdfFileWriter()
		output_file = filedialog.asksaveasfile(mode='wb',defaultextension=".pdf",filetypes=(("pdf files", "*.pdf"),("all files", "*.*"))) 
		for doc in pdf_list:
			doc.add_to_writer(writer)
		writer.write(output_file)
		output_file.close()
		messagebox.showinfo("Succesfull","The PDFs were Merged")
	except AttributeError:
		pass


    

def display(*args):
	try:

		index=int(listbox.curselection()[0])
		value=listbox.get(index)
		filename.set(value)
		pages.set(pdf_list[index].pages)
		start.set(pdf_list[index].start)
		end.set(pdf_list[index].end)
	except:
		index=int(listbox.curselection()[0])
		# print(index)
		pdf_list.pop(index)
		# print(pdf_list)
		listbox.delete(ANCHOR)

def set_start(*args):
	index=int(listbox.curselection()[0])
	pdf_list[index].start=int(start.get())
	
def set_end(*args):
	index=int(listbox.curselection()[0])
	pdf_list[index].end=int(end.get())

pdf_list=[]

root= Tk()
root.title("PDF Merger with Python")
adjustWindow(root)


pygame.init()
frame=Frame(root, background='#013243')
frame.place(x=0,y=100,width=900, height=500)

global filename,pages,start,end,s1,s2,s3,s4

filename=StringVar()
pages=StringVar()
start=StringVar()
end=StringVar()

# , command=loadpdf
# ,command=removepdf
Label(root,text="PDF Merger Using Python", font=("Open Sans", 20, 'bold'), fg='#00b5cc', bd=3,bg='#013243').place(x=300,y=50)

Button(frame, text="Add PDF", font=("Open Sans", 10, 'bold'), fg='#00b5cc', bg='#013243', bd=3,command=load,width=10).place(x=40,y=50)
# Label(frame, text="").grid(row=2,column=0)
Button(frame, text="Remove PDF", font=("Open Sans", 10, 'bold'), fg='#00b5cc', bg='#013243', bd=3,command=remove, width=10).place(x=40,y=150)

# ,display

listbox=DragDropListbox(root,pdf_list)
listbox.bind('<<ListboxSelect>>',display)
listbox.place(x=240,y=150,width=200)

Label(frame,text="File: ", font=("Open Sans", 10, 'bold'), fg='#00b5cc', bd=3,bg='#013243').place(x=600,y=50)

s1=Entry(frame,textvariable=filename,width=30)
s1.place(x=650,y=50)

Label(frame,text="Pages: ", font=("Open Sans", 10, 'bold'), fg='#00b5cc', bd=3,bg='#013243').place(x=600,y=100)


s2=Entry(frame,textvariable=pages,width=20)
s2.place(x=650,y=100)


Label(frame,text="Start: ", font=("Open Sans", 10, 'bold'), fg='#00b5cc', bd=3,bg='#013243').place(x=600,y=150)
s3=Entry(frame,textvariable=start,width=20)
s3.place(x=650,y=150)
Label(frame,text="End: ", font=("Open Sans", 10, 'bold'), fg='#00b5cc', bd=3,bg='#013243').place(x=600,y=200)
s4=Entry(frame,textvariable=end,width=20)
s4.place(x=650,y=200)

# command=lambda:save_pdf(),
start.trace('w',set_start)
end.trace('w',set_end)
Button(frame, text="Combine/Save PDF",command=save_pdf,width=20, font=("Open Sans", 10, 'bold'), fg='#00b5cc', bg='#013243', bd=3).place(x=380,y=430)

Label(frame,text="Copyrights:Reuben and Rhea", font=("Open Sans", 10, 'bold'), fg='#00b5cc', bd=3,bg='#013243').place(x=700,y=480)
root.mainloop()