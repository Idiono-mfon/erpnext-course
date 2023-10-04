# Copyright (c) 2023, Idysman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ClientSideScriptingDoctype(Document):

    @frappe.whitelist()
    def frappe_call(self, msg):
        # import time
        # time.sleep(5)
        # frappe.msgprint(msg)
        # self.moble_no = "07039331481"
        return "Hi, this message from 'frappe_call' method"
