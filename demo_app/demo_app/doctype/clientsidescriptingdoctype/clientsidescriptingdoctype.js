// Copyright (c) 2023, Idysman and contributors
// For license information, please see license.txt

frappe.ui.form.on("ClientSideScriptingDoctype", {
  refresh: function (frm) {
    // frappe.msgprint("Hello world!");
    // frappe.throw("Yeah, Erro");

    // Adding intro message

    // frm.set_intro("Now you can create a new client side scripting doctype");

    // Add this when the form is new

    if (frm.is_new()) {
      frm.set_intro("Now you can create a new client side scripting doctype");
    }
    // Adding a custom button
    // frm.add_custom_button("Click Me Button", () => {
    //   frappe.msgprint("YOu clicke me");
    // });

    // Adding a custom dropDown button
    frm.add_custom_button(
      "Click Me Button1",
      () => {
        frappe.msgprint("YOu clicke me");
      },
      "click me"
    );

    frm.add_custom_button(
      "Click Me Button 2",
      () => {
        frappe.msgprint("YOu clicke me again");
      },
      "click me"
    );
  },
  // onload: function (frm) {
  //   frappe.msgprint("Yeah this is loaded!");
  // },
  validate: function (frm) {
    // Triggered before saving the documents
    // frappe.throw("This is an error!");
    frm.set_value(
      "full_name",
      `${frm.doc.first_name} ${frm.doc.middle_name} ${frm.doc.last_name}`
    );

    let row = frm.add_child("family_members", {
      name1: "Johnson jose",
      relation: "Fathers",
      age: 56,
    });
  },
  // before_save: function (frm) {
  //   // Triggered before saving the documents
  //   frappe.throw("This is an error from 'before_save' event!");
  // },
  /**
   * EXTRACTING FORM VALUES
   *
   */
  after_save: function (frm) {
    // Triggered after saving the documents
    // frappe.throw("This is an error from 'after_save' event!");
    frappe.msgprint(
      `The full Name is: ${frm.doc.first_name} ${frm.doc.middle_name} ${frm.doc.last_name}`
    );

    for (const row of frm.doc.family_members) {
      frappe.msgprint(
        `${row.idx} The family member name is: ${row.name1}, and the relation is ${row.relation} `
      );
    }
  },
  check: function (frm) {
    // Field base event
    // check here is a field name
    // frappe.throw("This is an error from 'check' event!");
    frm.set_df_property("first_name", "reqd", 1);

    frm.set_df_property("middle_name", "read_only", 1);

    frm.toggle_reqd("age", true);
  },
  // family_members_on_form_rendered: function (frm) {
  //   // Field base event
  //   // here we are targetttig the child table
  //   frappe.throw("This is an error from 'check' event!");
  // },
  // before_submit: function (frm) {
  //   // Field base event
  //   // Triggered before submittign the form
  //   frappe.throw("This is an error from 'before_submit' event!");
  // },
  // on_submit: function (frm) {
  //   // Field base event
  //   // Triggered after submitting the form
  //   frappe.throw("This is an error from 'on_submit' event!");
  // },
  // before_cancel: function (frm) {
  //   // Field base event
  //   // Triggered before cancelling the form submission
  //   frappe.throw("This is an error from 'before_cancel' event!");
  // },
  // after_cancel: function (frm) {
  //   // Field base event
  //   // Triggered after cancelling the form submission
  //   frappe.throw("This is an error from 'after_cancel' event!");
  // },
});

/**********************************************************************
 * CHILD TABLE EVENTS
 ***********************************************************************/

// frappe.ui.form.on("Family Members", {
//   // cdt: Child doctype name
//   // cdn: row name
//   name1: function (frm) {
//     frappe.msgprint("Hello ID from 'child doctype' name1 field event ");
//   },
//   age: function (frm, cdt, cdn) {
//     frappe.msgprint("Hello ID from 'child doctype' age field event ");
//   },
// });
