// Copyright (c) 2023, Idysman and contributors
// For license information, please see license.txt

frappe.ui.form.on("ServerSide Scripting Doctype", {
  // refresh: function(frm) {

  // }

  //   check: function (frm) {
  //     // Analogous to make an ajax request to the server
  //     frm.call({
  //       doc: frm.doc,
  //       method: "frm_call",
  //       args: {
  //         msg: "Hello",
  //       },
  //       freeze: true, //you want the screen to freeze
  //       freeze_message: __("Calling frm_call method on the server"),
  //       callback: function (r) {
  //         frappe.msgprint(r.message);
  //       },
  //     });
  //   },

  check: function (frm) {
    // Analogous to make an ajax request to the server
    // Using frappe.call() to send the request to a method in another file
    frappe.call({
      doc: frm.doc,
      method:
        "demo_app.doctype.clientsidescriptingdoctype.clientsidescriptingdoctype.frappe_call",
      args: {
        msg: "Hello",
      },
      freeze: true, //you want the screen to freeze
      freeze_message: __("Calling frm_call method on the server"),
      callback: function (r) {
        frappe.msgprint(r.message);
      },
    });
  },
});
