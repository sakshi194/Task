import frappe

def get_salary_structure_for_employee(employee):
    regime = frappe.db.get_value("Employee", employee, "custom_tax_regime_preference")
    if regime == "Old Regime":
        return "Salary Structure - Old Regime"
    elif regime == "New Regime":
        return "Salary Structure - New Regime"
    return None


def assign_salary_structure(doc, method):
    if not doc.salary_structure:
        salary_structure = get_salary_structure_for_employee(doc.employee)
        if salary_structure:
            doc.salary_structure = salary_structure
