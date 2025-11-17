# student clubs
from pyscript import display


dance = {'Jen', 'Bea', 'Jim', 'Jane', 'Fia'}
glee = {'Lorraine', 'Jen', 'Bea', 'Sam', 'Zae'}

display(f"Students in at least one club: {dance | glee}", target='output')
display(f"Students who belong to both clubs: {dance & glee}", target='output')
display(f"Students only in the first club: {dance}", target='output')
display(f"Students only in the second club: {glee}", target='output')
display(f"Students who are in exactly one club: {glee ^ dance}", target='output')
