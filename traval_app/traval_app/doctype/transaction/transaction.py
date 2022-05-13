# Copyright (c) 2022, efeone and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Transaction(Document):
	def before_save(self):
		passengers = len(self.passenger_details)
		print (passengers)
		self.no_passenger = passengers



	def before_submit(self):
		travel_category = frappe.get_doc("Travel Category", self.cost)
		passengers = self.no_passenger
		self.payment = travel_category.cost * passengers
