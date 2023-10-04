# Copyright (c) 2023, Idysman and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ServerSideScriptingDoctype(Document):
    # def validate(self):
    #     frappe.msgprint(
    #         f"Hello my full name is: {self.first_name} {self.middle_name} {self.last_name}")
    # frappe.msgprint("Hello world")

    # def validate(self):
    #     # Getting data from child table
    #     for row in self.get("family_members"):
    #         frappe.msgprint(
    #             f"{row.idx}. The family memeber name is {row.name1} and relation is {row.relation}")

    def validate(self):
        print("Hi")
        # self.get_document()
        # self.new_document()
        # self.set_document()
        # self.get_list()
        # self.get_value()
        # self.set_value()
        # self.doc_exists()
        # self.count_docs()
        # self.sql()
        # frappe.delete_doc('ClientSideScriptingDoctype', 'PR0003')
        # self.get_and_delete_doc()

    def get_document(self):
        #  frappe.get_doc(doctype, document_name)
        doc = frappe.get_doc("ClientSideScriptingDoctype",
                             self.client_side_doc)
        frappe.msgprint(
            f"Clientside doc First Name is {doc.first_name} and age is {doc.age}")

        # Get the child table of the client side doctype

        for row in doc.get("family_members"):
            frappe.msgprint(
                f"{row.idx}. Child Doc family member name is {row.name1} and relation is {row.relation}")

    def new_document(self):
        # Creating a new child doc
        doc = frappe.new_doc("ClientSideScriptingDoctype")
        doc.first_name = 'Jake'
        doc.last_name = "Jerry"
        doc.age = 13

        doc.append('family_members', {
            'name1': "Jane",
            'relation': "sister",
            'age': 14
        })

        doc.insert()  # or you can also doc.save()

        # some escape hatches used in doc.insert

        # doc.insert(
        #     ignore_permissions=True,  # ignore write permissions during insert
        #     ignore_links=True,  # ignore Lin validation in the document
        #     ignore_if_duplicate=True,  # ignore duplicateEntryError and insert record
        #     ignore_mandatory=True  # insert even if mandatory fields are not set
        # )

        # some escape hatches used in doc.save
        # doc.save(
        #     ignore_permissions=True,  # ignore write permissions during insert
        #     ignore_version=True,  # will not create a version record

        # )

    def get_and_delete_doc(self):
        doc = frappe.get_doc('ClientSideScriptingDoctype', "PR0003")
        doc.delete()

    def set_document(self):
        doc = frappe.get_doc('ClientSideScriptingDoctype', "PR0003")
        doc.db_set('age', 45)

    def get_list(self):
        # frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)
        docs = frappe.db.get_list('ClientSideScriptingDoctype',
                                  filters={
                                      'check': 0
                                  },
                                  fields=['first_name', 'age']
                                  )
        print(docs)

        for doc in docs:
            frappe.msgprint(
                f"The Child first Name is {doc.first_name} and age is {doc.age}")

    def get_value(self):
        # frappe.db.get_value(doctype, name, fieldnames) or frappe.db.get_value(doctype, filters, fieldnames)
        first_name, age = frappe.db.get_value(
            'ClientSideScriptingDoctype', 'PR0003', ['first_name', 'age'])
        frappe.msgprint(
            f"The Child first Name is {first_name} and age is {age}")

    def set_value(self):
        frappe.db.set_value('ClientSideScriptingDoctype',
                            'PR0003', 'first_name', 'jane')

    def doc_exists(self):
        if frappe.db.exists('ClientSideScriptingDoctype', 'PR0003'):
            frappe.msgprint('The document exists in Database')
        else:
            frappe.msgprint('The document does not exists in Database')

    def count_docs(self):
        doc_count = frappe.db.count('ClientSideScriptingDoctype', {"check": 0})
        frappe.msgprint(f'The unchecked document count is {doc_count}')

    def sql(self):
        docs = frappe.db.sql("""
                             SELECT 
                             	first_name,
                             	age
                             
                             FROM 
                             `tabClientSideScriptingDoctype`
                             
                             WHERE 
                             	`check` = 0
                             """, as_dict=1)
        for doc in docs:
            frappe.msgprint(
                f"The Child first Name is {doc.first_name} and age is {doc.age}")

    @frappe.whitelist()
    def frm_call(self, msg):
        import time
        time.sleep(5)
        # frappe.msgprint(msg)
        self.moble_no = "07039331481"
        return "Hi, this message from frm_call method"

    # def before_save(self):
    #     # Triggered before saving the data to database
    #     frappe.throw("Hello frappe from 'before_save' event")

    # def before_insert(self):
    #     # Triggered before inserting the data to database
    #     frappe.throw("Hello frappe from 'before_insert' event")

    # def after_insert(self):
    #     # Triggered after inserting the event to database
    #     frappe.throw("Hello frappe from 'after_insert' event")

    # def on_update(self):
    #     # Triggered after updating the data to database
    #     frappe.msgprint("Hello frappe from 'on_update' event")

    # def before_submit(self):
    #     # Triggered before saving the event to database
    #     frappe.msgprint("Hello frappe from 'before_submit' event")

    # def on_submit(self):
    #     # Triggered after submission
    #     frappe.msgprint("Hello frappe from 'on_submit' event")

    # def on_cancel(self):
    #     # Triggered before saving the event to database
    #     frappe.msgprint("Hello frappe from 'on_cancel' event")

    # def on_trash(self):
    #     # Triggered before saving the event to database
    #     frappe.msgprint("Hello frappe from 'on_trash' event")

    # def after_delete(self):
    #     # Triggered before saving the event to database
    #     frappe.msgprint("Hello frappe from 'after_delete' event")
