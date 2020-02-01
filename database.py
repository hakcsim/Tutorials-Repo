import sqlite3

class Employee:

    # class variable - shared between instances
    raise_amount = 1.04

    num_of_emps = 0

    def __init__(self, first, last, pay):

        # instance variables - unique to each instance

        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps += 1

    @property
    def email(self):
        return f'{self.first}.{self.last}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'


# in memory databas
conn = sqlite3.connect(':memory:') 

# in file
# conn = sqlite3.connect('./test_files/employee.db')

cur = conn.cursor()

def insert_emp(emp):
    # will always commit
    with conn:    
        cur.execute('INSERT INTO employees VALUES (:first, :last, :pay)', {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    cur.execute('SELECT * FROM employees WHERE last=:last', {'last': lastname})
    return cur.fetchall()

def update_pay(emp, pay):
    with conn:
        cur.execute('''UPDATE employees SET pay=:pay 
                    WHERE first=:first AND last=:last 
                    ''', {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        cur.execute('DELETE FROM employees WHERE first=:first AND last=:last', 
                    {'first':emp.first, 'last':emp.last})


# SQL Storage Classes and Datatypes
# NULL,
# INTEGER,
# REAL,
# TEXT,
# BLOB

try:
    cur.execute('''CREATE TABLE employees (
                first text,
                last text,
                pay integer
            )''')

    conn.commit()
except sqlite3.OperationalError:
    print('employees table already exists')    

# cur.execute('SELECT * FROM employees WHERE last="Schafer"')
cur.execute('SELECT * FROM employees')

# return tuple
# data = cur.fetchone() 

# return list
data = cur.fetchall()

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)
emp_3 = Employee('Hak', 'Sim', 9000000)

if len(data) == 0:
    insert_emp(emp_3)
    cur.execute('INSERT INTO employees VALUES (?, ?, ?)', (emp_1.first, emp_1.last, emp_1.pay))
    cur.execute('INSERT INTO employees VALUES (:first, :last, :pay)', {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay})
    cur.execute('INSERT INTO employees VALUES ("Mary", "Schafer", 50000)')
    cur.execute('INSERT INTO employees VALUES ("Corey", "Schafer", 70000)')
    conn.commit()
else:
    print(data)

cur.execute('SELECT * FROM employees WHERE last=?', ('Schafer',))

print(cur.fetchall())

cur.execute('SELECT * FROM employees WHERE last=:last', {'last': 'Doe'})

print(cur.fetchall())

update_pay(emp_3, 1000000000)
print(get_emps_by_name(emp_3.last))

remove_emp(emp_1)
print(get_emps_by_name(emp_1.last))

conn.close()