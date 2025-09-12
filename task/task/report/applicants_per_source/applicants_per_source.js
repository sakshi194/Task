// Copyright (c) 2025, sakshi
// For license information, please see license.txt

frappe.query_reports["Applicants per Source"] = {
    "filters": [
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
            reqd: 1
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            default: frappe.datetime.get_today(),
            reqd: 1
        },
        { fieldname: "source", label: __("Source"), fieldtype: "Link", options: "Job Applicant Source", reqd: 0 } ] };