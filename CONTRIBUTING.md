# Contributing to `gcp-mlops`

Thank you for your interest in contributing to `gcp-mlops`. This repository is a collection of **470+ interactive notebooks**, end-to-end reference workflows, solution prototypes, and packaged [Agent Skills](./agent-skills/README.md) across Google Cloud's AI and data ecosystem (Gemini Enterprise, Vertex AI, BigQuery ML, BigQuery AI Functions, Agent Development Kit, Dataflow, Dataproc, Managed Airflow, AlloyDB, Spanner, Bigtable, and more).

Issues and pull requests for bug fixes, documentation improvements, link updates, and workflow enhancements are welcome.

---

## 1. Before You Open a Pull Request

- **Small fixes (typos, broken links, API parameter updates):** Feel free to open a pull request directly with a clear description of the fix.
- **New notebooks, subprojects, or major restructuring:** Please open an [issue](https://github.com/statmike/gcp-mlops/issues) first to discuss scope and directory placement so it aligns with the repository's structure.

---

## 2. Public-Repository & Credential Hygiene

Every contribution must follow these security and privacy rules:

- **Application Default Credentials (ADC) only:** Never load or commit service account JSON key files (`*-key.json`, `*.json.key`, `service-account*.json`). Notebooks, scripts, and agents authenticate via Application Default Credentials (`gcloud auth application-default login` locally or attached service accounts in Google Cloud runtimes).
- **Zero proprietary or customer data:** Never include customer names, engagement identifiers, internal hostnames, credentials, or personal local filesystem paths in notebooks, code, configs, or persisted cell outputs.
- **Self-contained, reproducible workflows:** Notebooks should rely on public datasets, synthetic data generated in-notebook, or resources created by the workflow's own setup steps.

---

## 3. Verification Gates

Depending on what your pull request touches, run the relevant checks before submitting:

### Header & Link Hygiene (`architectures/headers/sync_headers.py`)

When adding or updating notebooks (`.ipynb`) or markdown guides (`.md`) in `gcp-mlops`, verify that standard repository headers are in sync:

```bash
python3 architectures/headers/sync_headers.py --check
# Or apply headers automatically:
python3 architectures/headers/sync_headers.py --apply
```

### BigQuery ML, BigQuery AI & Agent Skills ([`statmike/bigquery-data-science`](https://github.com/statmike/bigquery-data-science))

The BigQuery ML (`bigquery-ml/`), BigQuery AI (`bigquery-ai/`), and 4-Lens Agent Skills (`skills/`) curricula have graduated to the standalone repository **[`statmike/bigquery-data-science`](https://github.com/statmike/bigquery-data-science)** and Python package **[`bigquery-data-science` on PyPI](https://pypi.org/project/bigquery-data-science/)**. Please open issues or pull requests for those notebooks, SQL scripts, and skills directly in [`statmike/bigquery-data-science`](https://github.com/statmike/bigquery-data-science) (see its local [`CONTRIBUTING.md`](https://github.com/statmike/bigquery-data-science/blob/main/CONTRIBUTING.md) for the `uv run bigquery-data-science sweep` verification gate).

### Python Subprojects (`Applied ML/`, `data+ai/`, `MLOps/`)

When modifying a standalone Python or ADK subproject that includes its own `pyproject.toml`, run its local linter, type checker, and test suite (for example, `uv run ruff check .`, `uv run mypy`, and `uv run pytest`) from that subproject's directory.

---

## 4. Contributor License Agreement

Contributions to this project must be accompanied by a [Contributor License Agreement](https://cla.developers.google.com/about) (CLA). You (or your employer) retain the copyright to your contribution; this simply gives permission to use and redistribute your contributions as part of the project.

If you have not already done so, please complete your CLA at <https://cla.developers.google.com/> before submitting a pull request.

---

## 5. Community Guidelines & License

This project follows [Google's Open Source Community Guidelines](https://opensource.google/conduct/) and [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md).

By contributing to `gcp-mlops`, you agree that your contributions will be licensed under the [Apache License 2.0](./LICENSE).

This is not an officially supported Google product. It is built on Google products and is neither endorsed nor supported by Google.
