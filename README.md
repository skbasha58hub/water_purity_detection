# 💧 Smart Water Quality Analyzer using Image Processing

## 📌 Project Overview
This project is a **computer vision–based water quality analyzer** that uses a webcam and image processing techniques to detect suspended particles in water.  
By analyzing the number of impurities, the system determines the **potability of water**, evaluates **disease risk**, and recommends suitable **purification methods** in real time.

---

## 🚀 Features
- 📷 **Live Camera Feed** – Captures and analyzes water samples in real time  
- 🔍 **Particle Detection** – Detects and counts impurities using OpenCV contour detection  
- 🎚 **Threshold Adjustment** – Adjustable slider to fine-tune detection sensitivity  
- ✅ **Potability Prediction** – Predicts whether the water is safe or unsafe for drinking  
- ⚠ **Risk Level Analysis** – Classifies contamination as **Low, Moderate, or High**  
- 💡 **Purification Suggestions** – Suggests methods like **Boiling, Chlorination, UV, or RO**  
- 🖼 **Image Capture** – Saves water sample snapshots for record keeping  
- 🖥 **Visual Feedback** – Highlights impurities and displays live results on video feed  

---

## 🛠️ Technologies Used
- **Python 3.x**
- **OpenCV** – Computer vision & image processing  
- **NumPy** – Numerical computation  
- **SciPy (ndimage)** – Object labeling & size filtering  

---

## ⚙️ Installation & Setup

1. **Clone this repository**
   git clone https:https://github.com/skbasha58hub/water_purity_detection.git
   cd water-quality-analyzer
   
🎮 Usage
Run the program → Webcam will open showing live feed
Adjust the Threshold slider to optimize impurity detection
Press c → Capture & save an image (water_sample.png)
Press q → Quit the program

📊 Working Principle
Convert water sample image to grayscale
Apply Gaussian Blur to reduce noise
Use binary thresholding to detect suspended particles
Count impurities using connected component labeling

Classify water quality:
≤ 10 particles → ✅ Potable (Low Risk)
11–50 particles → ⚠ Moderate Risk (Basic purification needed)
> 50 particles → ❌ Unsafe (Advanced purification required)

💡 Example Output
Particles Detected: 23
Risk Level: Moderate risk
Suggested Purification: Boiling or Chlorination

📌 Applications
Household water purity monitoring
Portable water testing in rural/remote areas
Educational tool in Environmental Science & Computer Vision
Preliminary testing in research laboratories

⚠ Limitations
Cannot detect chemical contaminants (e.g., arsenic, fluoride)
Accuracy depends on lighting & camera quality
Designed primarily for suspended particle detection

🔮 Future Scope
Integration with IoT sensors for chemical quality detection
Web dashboard for remote monitoring & reporting
Use of machine learning models for higher accuracy
Mobile app for real-time water analysis
