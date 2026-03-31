#  Email Spam Detection (Mini Project)

##  Student Details
- **Name:** [Your Name]  
- **Course:** FY BTech / BCA  
- **Subject:** Fundamentals of AI & ML  

---

##  Project Overview
This project is a simple implementation of an **Email Spam Detection system** using basic Machine Learning concepts.

The main goal is to classify messages as:
- **Spam** (unwanted / promotional messages)
- **Not Spam** (normal messages)

I built this project to understand how machines can learn patterns from text data and make predictions.

---

##  Objectives
- Learn basics of Machine Learning  
- Understand how text data is processed  
- Build a simple spam classifier  
- Combine rule-based logic with ML model  

---

##  Approach Used

This project uses **two methods together**:

### 1. Rule-Based Method
I created a simple function that checks for common spam words like:
- "win"
- "free"
- "money"
- "prize"

If these words are found, the message is likely spam.

---

### 2. Machine Learning Model
- Used **Naive Bayes Algorithm**
- Converted text into numbers using **CountVectorizer**
- Trained the model on a small dataset

---

###  Final Decision
Both results are combined:
> If either rule-based or ML predicts spam → Final output = Spam

---

##  Dataset
The dataset is manually created based on common real-life messages.

Example:

| Message | Label |
|--------|------|
| Win a free phone now | Spam |
| Are you coming to class? | Not Spam |
| Earn money online | Spam |

---

##  Technologies Used
- Python  
- Pandas  
- Scikit-learn  

---

## ▶️ How to Run the Project

1. Install required libraries:
