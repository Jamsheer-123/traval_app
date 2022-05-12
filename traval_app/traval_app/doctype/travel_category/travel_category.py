import frappe
from frappe.model.document import Document

class TravelCategory(Document):

	def before_save(self):
		rslocation = frappe.db.get_single_value("Travel Settings", "rslocation")
		travel_route = frappe.get_doc("Travel Route", self.route)
		stp = len(travel_route.stop)				
		self.cost = rslocation * stp