
```markdown
# 🔐 Data Masking for Privacy-Preserving Data Analytics

Data masking is a privacy technique used to protect sensitive information by replacing original data with fictional but realistic data. This process ensures data privacy while allowing datasets to be shared for data analytics and machine learning without compromising confidential information. In this project, we have implemented a simple data masking tool that allows users to upload a dataset, select attributes to mask, and download the masked version for secure analytics.
---

## 🚀 Features

- Upload CSV datasets via a web interface.
- Mask sensitive fields like name, email, phone, etc.
- Choose between:
  - 🔁 Random character substitution
  - 🔐 SHA-256 hashing
- Download privacy-preserved datasets in one click.
- Simple, intuitive interface using **Streamlit**.

---

## 📁 Dataset Info

- **Sample Dataset**: `sample.csv`
- **Size**: ~25 KB
- **Attributes**:
  - `Name`
  - `Email`
  - `Phone Number`
  - `City`
  - `Salary`

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Yash-Raj-96/Data-Masking.git
   cd Data-Masking
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run app.py
   ```

---

## 📊 Sample Data

### Before Masking
| Name  | Email           | Phone Number | City        | Salary |
|-------|------------------|--------------|-------------|--------|
| Alice | alice@gmail.com  | 9876543210   | New York    | 70000  |
| Bob   | bob@gmail.com    | 8765432109   | Los Angeles | 85000  |

### After Masking (Random Characters)
| Name   | Email      | Phone Number | City     | Salary |
|--------|------------|--------------|----------|--------|
| k98kK2 | c34FG56n   | M9shd01L     | rTzW0PL  | 70000  |
| H6kP9r | Tm65BsaF   | 29asfDd      | bFgTd1P  | 85000  |

---

## 🖼️ Screenshots

> Add these screenshots in the `screenshots/` folder and update paths accordingly.

| Step                          | Preview |
|-------------------------------|---------|
| 📤 Upload Dataset             | ![Upload](screenshots/upload.png) |
| ✅ Select Masking Options     | ![Select](screenshots/select_columns.png) |
| 🛡️ View Masked Output         | ![Masked](screenshots/masked_output.png) |

---

## 🛠️ How to Use

1. Launch the app using:
   ```bash
   streamlit run app.py
   ```
2. Upload your CSV file (e.g., `sample.csv`).
3. Select the fields you want to mask.
4. Choose the masking method.
5. Click **"Mask Data"** to generate output.
6. Download the masked dataset from `masked_data/masked_output.csv`.

---

## 📁 Project Structure

```
Data-Masking/
│
├── app.py                    # Streamlit app
├── masking.py                # Masking functions
├── sample.csv                # Sample dataset (optional)
├── requirements.txt          # Dependencies
├── masked_data/              # Output folder for masked files
├── screenshots/              # Screenshots for README (optional)
└── README.md                 # Project documentation
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 💡 Author

Made with ❤️ by [Yash Raj](https://github.com/Yash-Raj-96)

```
