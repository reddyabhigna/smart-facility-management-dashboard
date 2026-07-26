# smart-facility-management-dashboard
# 🏢 Smart Facility Management Dashboard

An interactive **Smart Facility Management Dashboard** that helps monitor and analyze facility operations through real-time visualizations and analytics. The application provides insights into energy consumption, asset management, maintenance activities, occupancy, security events, alerts, and operational costs.

---

## 📌 Project Overview

This project is designed to centralize facility management data into a single dashboard, enabling administrators and facility managers to make data-driven decisions.

The dashboard combines a modern React frontend with a Python backend to provide an intuitive user experience and efficient data processing.

---

## ✨ Features

* 🏠 Dashboard Overview
* ⚡ Energy Consumption Analytics
* 🏢 Facility Management
* 🛠 Asset Monitoring
* 🔧 Maintenance Tracking
* 👥 Occupancy Analytics
* 🔐 Security Event Monitoring
* 🚨 Alert Management
* 💰 Cost Analysis
* 📊 Interactive Charts
* 📈 KPI Cards
* 🔍 Dynamic Filters
* 📥 Export Reports

---
<img width="1176" height="892" alt="Screenshot 2026-07-22 190324" src="https://github.com/user-attachments/assets/1d700407-288c-40d0-92f5-6f365a42aa9d" />

## 🛠 Technology Stack

### Frontend

* React
* Vite
* JavaScript
* HTML5
* CSS3

### Backend

* Python
* FastAPI

### Data & Visualization

* Excel Dataset
* Plotly / Chart Library
* Pandas

---

## 📂 Project Structure

```text
smart-facility-dashboard/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── app/
│   │   ├── routers/
│   │   ├── main.py
│   │   └── data_store.py
│   └── requirements.txt
│
├── data/
│   └── Smart_Facility_Management_Dataset_200Rows.xlsx
│
└── README.md
```

---

## 📊 Dashboard Modules

### 🏠 Home Dashboard

* Facility Summary
* Overall KPIs
* Operational Overview

### ⚡ Energy Analytics

* Electricity Consumption
* HVAC Usage
* Lighting Usage
* Water Consumption
* Energy Trends

### 🏢 Facilities

* Facility Details
* Area Distribution
* Facility Comparison

### 🛠 Assets

* Asset Status
* Asset Distribution
* Installation History

### 🔧 Maintenance

* Maintenance Records
* Maintenance Status
* Maintenance Cost

### 👥 Occupancy

* Occupancy Trend
* Floor-wise Occupancy
* Room Utilization

### 🔐 Security

* Security Events
* Severity Analysis
* Event Status

### 🚨 Alerts

* Active Alerts
* Priority Levels
* Alert Status

### 💰 Cost Analytics

* Energy Cost
* Water Cost
* Maintenance Cost
* Total Operational Cost

---

## 📈 Key Performance Indicators (KPIs)

* Total Facilities
* Total Assets
* Active Assets
* Total Energy Consumption
* Water Consumption
* Maintenance Cost
* Active Alerts
* Security Events
* Occupancy Count
* Total Operational Cost

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-username/smart-facility-dashboard.git
```

### Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

### Backend Setup

```bash
cd backend

pip install -r requirements.txt

uvicorn app.main:app --reload
```

The frontend typically runs on **http://localhost:5173** and the backend on **http://localhost:8000**.

---

## 📁 Dataset

The application uses a structured Excel dataset containing multiple related tables:

* Facilities
* Energy Usage
* Assets
* Maintenance Records
* Occupancy
* Security Events
* Alerts
* Cost Reports

---

## 📸 Screenshots

Add screenshots after running the application.

```
assets/
├── dashboard.png
├── energy.png
├── facilities.png
├── maintenance.png
├── security.png
└── cost.png
```

---

## 🎯 Future Enhancements

* AI-Based Energy Consumption Prediction
* Predictive Maintenance
* Carbon Footprint Estimation
* IoT Sensor Integration
* User Authentication
* Email & SMS Notifications
* Cloud Deployment
* Mobile Responsive Design
* Report Generation (PDF/Excel)

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

