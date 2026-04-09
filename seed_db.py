import sqlite3
import os

def seed():
    conn = sqlite3.connect("cms.db")
    c = conn.cursor()

    # Clear existing to avoid duplicates if re-run
    c.execute("DELETE FROM jobs")
    c.execute("DELETE FROM events")
    c.execute("DELETE FROM resources")

    # Mock Jobs
    jobs = [
        ("Junior Frontend Developer", "CareerbyAL Tech", "Remote", "Join our fast-growing team to build modern React applications. Knowledge of CSS and JavaScript is a must.", "React, CSS, JavaScript", "2026-05-15"),
        ("Python Backend Intern", "DataFlow Solutions", "New York", "Work on scalable Flask APIs and database management. Great opportunity for students.", "Python, Flask, SQL", "2026-06-01"),
        ("UI/UX Design Specialist", "Creative Studio", "London", "Help us design premium user experiences for global clients. Portfolio required.", "Figma, Adobe XD", "2026-05-20"),
        ("Data Analyst", "FinCorp", "Singapore", "Analyze market trends and provide actionable insights using Python and Tableau.", "Python, Tableau, R", "2026-07-10")
    ]
    c.executemany("INSERT INTO jobs (title, company, location, description, skills_required, deadline) VALUES (?,?,?,?,?,?)", jobs)

    # Mock Events
    events = [
        ("Resume Building Workshop", "2026-04-20", "10:00 AM", "Learn how to optimize your CV for ATS and get a 90+ score on CareerbyAL."),
        ("Interview Preparation Masterclass", "2026-04-25", "02:00 PM", "Master the STAR method and common behavioral interview questions with our experts."),
        ("Tech Career Fair 2026", "2026-05-05", "11:00 AM", "Connect with top recruiters from 50+ tech companies live online.")
    ]
    c.executemany("INSERT INTO events (title, date, time, description) VALUES (?,?,?,?)", events)

    # Mock Resources
    resources = [
        ("Guide to Modern Resume Layouts", "Resume Tips", "A comprehensive guide to structured resumes.", "https://example.com/resume-guide"),
        ("Top 50 Interview Questions", "Interview Prep", "Commonly asked tech interview questions.", "https://example.com/interview-prep"),
        ("Consult with AL", "Counseling", "Official website for personalized career mentoring.", "http://127.0.0.1:5000/appointments")
    ]
    c.executemany("INSERT INTO resources (title, category, content, link) VALUES (?,?,?,?)", resources)

    conn.commit()
    conn.close()
    print("Database seeded successfully with CareerbyAL mocks!")

if __name__ == "__main__":
    seed()
