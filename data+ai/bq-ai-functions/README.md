![tracker](https://us-central1-vertex-ai-mlops-369716.cloudfunctions.net/pixel-tracking?path=statmike%2Fgcp-mlops%2Fdata%2Bai%2Fbq-ai-functions&file=README.md)
<!--- header table --->
<table>
<tr>     
  <td style="text-align: center">
    <a href="https://github.com/statmike/gcp-mlops/blob/main/data%2Bai/bq-ai-functions/README.md">
      <img width="32px" src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/github.svg" alt="GitHub logo">
      <br>View on<br>GitHub
    </a>
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <b>Share On: </b> 
    <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ai-functions/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/linkedin.svg" alt="Linkedin Logo" width="20px"></a> 
    <a href="https://reddit.com/submit?url=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ai-functions/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/reddit.png" alt="Reddit Logo" width="20px"></a> 
    <a href="https://bsky.app/intent/compose?text=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ai-functions/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/bluesky.svg" alt="BlueSky Logo" width="20px"></a> 
    <a href="https://x.com/intent/post?url=https://github.com/statmike/gcp-mlops/blob/main/data%252Bai/bq-ai-functions/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/x.svg" alt="X (Twitter) Logo" width="20px"></a> 
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
    <a href="https://raw.githubusercontent.com/statmike/gcp-mlops/main/data%2Bai/bq-ai-functions/README.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/download.svg" alt="Download icon" width="20px"></a> <a href="https://raw.githubusercontent.com/statmike/gcp-mlops/main/data%2Bai/bq-ai-functions/README.md">Download File</a> <i>(right-click and "Save As")</i>
  </td>
</tr>
</table><br/><br/>

---
# BigQuery AI (`bigquery-ai`)
> You are here: `gcp-mlops/data+ai/bq-ai-functions/README.md` ([⬅ Back to Data + AI](../readme.md) · [Repository Front Door](../../readme.md) · [Agent Skills](../../agent-skills/README.md))

[![PyPI](https://img.shields.io/pypi/v/bigquery-data-science?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/bigquery-data-science/)
[![BigQuery AI Hub on GitHub](https://img.shields.io/badge/GitHub-statmike%2Fbigquery--data--science%2Fbigquery--ai-0F9D58?style=for-the-badge&logo=github&logoColor=white)](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai)
[![bigquery-ai Skill](https://img.shields.io/badge/Agent%20Skill-bigquery--ai%20(4--Lens)-8E24AA?style=for-the-badge)](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ai/SKILL.md)
[![BigQuery ML Sibling](https://img.shields.io/badge/Sibling%20Hub-BigQuery%20ML-4285F4?style=for-the-badge)](../bq-ml/README.md)

> [!IMPORTANT]
> **Dedicated Repository & PyPI Package (`statmike/bigquery-data-science`):**
> The complete **BigQuery AI** notebook curriculum, standalone `.sql` scripts, deep reference guides, and **4-Lens `bigquery-ai` Agent Skill** live in **[`statmike/bigquery-data-science/bigquery-ai`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai)** and ship on PyPI as **[`bigquery-data-science`](https://pypi.org/project/bigquery-data-science/)**.
>
> Call Gemini, generate embeddings, run semantic and hybrid search, forecast with TimesFM, predict on tabular data with TabFM, and process multimodal documents directly in BigQuery SQL (`AI.*` and remote `ML.*` functions) — with no ML training infrastructure to manage.

---

## How BigQuery AI Functions Relate

```mermaid
flowchart TD
    subgraph GEN["1. General-Purpose Generation (Gemini)"]
        direction TB
        G1["AI.GENERATE (Scalar · No CREATE MODEL)<br/>Text or structured output_schema · Multimodal ObjectRef"]
        G2["Typed Scalar Shorthands (No CREATE MODEL)<br/>AI.GENERATE_BOOL · AI.GENERATE_DOUBLE · AI.GENERATE_INT"]
        G3["Table-Valued & Utility Functions<br/>AI.GENERATE_TABLE (TVF structured output)<br/>AI.GENERATE_TEXT / ML.GENERATE_TEXT (TVF · requires CREATE MODEL)<br/>AI.COUNT_TOKENS (Free local input token counter)"]
        G1 --> G2 --> G3
    end

    subgraph MGD["2. Managed Task Functions (Gemini · No CREATE MODEL)"]
        direction TB
        M1["AI.IF — Auto-optimized boolean filter (SELECT / WHERE / JOIN)"]
        M2["AI.SCORE — Auto-rubric continuous scoring (FLOAT64)"]
        M3["AI.CLASSIFY — Multi-category assignment (STRING / ARRAY&lt;STRING&gt;)"]
        M4["AI.AGG — Group-level summarization across rows (GROUP BY)"]
        M1 --- M2 --- M3 --- M4
    end

    subgraph EMB["3. Embeddings & Semantic / Hybrid Search"]
        direction TB
        E1["Embedding Generation<br/>AI.EMBED (Scalar · No CREATE MODEL · Text &amp; Multimodal)<br/>AI.GENERATE_EMBEDDING / ML.GENERATE_EMBEDDING (TVF · requires CREATE MODEL)"]
        E2["Similarity &amp; Vector Retrieval<br/>AI.SIMILARITY (Scalar cosine similarity between 2 inputs)<br/>VECTOR_SEARCH + CREATE VECTOR INDEX (Top-K over pre-computed embeddings)<br/>AI.SEARCH (Simplified search over autonomous embedding column)<br/>Hybrid Search = VECTOR_SEARCH / AI.SEARCH + SEARCH (BM25) + RRF"]
        E1 --> E2
    end

    subgraph PRED["4. Predictive AI & Augmented Analytics (No CREATE MODEL)"]
        direction TB
        P1["TimesFM (Time Series)<br/>AI.FORECAST · AI.DETECT_ANOMALIES · AI.EVALUATE<br/>(Pin model =&gt; 'TimesFM 2.5' or 'TimesFM 3.0')"]
        P2["TabFM (Zero-Shot Tabular)<br/>AI.PREDICT · AI.EVALUATE<br/>(Inline training + test tables in one query)"]
        P3["Augmented Analytics &amp; Causal Impact<br/>AI.KEY_DRIVERS (Segment driver analysis)<br/>AI.CAUSAL_EFFECT (Counterfactual impact → covered in bigquery-ml)"]
        P1 --- P2 --- P3
    end

    subgraph DOC["5. Document Processing & Pre-Trained Cloud AI Service Models"]
        direction TB
        D1["Document AI<br/>ML.PROCESS_DOCUMENT (Object table + Document AI processor + REMOTE model)<br/>AI.PARSE_DOCUMENT (Layout Parser · currently offline / docs withdrawn)"]
        D2["Cloud AI Service Models (All require CREATE MODEL ... REMOTE)<br/>ML.TRANSLATE (Translation V3) · ML.UNDERSTAND_TEXT (Natural Language)<br/>ML.ANNOTATE_IMAGE (Vision API) · ML.TRANSCRIBE (Speech-to-Text V2)"]
        D1 --- D2
    end

    GEN --- MGD
    EMB --- PRED
    MGD --- DOC
    PRED --- DOC

    classDef data fill:#E8F0FE,stroke:#4285F4,stroke-width:2px,color:#174EA6
    classDef config fill:#FEF7E0,stroke:#F9AB00,stroke-width:2px,color:#7A5A00
    classDef route fill:#FCE8E6,stroke:#EA4335,stroke-width:2px,color:#A50E0E
    classDef compute fill:#E6F4EA,stroke:#34A853,stroke-width:2px,color:#0D652D
    class G1,G2,G3 data
    class M1,M2,M3,M4 compute
    class E1,E2 config
    class P1,P2,P3 route
    class D1,D2 data
```

---

## Navigate the BigQuery AI Hub (`statmike/bigquery-data-science/bigquery-ai`)

| Category / Folder | What It Covers | Direct Entry Points in `statmike/bigquery-data-science` |
| :--- | :--- | :--- |
| **Start Here & Reference Guides** | Interactive tour of BigQuery AI, connections/models/permissions setup, synthetic PDF generator (`data/documents/`), and the complete `AI.*` + remote `ML.*` reference index. | [**`bigquery-ai/README.md`**](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/README.md) · [`overview.ipynb`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/overview.ipynb) · [`RESOURCES.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/RESOURCES.md) · [`setup/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/setup) · [`reference/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/reference) |
| **1. General-Purpose Generation (`functions/`)** | Free-form text, structured schemas (`output_schema`), multimodal `ObjectRef` inputs, and free local token counting: `AI.GENERATE`, `AI.GENERATE_TABLE`, `AI.GENERATE_TEXT`, `ML.GENERATE_TEXT`, `AI.GENERATE_BOOL`, `AI.GENERATE_DOUBLE`, `AI.GENERATE_INT`, and `AI.COUNT_TOKENS`. | [**`bigquery-ai/functions/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/functions) · [`reference/general-purpose-functions.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/general-purpose-functions.md) |
| **2. Managed Task Functions (`functions/`)** | Simplified, prompt-optimized Gemini functions that require no `CREATE MODEL`: `AI.IF` (boolean filter in `SELECT`/`WHERE`/`JOIN`), `AI.SCORE` (auto-rubric `FLOAT64`), `AI.CLASSIFY` (single or multi-label categories), and `AI.AGG` (group-level summarization across rows). | [**`bigquery-ai/functions/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/functions) · [`reference/managed-functions.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/managed-functions.md) |
| **3. Embeddings, Vector Search & Hybrid Search (`functions/`)** | Text & multimodal embeddings (`AI.EMBED`, `AI.GENERATE_EMBEDDING`, `ML.GENERATE_EMBEDDING`), pairwise cosine similarity (`AI.SIMILARITY`), indexed nearest-neighbor search (`VECTOR_SEARCH` + `CREATE VECTOR INDEX`), autonomous search (`AI.SEARCH`), and **Hybrid Search** (semantic + BM25 lexical + Reciprocal Rank Fusion reach math). | [**`bigquery-ai/functions/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/functions) · [`reference/embedding-generation-and-semantic-search.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/embedding-generation-and-semantic-search.md) |
| **4. Predictive AI & Augmented Analytics (`functions/`)** | Zero-training foundation models in SQL: **TimesFM** (`AI.FORECAST`, `AI.DETECT_ANOMALIES`, `AI.EVALUATE` across `TimesFM 2.5` and `TimesFM 3.0`), **TabFM** (`AI.PREDICT`, `AI.EVALUATE` for inline zero-shot tabular regression/classification), segment driver discovery (`AI.KEY_DRIVERS`), and counterfactual impact (`AI.CAUSAL_EFFECT`). | [**`bigquery-ai/functions/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/functions) · [`reference/predictive-ai.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/predictive-ai.md) · [`reference/augmented-analytics.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/augmented-analytics.md) |
| **5. Document Processing & Cloud AI Service Models (`functions/`)** | Object tables (`OBJ.MAKE_REF`, `ObjectRef`), Document AI (`ML.PROCESS_DOCUMENT`, `AI.PARSE_DOCUMENT`), and versioned Cloud AI APIs (`ML.TRANSLATE`, `ML.UNDERSTAND_TEXT`, `ML.ANNOTATE_IMAGE`, `ML.TRANSCRIBE`). | [**`bigquery-ai/functions/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/functions) · [`reference/document-processing.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/document-processing.md) · [`reference/cloud-ai-service-models.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/cloud-ai-service-models.md) · [`reference/unstructured-data-infrastructure.md`](https://github.com/statmike/bigquery-data-science/blob/main/bigquery-ai/reference/unstructured-data-infrastructure.md) |
| **[`workflows/`](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/workflows)**<br/>*End-to-End Composed Multi-Function Workflows* | Complete pipelines composing multiple `AI.*` and `ML.*` functions: Web-Grounded Data Enrichment + TabFM, Content Analysis & Moderation, Semantic Search (3 ways), Hybrid Product Catalog Search (RRF analysis), RAG Pipeline, Document RAG & Intelligence, Time Series Intelligence, Zero-Shot Tabular Prediction, Metric Diagnostics (with placebo causal checks), Log Triage, Multimodal Analysis, and Image Deduplication. | [**`bigquery-ai/workflows/`**](https://github.com/statmike/bigquery-data-science/tree/main/bigquery-ai/workflows) · [`skills/bigquery-ai/reference/workflows.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ai/reference/workflows.md) |
| **[`skills/bigquery-ai/`](https://github.com/statmike/bigquery-data-science/tree/main/skills/bigquery-ai)**<br/>*4-Lens Agent Skill* | Decision trees, empirically verified gotchas, surgical `< 25 KB` per-function syntax cards ([`syntax/INDEX.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ai/syntax/INDEX.md)), and clean markdown textbook narratives (`narrative/*.md`). | [**`skills/bigquery-ai/SKILL.md`**](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ai/SKILL.md) · [`syntax/INDEX.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-ai/syntax/INDEX.md) · [`skills/bigquery-data-science/SKILL.md`](https://github.com/statmike/bigquery-data-science/blob/main/skills/bigquery-data-science/SKILL.md) |

---

## Quickstart — Skills, CLI, MCP & Notebooks

```bash
# 1. Install the 4-Lens Agent Skills (bigquery-data-science, bigquery-ml, bigquery-ai):
uvx bigquery-data-science install                     # into ./.agents/skills & ./.claude/skills
uvx bigquery-data-science install --global            # into ~/.agents/skills & ~/.claude/skills
npx skills add statmike/bigquery-data-science         # via skills.sh CLI
pip install bigquery-data-science && bigquery-data-science install

# 2. Triage tasks & look up exact BigQuery AI syntax from the terminal:
uvx bigquery-data-science triage "extract structured fields from PDF invoices"
uvx bigquery-data-science lookup AI.GENERATE_TABLE
uvx bigquery-data-science lookup AI.FORECAST
uvx bigquery-data-science search "hybrid search reciprocal rank fusion"

# 3. Attach the zero-dependency stdio MCP server to Claude Code:
claude mcp add bigquery-data-science -- uvx bigquery-data-science mcp

# 4. Clone & run the BigQuery AI notebooks locally:
git clone https://github.com/statmike/bigquery-data-science.git
cd bigquery-data-science
uv sync --extra all && uv run bigquery-data-science kernel --user
```
