import frappe


def after_install():
    from sales_performance_dashboard.sales_performance_dashboard.setup.create_dashboard import sync_all_dashboards

    sync_all_dashboards()
    frappe.clear_cache()


def after_migrate():
    from sales_performance_dashboard.sales_performance_dashboard.setup.create_dashboard import sync_all_dashboards

    sync_all_dashboards()
    frappe.clear_cache()
