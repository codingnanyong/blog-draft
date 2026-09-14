# Roadmap / Series Plan

## The "Codigdex" series concept

Like a Pokédex, each series (`#number`) is one technology **chapter**. Each week within a chapter observes a distinct specimen such as `NO.001` or `NO.002`, then formally registers that specimen in the Codigdex at the very end of the post. The final week registers its own specimen and also marks the whole chapter complete.

> **Week count isn't fixed at 5.** Each chapter's week table below is the specific breakdown decided for that chapter, and it's re-decided per chapter based on its learning curve. See [Criteria for picking the next chapter](#criteria-for-picking-the-next-chapter) for details.

The user (codingnanyong) works as a Data Engineer, and chapter selection for this blog prioritizes doubling as on-the-job study. `#01` Git → `#02` Linux → `#03` Docker → `#04` CI/CD → `#05` Kubernetes form the common foundation any developer needs (collaboration, operating system, containers, automation, orchestration); from `#06` on, the track moves into chapters that map directly onto Data Engineering work (workflow orchestration, distributed processing/streaming, analytics engineering/warehousing).

## #01 — Git (5-week breakdown)

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Git basics — first encounter | 2026-09-03 | COD-41 | Published |
| Week 2 | Git branching and merging | 2026-09-07 | COD-42 | Published |
| Week 3 | Undoing changes & merge conflicts | 2026-09-14 | COD-53 | Published |
| Week 4 | Remote repositories & rebase | 2026-09-21 | COD-54 | Drafted |
| Week 5 | Collaboration workflow (wrap-up) | 2026-09-28 | COD-55 | Drafted |

Each week follows the same process defined in [Git branch strategy](GIT_WORKFLOW.md) and [Content & publishing workflow](WORKFLOW.md). NO.001 through NO.005 are registered individually at the end of their respective posts; once week 5 is registered, the Git chapter is complete and the series moves on to the next chapter, `#02` Linux.

## #02 — Linux (draft — proposed 5 weeks, not confirmed)

The user has picked Linux as the chapter after Git. The user's separate game project, [codigdex](https://github.com/codingnanyong/codigdex), sets `CH.01 Git → CH.02 Terminal · Linux` as the **junior common path** for every role, and leaves Docker out of that common path because containers are much easier to learn once you understand the terminal, processes, and networking. So that the blog shares the same common foundation, Linux takes the `#02` slot and Docker moves back one slot to `#03`. The weekly breakdown below mirrors the game's CH.02 Lv.1-Lv.5 stages and is a proposal, not yet confirmed.

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Linux basics — first encounter (shell & terminal, `pwd`/`ls`/`cd`) | 2026-10-05 | TBD | Proposed |
| Week 2 | Paths & files (absolute/relative paths, `mkdir`/`cp`/`mv`/`rm`/`find`) | 2026-10-12 | TBD | Proposed |
| Week 3 | Permissions & users (`rwx`, `chmod`/`chown`, `sudo`) | 2026-10-19 | TBD | Proposed |
| Week 4 | Pipes & processes (`\|`/`>`/`>>`, `ps`/`top`/`kill`, background jobs) | 2026-10-26 | TBD | Proposed |
| Week 5 | The kernel & the OS (kernel, system calls, boot, `systemctl`, wrap-up registration) | 2026-11-02 | TBD | Proposed |

Once this 5-week breakdown is confirmed, Linear issues (parent + standard sub-issues) and Notion sprints will be created. If the actual pacing turns out different once underway, the week count may be adjusted.

## #03 — Docker (draft — proposed 5 weeks, not confirmed)

Originally proposed as `#02`, now moved back one slot to follow Linux (`#02`). Images and containers ultimately run on top of Linux processes and filesystems, so meeting Docker after observing the shell, permissions, and processes is the more natural order. Below is a proposed curriculum following the same "basics → applied → collaboration/real-world" three-stage structure as Git — not yet confirmed.

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Docker basics — first encounter (images, containers, Dockerfile) | 2026-11-09 | TBD | Proposed |
| Week 2 | Building images & layers (writing a Dockerfile, layer caching, multi-stage builds) | 2026-11-16 | TBD | Proposed |
| Week 3 | Volumes & networking (data persistence, container-to-container communication) | 2026-11-23 | TBD | Proposed |
| Week 4 | Docker Compose (multi-container orchestration) | 2026-11-30 | TBD | Proposed |
| Week 5 | Real-world collaboration workflow (registries, CI/CD integration, wrap-up registration) | 2026-12-07 | TBD | Proposed |

## #04 — CI/CD (GitHub Actions) (order confirmed, curriculum and week count TBD)

Confirmed as the chapter after Docker (#03). Automating the build/deploy of the images made in Docker follows naturally right after it, and it also picks up directly where the Git series' last week (PR → Review → Merge) left off. This repo's own automation (Linear/GitHub integration, PR policy) can serve as real material. Weekly curriculum not yet discussed, and likewise won't be forced into 5 weeks — it'll be sized to the chapter.

## #05 candidate (under consideration)

- Kubernetes — the user is considering this as the chapter after CI/CD (#04). Not yet confirmed; the weekly breakdown will be discussed once #04 wraps up. Given how much ground it covers, running longer than 5 weeks is a natural option to consider.

## #06+ candidates — Data Engineer track (under consideration)

Building on the common infrastructure foundation through `#05` Kubernetes, the chapters under consideration for the following slots map directly onto Data Engineering work. The user actually uses Airflow, Kafka, and dbt on the job, has implemented a Medallion Architecture on PostgreSQL + TimescaleDB in-house, and migrated that infrastructure from Docker to Kubernetes — so this track draws on real work experience rather than hypothetical study. Order, confirmation, and week counts are all still undiscussed — the notes below are directional.

- **Workflow orchestration (Airflow)** — batch/ETL scheduling, DAG-based pipeline management. A natural next step that carries the "automation/orchestration" thread from CI/CD and Kubernetes into the data-pipeline context.
- **Streaming & messaging (Kafka)** — event-driven architecture, real-time data ingestion.
- **Analytics engineering (dbt)** — the transform (T) layer, data modeling, query optimization.
- **Data warehouse architecture — Medallion Architecture (PostgreSQL + TimescaleDB)** — a capstone case study tying the earlier chapters (orchestration, streaming, transformation) together. Covers Raw → Bronze → Silver → Gold layering and time-series-specific data characteristics.

## #10+ broader candidate pool — real-world experience (under consideration)

The topics below are also under consideration, and the user has actually applied them on the job (not hypothetical study material). Order, whether each becomes its own chapter, and week counts are all undecided — the specific tools covered will be confirmed again when each chapter is actually drafted.

- **Storage/warehouse layer** — data lake vs. warehouse vs. lakehouse concepts, table formats (Iceberg/Delta Lake/Hudi), file formats (Parquet/ORC/Avro), partitioning & clustering strategy
- **Ingestion & integration** — Change Data Capture (CDC), ELT tools (Fivetran/Airbyte/Singer-style), API-based ingestion pipeline design
- **Orchestration alternatives/comparison** — Dagster, Prefect, etc. vs. Airflow, data lineage & cataloging
- **Quality, testing & governance** — data quality testing (Great Expectations, dbt test), data contracts, PII masking & access control
- **Distributed/large-scale processing** — Spark (batch), Flink (stream processing)
- **SQL/performance deep-dive** — query optimization, execution plan analysis, indexing strategy, advanced SQL patterns (window functions, etc.)
- **Monitoring & operations** — pipeline monitoring/alerting (Airflow SLAs, Prometheus+Grafana), incident response & backfill strategy
- **Infrastructure/cloud** — Terraform (IaC), cloud data services
- **Data modeling** — dimensional modeling (star/snowflake schema), SCD (Slowly Changing Dimension)

## Estimated yearly coverage (rough estimate, not confirmed)

Posts publish weekly on Monday. The timeline below assumes each chapter runs 5 weeks, purely for estimation — once `#04`/`#05`'s actual week counts are confirmed, everything after shifts accordingly.

- **Within 2026**: `#01` Git (published/drafted, through ~09-28) → `#02` Linux (through ~11-02) → `#03` Docker (through ~12-07) → `#04` CI/CD weeks 1-3 (~12-14 to ~12-28, with the rest rolling into the next year under a 5-week assumption)
- **From 2027 on**: `#04` CI/CD wraps up (~01-11) → `#05` Kubernetes (through ~02-15, assuming 5 weeks) → then the Data Engineer track proceeds in sequence (`#06` Airflow → `#07` Kafka → `#08` dbt → `#09` Medallion Architecture on PostgreSQL+TimescaleDB). Track chapters may run longer than 5 weeks (especially the closing capstone), so exact completion dates will be recalculated once each chapter is confirmed.
- **Total material on hand (estimate)**: assuming 5 weeks each, `#01`-`#09` (confirmed/proposed) add up to roughly 45 weeks (2026-09 through 2027-07). Adding the `#10`+ broader candidate pool (9 categories), each turned into its own 3-5 week chapter, adds roughly another 27-45 weeks — putting **enough weekly material on hand to run through roughly early-to-mid 2028** (about 1.4-1.7 years from today). How many chapters the `#10`+ categories end up splitting (or merging) into is still undecided, so the actual total will shift.

## Criteria for picking the next chapter

- A technology or tool used repeatedly in practice, worth revisiting from the basics
- A topic that naturally splits into a "basics → applied → collaboration/real-world" three-stage structure, like Git
- **Week count isn't fixed at 5** — scale it to the chapter's actual learning curve (more than 5 weeks is fine for a bigger topic, and fewer than 5 is fine for a simpler one). #01 Git and #02 Linux / #03 Docker (draft) happening to be 5 weeks is just the outcome for those specific chapters, not a rule future chapters must follow.
- **Prioritize topics that genuinely map onto the user's job (Data Engineer)** — so that writing the blog doubles as job-relevant study. Once the common foundation (Git/Linux/Docker/CI-CD/Kubernetes) is covered, prioritize tools the user actually uses on the job (Airflow, Kafka, dbt, a Medallion Architecture on PostgreSQL+TimescaleDB, etc.).

## Where it's tracked

- Linear: a parent issue per week (e.g. COD-42, COD-53-55) plus 7 standard sub-issues
- Notion Sprint Tracker: each week is registered as Sprint 02-05 with its objective, duration, and deliverables
