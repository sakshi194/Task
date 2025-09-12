import frappe

def execute(filters=None):
    if not filters:
        filters = {}

    from_date = filters.get("from_date")
    to_date = filters.get("to_date")
    source = filters.get("source")

    conditions = "1=1"
    values = {}

    if from_date and to_date:
        conditions += " AND creation BETWEEN %(from_date)s AND %(to_date)s"
        values.update({"from_date": from_date, "to_date": to_date})

    if source:
        conditions += " AND source = %(source)s"
        values.update({"source": source})

    data = frappe.db.sql(f"""
        SELECT 
            COALESCE(source, 'Not Specified') AS source,
            COUNT(name) AS total_applicants
        FROM `tabJob Applicant`
        WHERE {conditions}
        GROUP BY source
        ORDER BY total_applicants DESC
    """, values=values, as_dict=True)

    columns = [
        {"label": "Source of Application", "fieldname": "source", "fieldtype": "Data", "width": 200},
        {"label": "Total Applicants", "fieldname": "total_applicants", "fieldtype": "Int", "width": 150},
    ]

    chart = None
    if data:
        chart = {
            "data": {
                "labels": [d["source"] for d in data],
                "datasets": [{"name": "Applicants", "values": [d["total_applicants"] for d in data]}],
            },
            "type": "bar"
        }

    return columns, data, None, chart
