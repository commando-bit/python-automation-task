# 📊 Automated Excel Data Cleaning & Sanitization Engine

An enterprise-ready Python automation tool designed to clean, deduplicate, format, and structure raw/messy Excel spreadsheets automatically.

## 🎯 What Problem This Solves
Manual data cleaning in Excel takes hours and is prone to human error. This automated pipeline:
- Eliminates manual sorting & duplication removal.
- Standardizes messy text formatting across thousands of rows instantly.
- Prepares accurate datasets ready for analytics or business reporting.

## ✨ Key Features & Capabilities
- **Duplicate Removal:** Automatically detects and strips duplicate rows.
- **Text Standardization:** Strips leading/trailing whitespaces and standardizes column names.
- **Null Value Handling:** Safely replaces missing cells with defined default fallbacks.
- **Automated Export:** Generates clean, ready-to-use output files (`.xlsx`) instantly.

## 🛠️ Tech Stack & Dependencies
- **Language:** Python 3.x
- **Libraries:** Pandas, OpenPyXL

## 💻 Quick Start & Usage

1. **Install required libraries:**
   ```bash
   pip install pandas openpyxl
