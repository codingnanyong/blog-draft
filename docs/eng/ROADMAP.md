# Roadmap / Series Plan

## The "Codigdex" series concept

Like a Pokédex, each series (`#number`) is one technology **chapter**. Each week within a chapter observes a distinct specimen such as `NO.001` or `NO.002`, then formally registers that specimen in the Codigdex at the very end of the post. The final week registers its own specimen and also marks the whole chapter complete.

> **Week count follows specimen count.** Each week registers one specimen, so a chapter with five specimens runs five weeks. See [Criteria for picking the next chapter](#criteria-for-picking-the-next-chapter) for details.

Chapter order follows the dex numbers of the user's game, [codigdex](https://github.com/codingnanyong/codigdex) (decided 2026-11-02). The earlier plan moved Data Engineering chapters forward starting from `#03` Docker; the series now follows the game: `#01` Git → `#02` Linux → `#03` HTML/CSS → `#04` JavaScript. Docker is `#11` and data pipelines are `#18`. The user works as a Data Engineer, and that experience becomes material when the matching chapter arrives.

## #01 — Git (5-week breakdown)

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Git basics — first encounter | 2026-09-03 | COD-41 | Published |
| Week 2 | Git branching and merging | 2026-09-07 | COD-42 | Published |
| Week 3 | Undoing changes & merge conflicts | 2026-09-14 | COD-53 | Published |
| Week 4 | Remote repositories & rebase | 2026-09-21 | COD-54 | Published |
| Week 5 | Collaboration workflow (wrap-up) | 2026-09-28 | COD-55 | Published |

Each week follows the same process defined in [Git branch strategy](GIT_WORKFLOW.md) and [Content & publishing workflow](WORKFLOW.md). NO.001 through NO.005 are registered individually at the end of their respective posts; once week 5 is registered, the Git chapter is complete and the series moves on to the next chapter, `#02` Linux.

## #02 — Linux (5-week chapter, published)

The user has picked Linux as the chapter after Git. The user's separate game project, [codigdex](https://github.com/codingnanyong/codigdex), sets `CH.01 Git → CH.02 Terminal · Linux` as the **junior common path** for every role, and leaves Docker out of that common path because containers are much easier to learn once you understand the terminal, processes, and networking. So that the blog shares the same common foundation, Linux takes the `#02` slot. Following the game's CH.02 Lv.1–Lv.5 stages, the blog observed NO.006–NO.010 and published all five weeks in both languages.

| Week | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- |
| Week 1 | Linux basics — first encounter (shell & terminal, `pwd`/`ls`/`cd`) | 2026-10-05 | COD-343 | Published |
| Week 2 | Paths & files (absolute/relative paths, `mkdir`/`cp`/`mv`/`rm`/`find`) | 2026-10-12 | COD-350 | Published |
| Week 3 | Permissions & users (`rwx`, `chmod`/`chown`, `sudo`) | 2026-10-19 | COD-360 | Published |
| Week 4 | Pipes & processes (`\|`/`>`/`>>`, `ps`/`top`/`kill`, background jobs) | 2026-10-26 | COD-369 | Published |
| Week 5 | The kernel & the OS (kernel, system calls, boot, `systemctl`, wrap-up registration) | 2026-11-02 | COD-402 | Published |

The user reported Week 1 (NO.006) published on both Velog and Medium. PR #124 includes the Korean and English posts, five images per language, and updated Git registration cards. The date remains 2026-10-05, the Monday of the publication week; publication on both platforms was reported on 2026-10-08. The user reported Week 2 (NO.007) published on both Velog and Medium on 2026-10-13. PRs #127, #128, and #130 include the Korean and English posts with seven images per language (thumbnail, 01–04, and explanatory 05–06); the date remains 2026-10-12, the Monday of the publication week. The user reported Week 3 (NO.008) published on both Velog and Medium on 2026-10-19. The `feat/cod-360-permissions-users` PR includes the Korean and English posts with eight images per language (thumbnail, 01–04, and explanatory 05–07); the date is 2026-10-19, the publication Monday itself. Linear issues (parent + standard sub-issues) and Notion sprints for the remaining weeks will be created once their breakdown is confirmed. If the actual pacing turns out different once underway, the week count may be adjusted.

The user confirmed Week 4 from the roadmap on 2026-10-26. Recurring issue COD-369 and its six standard sub-issues were automatically created on 2026-10-20 at 00:32 KST, then deleted at 08:33 KST that day. The original parent and children were restored and reused. Drafting Cycle 8 (2026-10-26–11-01) and Notion Sprint 09 are In Progress at 2/6 (topic selection and drafting complete). Actual Claude Code authored the Korean and English drafts; Codex generated, inspected, and linked eight images per language, sixteen total. The user reported both Velog and Medium published on 2026-10-26, the same as the planned date. The roadmap retains 2026-10-26 as the existing planned publication date and records that it overlaps the drafting start week. Actual publication remains unconfirmed until the user reports it.

Week 5 (NO.010) uses the existing recurring issue COD-402. Actual Claude Code wrote the Korean and English articles; Codex generated, inspected, and linked seven images per language, fourteen total. The user reported both Velog and Medium published on 2026-11-02, matching the planned publication date. Both articles are `status: published`. Deliverables are in `posts/2026/11/#010_kernel-os/`. Checks confirmed nineteen matching code blocks, matching heading structures, and valid image paths. The final NO.010 registration card completes the Linux chapter at 5/5.

## #03 — HTML/CSS (week 1 published, week 2 topic confirmed)

On 2026-11-02 the user decided to take every chapter after Linux (`#02`) in the game's dex-number order. NO.011–015, the numbers after NO.010, are the specimens of the game's `ch03.html-css`. On 2026-11-07 the user confirmed semantic HTML for the next post. Codex is preparing the Korean and English drafts and images for week 1; the remaining weeks follow the game's specimen and concept order as a proposal.

| Week | Dex number · specimen | Topic | Publish Date | Linear | Status |
| --- | --- | --- | --- | --- | --- |
| Week 1 | NO.011 Structure Sprout | HTML/CSS basics — first encounter (semantic HTML) | 2026-11-09 | COD-441 | Published |
| Week 2 | NO.012 Style Shell | The box model | 2026-11-16 | TBD | Proposed |
| Week 3 | NO.013 Cascade Weaver | The cascade (specificity and source order) | 2026-11-23 | TBD | Proposed |
| Week 4 | NO.014 Breakpoint Knight | Media queries | 2026-11-30 | TBD | Proposed |
| Week 5 | NO.015 Responsive Layout Paladin | Accessibility (wrap-up registration) | 2026-12-07 | TBD | Proposed |

For week 1 (NO.011), the user reported both Velog and Medium published on 2026-11-13. The final drafts reviewed with Claude and eight selected images per language are published; both manuscripts now use `status: published`. The date remains 2026-11-09, the Monday of the publication week. The report date is recorded separately; the exact day of publication has not been asserted.

## #04 onward — game order (order confirmed, weekly breakdowns confirmed before each chapter)

Blog `#NN` uses the same number as game `CH.NN`, and each week registers one specimen. Publish windows assume every chapter runs 5 weeks with no gaps. Core concepts follow the game's Lv.1–Lv.5 order. Some specimen names don't line up with their topics (for example, NO.054 Registry Carrier's concept is Volume), so recheck them when each chapter starts.

| Chapter | Topic | Dex numbers | Core concepts | Publish window (estimate) |
| --- | --- | --- | --- | --- |
| #04 | JavaScript | NO.016–020 | Variable → Function → Event → Promise → async/await | 2026-12-14 – 2027-01-11 |
| #05 | HTTP/API | NO.021–025 | Request/Response → Status code → Header → REST endpoint → API token | 2027-01-18 – 02-15 |
| #06 | Python | NO.026–030 | Indentation → Collection → Function/Module → Exception → Virtual environment | 2027-02-22 – 03-22 |
| #07 | SQL | NO.031–035 | SELECT/WHERE → Primary key → JOIN → Index → Transaction | 2027-03-29 – 04-26 |
| #08 | Networking | NO.036–040 | IP address → DNS → TCP → Router → Load balancer | 2027-05-03 – 05-31 |
| #09 | Testing | NO.041–045 | Unit test → Assertion → Mock → Integration test → Regression test | 2027-06-07 – 07-05 |
| #10 | Security/Auth | NO.046–050 | Hash → Authentication → Authorization → Input validation → Least privilege | 2027-07-12 – 08-09 |
| #11 | Docker | NO.051–055 | Image → Container → Dockerfile → Volume → Registry | 2027-08-16 – 09-13 |
| #12 | CI/CD | NO.056–060 | Build → Automated test → Pipeline → Deployment → Rollback | 2027-09-20 – 10-18 |
| #13 | Kubernetes | NO.061–065 | Pod → Deployment → Service → ConfigMap/Secret → Autoscaling | 2027-10-25 – 11-22 |
| #14 | Cloud/IaC | NO.066–070 | Resource → State → Plan → Module → Immutable infrastructure | 2027-11-29 – 12-27 |
| #15 | Monitoring | NO.071–075 | Metric → Log → Trace → Alert → SLI/SLO | 2028-01-03 – 01-31 |
| #16 | React | NO.076–080 | Component → Props → State → Hook → Key | 2028-02-07 – 03-06 |
| #17 | Server framework | NO.081–085 | Route → Middleware → Controller → Service layer → Dependency injection | 2028-03-13 – 04-10 |
| #18 | Data pipeline | NO.086–090 | Extract → Transform → Load → Batch/Stream → Data quality | 2028-04-17 – 05-15 |
| #19 | Workflow orchestration | NO.091–095 | DAG → Task → Dependency → Schedule → Retry | 2028-05-22 – 06-19 |
| #20 | Basic statistics | NO.096–100 | Sample → Probability → Distribution → Variance → Inference | 2028-06-26 – 07-24 |
| #21 | Data visualization | NO.101–105 | Chart selection → Scale → Color → Annotation → Visual story | 2028-07-31 – 08-28 |
| #22 | BI tools | NO.106–110 | Metric → Dimension → Semantic model → Filter/Drill → Dashboard governance | 2028-09-04 – 10-02 |
| #23 | Platform & SRE (tier two) | NO.111–115 | Integrating deployment, signals, promises, and incident response | 2028-10-09 – 11-06 |
| #24 | Full stack (tier two) | NO.116–120 | API contracts → Request state → Transactions → Tracing → Integration checks | 2028-11-13 – 12-11 |
| #25 | ML serving (tier two) | NO.121–125 | Sample quality → Feature parity → Evaluation → Inference contracts → Integration checks | 2028-12-18 – 2029-01-15 |
| #26 | MLOps (tier two) | NO.126–130 | Lineage → Training pipelines → Model registration → Drift detection → Retraining | 2029-01-22 – 02-19 |
| #27 | Analytics (tier two) | NO.131–135 | Table grain → Data tests → Metric definitions → Dependencies → Analytical delivery | 2029-02-26 – 03-26 |

### Open-source expeditions (NO.136–173)

After `#27` come the game's expedition chapters `EX.01`–`EX.09`. Each tool is one specimen, for 38 weeks in total; with no gaps that runs 2029-04-02 – 2029-12-17. Their blog chapter numbers and grouping will be decided before they start.

- **EX.01 Hadoop ecosystem**: Hadoop, HDFS, YARN, MapReduce, Hive, HBase, ZooKeeper, Parquet, Avro
- **EX.02 Workflows**: Airflow
- **EX.03 Ingestion & streaming**: Kafka, Kafka Connect, Debezium, Flink
- **EX.04 Lakes & queries**: Spark, Iceberg, Delta Lake, Hudi, DuckDB, Trino
- **EX.05 Quality & lineage**: dbt Core, Great Expectations, OpenLineage, Marquez
- **EX.06 Analytics & visualization**: Superset
- **EX.07 Machine learning**: MLflow, DVC, Feast, scikit-learn
- **EX.08 Platform & observability**: Prometheus, Grafana, OpenTelemetry, OpenTofu, Argo CD
- **EX.09 Applications**: PostgreSQL, Playwright, TanStack Query, Zod

### Real-world material

The user actually uses Airflow, Kafka, and dbt on the job, has implemented a Medallion Architecture on PostgreSQL + TimescaleDB in-house, and migrated infrastructure from Docker to Kubernetes. The order follows the game, and this experience becomes material when the matching chapter arrives. Topics with no matching specimen, such as Medallion Architecture, have no dex number, so whether they become posts outside the regular chapters will be decided then. Other candidate topics such as data modeling, CDC, partitioning, query optimization, and backfill strategy follow the same rule: work them into a related chapter or cover them in a separate post.

## Estimated yearly coverage (rough estimate, not confirmed)

Posts publish weekly on Monday. The estimate below uses the gap-free schedule above, and any skipped week pushes everything after it back. The game's numbers can change during development, so recheck the game repo when each chapter starts.

- **2026**: `#01` Git → `#02` Linux → `#03` HTML/CSS → `#04` JavaScript begins
- **2027**: `#04` JavaScript wraps up → `#05` HTTP/API → `#06` Python → `#07` SQL → `#08` Networking → `#09` Testing → `#10` Security/Auth → `#11` Docker → `#12` CI/CD → `#13` Kubernetes → `#14` Cloud/IaC
- **2028**: `#15` Monitoring → `#16` React → `#17` Server framework → `#18` Data pipeline → `#19` Workflow orchestration → `#20` Basic statistics → `#21` Data visualization → `#22` BI tools → `#23` Platform & SRE → `#24` Full stack → `#25` ML serving begins
- **2029**: `#25` ML serving wraps up → `#26` MLOps → `#27` Analytics → open-source expeditions `EX.01`–`EX.09`
- **Total material**: NO.011 through NO.173 is 163 weeks, about three years.

## Criteria for picking the next chapter

- **Follow the game's dex-number order** — the next chapter is the game chapter holding the number after the last registered one. Blog `#NN` matches game `CH.NN`.
- **Week count follows specimen count** — each week registers one specimen, so a chapter with five specimens runs five weeks.
- **Confirm weekly topics before a chapter starts** — the game's concept order is the default, adjusted with the user to fit the writing.
- **Use job-related experience as material** — it doesn't move a chapter earlier; the matching chapter draws on the user's real experience.

## Where it's tracked

- Linear: a parent issue per week (e.g. COD-42, COD-53-55) plus 7 standard sub-issues
- Notion Sprint Tracker: each week is registered as Sprint 02-05 with its objective, duration, and deliverables
