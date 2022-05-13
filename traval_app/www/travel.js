$(document).ready(function() {
     $('form').on('submit', function(event) {
		frappe.call({
			method: "traval_app.www.api.get_from_data", // write a function in api file
			args:{
				'pname': $('#passName').val(),
				'page': $('#passAge').val(),
        'pnumber': $('#passPhone').val(),
			},
			callback: function(r) {
				frappe.msgprint("Your Message")
			}
		});
      event.preventDefault();
      });
});
