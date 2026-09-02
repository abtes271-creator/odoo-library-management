\# Library Management — Odoo Module



A custom Odoo 17 module built to learn Odoo development: manages books, members, and borrowing transactions with a full workflow.



\## Features

\- Book catalog with copy tracking

\- Member registry

\- Borrowing workflow (Draft → Borrowed → Returned) with automatic copy count updates

\- Built entirely as a custom Odoo module (models, views, security, business logic)



\## Tech Stack

\- Odoo 17.0

\- PostgreSQL

\- Docker / Docker Compose



\## Running it locally



1\. Clone this repo

2\. Run:

3\. Visit http://localhost:8069, create a database

4\. Go to Apps, remove the "Apps" filter, search "Library Management", click Install

5\. Find it under the "Library" menu



\## What I learned

\- Odoo's ORM and model system (`models.Model`, field types, relations)

\- Many2one relations between models

\- Access control via `ir.model.access.csv`

\- View architecture (form, tree, actions, menus)

\- Business logic with Python methods callable from buttons (`type="object"`)

