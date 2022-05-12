# Copyright (c) 2022, efeone and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Transaction(Document):
	def before_save(self):
		passengers = len(self.passenger_details)
		print (passengers)
		self.no_passenger = passengers
		cost = frappe.db.get_single_value("Travel Category", "cost")
		self.payment = passengers * cost