import frappe
from frappe.model.document import Document
from frappe.model.docstatus import Docstatus

class Travalseat(Document):
'''	def beforesubmit():

		total_seat = frappe.db.get_single_value("Travel Catogory", "total_seat")
		no_passenger=frappe.db.get_single_value("Transaction", "no_passenger")
		self.reserved_seat=
