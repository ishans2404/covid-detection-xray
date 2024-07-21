# CovidVision: Advanced COVID-19 Detection from Lung X-rays with Deep Learning

## Project Overview

The "CovidVision: Advanced COVID-19 Detection from Lung X-rays with Deep Learning" project aims to utilize deep learning algorithms to analyze lung X-ray images for signs of COVID-19 infection. This system provides accurate and rapid diagnosis to aid in the early detection and containment of the virus.

## Objectives

- Develop and deploy an AI system to detect COVID-19 from lung X-rays.
- Integrate the system with hospital systems for expedited diagnosis.
- Deploy in rural clinics for enhanced screening.
- Utilize by public health authorities to monitor trends and allocate resources for targeted interventions.

## Project Initialization and Planning

### Define Problem Statement

*Problem Description:* The need for rapid, accurate COVID-19 diagnosis, especially in overwhelmed hospitals and rural areas with limited access to expert radiologists.

*Impact:* Solving this problem will lead to faster diagnosis, improved patient management, containment of the virus in underserved areas, and informed public health interventions.

### Initial Project Planning

*Plan:* Detailed planning of project phases, timelines, resource allocation, and risk management.

### Project Proposal (Proposed Solution)

*Approach:* Utilize deep learning algorithms and vast datasets to analyze lung X-ray images for signs of COVID-19 infection. Implement the system in hospitals, rural clinics, and public health monitoring.

*Key Features:*
- Rapid and correct analysis of lung X-rays.
- Integration with existing hospital systems for efficient triage.
- Accessibility for rural clinics with limited radiology ability.
- Real-time data analysis for public health monitoring and resource allocation.

## Data Collection and Preprocessing

### Data Collection Plan and Raw Data Sources Identified

*Data Source:* COVID-19 Radiography Database (available on Kaggle)  
*URL:* [COVID-19 Radiography Database](https://www.kaggle.com/datasets/tawsifurrahman/covid19-radiography-database)  
*Format:* Image  
*Size:* 806.84 MB  
*Access Permissions:* Public

### Data Quality Report

*Data Quality Issue:* Class imbalance with one class having substantially more data than the other, which may lead to increased variance and potential bias in the model.  
*Severity:* Moderate  
*Resolution Plan:* Under Sampling

### Data Preprocessing

*Steps:*
- Visualization of class distribution
- Resizing images to 224x224 pixels
- Normalizing pixel values between 0 and 255
- Label encoding the classes (COVID, normal)
- Reshaping the processed images and class labels into NumPy arrays for classification

## Model Development

### Model Selection Report

*Model:* Convolutional Neural Network (CNN) leveraging the VGG19 architecture, pre-trained on the ImageNet dataset.  
*Description:* The model classifies chest X-ray images into two categories: COVID-19 positive and normal, utilizing the powerful feature extraction capabilities of a deep network trained on a large and diverse dataset, which is fine-tuned for this specific task.

### Tuning Documentation

*Model 1 Tuned Hyperparameters:*
1. *Epochs:* 40
2. *Initial Learning Rate:* 1e-5
3. *Decay Steps:* 10
4. *Decay Rate:* 1.0
5. *Batch Size:* 32
6. *Patience:* 5

### Results

Comparison of performance metrics before and after tuning to justify the final model selection.

## Final Model Selection Justification

*Final Model:* VGG19-based CNN model  
*Reasoning:* Chosen for its strong feature extraction capabilities, effective use of transfer learning, and balanced approach to handling the dataset. Its high accuracy on test data and good performance on training and validation data validated its effectiveness in classifying chest X-ray images into COVID-19 positive and normal categories.

## Output Screenshots

Screenshots showcasing the final model's predictions and performance metrics.

## Advantages & Disadvantages

*Advantages:*
- Rapid and accurate COVID-19 detection
- Effective use of transfer learning
- Integration with existing healthcare systems

*Disadvantages:*
- Dependency on high-quality images
- Potential biases due to class imbalance

## Conclusion

The project successfully developed an AI system for rapid and accurate COVID-19 detection from lung X-rays, aiding in early diagnosis and containment of the virus.

## Future Scope

- Expansion to detect other respiratory diseases
- Integration with more healthcare systems
- Continuous improvement with more diverse datasets

---

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ishans2404/covid-detection-xray/blob/2819ac2befa06be91d51063a51baedac90d8914e/LICENSE) file for details.
