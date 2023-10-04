frappe.pages["programming-page"].on_page_load = function (wrapper) {
  var page = frappe.ui.make_app_page({
    parent: wrapper,
    title: "Demo page",
    single_column: true,
  });

  page.set_title("My page");

  page.set_indicator("Done", "green");

  let $btn = page.set_primary_action("New", () =>
    frappe.msgprint("Clicked new button")
  );

  let $btnOne = page.set_secondary_action("Refresh", () =>
    frappe.msgprint("Clicked refresh")
  );

  page.add_menu_item("Send Email", () => frappe.msgprint("Clicked send mail"));

  page.add_action_item("Delete", () => frappe.msgprint("Clicked delete"));

  let field = page.add_field({
    label: "Status",
    fieldtype: "Select",
    fieldname: "status",
    options: ["Open", "Closed", "Cancelled"],
    change() {
      frappe.msgprint(field.get_value());
    },
  });

  //   $(frappe.render_template("index", {})).appendTo(page.body);
  $(frappe.render_template("programming_page", { data: "Hi Frappe" })).appendTo(
    page.body
  );
};
