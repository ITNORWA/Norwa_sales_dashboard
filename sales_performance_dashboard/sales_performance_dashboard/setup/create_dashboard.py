# -*- coding: utf-8 -*-
# Copyright (c) 2024, Your Company
# For license information, please see license.txt

"""
Script to create Personal Sales Dashboard
Run: bench execute sales_performance_dashboard.sales_performance_dashboard.setup.create_dashboard.create_personal_dashboard
"""

import json
import os

import frappe
from sales_performance_dashboard.api.access_settings import apply_workspace_roles_from_settings
from frappe import _


def _ensure_doc_from_json(doctype: str, json_path: str):
    if not os.path.exists(json_path):
        raise FileNotFoundError(json_path)
    with open(json_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    name = data.get("name") or data.get("chart_name") or data.get("source_name")
    if not name:
        raise ValueError(f"Missing name in {json_path}")
    if frappe.db.exists(doctype, name):
        frappe.delete_doc(doctype, name, ignore_permissions=True, force=True)
    doc = frappe.get_doc(data)
    doc.flags.ignore_links = True
    doc.flags.ignore_validate = True
    doc.insert(ignore_permissions=True)
    return name


def ensure_personal_dashboard_charts():
    """Ensure Personal Sales Dashboard chart sources and charts exist in DB."""
    base = frappe.get_app_path(
        "sales_performance_dashboard",
        "sales_performance_dashboard",
    )
    items = [
        # (doctype, relative_path)
        ("Dashboard Chart Source", "dashboard_chart_source/personal_sales_order_trend/personal_sales_order_trend.json"),
        ("Dashboard Chart", "dashboard_chart/personal_sales_order_trend/personal_sales_order_trend.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/personal_top_customers/personal_top_customers.json"),
        ("Dashboard Chart", "dashboard_chart/personal_top_customers/personal_top_customers.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/personal_sales_order_analysis/personal_sales_order_analysis.json"),
        ("Dashboard Chart", "dashboard_chart/personal_sales_order_analysis/personal_sales_order_analysis.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/personal_item_sales_monthly/personal_item_sales_monthly.json"),
        ("Dashboard Chart", "dashboard_chart/personal_item_sales_monthly/personal_item_sales_monthly.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/personal_item_sales_(monthly)/personal_item_sales_(monthly).json"),
        ("Dashboard Chart", "dashboard_chart/personal_item_sales_(monthly)/personal_item_sales_(monthly).json"),
        ("Dashboard Chart Source", "dashboard_chart_source/personal_sales_funnel/personal_sales_funnel.json"),
        ("Dashboard Chart", "dashboard_chart/personal_sales_funnel/personal_sales_funnel.json"),
        ("Custom HTML Block", "custom_html_block/personal_sales_funnel/personal_sales_funnel.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/personal_leads_by_source/personal_leads_by_source.json"),
        ("Dashboard Chart", "dashboard_chart/personal_leads_by_source/personal_leads_by_source.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/personal_forecasted_revenue/personal_forecasted_revenue.json"),
        ("Dashboard Chart", "dashboard_chart/personal_forecasted_revenue/personal_forecasted_revenue.json"),
        ("Custom HTML Block", "custom_html_block/personal_item_sales_monthly_table/personal_item_sales_monthly_table.json"),
        ("Custom HTML Block", "custom_html_block/personal_top_customers_table/personal_top_customers_table.json"),
        ("Custom HTML Block", "custom_html_block/personal_sales_order_analysis_block/personal_sales_order_analysis_block.json"),
        ("Custom HTML Block", "custom_html_block/personal_project_pipeline/personal_project_pipeline.json"),
        ("Custom HTML Block", "custom_html_block/personal_project_status_finance/personal_project_status_finance.json"),
        ("Custom HTML Block", "custom_html_block/personal_project_delivery_health/personal_project_delivery_health.json"),
        ("Custom HTML Block", "custom_html_block/personal_project_value_billing/personal_project_value_billing.json"),
        ("Custom HTML Block", "custom_html_block/my_sales_targets_shortcut/my_sales_targets_shortcut.json"),
        ("Custom HTML Block", "custom_html_block/revenue_wave_card/revenue_wave_card.json"),
        ("Custom HTML Block", "custom_html_block/personal_dashboard_filters/personal_dashboard_filters.json"),
    ]
    for doctype, rel_path in items:
        path = os.path.join(base, rel_path)
        if not os.path.exists(path):
            continue
        _ensure_doc_from_json(doctype, path)
    frappe.db.commit()
    print("✅ Personal Sales Dashboard charts ensured.")


def ensure_department_dashboard_assets():
    """Ensure Department Sales Dashboard chart source and chart exist in DB."""
    base = frappe.get_app_path(
        "sales_performance_dashboard",
        "sales_performance_dashboard",
    )
    items = [
        ("Dashboard Chart Source", "dashboard_chart_source/department_sales_order_trend/department_sales_order_trend.json"),
        ("Dashboard Chart", "dashboard_chart/department_sales_order_trend/department_sales_order_trend.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/department_forecasted_revenue/department_forecasted_revenue.json"),
        ("Dashboard Chart", "dashboard_chart/department_forecasted_revenue/department_forecasted_revenue.json"),
        ("Dashboard Chart Source", "dashboard_chart_source/department_sales_funnel/department_sales_funnel.json"),
        ("Custom HTML Block", "custom_html_block/department_dashboard_filters/department_dashboard_filters.json"),
        ("Custom HTML Block", "custom_html_block/department_kpi_cards/department_kpi_cards.json"),
        ("Custom HTML Block", "custom_html_block/department_kpi_revenue_customers/department_kpi_revenue_customers.json"),
        ("Custom HTML Block", "custom_html_block/department_kpi_deals_pipeline/department_kpi_deals_pipeline.json"),
        ("Custom HTML Block", "custom_html_block/department_kpi_customers/department_kpi_customers.json"),
        ("Custom HTML Block", "custom_html_block/department_target_slippage/department_target_slippage.json"),
        ("Custom HTML Block", "custom_html_block/department_weighted_pipeline_coverage/department_weighted_pipeline_coverage.json"),
        ("Custom HTML Block", "custom_html_block/department_sales_order_trend_block/department_sales_order_trend_block.json"),
        ("Custom HTML Block", "custom_html_block/department_forecasted_revenue_block/department_forecasted_revenue_block.json"),
        ("Custom HTML Block", "custom_html_block/department_gross_margin_trend/department_gross_margin_trend.json"),
        ("Custom HTML Block", "custom_html_block/department_discount_leakage/department_discount_leakage.json"),
        ("Custom HTML Block", "custom_html_block/department_payment_delay_cost/department_payment_delay_cost.json"),
        ("Custom HTML Block", "custom_html_block/department_top_customers_table/department_top_customers_table.json"),
        ("Custom HTML Block", "custom_html_block/department_project_pipeline/department_project_pipeline.json"),
        ("Custom HTML Block", "custom_html_block/department_project_delivery_health/department_project_delivery_health.json"),
        ("Custom HTML Block", "custom_html_block/department_sales_funnel/department_sales_funnel.json"),
    ]
    for doctype, rel_path in items:
        path = os.path.join(base, rel_path)
        if not os.path.exists(path):
            continue
        _ensure_doc_from_json(doctype, path)
    frappe.db.commit()
    print("✅ Department Sales Dashboard assets ensured.")


def ensure_company_dashboard_assets():
    """Ensure Company Sales Dashboard custom assets exist in DB."""
    base = frappe.get_app_path(
        "sales_performance_dashboard",
        "sales_performance_dashboard",
    )
    items = [
        ("Custom HTML Block", "custom_html_block/company_dashboard_filters/company_dashboard_filters.json"),
        ("Custom HTML Block", "custom_html_block/company_pipeline_overview/company_pipeline_overview.json"),
        ("Custom HTML Block", "custom_html_block/company_revenue_by_source/company_revenue_by_source.json"),
        ("Custom HTML Block", "custom_html_block/company_revenue_waterfall/company_revenue_waterfall.json"),
        ("Custom HTML Block", "custom_html_block/company_gross_margin_trend/company_gross_margin_trend.json"),
        ("Custom HTML Block", "custom_html_block/company_payment_delay_cost/company_payment_delay_cost.json"),
        ("Custom HTML Block", "custom_html_block/company_target_slippage/company_target_slippage.json"),
        ("Custom HTML Block", "custom_html_block/company_weighted_pipeline_coverage/company_weighted_pipeline_coverage.json"),
        ("Custom HTML Block", "custom_html_block/company_deal_conversion_rate/company_deal_conversion_rate.json"),
        ("Custom HTML Block", "custom_html_block/company_project_status_finance/company_project_status_finance.json"),
    ]
    for doctype, rel_path in items:
        path = os.path.join(base, rel_path)
        if not os.path.exists(path):
            continue
        _ensure_doc_from_json(doctype, path)
    frappe.db.commit()
    print("✅ Company Sales Dashboard assets ensured.")
def create_personal_dashboard():
    """Create Personal Sales Dashboard with all number cards"""
    
    dashboard_name = "Personal Sales Dashboard"
    
    # First, let's verify cards exist
    print("Checking for existing Number Cards...")
    all_cards = frappe.get_all('Number Card', 
        filters={'name': ['like', 'Personal%']},
        fields=['name'],
        pluck='name'
    )
    
    print(f"Found {len(all_cards)} cards:")
    for card in all_cards:
        print(f"  - {card}")
    
    if not all_cards:
        print("\n❌ No Number Cards found! Please create cards first.")
        return None

    # Check if dashboard exists
    if frappe.db.exists('Dashboard', dashboard_name):
        print(f"\nUpdating existing dashboard: {dashboard_name}")
        dashboard = frappe.get_doc('Dashboard', dashboard_name)
        # Clear existing cards
        dashboard.cards = []
        dashboard.charts = []
    else:
        print(f"\nCreating new dashboard: {dashboard_name}")
        dashboard = frappe.new_doc('Dashboard')
        dashboard.dashboard_name = dashboard_name
    
    # Set dashboard properties
    dashboard.module = 'Sales Performance Dashboard'
    dashboard.is_default = 0
    dashboard.is_standard = 0
    
    # Define card layout using EXACT card names as they exist in database
    cards_layout = [
        # Row 1: Revenue Metrics
        ['Personal - Total Revenue', 'Personal - Total Collected', 'Personal - Total Outstanding'],
        
        # Row 2: Target Metrics
        ['Personal - Monthly Target', 'Personal - Target Achievement', 'Personal - Total Invoices'],
        
        # Row 3: Lead & Opportunity Metrics
        ['Personal - Total Leads', 'Personal - Total Opportunities', 'Personal - Opportunities Value'],
        
        # Row 4: Deal Status
        ['Personal - Won Deals', 'Personal - Lost Deals'],
        
        # Row 5: Customer Metrics - Week
        ['Personal - New Customers Week', 'Personal - Customers Served Week'],
        
        # Row 6: Customer Metrics - Month
        ['Personal - New Customers Month', 'Personal - Customers Served Month'],
        
        # Row 7: Appointments
        ['Personal - Total Appointments', 'Personal - Open Appointments', 'Personal - Closed Appointments'],
    ]
    
    # Add cards to dashboard
    cards_added = 0
    for row_idx, row_cards in enumerate(cards_layout):
        for col_idx, card_name in enumerate(row_cards):
            if card_name in all_cards:
                dashboard.append('cards', {
                    'card': card_name,
                })
                cards_added += 1
                print(f"  ✓ Added: {card_name}")
            else:
                print(f"  ✗ Skipped (not found): {card_name}")
    
    # ERPNext dashboards require at least one chart, but we can leave it empty
    # The charts field is a table, so we don't need to add anything if not required in your version
    
    # Save dashboard
    try:
        dashboard.save(ignore_permissions=True)
        frappe.db.commit()
        
        print("\n" + "="*50)
        print(f"✅ Dashboard '{dashboard_name}' created/updated successfully!")
        print(f"📊 Total cards added: {cards_added}")
        print("="*50)
        
        print("\nTo view the dashboard:")
        print(f"Go to: Home → Dashboards → {dashboard_name}")
        
        return dashboard
        
    except Exception as e:
        print(f"\n❌ Error creating dashboard: {str(e)}")
        print("\nTrying alternative approach without strict validation...")
        
        # Alternative: Create dashboard via SQL if validation fails
        frappe.db.sql("""
            INSERT INTO `tabDashboard` (name, dashboard_name, module, is_default, is_standard)
            VALUES (%s, %s, %s, 0, 0)
            ON DUPLICATE KEY UPDATE 
                dashboard_name = VALUES(dashboard_name),
                module = VALUES(module)
        """, (dashboard_name, dashboard_name, 'Sales Performance Dashboard'))
        
        frappe.db.commit()
        print("✅ Dashboard created via direct SQL")
        
        return None


def sync_personal_workspace():
    """Sync the Personal Sales Dashboard workspace from its JSON definition."""
    ensure_personal_dashboard_charts()
    workspace_path = frappe.get_app_path(
        "sales_performance_dashboard",
        "sales_performance_dashboard",
        "workspace",
        "personal_sales_dashboard",
        "personal_sales_dashboard.json",
    )

    if not os.path.exists(workspace_path):
        raise FileNotFoundError("Personal Sales Dashboard workspace JSON not found.")

    with open(workspace_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    # Keep project status & finance block out of Personal workspace.
    if data.get("content"):
        content_rows = json.loads(data["content"])
        content_rows = [
            row for row in content_rows
            if not (
                row.get("id") == "psd-project-status-finance"
                and row.get("type") == "custom_block"
            )
            and row.get("data", {}).get("custom_block_name") != "Personal Project Status & Finance"
        ]
        data["content"] = json.dumps(content_rows)

    data["custom_blocks"] = [
        row
        for row in (data.get("custom_blocks") or [])
        if row.get("custom_block_name") != "Personal Project Status & Finance"
    ]

    name = data.get("name") or "Personal Sales Dashboard"
    if frappe.db.exists("Workspace", name):
        frappe.delete_doc("Workspace", name, ignore_permissions=True, force=True)

    doc = frappe.get_doc(data)
    doc.flags.ignore_links = True
    doc.flags.ignore_validate = True
    doc.insert(ignore_permissions=True)
    apply_workspace_roles_from_settings()
    frappe.db.commit()
    print(f"✅ Workspace '{name}' synced from JSON.")


def sync_department_workspace():
    """Sync the Department Sales Dashboard workspace from JSON."""
    ensure_department_dashboard_assets()
    workspace_path = frappe.get_app_path(
        "sales_performance_dashboard",
        "sales_performance_dashboard",
        "workspace",
        "department_sales_dashboard",
        "department_sales_dashboard.json",
    )

    if not os.path.exists(workspace_path):
        raise FileNotFoundError("Department Sales Dashboard workspace JSON not found.")

    with open(workspace_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    name = data.get("name") or "Department Sales Dashboard"
    if frappe.db.exists("Workspace", name):
        frappe.delete_doc("Workspace", name, ignore_permissions=True, force=True)

    doc = frappe.get_doc(data)
    doc.flags.ignore_links = True
    doc.flags.ignore_validate = True
    doc.insert(ignore_permissions=True)
    apply_workspace_roles_from_settings()
    frappe.db.commit()
    print(f"✅ Workspace '{name}' synced from JSON.")


def sync_company_workspace():
    """Sync the Company Sales Dashboard workspace from JSON."""
    ensure_company_dashboard_assets()
    workspace_path = frappe.get_app_path(
        "sales_performance_dashboard",
        "sales_performance_dashboard",
        "workspace",
        "company_sales_dashboard",
        "company_sales_dashboard.json",
    )

    if not os.path.exists(workspace_path):
        raise FileNotFoundError("Company Sales Dashboard workspace JSON not found.")

    with open(workspace_path, "r", encoding="utf-8") as handle:
        data = json.load(handle)

    name = data.get("name") or "Company Sales Dashboard"
    if frappe.db.exists("Workspace", name):
        frappe.delete_doc("Workspace", name, ignore_permissions=True, force=True)

    doc = frappe.get_doc(data)
    doc.flags.ignore_links = True
    doc.flags.ignore_validate = True
    doc.insert(ignore_permissions=True)
    apply_workspace_roles_from_settings()
    frappe.db.commit()
    print(f"✅ Workspace '{name}' synced from JSON.")


def debug_personal_workspace():
    """Print workspace DB state for troubleshooting."""
    name = "Personal Sales Dashboard"
    row = frappe.db.get_value(
        "Workspace",
        name,
        ["name", "public", "content", "module", "label", "title"],
        as_dict=True,
    )
    print("Workspace row:", row)
    if row and row.get("content"):
        print("Content length:", len(row["content"]))
    else:
        print("No content saved in DB.")
    return row


def debug_personal_workspace_custom_blocks():
    """Print custom blocks configured on the Personal Sales Dashboard workspace."""
    ws = frappe.get_doc("Workspace", "Personal Sales Dashboard")
    print("Custom blocks:")
    for cb in ws.custom_blocks:
        print(f" - {cb.custom_block_name} (label: {cb.label})")


def debug_personal_charts():
    """Print chart and chart source existence for Personal Sales Dashboard."""
    charts = [
        "Personal Sales Order Trend",
        "Personal Top Customers",
        "Personal Sales Order Analysis",
        "Personal Item Sales (Monthly)",
        "Personal Sales Funnel",
    ]
    for name in charts:
        chart_exists = frappe.db.exists("Dashboard Chart", name)
        source_exists = frappe.db.exists("Dashboard Chart Source", name)
        print(f"{name} -> chart={bool(chart_exists)}, source={bool(source_exists)}")


def debug_personal_funnel_block():
    """Print a snippet of the Personal Sales Funnel custom block script."""
    for name in ("Personal Sales Funnel v2", "Personal Sales Funnel"):
        exists = frappe.db.exists("Custom HTML Block", name)
        print(f"{name} exists:", bool(exists))
        if not exists:
            continue
        block = frappe.get_doc("Custom HTML Block", name)
        script = block.script or ""
        print(f"{name} has positionTooltip:", "positionTooltip" in script)
        print(f"{name} has requestAnimationFrame:", "requestAnimationFrame" in script)
        print(f"{name} script snippet:", script.replace("\\n", " ")[:240])


def sync_all_dashboards():
    """Idempotent full sync for cards, assets and workspaces."""
    from sales_performance_dashboard.sales_performance_dashboard.setup.create_number_cards import create_all_cards

    create_all_cards()
    sync_personal_workspace()
    sync_department_workspace()
    sync_company_workspace()
    print("✅ Sales dashboard full sync complete.")
