# 🧠 Alzheimer's Disease Stage Classification with Machine Learning

## 📌 Overview
This project uses machine learning to classify **stages of Alzheimer's disease** — not just whether someone has Alzheimer’s or not, but **which stage they are in**:  
- **Cognitively Normal (CN)**  
- **Early Mild Cognitive Impairment (EMCI)**  
- **Late Mild Cognitive Impairment (LMCI)**  
- **Alzheimer’s Disease (AD)**  

By focusing on **early and subtle transitions**, the model aims to support earlier detection and intervention — potentially helping patients get the care they need before it’s too late.

---

## 🎯 Purpose
Most machine learning models focus on binary classification (AD vs. CN), but **real-life diagnosis is more nuanced**.  
This project tackles that complexity by training a model to recognize **intermediate stages** like EMCI and LMCI.

### Why this matters:
- **Early detection = earlier treatment.**
- Families and caregivers can **prepare and plan.**
- Doctors can make **more informed decisions.**
- Research studies and clinical trials need better stage prediction.

---

## 🧪 Approach

- **Dataset:** ADNI dataset
- **Preprocessing:** Feature selection, normalization, handling class imbalance
- **Model:** XGBoost and Random Forest 
- **Evaluation:** Accuracy, confusion matrix, precision/recall per stage

---
---

## 📈 Results & Findings

- Accuracy: 87%
- F1-Score (AD stage): 0.81
- Most misclassified: EMCI and LMCI (model struggled with borderline cases)
- Feature importance highlights hippocampal volume, MMSE score, and cortical thickness as top predictors.

## 📊 Visualizations

- Confusion matrix and feature importance chart included in the notebook
- [Optional: Paste image here or link to `visuals/` folder]

---

## 🧠 Next Steps

- Try ensemble methods or deep learning (e.g., CNNs on MRI scans)
- Explore longitudinal data over time
- Integrate cognitive test scores and imaging features
- Apply SHAP for better interpretability

---

## 📂 How to Run

```bash
git clone https://github.com/christylaminated/alzheimers-stage-classifier.git
cd alzheimers-stage-classifier
pip install -r requirements.txt
jupyter notebook model.ipynb

## 📒 Notebook

All analysis, modeling, and evaluation steps are documented in `model.ipynb`.

## 🧪 Sample Data

A subset of anonymized ADNI-like data is provided in `data/sample_adni_subset.csv` for testing and reproducibility.

## 👤 Contributions

This project was completed individually as part of my exploration into AI for neuroscience and healthcare.


