# In your custom app: sspl_hrms/sspl_hrms/doctype/employee/employee.py

import frappe
from frappe.utils.pdf import get_pdf
from frappe.utils.file_manager import save_file

def on_update(doc, method):
    """Hooked to Employee on_update"""
    if doc.employment_type == "Exit":
        generate_experience_letter(doc)

def generate_experience_letter(doc):
    """Generate Experience Letter PDF for Exited Employee"""

    # Create HTML template (you can also store in Jinja template file)
    html = f"""
    <div style="font-family: Arial; padding: 20px;">
        <h2 style="text-align: center;">Experience Letter</h2>
        <p>To Whomsoever It May Concern,</p>
        <p>This is to certify that <b>{doc.employee_name}</b> was employed with
        <b>{frappe.defaults.get_global_default('company')}</b>
        from <b>{doc.date_of_joining}</b> to <b>{doc.relieving_date or frappe.utils.today()}</b>.</p>

        <p>During this period, {doc.first_name} worked as a <b>{doc.designation}</b>
        and contributed sincerely towards the responsibilities assigned.</p>

        <p>We wish {doc.first_name} success in all future endeavors.</p>

        <br><br>
        <p>HR Manager</p>
        <p><b>{frappe.defaults.get_global_default('company')}</b></p>
    </div>
    """

    # Convert HTML to PDF
    pdf_data = get_pdf(html)

    # Save PDF as File in Frappe (attached to Employee Doc)
    file_name = f"Experience_Letter_{doc.name}.pdf"
    save_file(file_name, pdf_data, "Employee", doc.name, is_private=0)

    frappe.msgprint(f"Experience Letter generated for {doc.employee_name}")
