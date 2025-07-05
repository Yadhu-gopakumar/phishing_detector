# 🔐 Phishing Detector Chrome Extension

This project is a Chrome extension that detects phishing websites using a machine learning model served via a Flask backend API. When a user visits a web page, the extension checks if the site is phishing, and if so, blocks access and shows a warning screen.

---

## 📌 Features

- Automatically checks all visited websites for phishing
- Uses a locally hosted Flask API with a trained ML model
- Redirects to a warning page if phishing is detected
- Simple popup UI for manual checking (optional)
- Clean and responsive UI for the warning page

---

## 🛠️ Technologies Used

- Chrome Extension (Manifest V3)
- Flask (Python Backend)
- Scikit-learn (ML Model)
- HTML, CSS, JavaScript

---

## 🗂️ Project Structure

- **extension/**: Contains all Chrome extension files (manifest, popup, background, blocked page)
- **server/**: Contains the Flask app and machine learning model

---

## 🚀 How It Works

1. User loads a webpage
2. Chrome extension sends the URL to the Flask API
3. The backend predicts whether it's phishing using the trained model
4. If phishing is detected, the tab is automatically redirected to a local warning screen

---

## 📋 Permissions Required

- Tab access
- Host access for all URLs
- Notifications (optional)

---

## 📦 How to Use

1. Train your phishing model and run the Flask server
2. Load the Chrome extension via `chrome://extensions` in Developer Mode
3. Visit any website — it will be automatically checked for phishing
4. If phishing is detected, the site is blocked

---

## 🔐 Notes

- This is a local project for demo/testing purposes
- The dataset and model used should be reliable and well-structured
- In production, the Flask API should be hosted securely with HTTPS

---

## 👨‍💻 Developed By

**Yadhu Gopakumar**  
[GitHub Profile](https://github.com/Yadhu-gopakumar)

---

## 📄 License

MIT License
