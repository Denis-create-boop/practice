
from daries import dariyes_database
from users.users_data import termcolor

darie = dariyes_database.Dariye


def create(name):
    dariye_name = input(f"{termcolor.colored("Введи название дневника ==>> ", "light_yellow")}")
    table = darie(name)
    table.create_table(darie_name=dariye_name)
    
    
def add_new_write(name):
    pass
   

def add_image(name):
    pass


def show_dariye(name):
    pass  
    
    
def del_dariye(name):
    pass
