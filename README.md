# Setup

**Setup** is a lightweight RPA bot orchestrator written in Python. It allows you to execute multiple Python-based RPA bots dynamically by reading configuration and input variables from an Excel file.

## 🚀 Overview

This application automates the execution of several RPA bots based on instructions provided in an Excel file. The file contains:

- **Input variables** (e.g., URLs, credentials, parameters)
- **Paths to sub-bot entry points** (e.g., `.main` files)

Each bot is executed in sequence using the specified variables, enabling centralized orchestration without a full-scale RPA platform.

---

## 📁 Folder Structure

