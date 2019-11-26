from tkinter import *

app = Tk()

#part
part_text = StringVar()
part_label = Label(app, text='Part Name',font=('bold',14), pady=20)
part_label.grid(row=0, column=0,stick='w')

part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0,column=1)
#customer
customer_text = StringVar()
customer_label = Label(app, text='Customer ', font=('bold',14))
customer_label.grid(row=0, column=2,stick='w')

customer_entry = Entry(app, textvariable=customer_text)
customer_entry.grid(row=0,column=3)
#Retailer
retailer_text = StringVar()
retailer_label = Label(app, text='Retailer',font=('bold',14) )
retailer_label.grid(row=1, column=0,stick='w')

customer_entry = Entry(app, textvariable=retailer_text)
customer_entry.grid(row=1,column=1)
#price
price_text = StringVar()
price_label = Label(app, text='Price',font=('bold',14))
price_label.grid(row=1, column=2,stick='w')

price_entry = Entry(app, textvariable= price_text)
price_entry.grid(row=1,column=3)

#Parts List(ListBox)
parts_list = Listbox(app, height=8, width=50,border=0)
parts_list.grid(row=3, column=0, columnspan=3,rowspan=6, pady=20, padx=20)
#create scroll
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
#set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)

app.title('Part Manager')
app.geometry('700x350')


app.mainloop()
