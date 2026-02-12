ticket_list = {
    "233": "PIPPO", 
    "4343": "Pluto" 
}

id_ticket = "233"

for k , v in ticket_list.items():
    if k == id_ticket:
        ticket_da_chiudere = v
        
print (ticket_da_chiudere)