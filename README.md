# 🚀 OpportunityHub

## 🎯 Student Opportunity Discovery Platform

**OpportunityHub** is a unified, intelligent student opportunity discovery platform designed to connect students with high-impact career and educational opportunities. By bringing internships, hackathons, scholarships, competitions, workshops, certifications, courses, fellowships, and jobs into a single centralized hub, OpportunityHub empowers students to discover, track, and apply for opportunities tailored specifically to their skills and aspirations.

- **Live Demo:** [https://opportunityhub-xq4i.onrender.com](https://opportunityhub-xq4i.onrender.com)
- **GitHub Repository:** [https://github.com/shubham-bahadurge/OpportunityHub](https://github.com/shubham-bahadurge/OpportunityHub)

---

## 💡 Problem Statement

College and university students face a fractured opportunity landscape:
- **Information Fragmentation:** Opportunities are scattered across dozens of disparate job boards, company career portals, university mailing lists, Discord channels, and social media platforms.
- **Search Fatigue & Missed Deadlines:** Students spend countless hours searching through irrelevant postings and frequently discover valuable opportunities only after application deadlines have passed.
- **Poor Personalization:** Traditional job boards lack granular matching tailored to student academic backgrounds, emerging skill sets, and specific career interests.
- **Unclear Skill Gaps:** Students often do not know which specific skills they are missing to qualify for their dream internships or technical hackathons.

---

## 💡 Our Solution

OpportunityHub bridges the gap between ambitious students and career-launching opportunities by offering:
- **Centralized Opportunity Discovery:** Access internships, hackathons, scholarships, and courses in one curated platform.
- **Student Profile Creation:** Simple, comprehensive profile setup capturing education level, technical skills, domain interests, and preferred opportunity categories.
- **Personalized Recommendations:** Automated matching engine evaluating student profiles against opportunity requirements.
- **Opportunity Match Percentage:** Instant transparency on how well an opportunity fits a student (e.g., *95% Match*).
- **Matched Skills & Interests:** Clear highlights of overlapping skills and shared interest areas.
- **Skill-Gap Insights:** Actionable intelligence showing students exactly what skills they should learn next to become qualified.
- **Deadline Urgency:** Dynamic visual badges indicating countdown and urgency (Closing Soon, Upcoming, Open, or Expired).
- **Search & Filtering:** Keyword search, multi-category filters, and flexible sorting (Best Match, Deadline, Alphabetical).
- **Save Opportunities:** Persistent bookmarking system to save and review opportunities anytime.
- **Direct Application Links:** Verified external links taking students straight to official application portals in a new tab.

---

## ⭐ Key Features

| Feature | Description |
|---|---|
| **🎯 Personalized Opportunity Matching** | Evaluates student profile attributes against opportunity prerequisites to deliver ranked recommendations. |
| **📊 Match Percentage** | Dynamic score badge showing the alignment between the student's background and each opportunity. |
| **🔍 "Why This Matches You"** | Detailed breakdown on opportunity detail pages showcasing verified skill matches, interest overlap, education eligibility, and category preference. |
| **💡 Skill Gap Analysis** | Compares required skills against student skills—alerts students if skills are missing (*"Learn Docker, Kubernetes"*) or confirms full readiness (*"You have all required skills!"*). |
| **⏳ Deadline Urgency** | Real-time date calculations displaying dynamic badges: *Closing Soon*, *Upcoming*, *Open*, or *Expired*. |
| **🔎 Smart Search** | Instant multi-field filtering across titles, descriptions, organizations, skills, and categories. |
| **🏷️ Category Filters** | One-click filtering across Internships, Hackathons, Courses, Certifications, Scholarships, Competitions, and Workshops. |
| **🔀 Sorting Options** | Sort opportunities by Best Match, Upcoming Deadline, or Opportunity Name. |
| **🔖 Save / Unsave Opportunities** | Client-side persistent bookmarking powered by browser `localStorage` with instant status updates across all views. |
| **📂 Saved Opportunities Hub** | Dedicated `/saved` page to review, manage, and access bookmarked opportunities. |
| **📄 Detailed Opportunity Pages** | Full breakdown of opportunity scope, eligibility criteria, mode (Remote/Hybrid/In-person), location, and organization details. |
| **🔗 Apply Now** | Direct, secure external redirection opening official application portals in a separate browser tab. |
| **📈 Personalized Dashboard** | Overview displaying real-time platform statistics, dynamic top recommendation picks, and current skill sets. |
| **📱 Responsive UI** | Clean, modern user interface optimized across desktop, tablet, and mobile displays. |

---

## 🧠 Matching System

OpportunityHub uses a deterministic scoring algorithm implemented in [`matching.py`](matching.py) that evaluates four weighted dimensions:

$$\text{Total Score} = \text{Skills (40)} + \text{Interests (30)} + \text{Category (20)} + \text{Education (10)}$$

1. **Skills Match (40 Points Maximum):**
   $$\text{Skill Score} = \left(\frac{|\text{Matched Skills}|}{|\text{Opportunity Required Skills}|}\right) \times 40$$
2. **Interests Match (30 Points Maximum):**
   $$\text{Interest Score} = \left(\frac{|\text{Matched Interests}|}{|\text{Opportunity Related Interests}|}\right) \times 30$$
3. **Preferred Category (20 Points Maximum):**
   - Awards **20 points** if the opportunity's category matches any of the student's selected preferred categories.
4. **Education Eligibility (10 Points Maximum):**
   - Awards **10 points** if the student's education level matches the opportunity's eligibility list (or if the opportunity is open to all).

Opportunities are ranked in descending order of total score to present the most relevant recommendations at the top of the student's dashboard.

---

## 🛠️ Technology Stack

- **Backend:** Python, Flask 3.1.3, Gunicorn 23.0.0
- **Frontend:** HTML5, CSS3 (Modern Flexbox/Grid, Responsive Design), Vanilla JavaScript (ES6+)
- **Data Visualization & UI Elements:** Chart.js, Custom SVG/Unicode Icons
- **Storage & State:** Browser `localStorage` (client-side persistence for student profile and bookmarks)
- **Containerization & Deployment:** Docker, GitHub, Render

---

## 📁 Project Structure

```text
OpportunityHub/
├── app.py                      # Flask application factory, routing & API endpoints
├── opportunities.py            # Opportunity data models and dataset
├── matching.py                 # Weighted recommendation matching algorithm
├── test_matching.py            # Unit verification script for recommendation scoring
├── requirements.txt            # Production Python dependencies
├── Dockerfile                  # Production container configuration
├── .dockerignore               # Container build exclusions
├── templates/
│   ├── index.html              # Landing page with hero, stats, and platform overview
│   ├── profile.html            # Student profile creation and editing form
│   ├── dashboard.html          # Personalized student dashboard and top picks
│   ├── opportunities.html      # Search, filter, and discover all opportunities
│   ├── opportunity_details.html# In-depth opportunity view with "Why This Matches You"
│   └── saved.html              # Bookmarked and saved opportunities page
└── static/
    └── css/
        └── style.css           # Global stylesheet and responsive design system
```

---

## 🚀 Run Locally

### Prerequisites
- Python 3.10+ installed
- Git installed

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shubham-bahadurge/OpportunityHub.git
   cd OpportunityHub
   ```

2. **Create and activate a virtual environment:**
   - **macOS / Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the Flask development server:**
   ```bash
   python app.py
   ```

5. **Open your browser:**
   Navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## 🐳 Docker

You can run OpportunityHub in a containerized environment using Docker:

1. **Build the Docker image:**
   ```bash
   docker build -t opportunityhub .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8080:8080 opportunityhub
   ```

3. **Access the application:**
   Navigate to `http://localhost:8080` in your browser.

---

## ☁️ Deployment

OpportunityHub is deployed live using **Docker on Render**. Render automatically pulls from the `main` branch on GitHub, builds the container using the project's production `Dockerfile`, and serves the application using `gunicorn` bound to the designated production port.

- **Live URL:** [https://opportunityhub-xq4i.onrender.com](https://opportunityhub-xq4i.onrender.com)

---

## 🧪 Testing

The platform has been validated through automated verification and manual flow testing:
- **Algorithm Testing:** [`test_matching.py`](test_matching.py) verifies score accuracy, weighting, and edge-case handling across student profiles.
- **End-to-End User Flow Verification:**
  $$\text{Home} \longrightarrow \text{Profile} \longrightarrow \text{Dashboard} \longrightarrow \text{Opportunities} \longrightarrow \text{Details} \longrightarrow \text{Save} \longrightarrow \text{Saved Hub} \longrightarrow \text{Apply Now}$$
- **Routing & Endpoint Tests:** All core routes (`/`, `/profile`, `/dashboard`, `/opportunities`, `/saved`, `/opportunity/<id>`, `/api/recommendations`) return valid HTTP status codes and properly formatted JSON payloads.

---

## 🎯 Project Impact

- **Drastically Reduced Discovery Time:** Eliminates the need to search dozens of websites by aggregating student opportunities in one place.
- **Higher Relevance:** Prevents information overload by highlighting opportunities that directly align with a student's degree, skills, and passions.
- **Targeted Upskilling:** Clarifies skill gaps so students know precisely which technologies or concepts to focus on before applying.
- **Increased Application Rates:** Transparent eligibility and direct application links remove friction and encourage students to submit applications before deadlines pass.
- **Leveling the Playing Field:** Provides equal access to verified student programs regardless of geographic location or institutional network.

---

## 🔮 Future Scope

The following enhancements represent future development milestones beyond the initial hackathon prototype:
- **Real-Time Opportunity Aggregation:** Automated web crawlers and API integrations to continuously ingest listings from official employer portals and student communities.
- **Verified Opportunity Sources:** Employer verification badges and official partnership pipelines for direct recruitment.
- **Intelligent Email & Push Notifications:** Automated alerts for closing deadlines and newly posted opportunities matching the student's profile.
- **Advanced AI Matching:** Embedding-based semantic matching using LLMs for resume parsing and deep contextual compatibility.
- **User Authentication & Cloud Persistence:** Secure multi-tenant database integration (PostgreSQL) with user accounts and OAuth login (Google / GitHub).
- **Application Tracking System (ATS):** Built-in kanban board for students to monitor application stages (*Applied*, *Interviewing*, *Accepted*).
- **Intelligent Career Path Suggestions:** Personalized roadmaps recommending step-by-step courses, hackathons, and certifications to reach target roles.

*(Note: Items listed above are planned for future releases and are not part of the current demo build.)*

---

## ⚠️ Current Demo Limitation

The current demonstration version uses a curated opportunity dataset defined in [`opportunities.py`](opportunities.py) with sample application URLs (`https://example.com/apply/...`). In a full production deployment, these records would be populated dynamically from live external APIs and verified employer partner portals.

---

## 👥 Team

- **Team Name:** Godlike

---

## 📌 Links

- **Live Application:** [https://opportunityhub-xq4i.onrender.com](https://opportunityhub-xq4i.onrender.com)
- **Source Code Repository:** [https://github.com/shubham-bahadurge/OpportunityHub](https://github.com/shubham-bahadurge/OpportunityHub)

---

*Empowering Students. Building Futures. One Opportunity at a Time. 🚀*
