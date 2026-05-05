# PhishShield-XAI: Adversarial Phishing Detection

### Authors:
- **Muhammad Hashir**
- **Amber Khurshid**

![PhishShield Banner](phishshield_banner_1778007048455.png)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-EB6424?style=for-the-badge)](https://xgboost.ai/)

**PhishShield-XAI** is an industrial-grade, adversarial-resistant phishing detection platform. It combines high-capacity ensemble machine learning with **Explainable AI (XAI)** to provide security analysts with real-time, transparent threat intelligence.

## 🌟 Key Features

- **🛡️ Adversarial Hardening**: Trained on 1000+ stealthy, LLM-generated phishing samples designed to evade traditional filters.
- **🧠 Explainable AI (SHAP & LIME)**:
  - **SHAP**: Global feature importance (why the model thinks an email is suspicious).
  - **LIME**: Local word-level highlights (identifying specific malicious tokens in the text).
- **🚀 Real-Time API**: High-performance FastAPI backend with sub-50ms inference time.
- **🎨 Glassmorphic Dashboard**: A modern, responsive web interface for real-time email analysis.
- **📈 Adaptive Defense**: Built-in "Arms Race" simulator to measure and improve evasion resistance.

## 🏗️ Project Architecture

```mermaid
graph TD
    A[User Input] -->|Email Text| B(FastAPI Backend)
    B --> C{Feature Extraction}
    C -->|Linguistic & TF-IDF| D[Ensemble Model: RF + XGB]
    D --> E[Prediction & Confidence]
    D --> F[XAI Engine: SHAP & LIME]
    F --> G[LLM Explanation]
    G --> H[Vite Frontend Dashboard]
```

## 📂 Repository Structure

- `src/`: Core logic (API, Engine, XAI, Simulator).
- `web/`: Frontend dashboard (Vite + Vanilla JS).
- `data/`: Raw and adversarial datasets.
- `models/`: Serialized model artifacts.
- `notebooks/`: Research pipeline and pipeline documentation.
- `scripts/`: Automation for training, testing, and demos.

## 🚀 Quick Start

### 1. Setup Environment
```bash
chmod +x setup.sh run.sh
./setup.sh
```

### 2. Launch Platform
```bash
./run.sh
```

## 🧪 Testing & Verification
We have included a rigorous test suite of 16 complex scenarios (Homographs, BEC, Shortened URLs). Run it with:
```bash
./venv/bin/python scripts/rigorous_test.py
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
