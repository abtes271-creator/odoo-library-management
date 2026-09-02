# Library Management — Odoo Module

A custom Odoo 17 module built to learn Odoo development end-to-end: manages books, members, and borrowing transactions with a full workflow, automatic fine calculation, and a kanban dashboard.

## Features
- Book catalog with live copy-count tracking (kanban dashboard view)
- Member registry
- Borrowing workflow (Draft → Borrowed → Returned) via status-bar buttons
- Automatic overdue detection and fine calculation (computed fields)
- Search, filters (Overdue), and Group By (Status) on borrowings
- Demo data included (3 books, 2 members) so it's usable immediately after install

## Tech Stack
- Odoo 17.0
- PostgreSQL
- Docker / Docker Compose

## Running it locally

1. Clone this repo
2. Run:
3. Visit http://localhost:8069, create a database
4. Go to Apps, remove the "Apps" filter, search "Library Management", click Install
5. Find it under the "Library" menu — Books, Members, Borrowings

## What I learned
- Odoo's ORM and model system (`models.Model`, field types, relations)
- Many2one relations between models
- Access control via `ir.model.access.csv`
- View architecture: form, tree, kanban, search views, actions, menus
- Business logic via Python methods callable from buttons (`type="object"`)
- Computed fields with `@api.depends` and `store=True`
- Demo/seed data via XML records