# 🧠 Alzheimer's Disease Prediction Using Machine Learning

This project explores machine learning models to predict Alzheimer's Disease progression using structural MRI data and cognitive assessment scores. Neuroimaging biomarkers were extracted using FastSurfer from ADNI (Alzheimer’s Disease Neuroimaging Initiative) MRI scans, and predictive models were developed and evaluated based on these features.

## 📚 Project Summary

- **Data Source:** Alzheimer's Disease Neuroimaging Initiative (ADNI)
- **Neuroimaging Processing Tool:** [FastSurfer](https://github.com/Deep-MI/FastSurfer)
- **Machine Learning Models:** Random Forest, Gradient Boosting
- **Objective:** Classify stages of Alzheimer's Disease using MRI-based and cognitive features

## 🧠 Methodology

1. **Data Preprocessing**
   - Structural MRI scans were preprocessed and segmented using FastSurfer.
   - Extracted features include cortical thickness, surface area, and subcortical volumes.

2. **Feature Engineering**
   - Combined imaging biomarkers with cognitive assessment scores.

3. **Model Training**
   - Trained classification models: Random Forest, Gradient Boosting
   - Evaluated performance using metrics like MAE, accuracy, and ROC-AUC.

## 📊 Results

- **Best Model:** XGBoost
- **Mean Absolute Error (MAE):** 27.38 €/MWh (if applicable to price prediction; update this for AD metrics)
- Accuracy and other metrics: *(Add once evaluated)*

## 💡 Key Takeaways

- Neuroimaging features provide significant insight into Alzheimer's progression.
- Combining MRI and cognitive data boosts predictive performance.
- FastSurfer enables efficient and accurate extraction of brain imaging biomarkers.

## 🛠 Technologies Used

- Python, NumPy, Pandas
- Scikit-learn, XGBoost, Matplotlib
- FastSurfer (for MRI segmentation)
- Jupyter Notebook

## 📂 Folder Structure

