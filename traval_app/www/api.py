from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_from_data(pname,page,pnumber,gnore_permissions=True):
	data = frappe.new_doc("Transaction")
	passenger_table = data.append('passenger_details')
	passenger_table.passenger_name = pname
	passenger_table.age = page
	passenger_table.mobile = pnumber	
	data.save()
    
	frappe.db.commit()
