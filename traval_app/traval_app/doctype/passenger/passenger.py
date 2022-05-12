# Copyright (c) 2022, efeone and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


def before_save(self):
	self.arrival()

class Passenger(Document):
	pass
def arrival(self):
	arrival_date = frappe.get_single_value("Travel Category", "arrival_date")