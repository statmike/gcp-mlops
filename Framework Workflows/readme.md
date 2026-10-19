![tracker](https://us-central1-vertex-ai-mlops-369716.cloudfunctions.net/pixel-tracking?path=statmike%2Fgcp-mlops%2FFramework+Workflows&file=readme.md)
<!--- header table --->
<table>
<tr>     
  <td style="text-align: center">
    <a href="https://github.com/statmike/gcp-mlops/blob/main/Framework%20Workflows/readme.md">
      <img width="32px" src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/github.svg" alt="GitHub logo">
      <br>View on<br>GitHub
    </a>
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <b>Share On: </b> 
    <a href="https://www.linkedin.com/sharing/share-offsite/?url=https://github.com/statmike/gcp-mlops/blob/main/Framework%2520Workflows/readme.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/linkedin.svg" alt="Linkedin Logo" width="20px"></a> 
    <a href="https://reddit.com/submit?url=https://github.com/statmike/gcp-mlops/blob/main/Framework%2520Workflows/readme.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/reddit.png" alt="Reddit Logo" width="20px"></a> 
    <a href="https://bsky.app/intent/compose?text=https://github.com/statmike/gcp-mlops/blob/main/Framework%2520Workflows/readme.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/bluesky.svg" alt="BlueSky Logo" width="20px"></a> 
    <a href="https://twitter.com/intent/tweet?url=https://github.com/statmike/gcp-mlops/blob/main/Framework%2520Workflows/readme.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/x.svg" alt="X (Twitter) Logo" width="20px"></a> 
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <b>Connect With Author On: </b> 
    <a href="https://www.linkedin.com/in/statmike"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/linkedin.svg" alt="Linkedin Logo" width="20px"></a>
    <a href="https://www.github.com/statmike"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/github.svg" alt="GitHub Logo" width="20px"></a> 
    <a href="https://www.youtube.com/@statmike-channel"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/youtube.svg" alt="YouTube Logo" width="20px"></a>
    <a href="https://bsky.app/profile/statmike.bsky.social"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/bluesky.svg" alt="BlueSky Logo" width="20px"></a> 
    <a href="https://x.com/statmike"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/x.svg" alt="X (Twitter) Logo" width="20px"></a>
  </td>
</tr>
<tr>
  <td style="text-align: right">
    <a href="https://raw.githubusercontent.com/statmike/gcp-mlops/main/Framework%20Workflows/readme.md"><img src="https://raw.githubusercontent.com/statmike/gcp-mlops/main/architectures/headers/icons/download.svg" alt="Download icon" width="20px"></a> <a href="https://raw.githubusercontent.com/statmike/gcp-mlops/main/Framework%20Workflows/readme.md">Download File</a> <i>(right-click and "Save As")</i>
  </td>
</tr>
</table><br/><br/>

---
# Framework Workflows
> You are here: `gcp-mlops/Framework Workflows/readme.md` ([⬅ Back to Repository Front Door](../readme.md))

Using the tools from [MLOps](../MLOps/readme.md) and [Data + AI](../data+ai/readme.md) in end-to-end workflows for specific ML frameworks (**39 notebooks**). For each framework, the workflows focus on a common task so you can compare them directly:
> Training and serving models on shared data stored in Google BigQuery

Information and cloud resources are intentionally shared across frameworks:
- **Shared Source Data**: Every framework trains on the same source data in BigQuery with consistent preparation and splits.
- **Shared Vertex AI Resources**:
  - **Vertex AI Model Registry** — Models register as versions under a shared registry structure.
  - **Vertex AI Feature Store** — Online feature serving is shared across framework examples.
  - **Vertex AI Prediction Endpoints** — Endpoints follow the same deployment and cleanup lifecycle.

```mermaid
%%{init: {'flowchart': {'wrappingWidth': 650, 'nodeSpacing': 25, 'rankSpacing': 30}}}%%
flowchart TD
    BQ["Shared Source Data in Google BigQuery"]
    BQ --> Train["Framework-Specific Training & Packaging (39 Notebooks)<br/>PyTorch (20) · R on GCP (6) · Vertex AI AutoML (6)<br/>Keras 3 Multi-Backend (3) · CatBoost (3) · Flax/JAX (1)"]
    Train --> Reg["Shared Vertex AI Model Registry & Feature Store"]
    Reg --> Serve["Cross-Service Model Serving & Inference<br/>Vertex AI Endpoints · BigQuery ML (ONNX/TF) · AlloyDB · Spanner<br/>Dataflow RunInference · TorchServe · Custom FastAPI Containers"]

    classDef top fill:#1a73e8,stroke:#0b57d0,stroke-width:2px,color:#ffffff
    classDef stage fill:#e8f0fe,stroke:#1a73e8,stroke-width:1.5px,color:#174ea6
    classDef detail fill:#f1f5f9,stroke:#475569,stroke-width:1.5px,color:#0f172a
    class BQ top
    class Train,Serve stage
    class Reg detail
```

## Frameworks

- **[PyTorch (`PyTorch/`)](./PyTorch/readme.md)** (20 notebooks) — Custom autoencoder training plus 19 serving patterns spanning Vertex AI Endpoints, BigQuery ML (via ONNX), AlloyDB, Spanner, Dataflow `RunInference`, TorchServe, and load testing.
- **[R on Google Cloud (`R/`)](./R/readme.md)** (6 notebooks) — One shared Generalized Linear Model (GLM) workflow executed across four GCP runtimes (interactive notebook, Vertex AI Custom Training container, Dataproc Serverless SparkR, and Vertex AI Pipelines), plus high-throughput BigQuery-to-R reads via Apache Iceberg/`arrow` and custom R model serving.
- **[Vertex AI AutoML (`Vertex AI AutoML/`)](./Vertex%20AI%20AutoML/readme.md)** (6 notebooks) — Tabular classification, neural architecture inspection, TabNet, Wide & Deep, and feature engineering.
- **[Keras (`Keras/`)](./Keras/readme.md)** (3 notebooks) — Multi-backend Keras 3 running on JAX and TensorFlow backends, autoencoder training, and BigQuery serving.
- **[CatBoost (`CatBoost/`)](./CatBoost/readme.md)** (3 notebooks) — Gradient boosted trees served via custom FastAPI containers with Feature Store integration.
- **[Flax / JAX (`Flax/`)](./Flax/readme.md)** (1 notebook) — Neural network training and serving with JAX and Flax.
- **[BigQuery ML (`BQML/`)](./BQML/readme.md)** — Connects this shared dataset to BigQuery ML (for the full 62-notebook BigQuery ML curriculum, see [`data+ai/bq-ml/`](../data+ai/bq-ml/README.md)).

### Additional Foundational Framework Series at Repo Root
- **[`04 - scikit-learn`](../04%20-%20scikit-learn/readme.md)** (12 notebooks) & **[`05 - TensorFlow`](../05%20-%20TensorFlow/readme.md)** (28 notebooks) — Custom training jobs (script, source distribution, custom container), hyperparameter tuning, Vertex AI Pipelines, explainability, and serving.

