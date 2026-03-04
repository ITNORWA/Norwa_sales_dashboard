import frappe
import json

DEFAULTS = {
    "psd_sales_user": 1,
    "psd_sales_manager": 1,
    "psd_system_manager": 1,
    "psd_administrator": 1,
    "dsd_sales_user": 1,
    "dsd_sales_manager": 1,
    "dsd_system_manager": 1,
    "dsd_administrator": 1,
    "csd_sales_user": 0,
    "csd_sales_manager": 1,
    "csd_system_manager": 1,
    "csd_administrator": 1,
    "sales_user_targets_mode": "Scoped",
    "sales_manager_targets_mode": "All",
    "annual_financing_rate": 18,
}

ROLE_FIELDS = {
    "Personal Sales Dashboard": {
        "Sales User": "psd_sales_user",
        "Sales Manager": "psd_sales_manager",
        "System Manager": "psd_system_manager",
        "Administrator": "psd_administrator",
    },
    "Department Sales Dashboard": {
        "Sales User": "dsd_sales_user",
        "Sales Manager": "dsd_sales_manager",
        "System Manager": "dsd_system_manager",
        "Administrator": "dsd_administrator",
    },
    "Company Sales Dashboard": {
        "Sales User": "csd_sales_user",
        "Sales Manager": "csd_sales_manager",
        "System Manager": "csd_system_manager",
        "Administrator": "csd_administrator",
    },
}

ALLOWED_DASHBOARD_ROLES = ("Sales User", "Sales Manager", "System Manager", "Administrator")


def _sanitize_workspace_links(ws):
    """Drop stale custom block references so workspace save doesn't fail on missing links."""
    valid_blocks = set(frappe.get_all("Custom HTML Block", pluck="name"))

    ws.set(
        "custom_blocks",
        [row for row in (ws.custom_blocks or []) if row.custom_block_name in valid_blocks],
    )

    if not ws.content:
        return

    try:
        rows = json.loads(ws.content)
    except Exception:
        return

    changed = False
    cleaned = []
    for row in rows:
        if row.get("type") != "custom_block":
            cleaned.append(row)
            continue

        block_name = (row.get("data") or {}).get("custom_block_name")
        if block_name and block_name in valid_blocks:
            cleaned.append(row)
            continue

        changed = True

    if changed:
        ws.content = json.dumps(cleaned)


def get_access_settings():
    settings = dict(DEFAULTS)
    if not frappe.db.exists("DocType", "Sales Dashboard Access Settings"):
        return settings

    doc = frappe.get_single("Sales Dashboard Access Settings")
    for key in DEFAULTS:
        value = doc.get(key)
        if value is not None and value != "":
            settings[key] = value
    return settings


def get_workspace_roles_map(settings: dict | None = None) -> dict[str, list[str]]:
    settings = settings or get_access_settings()

    role_map: dict[str, list[str]] = {}
    for workspace, role_field_map in ROLE_FIELDS.items():
        roles = [role for role, field in role_field_map.items() if int(settings.get(field) or 0) == 1]
        role_map[workspace] = roles
    return role_map


def apply_workspace_roles_from_settings(settings_doc=None):
    # Restricted visibility mode: only approved sales roles can access dashboards.
    for workspace_name in ROLE_FIELDS:
        if not frappe.db.exists("Workspace", workspace_name):
            continue

        ws = frappe.get_doc("Workspace", workspace_name)
        _sanitize_workspace_links(ws)
        # Workspaces can temporarily contain stale links during upgrades.
        # We still need role updates to apply without being blocked by link validation.
        ws.flags.ignore_links = True
        ws.flags.ignore_validate = True
        ws.public = 1
        ws.for_user = ""
        ws.is_hidden = 0
        ws.set("roles", [])
        for role in ALLOWED_DASHBOARD_ROLES:
            ws.append("roles", {"role": role})
        ws.save(ignore_permissions=True)

    frappe.clear_cache()


def get_targets_mode_for_user(user: str) -> str:
    if frappe.has_role(user=user, role="Administrator") or frappe.has_role(user=user, role="System Manager"):
        return "All"

    settings = get_access_settings()
    modes = []

    if frappe.has_role(user=user, role="Sales Manager"):
        modes.append(settings.get("sales_manager_targets_mode", "All"))
    if frappe.has_role(user=user, role="Sales User"):
        modes.append(settings.get("sales_user_targets_mode", "Scoped"))

    if "All" in modes:
        return "All"
    if "Scoped" in modes:
        return "Scoped"
    return "None"


def get_annual_financing_rate() -> float:
    settings = get_access_settings()
    value = settings.get("annual_financing_rate", 18)
    try:
        rate = float(value)
    except (TypeError, ValueError):
        rate = 18.0
    if rate < 0:
        rate = 0.0
    return rate


@frappe.whitelist()
def reset_access_defaults():
    """Reset access settings to safe defaults and apply to workspaces."""
    if not frappe.has_permission("Sales Dashboard Access Settings", ptype="write"):
        frappe.throw("Not permitted", frappe.PermissionError)

    doc = frappe.get_single("Sales Dashboard Access Settings")
    for key, value in DEFAULTS.items():
        doc.set(key, value)
    doc.save(ignore_permissions=True)
    apply_workspace_roles_from_settings(doc)
    frappe.db.commit()
    return {"ok": True}
