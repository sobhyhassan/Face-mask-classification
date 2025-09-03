# 😷 Face Mask Detection – CNN Project  acc(~97%)

## 🔍 Overview  
A deep learning project to detect **whether a person is wearing a face mask or not** using **Convolutional Neural Networks (CNNs)**.  
The goal is to build a reliable, real-time model that can assist in public safety and monitoring systems.  

---

## 📂 Dataset  
- Images are divided into two categories:  
  - 🟢 `with_mask`  
  - 🔴 `without_mask`  
- **Preprocessing:**  
  - Resize to **128x128**  
  - Normalize pixel values `[0,1]`  
  - Encode labels → `1 = with_mask`, `0 = without_mask`  
- **Split:** 80% train / 20% test  

---

## 🛠 Model Workflow  
1. **Data Augmentation** → rotation, zoom, flip, shift (to make model robust).  
2. **CNN Architecture** → 3 convolution blocks + dense layers + dropout.  
3. **Training** → optimizer = Adam, loss = Binary Crossentropy.  
4. **Evaluation** → accuracy, precision, recall, F1-score, confusion matrix.  

---

## 🧠 Model Architecture  
Conv2D(32) → MaxPooling2D
Conv2D(64) → MaxPooling2D
Conv2D(128) → MaxPooling2D
Flatten → Dense(128, relu) → Dropout(0.5) → Dense(1, sigmoid)


---

## 📊 Performance  

- **Accuracy:** ~97%  
- **Precision / Recall / F1:** ~0.96 – 0.97  
- **Confusion Matrix:** few misclassifications (~3%).  

### Confusion Matrix  
<img width="510" height="393" alt="959accb8-a9e4-4486-8665-3b22d59591bd" src="https://github.com/user-attachments/assets/91646a3a-00f7-4ec0-8bc1-1ac27fc6a529" />


### Training Curves  
<img width="1018" height="470" alt="119a0bc5-027d-4497-a202-acc0deb220bf" src="https://github.com/user-attachments/assets/3aaf059d-01da-48bc-a8f4-e6ffbd7be077" />

---

## 🚀 Deployment  

### 🔹 Streamlit App  
The trained model was deployed using **Streamlit**:  
- User uploads an image.  
- The app preprocesses it (resize → normalize → convert to array).  
- Model predicts: **With Mask 😷** or **Without Mask ❌**.  
- Prediction is displayed on the interface.  

## ✅ Key Takeaways
- CNN model performs very well on mask detection (~97%).
- Robustness achieved with augmentation + dropout.
- Streamlit deployment makes the model easy to demo and test in real time.
- Ready for integration in web apps, mobile apps, or security systems.
