app_name = "sales_performance_dashboard"
app_title = "Sales Performance Dashboard"
app_publisher = "Custom"
app_description = "Sales targets and performance tracking"
app_email = "custom@example.com"
app_license = "mit"
fixtures = ["Module Def"]

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "sales_performance_dashboard",
# 		"logo": "/assets/sales_performance_dashboard/logo.png",
# 		"title": "Sales Performance Dashboard",
# 		"route": "/sales_performance_dashboard",
# 		"has_permission": "sales_performance_dashboard.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/sales_performance_dashboard/css/sales_performance_dashboard.css"
# app_include_js = "/assets/sales_performance_dashboard/js/sales_performance_dashboard.js"

# include js, css files in header of web template
# web_include_css = "/assets/sales_performance_dashboard/css/sales_performance_dashboard.css"
# web_include_js = "/assets/sales_performance_dashboard/js/sales_performance_dashboard.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "sales_performance_dashboard/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "sales_performance_dashboard/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "sales_performance_dashboard.utils.jinja_methods",
# 	"filters": "sales_performance_dashboard.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "sales_performance_dashboard.install.before_install"
# after_install = "sales_performance_dashboard.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "sales_performance_dashboard.uninstall.before_uninstall"
# after_uninstall = "sales_performance_dashboard.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "sales_performance_dashboard.utils.before_app_install"
# after_app_install = "sales_performance_dashboard.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "sales_performance_dashboard.utils.before_app_uninstall"
# after_app_uninstall = "sales_performance_dashboard.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "sales_performance_dashboard.notifications.get_notification_config"

# Permissions
# -----------
# Sales Targets is intentionally open to all eligible desk users.

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"sales_performance_dashboard.tasks.all"
# 	],
# 	"daily": [
# 		"sales_performance_dashboard.tasks.daily"
# 	],
# 	"hourly": [
# 		"sales_performance_dashboard.tasks.hourly"
# 	],
# 	"weekly": [
# 		"sales_performance_dashboard.tasks.weekly"
# 	],
# 	"monthly": [
# 		"sales_performance_dashboard.tasks.monthly"
# 	],
# }
scheduler_events = {
    "cron": {
        "*/1 * * * *": [
            "sales_performance_dashboard.tasks.update_sales_targets",
        ]
    }
}

# Testing
# -------

# before_tests = "sales_performance_dashboard.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "sales_performance_dashboard.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "sales_performance_dashboard.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["sales_performance_dashboard.utils.before_request"]
# after_request = ["sales_performance_dashboard.utils.after_request"]

# Job Events
# ----------
# before_job = ["sales_performance_dashboard.utils.before_job"]
# after_job = ["sales_performance_dashboard.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"sales_performance_dashboard.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
# Installation
# ------------

after_install = "sales_performance_dashboard.install.after_install"
after_migrate = ["sales_performance_dashboard.install.after_migrate"]
