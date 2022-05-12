from __future__ import unicode_literals
import frappe

@frappe.whitelist()
def get_from_data(fname,lname,gnore_permissions=True):
	pass
	# data = frappe.new_doc("Lead")
	# data.lead_name = fname + lname
	# data.save()
