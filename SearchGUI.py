from tkinter import *
from searchengine.searcher import *
import PIL
from PIL import ImageTk, Image

default_values = ('', '')
fields = 'Query', 'City'

def makeform(root, fields):
	"""
	    Create search window
	"""
	entries = []
	for i, field in enumerate(fields):

		row = Frame(root)
		lab = Label(row, width=15, text=field, anchor='center')
		ent = Entry(row)
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		ent.insert(10,default_values[i])
		entries.append((field, ent))

	row = Frame(root)
	lab = Label(row, width=15, text="Type", anchor='center')
	variable1 = StringVar(root)
	row.pack(side=TOP, fill=X, padx=5, pady=5)
	lab.pack(side=TOP)
	variable1.set("All")
	w = OptionMenu(root, variable1, "Cross/enduro", "Custom", "Fyrhjuling/ATV", "Offroad", "Scooter", "Sport", "Touring", "Övrigt", "All")
	w.pack(side = TOP)
	entries.append(("Motor cycle type", variable1))

	row = Frame(root)
	lab = Label(row, width=15, text="Maximum model year", anchor='center')
	variable3 = StringVar(root)
	row.pack(side=TOP, fill=X, padx=5, pady=5)
	lab.pack(side=TOP)
	variable3.set("2018")
	w = OptionMenu(root, variable3, "2018", "2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981")
	w.pack(side = TOP)
	entries.append(("Max model year", variable3))

	row = Frame(root)
	lab = Label(row, width=15, text="Minimum model year", anchor='center')
	variable2 = StringVar(root)
	row.pack(side=TOP, fill=X, padx=5, pady=5)
	lab.pack(side=TOP)
	variable2.set("1981")
	w = OptionMenu(root, variable2, "2018", "2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981")
	w.pack(side = TOP)
	entries.append(("Min model year", variable2))

	return entries

def search(entries):
	"""
		Use searcher.py to create and display results
	"""
	# Handles VehicleType = All
	if entries[2][1].get() == "All":
		res = searcher.price(query=entries[0][1].get(), location=entries[1][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())
		returned_docs = searcher.similar(query=entries[0][1].get(), location=entries[1][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())
		# Handles Location = All
		if entries[1][1].get() == "All" or entries[1][1].get() == "":
			res = searcher.price(query=entries[0][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())
			returned_docs = searcher.similar(query=entries[0][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())
	# Handles Location = All 
	elif entries[1][1].get() == "All" or entries[1][1].get() == "":
		res = searcher.price(query=entries[0][1].get(), vehicle_type=entries[2][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())
		returned_docs = searcher.similar(query=entries[0][1].get(), vehicle_type=entries[2][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())
	else:
		res = searcher.price(query=entries[0][1].get(), location=entries[1][1].get(), vehicle_type=entries[2][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())
		returned_docs = searcher.similar(query=entries[0][1].get(), location=entries[1][1].get(), vehicle_type=entries[2][1].get(),  max_model_year=entries[3][1].get(), min_model_year=entries[4][1].get())

	

	if res == None:
		res_frame_ = Tk()
		res_frame_.title('Sorry...')

		w = Label(res_frame_, text='No match for this query.\nPlease try again with other specifications!')
		w.pack(padx=20, pady=20)

		b = Button(res_frame_, text='Quit', command=res_frame_.destroy)
		b.pack(side=BOTTOM, padx=5, pady=5)
		res_frame_.mainloop()
	else:
		res_frame = Tk()
		res_frame.title('Results')

		for entry in entries:
			field = entry[0]
			text = entry[1].get()
			Label(res_frame, text='%s: "%s"' % (field, text)).pack(side=TOP)
		Label(res_frame, text='Number of hits: %s' % len(returned_docs), bg='grey', fg='white').pack(side=TOP,padx=20,pady=20)
		w = Label(res_frame, text="""
	    Average price: {}
	    Median price: {}
	    Max price: {}
	    Min price: {}
	    """.format(\
	        round(res["average_price"],2),
	        res["median_price"],
	        res["max_price"],
	        res["min_price"],
	        ))
		w.pack(side=LEFT, padx=20, pady=20)

		b = Button(res_frame, text='Quit', command=res_frame.destroy)
		b.pack(side=BOTTOM, padx=5, pady=5)
		res_frame.mainloop()

	

if __name__ == '__main__':

	root = Tk()

	img = ImageTk.PhotoImage(Image.open('ducati_draw.jpg').resize((500,250)))
	panel = Label(root, image = img)
	panel.pack(side = "top", fill = "both", expand = "yes")

	root.title('Searcher')
	searcher = Searcher()

	ents = makeform(root, fields)
	root.bind('<Return>', (lambda event, e=ents: search(e)))   

	# Quit button
	b1 = Button(root, text='Quit', command=quit)
	b1.pack(side=LEFT, padx=5, pady=5)
	# Search button
	b2 = Button(root, text='Search', command=(lambda e=ents: search(e)))
	b2.pack(side=RIGHT, padx=5, pady=5)

	root.mainloop()



