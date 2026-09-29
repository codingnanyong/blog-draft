# Authority and editing constraints

The user decides when anything moves forward; agents draft and revise.

- Keep `status: draft` until the user explicitly approves publication.
- Do not publish, upload, push a branch (it triggers issue and PR creation), merge, move tags, or message external services without the user's explicit go-ahead. Approval covers the action it was given for, not later ones.
- Preserve frontmatter fields, document language, heading structure, and intentional links unless the task requires changing them.
- Keep unrelated user changes intact, including uncommitted edits you did not make; leave them out of your commits.
- Do not invent personal experiences or results the user did not provide. The user's confirmed work stack (Airflow, Kafka, dbt, a PostgreSQL + TimescaleDB Medallion architecture, a Docker → Kubernetes migration) is real material; ask which specific tool they used before naming one.
- When a process slip is found (a missed tracker update, missing PR metadata, leftover branches), fix it and then codify it: automate it in `.github/workflows/` or `.agents/hooks/` where possible, and write it down in `.agents/rules/` otherwise.
- At handoff, report the changed document paths, generated image paths, and any remaining review items.
