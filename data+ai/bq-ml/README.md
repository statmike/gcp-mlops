![tracker](https://us-central1-vertex-ai-mlops-369716.cloudfunctions.net/pixel-tracking?path=statmike%2Fgcp-mlops%2Fdata%2Bai%2Fbq-ml&file=README.md)
<!--- header table --->
<table>
<tr>     
  <td style="text-align: center">
    <a href="https://github.com/statmike/gcp-mlops/blob/main/data%2Bai/bq-ml/README.md">
      <img width="32px" src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/github.svg" alt="GitHub logo">
      <br>View on<br>GitHub
    </a>
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <b>Share On: </b> 
    <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ml/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/linkedin.svg" alt="Linkedin Logo" width="20px"></a> 
    <a href="https://reddit.com/submit?url=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ml/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/reddit.png" alt="Reddit Logo" width="20px"></a> 
    <a href="https://bsky.app/intent/compose?text=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ml/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/bluesky.svg" alt="BlueSky Logo" width="20px"></a> 
    <a href="https://x.com/intent/post?url=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ml/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/x.svg" alt="X (Twitter) Logo" width="20px"></a> 
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <b>Connect With Author On: </b> 
    <a href="https://www.linkedin.com/in/statmike"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/linkedin.svg" alt="Linkedin Logo" width="20px"></a>
    <a href="https://github.com/statmike"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/github.svg" alt="GitHub Logo" width="20px"></a> 
    <a href="https://www.youtube.com/@statmike-channel"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/youtube.svg" alt="YouTube Logo" width="20px"></a>
    <a href="https://bsky.app/profile/statmike.bsky.social"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/bluesky.svg" alt="BlueSky Logo" width="20px"></a> 
    <a href="https://x.com/statmike"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/x.svg" alt="X (Twitter) Logo" width="20px"></a>
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <a href="https://raw.githubusercontent.com/statmike/gcp-mlops/main/data%2Bai/bq-ml/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/download.svg" alt="Download icon" width="20px"></a> <a href="https://raw.githubusercontent.com/statmike/gcp-mlops/main/data%2Bai/bq-ml/README.md">Download File</a> <i>(right-click and "Save As")</i>
  </td>
</tr>
</table><br/><br/>

---
# BigQuery ML (`bigquery-ml`)
> You are here: `gcp-mlops/data+ai/bq-ml/README.md` ([⬅ Back to Data + AI](../readme.md) · [Repository Front Door](../../readme.md) · [Agent Skills](../../agent-skills/README.md))

[![PyPI](https://img.shields.io/pypi/v/bigquery-data-science?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/bigquery-data-science/)
[![BigQuery ML Hub on GitHub](https://img.shields.io/badge/GitHub-statmike%2Fbigquery--data--science%2Fbigquery--ml-4285F4?style=for-the-badge&logo=github&logoColor=white)](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml)
[![bigquery-ml Skill](https://img.shields.io/badge/Agent%20Skill-bigquery--ml%20(4--Lens)-8E24AA?style=for-the-badge)](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ml/SKILL.md)
[![BigQuery AI Sibling](https://img.shields.io/badge/Sibling%20Hub-BigQuery%20AI-0F9D58?style=for-the-badge)](../bq-ai-functions/README.md)

> [!IMPORTANT]
> **Dedicated Repository & PyPI Package (`statmike/bigquery-data-science`):**
> The complete **BigQuery ML** notebook curriculum, standalone `.sql` scripts, deep reference guides, and **4-Lens `bigquery-ml` Agent Skill** live in **[`statmike/bigquery-data-science/bigquery-ml`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml)** and ship on PyPI as **[`bigquery-data-science`](https://pypi.org/project/bigquery-data-science/)**.
>
> Train, evaluate, explain, monitor, and schedule machine learning models entirely in BigQuery SQL (`CREATE MODEL` + `ML.*` functions) — with zero data movement and every option, edge case, and error message verified against live BigQuery.

---

## How BigQuery ML Fits Together

```mermaid
flowchart TD
    DATA["DATA (BigQuery Table or Query)"] --> PREP["Model-Free ML.* Preprocessing & Point-in-Time Features<br/>ML.STANDARD_SCALER · ML.BUCKETIZE · ML.ONE_HOT_ENCODER<br/>ML.IMPUTER · ML.FEATURE_CROSS · ML.ENTITY_FEATURES_AT_TIME<br/>(Standalone in SELECT/FROM, or embedded inside TRANSFORM)"]
    PREP --> MODEL["CREATE MODEL<br/>Trains & stores a model in your dataset (+ optional TRANSFORM & NUM_TRIALS)<br/>LOGISTIC_REG · LINEAR_REG · BOOSTED_TREE_* · RANDOM_FOREST_*<br/>DNN_* · WIDE_AND_DEEP_* · AUTOML_* · ARIMA_PLUS · ARIMA_PLUS_XREG<br/>KMEANS · PCA · AUTOENCODER · MATRIX_FACTORIZATION · CONTRIBUTION_ANALYSIS"]

    MODEL --> EVAL["Evaluation<br/>ML.EVALUATE · ML.METRICS<br/>ML.CONFUSION_MATRIX<br/>ML.ROC_CURVE · ML.ARIMA_EVALUATE"]
    MODEL --> INFER["Inference & Scoring<br/>ML.PREDICT · ML.FORECAST<br/>ML.RECOMMEND · ML.DETECT_ANOMALIES<br/>ML.GET_INSIGHTS · ML.TRANSFORM"]
    MODEL --> LOCAL_EXP["Local Explainability<br/>ML.EXPLAIN_PREDICT<br/>ML.EXPLAIN_FORECAST<br/>(Per-row feature attributions)"]
    MODEL --> GLOBAL_EXP["Global Explainability & Weights<br/>ML.GLOBAL_EXPLAIN · ML.FEATURE_IMPORTANCE<br/>ML.WEIGHTS · ML.ADVANCED_WEIGHTS<br/>ML.CENTROIDS · ML.PRINCIPAL_COMPONENTS"]
    MODEL --> META["Training & Tuning Metadata<br/>ML.TRAINING_INFO · ML.FEATURE_INFO<br/>ML.TRIAL_INFO · ML.HOLIDAY_INFO"]

    subgraph MGMT["Model Portability, Remote Serving & Monitoring"]
        direction LR
        PORT["Import / Export / Remote<br/>EXPORT MODEL (→ GCS / Vertex Registry)<br/>Imported (ONNX · TF · TFLite · XGBoost)<br/>REMOTE WITH CONNECTION (→ Vertex Endpoint)<br/>TRANSFORM_ONLY (reusable preprocessing)"]
        MON["Dataset Drift & Skew Monitoring<br/>ML.DESCRIBE_DATA · ML.VALIDATE_DATA_SKEW<br/>ML.VALIDATE_DATA_DRIFT · ML.TFDV_*"]
    end

    subgraph OPS["Production Orchestration (bigquery-ml/pipelines/)"]
        direction LR
        PIPE["Scheduled Retrain, Drift Gate & Scoring<br/>SQL Scripting · Scheduled Queries · Dataform · dbt<br/>Cloud Workflows · Managed Airflow (Composer Gen 3) · Vertex AI Pipelines (KFP)"]
    end

    EVAL --> MGMT
    INFER --> MGMT
    LOCAL_EXP --> MGMT
    GLOBAL_EXP --> MGMT
    META --> MGMT
    MGMT --> OPS

    classDef data fill:#E8F0FE,stroke:#4285F4,stroke-width:2px,color:#174EA6
    classDef config fill:#FEF7E0,stroke:#F9AB00,stroke-width:2px,color:#7A5A00
    classDef route fill:#FCE8E6,stroke:#EA4335,stroke-width:2px,color:#A50E0E
    classDef compute fill:#E6F4EA,stroke:#34A853,stroke-width:2px,color:#0D652D
    class DATA,PREP data
    class MODEL route
    class EVAL,INFER,LOCAL_EXP,GLOBAL_EXP,META compute
    class PORT,MON,PIPE config
```

---

## Navigate the BigQuery ML Hub (`statmike/bigquery-data-science/bigquery-ml`)

| Category / Folder | What It Covers | Direct Entry Points in `statmike/bigquery-data-science` |
| :--- | :--- | :--- |
| **Start Here & Reference Guides** | Interactive tour of BigQuery ML, environment/connection/IAM setup, and the complete `CREATE MODEL` + `ML.*` reference index. | [**`bigquery-ml/README.md`**](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/README.md) · [`overview.ipynb`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/overview.ipynb) · [`RESOURCES.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/RESOURCES.md) · [`setup/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/setup) · [`reference/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/reference) |
| **[`models/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/models)**<br/>*Per-Model Lifecycle Deep Dives (`.ipynb` + `.sql`)* | Full lifecycle (`CREATE MODEL` $\to$ `ML.EVALUATE` $\to$ `ML.PREDICT` / `ML.FORECAST` / `ML.RECOMMEND` $\to$ `ML.EXPLAIN_*` $\to$ hyperparameter tuning) across classification & regression (`LOGISTIC_REG`, `LINEAR_REG`, `BOOSTED_TREE_*`, `RANDOM_FOREST_*`, `DNN_*`, `WIDE_AND_DEEP_*`, `AUTOML_*`), unsupervised (`KMEANS`, `PCA`, `AUTOENCODER`), time series (`ARIMA_PLUS`, `ARIMA_PLUS_XREG`), recommendations (`MATRIX_FACTORIZATION`), key drivers (`CONTRIBUTION_ANALYSIS`), and portability (`TRANSFORM_ONLY`, `IMPORTED`, `EXPORT MODEL`, `REMOTE`). | [**`bigquery-ml/models/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/models) · [`reference/create-model-model-types.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/reference/create-model-model-types.md) · [`reference/comparison-tables.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/reference/comparison-tables.md) |
| **[`functions/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/functions)**<br/>*Model-Free `ML.*` Function Suites (`.ipynb` + `.sql`)* | Standalone utilities and `TRANSFORM`-clause building blocks: data profiling (`ML.DESCRIBE_DATA`, `ML.CORRELATION`), point-in-time feature retrieval (`ML.FEATURES_AT_TIME`, `ML.ENTITY_FEATURES_AT_TIME`), model-free evaluation (`ML.METRICS`), distribution drift/skew monitoring (`ML.VALIDATE_DATA_SKEW`, `ML.VALIDATE_DATA_DRIFT`, `ML.TFDV_*`), time-series decomposition (`ML.TREND`, `ML.SEASONALITY`, `ML.DETECT_CHANGE_POINTS`), image tensors (`ML.DECODE_IMAGE`, `ML.RESIZE_IMAGE`), scalers, encoders, feature crosses, bucketizers, vector distances, and text features. | [**`bigquery-ml/functions/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/functions) · [`reference/model-free-functions.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/reference/model-free-functions.md) · [`reference/model-lifecycle-functions.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/reference/model-lifecycle-functions.md) · [`reference/model-management-monitoring.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ml/reference/model-management-monitoring.md) |
| **[`workflows/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/workflows)**<br/>*End-to-End Composed SQL Workflows* | **Causal Inference & Econometrics in SQL** (Propensity Score Matching & IPTW, Double ML Price Elasticity, Uplift/CATE T-Learner, Difference-in-Differences with Callaway–Sant'Anna, Synthetic Control, `AI.CAUSAL_EFFECT` vs `ARIMA_PLUS`, and Survival Analysis) plus **Predictive & Analytical Workflows** (Point-in-Time Feature Store leakage quantification, Hierarchical & Regression-Based Forecasting, Embeddings Classification, RFM Segmentation, Order-Lapse & GA4 Churn, Recommendations, Fraud/Anomaly Detection, Cross-Validation, and Stacked Ensembling). | [**`bigquery-ml/workflows/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/workflows) · [`skills/bigquery-ml/reference/workflows-and-pipelines.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ml/reference/workflows-and-pipelines.md) |
| **[`pipelines/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/pipelines)**<br/>*Production MLOps & Orchestration* | The same drift-detection, conditional retraining, quality-gating, and batch-scoring loop implemented across **BigQuery SQL Scripting**, **Scheduled Queries**, **Dataform** (`dependOnDependencyAssertions`), **Cloud Workflows**, **dbt** (`dbt build` + custom `bqml_model` materialization), **Vertex AI Pipelines (KFP)**, and **Managed Airflow (Composer Gen 3)**. | [**`bigquery-ml/pipelines/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ml/pipelines) · [`skills/bigquery-ml/reference/workflows-and-pipelines.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ml/reference/workflows-and-pipelines.md) |
| **[`skills/bigquery-ml/`](https://github.com/statmike/bigquery-data-science/tree/main/skills/bigquery-ml)**<br/>*4-Lens Agent Skill* | Decision trees, empirically verified gotchas, surgical `< 25 KB` per-model/per-function syntax cards ([`syntax/INDEX.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ml/syntax/INDEX.md)), and clean markdown textbook narratives (`narrative/*.md`). | [**`skills/bigquery-ml/SKILL.md`**](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ml/SKILL.md) · [`syntax/INDEX.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ml/syntax/INDEX.md) · [`skills/bigquery-data-science/SKILL.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-data-science/SKILL.md) |

---

## Quickstart — Skills, CLI, MCP & Notebooks

```bash
# 1. Install the 4-Lens Agent Skills (bigquery-data-science, bigquery-ml, bigquery-ai):
uvx bigquery-data-science install                     # into ./.agents/skills & ./.claude/skills
uvx bigquery-data-science install --global            # into ~/.agents/skills & ~/.claude/skills
npx skills add statmike/bigquery-data-science         # via skills.sh CLI
pip install bigquery-data-science && bigquery-data-science install

# 2. Triage tasks & look up exact BigQuery ML syntax from the terminal:
uvx bigquery-data-science triage "forecast daily sales with promotions"
uvx bigquery-data-science lookup ARIMA_PLUS_XREG
uvx bigquery-data-science lookup ML.ENTITY_FEATURES_AT_TIME
uvx bigquery-data-science search "point-in-time feature leakage"

# 3. Attach the zero-dependency stdio MCP server to Claude Code:
claude mcp add bigquery-data-science -- uvx bigquery-data-science mcp

# 4. Clone & run the BigQuery ML notebooks locally:
git clone https://github.com/statmike/bigquery-data-science.git
cd bigquery-data-science
uv sync --extra all && uv run bigquery-data-science kernel --user
```
