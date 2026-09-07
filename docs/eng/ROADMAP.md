# Roadmap / Series Plan

## The "Codigdex" series concept

Like a Pokédex, each series (`#number`) covers one technical "specimen." A specimen is learned step by step over several weeks, from the basics to practical use, and the final week wraps up by formally registering that specimen in the "Codigdex."

> **Week count isn't fixed at 5.** Each specimen's week table below is the specific breakdown decided for that specimen, and it's re-decided per specimen based on its learning curve. See [Criteria for picking the next specimen](#criteria-for-picking-the-next-specimen) for details.

The user (codingnanyong) works as a Data Engineer, and specimen selection for this blog prioritizes doubling as on-the-job study. `#01` Git → `#02` Docker → `#03` CI/CD → `#04` Kubernetes form the common foundation any developer needs (collaboration, containers, automation, orchestration); from `#05` on, the track moves into specimens that map directly onto Data Engineering work (workflow orchestration, distributed processing/streaming, analytics engineering/warehousing).

## #01 — Git (5-week breakdown)

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Git basics — first encounter | 2026-09-03 | COD-41 | Published |
| Week 2 | Git branching and merging | 2026-09-07 | COD-42 | Published |
| Week 3 | Undoing changes & merge conflicts | 2026-09-14 | COD-53 | Drafted (awaiting publish) |
| Week 4 | Remote repositories & rebase | 2026-09-21 | COD-54 | Drafted |
| Week 5 | Collaboration workflow (wrap-up) | 2026-09-28 | COD-55 | Drafted |

Each week follows the same process defined in [Git branch strategy](GIT_WORKFLOW.md) and [Content & publishing workflow](WORKFLOW.md). Once week 5 wraps up, the Git specimen is formally registered in the Codigdex, and topic selection begins for the next specimen (`#02`).

## #02 — Docker (draft — proposed 5 weeks, not confirmed)

The user has picked Docker as the next specimen. Below is a proposed curriculum following the same "basics → applied → collaboration/real-world" three-stage structure as Git — not yet confirmed.

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Docker basics — first encounter (images, containers, Dockerfile) | 2026-10-05 | TBD | Proposed |
| Week 2 | Building images & layers (writing a Dockerfile, layer caching, multi-stage builds) | 2026-10-12 | TBD | Proposed |
| Week 3 | Volumes & networking (data persistence, container-to-container communication) | 2026-10-19 | TBD | Proposed |
| Week 4 | Docker Compose (multi-container orchestration) | 2026-10-26 | TBD | Proposed |
| Week 5 | Real-world collaboration workflow (registries, CI/CD integration, wrap-up registration) | 2026-11-02 | TBD | Proposed |

Once this 5-week breakdown is confirmed, Linear issues (parent + standard sub-issues) and Notion sprints will be created. If the actual pacing turns out different once underway, the week count may be adjusted.

## #03 — CI/CD (GitHub Actions) (order confirmed, curriculum and week count TBD)

Confirmed as the specimen after Docker (#02). Automating the build/deploy of the images made in Docker follows naturally right after it, and it also picks up directly where the Git series' last week (PR → Review → Merge) left off. This repo's own automation (Linear/GitHub integration, PR policy) can serve as real material. Weekly curriculum not yet discussed, and likewise won't be forced into 5 weeks — it'll be sized to the specimen.

## #04 candidate (under consideration)

- Kubernetes — the user is considering this as the specimen after CI/CD (#03). Not yet confirmed; the weekly breakdown will be discussed once #03 wraps up. Given how much ground it covers, running longer than 5 weeks is a natural option to consider.

## #05+ candidates — Data Engineer track (under consideration)

Building on the common infrastructure foundation through `#04` Kubernetes, the specimens under consideration for the following slots map directly onto Data Engineering work. The user actually uses Airflow, Kafka, and dbt on the job, has implemented a Medallion Architecture on PostgreSQL + TimescaleDB in-house, and migrated that infrastructure from Docker to Kubernetes — so this track draws on real work experience rather than hypothetical study. Order, confirmation, and week counts are all still undiscussed — the notes below are directional.

- **Workflow orchestration (Airflow)** — batch/ETL scheduling, DAG-based pipeline management. A natural next step that carries the "automation/orchestration" thread from CI/CD and Kubernetes into the data-pipeline context.
- **Streaming & messaging (Kafka)** — event-driven architecture, real-time data ingestion.
- **Analytics engineering (dbt)** — the transform (T) layer, data modeling, query optimization.
- **Data warehouse architecture — Medallion Architecture (PostgreSQL + TimescaleDB)** — a capstone case study tying the earlier specimens (orchestration, streaming, transformation) together. Covers Raw → Bronze → Silver → Gold layering and time-series-specific data characteristics.

## #09+ broader candidate pool — real-world experience (under consideration)

The topics below are also under consideration, and the user has actually applied them on the job (not hypothetical study material). Order, whether each becomes its own specimen, and week counts are all undecided — the specific tools covered will be confirmed again when each specimen is actually drafted.

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

Posts publish weekly on Monday. The timeline below assumes each specimen runs 5 weeks, purely for estimation — once `#03`/`#04`'s actual week counts are confirmed, everything after shifts accordingly.

- **Within 2026**: `#01` Git (published/drafted, through ~09-28) → `#02` Docker (through ~11-02) → `#03` CI/CD (through ~12-07, assuming 5 weeks) → `#04` Kubernetes weeks 1-3 (~12-14 to ~12-28, with the rest rolling into the next year under a 5-week assumption)
- **From 2027 on**: `#04` Kubernetes wraps up (~01-11) → then the Data Engineer track proceeds in sequence (`#05` Airflow → `#06` Kafka → `#07` dbt → `#08` Medallion Architecture on PostgreSQL+TimescaleDB). Track specimens may run longer than 5 weeks (especially the closing capstone), so exact completion dates will be recalculated once each specimen is confirmed.

## Criteria for picking the next specimen

- A technology or tool used repeatedly in practice, worth revisiting from the basics
- A topic that naturally splits into a "basics → applied → collaboration/real-world" three-stage structure, like Git
- **Week count isn't fixed at 5** — scale it to the specimen's actual learning curve (more than 5 weeks is fine for a bigger topic, and fewer than 5 is fine for a simpler one). #01 Git and #02 Docker (draft) happening to be 5 weeks is just the outcome for those specific specimens, not a rule future specimens must follow.
- **Prioritize topics that genuinely map onto the user's job (Data Engineer)** — so that writing the blog doubles as job-relevant study. Once the common foundation (Git/Docker/CI-CD/Kubernetes) is covered, prioritize tools the user actually uses on the job (Airflow, Kafka, dbt, a Medallion Architecture on PostgreSQL+TimescaleDB, etc.).

## Where it's tracked

- Linear: a parent issue per week (e.g. COD-42, COD-53-55) plus 7 standard sub-issues
- Notion Sprint Tracker: each week is registered as Sprint 02-05 with its objective, duration, and deliverables
