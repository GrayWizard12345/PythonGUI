import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from Customer import Customer
from Product import Product
from Staff import Staff
from Store import Store


def on_mousewheel(canvas: Canvas, event):
    canvas.yview_scroll(-1 * (event.delta / 120), 'units')


def add_product():
    text_variable_for_quantity = StringVar()
    text_variable_for_quantity.trace('w',
                                     lambda name, index, mode, arg=text_variable_for_quantity: validate_quantity(arg))
    inputs = [Combobox(product_inputs_frame, values=product_names, state="readonly"),
              Label(product_inputs_frame, bg='white', fg='black', width=22, relief="groove"),
              Label(product_inputs_frame, bg='white', fg='black', width=22, relief="groove"),
              Entry(product_inputs_frame, relief="groove", exportselection=0, justify='center',
                    textvariable=text_variable_for_quantity),
              Label(product_inputs_frame, bg='white', fg='black', width=22, relief="groove")]
    index = len(rows)
    inputs[0].bind("<<ComboboxSelected>>", lambda event, arg=index: init_other_inputs(event, arg))
    inputs[0].grid(row=index, column=0, pady=5)
    inputs[1].grid(row=index, column=1, pady=5)
    inputs[2].grid(row=index, column=2, pady=5)
    inputs[3].grid(row=index, column=3, pady=5)
    inputs[4].grid(row=index, column=4, pady=5)
    rows.append(inputs)


def validate_quantity(arg: StringVar):
    try:
        string = arg.get()
        int(string)
    except:
        messagebox.showerror("Validation failed!", "Quantity can only be an integer value!")
        arg.set('')


def exit_button_pressed():
    answer = messagebox.askokcancel("Confirm exit!", "Do you really want to exit?")
    if not answer:
        return
    else:
        sys.exit(0)


def init_data():
    customers = [Customer("01223", "Peter Parker", "Qo'yliq", 2.2, "90-932-75-98", ["Silver", 'Gold']),
                 Customer("75884", "Sherlock Holmes", "Backer street", 31415, "90-987-65-43", ["Regular", 'VIP'])]
    store = Store('U1510375', "John's Mall", "Ziyolar-9", "90-123-45-67")
    staff_members = [Staff("0", "02213", "Uncle Ben", "Manager"),
                     Staff("1", "45646", "Aunt May", "Cashier"),
                     Staff('2', "12345", "John Doe", "Owner")]
    products = [Product(69, "Cucumber", "Fresh and long cucumber", 69.69, 666),
                Product(666, "Tomatoes", "Red and plump", 12.14, 314),
                Product(123456, "Candies", "Sweet sweet candies", 50, 100)]
    return products, customers, staff_members, store


def init_other_inputs(event, row_number: int):
    # 1 2 4
    combobox = rows[row_number][0]
    print(combobox)
    rows[row_number][1].config(text=str(products[combobox.current()].product_code))
    rows[row_number][2].config(text=str(products[combobox.current()].price))
    rows[row_number][4].config(text=str(products[combobox.current()].points))


def on_close():
    if messagebox.askokcancel("Confirm exit", "Do you want to exit?"):
        main_window.destroy()


if __name__ == '__main__':
    rows = []
    products, customers, staff_members, store = init_data()
    product_names = []
    for i in products:
        product_names.append(i.name)

    # Main window is 75% of the screen
    main_window = Tk()
    main_window.winfo_toplevel().title("U1510375___U1510332")
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    main_window.config(width=screen_width * 0.75, height=screen_height * 0.75)
    # Installing shutdown hook
    main_window.protocol("WM_DELETE_WINDOW", on_close)
    # Do not allow widgets to control window size
    main_window.pack_propagate(0)
    main_window.grid_propagate(0)
    # Make the window not resizable
    main_window.resizable(False, False)

    greeting_label = Label(main_window, text="Welcome to the Store Management System!",
                           fg="gray", font=('bold', 24))
    greeting_label.pack(side=TOP)

    top_frame = Frame(main_window, padx=50, pady=50)

    top_frame.pack(fill=X, side=TOP)

    # Top frame widgets
    staff_names = []
    for i in staff_members:
        staff_names.append(i.name)
    staff_name_label = Label(top_frame, text="Staff Name:", fg='gray')
    staff_name_label.grid(row=0, column=0, sticky=W)
    staff_name_input = Combobox(top_frame, width=19, state="readonly", values=staff_names)

    staff_name_input.grid(row=0, column=1, sticky=W)

    customer_id_label = Label(top_frame, text="Customer ID:", fg='gray', pady=10)
    customer_id_label.grid(row=1, column=0, sticky=W)
    customer_ids = []
    for i in customers:
        customer_ids.append(i.ssn)
    customer_id_input = Combobox(top_frame, width=19, values=customer_ids, state="readonly")

    customer_id_input.grid(row=1, column=1, sticky=W)

    # Add more frame widgets
    add_more_frame = Frame(main_window, padx=50)
    add_more_frame.pack(fill=X, side=TOP)

    # Labels for input data
    labels_frame = Frame(main_window, padx=50)
    labels_frame.pack(fill=X, side=TOP)
    labels_frame.columnconfigure(0, weight=1)
    labels_frame.columnconfigure(1, weight=1)
    labels_frame.columnconfigure(2, weight=1)
    labels_frame.columnconfigure(3, weight=1)
    labels_frame.columnconfigure(4, weight=1)

    product_name_label = Label(labels_frame, text="Product Name", fg='black')
    product_name_label.grid(row=0, column=0, sticky=W)

    product_code_label = Label(labels_frame, text="Product Code", fg='black')
    product_code_label.grid(row=0, column=1, sticky=W)

    price_label = Label(labels_frame, text="Price", fg='black')
    price_label.grid(row=0, column=2, sticky=W)

    quantity_label = Label(labels_frame, text="Quantity", fg='black')
    quantity_label.grid(row=0, column=3, sticky=W)

    points_label = Label(labels_frame, text="Points", fg='black')
    points_label.grid(row=0, column=4, sticky=W)

    # Actual inputs
    # Creating scrollable frame
    frame = Frame(main_window, padx=50, height=400)
    frame.pack(side=TOP, fill=BOTH, expand=True)
    scrollable_canvas = Canvas(frame, height=400)
    scrollable_canvas.pack(side=TOP, fill=BOTH, expand=True)
    scrollable_canvas.config(relief='ridge', bd=0, highlightthickness=0)
    product_inputs_frame = Frame(scrollable_canvas, height=300, bg='#f1f1f1',
                                 highlightbackground="#A0A0A0", highlightcolor="#A0A0A0", highlightthickness=4)
    product_inputs_frame.pack(side=TOP, fill=BOTH)

    add_more_products_label = Label(add_more_frame, text="Add more products", fg='gray')
    add_more_products_label.pack(side=LEFT)
    add_more_products_button = Button(add_more_frame, text='+', fg='white',
                                      bg='#50C878', command=add_product)
    add_more_products_button.pack(side=LEFT)

    vertical_scroll = Scrollbar(scrollable_canvas, orient='vertical', command=scrollable_canvas.yview)
    scrollable_canvas.configure(yscrollcommand=vertical_scroll.set, scrollregion=scrollable_canvas.bbox("all"))

    vertical_scroll.pack(side=RIGHT, fill=Y)

    scrollable_canvas.create_window((0, 0), window=product_inputs_frame, anchor='nw')
    scrollable_canvas.bind_all("<MouseWheel>",
                               lambda event: scrollable_canvas.yview_scroll(-1 * (event.delta / 120), 'units'))
    # Definitions
    product_name_input = Combobox(product_inputs_frame, values=product_names, state="readonly")
    product_name_input.bind("<<ComboboxSelected>>", lambda event, arg=0: init_other_inputs(event, arg))
    product_code_input = Label(product_inputs_frame, bg='white', fg='black', width=22, relief="groove")
    product_price_input = Label(product_inputs_frame, bg='white', fg='black', width=22, relief="groove")
    sv = StringVar()
    sv.trace('w', lambda name, index, mode, arg=sv: validate_quantity(arg))
    product_quantity_input = Entry(product_inputs_frame, relief="groove", exportselection=0, justify='center',
                                   textvariable=sv)
    product_points_input = Label(product_inputs_frame, bg='white', fg='black', width=22, relief="groove")
    # Organizing widgets
    product_name_input.grid(row=0, column=0)
    product_code_input.grid(row=0, column=1)
    product_price_input.grid(row=0, column=2)
    product_quantity_input.grid(row=0, column=3)
    product_points_input.grid(row=0, column=4)
    print(product_name_input.current())
    rows.append(
        [product_name_input, product_code_input, product_price_input, product_quantity_input, product_points_input])
    # Control buttons here
    control_buttons_frame = Frame(main_window, padx=50, pady=30)
    control_buttons_frame.pack(side=LEFT)
    print_button = Button(control_buttons_frame, text="Print", fg="black", bg='#50C878', padx=30,
                          command=lambda: print(rows))
    print_button.pack(side=LEFT)
    close_button = Button(control_buttons_frame, text="Close", fg="black", bg='#50C878', padx=30,
                          command=exit_button_pressed)
    close_button.pack(side=LEFT)

    main_window.mainloop()
    # flat, groove, raised, ridge, solid, or sunken
