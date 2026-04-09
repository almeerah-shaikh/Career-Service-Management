# CareerbyAL: Premium AI-Powered Career Management System

## 🌟 Overview
**CareerbyAL** is a state-of-the-art, 3D-interactive professional growth platform. It leverages advanced AI (Google Gemini) to provide students and professionals with high-tier career services, including deep resume audits, automated professional CV generation, and smart internship matching.

---

## 🚀 Key Features

### 1. **Pro AI CV Checker (Deep Audit)**
- **Intelligent Scoring**: Analyzes your resume text or uploaded PDF/DOCX files.
- **3-Pillar Feedback**:
    - **High Five (Appreciation)**: AI-driven positive reinforcement of your current strengths.
    - **Room for Growth (Mistakes)**: Detailed list of specific errors (e.g., weak action verbs, missing quantification).
    - **The Strategy**: Step-by-step actionable plan to reach a 100/100 score.
- **Compatibility Meter**: Real-time visual representation of your job-readiness.

### 2. **Premium AI CV Builder**
- **Automated Restructuring**: Uses Gemini AI to rewrite your "trash" text into high-impact professional content.
- **Sleek DOCX Export**: One-click download of a business-standard Word document featuring:
    - Bold headers and horizontal section dividers.
    - Automated bullet points for experience.
    - Modern, centered contact headers.

### 3. **Pro Career Mentor (AI Chatbot)**
- **Context-Aware Memory**: Remembers your previous questions and goals within a session.
- **Interactive Quick Replies**: One-tap buttons for Resume Tips, Interview Prep, and Trending Jobs.
- **Deep Persona**: Acts as a Senior Career Consultant, guiding you to specific tools on the platform.

### 4. **Smart Job & Internship Matching**
- **Skill-Based Recommendations**: Automatically matches your profile skills with the database of latest job openings.
- **One-Click Apply**: Seamless application tracking system.

### 5. **Career Counseling Hub**
- **Appointment Booking**: Request one-on-one sessions with professional counselors.
- **Virtual Meeting Links**: Access direct Zoom or Google Meet links provided by your mentor.

---

## 🎨 Visual Aesthetics & UI
- **3D Depth & Motion**:
    - **Interactive Tilt**: Cards and hero elements rotate in 3D space based on mouse movement.
    - **Parallax Background**: Floating mesh gradients and moving 3D books create a layered, modern feel.
- **Glassmorphism**: Sleek, transparent UI components with frosted-glass effects.
- **Tactile Interaction**: Buttons with 3D press effects and smooth transitions.

---

## 🛠️ Technology Stack
- **Backend**: Python (Flask Framework)
- **Database**: SQLite3
- **AI Intelligence**: Google Gemini Pro (Generative AI)
- **Document Processing**: `python-docx` (Word), `pypdf` (PDF Parsing)
- **Frontend**: HTML5, Vanilla CSS3 (3D Transforms), JavaScript ES6

---

## 📂 Project Structure
- `app.py`: The heart of the application handling all AI logic, routes, and database operations.
- `templates/`: HTML5 Jinja2 templates for all pages (Home, CV Checker, Chatbot, etc.).
- `static/`:
    - `style.css`: Modern styling including 3D animations and glassmorphism.
    - `script.js`: Interactive 3D mouse-tracking and UI logic.
    - `uploads/`: Storage for user resumes and profile pictures.
- `cms.db`: SQLite database storing users, jobs, appointments, and events.

---

## 🔑 Setup & Running
1. **API Keys**: Ensure `GEMINI_API_KEY` is set in your environment variables to enable the AI features.
2. **Installation**:
   ```bash
   pip install flask pypdf python-docx google-generativeai
   ```
3. **Execution**:
   ```bash
   python app.py
   ```
4. **Access**:
   - Web: `http://127.0.0.1:5000`
   - Admin: `http://127.0.0.1:5000/admin_login` (Admin/Admin123)

---
Images:
<img width="1296" height="644" alt="image" src="https://github.com/user-attachments/assets/1ecc980b-f2ad-4219-8390-659cf9e11072" />
<img width="1283" height="649" alt="image" src="https://github.com/user-attachments/assets/2d4ae69a-3226-4065-af45-ee7acbc0bf9a" />
<img width="1339" height="648" alt="image" src="https://github.com/user-attachments/assets/b74719e5-4fa5-4f12-8b70-41c6a5b863b3" />



