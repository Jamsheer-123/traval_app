# Copyright (c) 2022, efeone and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Transaction(Document):
	def before_save():
		no_passenger = frappe.db.get_single_value("Passenger","no_passenger")
		cost = frappe.db.get_single_value("Traval Category","cost")
		self.payment = no_passenger*cost
	
