# 🚀 Zenith

**Zenith** is a **local-first, privacy-focused knowledge assistant** that integrates Retrieval-Augmented Generation (RAG), dual-embedding vector search, graph-based knowledge expansion, and multi-modal vision — all running entirely on your own hardware, with Telegram as the interface.

---

## ✨ Features

### 🔍 Dual-Embedding Retrieval

* Combines:

  * `all-MiniLM-L6-v2`
  * `intfloat/e5-small-v2`
* Uses **Reciprocal Rank Fusion (RRF)** for better semantic coverage.

### 🎯 Cross-Encoder Reranking

* Uses `ms-marco-MiniLM-L-6-v2`
* Improves precision of retrieved results.

### 🧠 Graph Knowledge Expansion

* Extracts entities from documents
* Builds a knowledge graph
* Expands queries using **2-hop relationships**

### 🖼️ Multi-Modal Vision

* Image captioning via Hugging Face pipelines
* CPU-based inference (no GPU needed)
* Extracts tags and links them to knowledge base

### ⚡ Semantic Caching

* Vector-based caching using `sqlite-vec`
* Features:

  * LRU eviction
  * TTL-based expiry
* Accelerates repeated queries

### 🛡️ Resilience

* Circuit breakers
* Exponential retries
* Dedicated thread pools (avoids asyncio blocking)
* Graceful shutdown handling

### 📊 Observability

* Built-in Prometheus metrics:

  * Request count
  * Latency
  * Circuit states
  * Queue lengths

---

## 🖥️ Hardware Requirements

| Component | Minimum  | Recommended                |
| --------- | -------- | -------------------------- |
| GPU       | Optional | NVIDIA GPU (≥ 3.5 GB VRAM) |
| CPU       | 4-core   | Modern multi-core          |
| RAM       | 8 GB     | 16 GB                      |

---

## ⚡ Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/zenith.git
cd zenith
```

### 2. Create Virtual Environment (Recommended: `uv`)

```bash
uv venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure Telegram Bot

```bash
export TELEGRAM_TOKEN="your_telegram_bot_token"
```

---

### 5. Download Models

```bash
huggingface-cli download microsoft/Phi-3.5-mini-instruct-gguf \
  Phi-3.5-mini-instruct-Q4_K_M.gguf \
  --local-dir ./models
```

---

## 🧠 LLM Server Setup (Dual-Server Architecture)

### 🔹 Server 1: Phi-3.5 (Primary Generator)

```bash
python -m llama_cpp.server \
  --model ./models/Phi-3.5-mini-instruct-Q4_K_M.gguf \
  --n_gpu_layers 20 \
  --n_ctx 4096 \
  --chat_format chatml \
  --port 8000 \
  --host 127.0.0.1
```

### 🔹 Server 2: Mistral-7B (Entity Extraction - CPU Only)

```bash
python -m llama_cpp.server \
  --model ./models/Mistral-7B-Instruct-v0.3.Q4_K_M.gguf \
  --n_gpu_layers 0 \
  --n_ctx 4096 \
  --chat_format mistral-instruct \
  --port 8001 \
  --host 127.0.0.1
```

---

### 7. Run the Bot

```bash
python -m src.main
```

---

### 8. Start Using Zenith (Telegram)

* 📄 Upload PDFs → Indexed into local DB
* 🖼️ Send images → Captioning + entity extraction
* 💬 Ask questions → RAG + Graph expansion + semantic routing

---

## ⚙️ Configuration

Located in:

```
src/config.py
```

Key settings:

* `CACHE_TTL_SECONDS`
* `CACHE_MAX_ENTRIES`
* Thread pool limits
* LLM server endpoints (8000 / 8001)

---

## 📁 Project Structure

```
zenith/
├── data/               # PDFs & processed markdown
├── local_db/           # Per-user SQLite databases
├── models/             # GGUF models
├── src/
│   ├── database/       # DB client, schema, migrations
│   ├── engine/         # Core AI pipeline
│   ├── monitoring/     # Prometheus metrics
│   ├── utils/          # Circuit breakers, workers
│   └── main.py         # Telegram bot entry
├── requirements.txt
└── README.md
```

---

## 🛠️ Troubleshooting


### ❗ CUDA Out of Memory

✔ Fix:

* Reduce:

```bash
--n_gpu_layers
```

* Ensure vision runs on CPU:

```python
device = -1
```

---

## 📜 License

Licensed under the **MIT License**.
See `LICENSE` file for details.

---

## 💡 Summary

Zenith is essentially:

> A **fully local, production-grade AI knowledge system** combining RAG, graph intelligence, and multi-modal understanding — without relying on external APIs.


