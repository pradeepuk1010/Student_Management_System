# FT-III Cloud Computing Case Study: Student Management System

A small Streamlit application for creating, viewing, and deleting student records. The project is designed to be developed/tested in Google Colab, stored in GitHub, and deployed using Streamlit Community Cloud.

## Technology stack

- **Google Colab:** cloud-hosted development and testing environment.
- **GitHub:** source-code hosting and version control.
- **Streamlit Community Cloud:** managed application hosting from a GitHub repository.
- **SQLite:** lightweight relational database for the academic prototype.
- **Pandas:** table display and CSV export.

> **Important limitation:** SQLite is stored in a local file. On hosted platforms, local file persistence is not guaranteed across rebuilds, restarts, or instance changes. Use a managed database such as PostgreSQL/Supabase or another persistent database for real multi-user/production use. This prototype has no authentication and should use synthetic/demo data only.

## Features

- Add student records (name, email, course)
- View records in a table
- Delete a selected record
- Input validation
- CSV export
- Database unit tests
- Evaluation checklist in the UI

## Files

```text
FT3_Student_Management_System/
├── app.py
├── database.py
├── requirements.txt
├── README.md
├── .gitignore
├── tests/
│   └── test_database.py
└── FT3_Colab_Testing.ipynb
```

## A. Test in Google Colab

1. Upload this repository to GitHub (see section B).
2. Open [Google Colab](https://colab.research.google.com/).
3. Create a notebook and run:

```python
!git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
%cd YOUR-REPOSITORY
!pip -q install -r requirements.txt
!python -m unittest discover -s tests -v
```

Replace `YOUR-USERNAME` and `YOUR-REPOSITORY` with your actual GitHub details.

To run the app inside Colab:

```python
!streamlit run app.py --server.port 8501 --server.address 0.0.0.0 > /tmp/streamlit.log 2>&1 &
```

This starts Streamlit inside the Colab runtime. To open it in a browser, use a temporary tunnel only if permitted by your environment. A Colab runtime is temporary and is not a persistent public deployment.

## B. Upload this project to GitHub

1. Sign in at [GitHub](https://github.com/).
2. Click **New repository**.
3. Name it `ft3-student-management-system`.
4. Set it to **Public** if you want to deploy it easily with Streamlit Community Cloud; do not upload credentials or personal student data.
5. Choose **Add file → Upload files**.
6. Extract this ZIP on your computer and upload `app.py`, `database.py`, `requirements.txt`, `README.md`, `.gitignore`, the `tests` folder, and the notebook file.
7. Commit the files to the repository.

## C. Deploy from GitHub to Streamlit Community Cloud

1. Open [Streamlit Community Cloud](https://share.streamlit.io/).
2. Sign in and connect your GitHub account.
3. Select **Create app** / **Deploy an app**.
4. Select your repository and branch (usually `main`).
5. Set the main file path to `app.py`.
6. Deploy and wait for the build to finish.
7. Open the generated app URL and test adding, viewing, and deleting records.

If deployment fails, inspect the Streamlit app logs. Ensure `app.py`, `database.py`, and `requirements.txt` are in the repository root.

## D. FT-III evaluation mapping

| Criterion | Evidence to capture |
|---|---|
| Problem analysis & cloud design (2) | Problem statement, requirements, architecture, and explanation of cloud services |
| Implementation & technical execution (8) | GitHub repository, deployment URL, CRUD demo, database tests, input validation, deployment settings |
| Results & technical evaluation (2) | Actual test output, response-time measurements, cost estimate, scalability discussion |
| Viva (3) | Explain Colab, GitHub, Streamlit hosting, SQLite, persistence limitations, security, and future scaling |

## E. Testing

Run in Colab or any Python environment:

```bash
python -m unittest discover -s tests -v
```

The tests cover insertion/retrieval, deletion, invalid email, and required fields. Save the actual test output as evidence.

## F. Performance and cost evaluation

Do not invent performance results. Record the actual values you observe. For a simple timing test, run this in Colab after importing the database functions:

```python
import time
from database import init_db, get_students
init_db()
start = time.perf_counter()
get_students()
elapsed_ms = (time.perf_counter() - start) * 1000
print(f"Database read time: {elapsed_ms:.2f} ms")
```

This measures a local database operation in the current runtime, not public web response latency.

- Colab and Streamlit hosting availability/limits depend on their current terms and account conditions.
- Check the selected hosting service's current pricing and limits before deployment.
- For AWS comparison, use the [AWS Pricing Calculator](https://calculator.aws/); do not claim the project costs ₹0 unless verified.

## G. Security and limitations

- Use fictional student data for the presentation.
- No authentication/authorization is implemented.
- Do not add API keys, passwords, access tokens, or secrets to GitHub.
- Public deployment makes the app URL accessible to others.
- SQLite local-file persistence is not guaranteed on managed hosting.
- Production improvements: authentication, authorization, HTTPS, CSRF protections, persistent managed database, backups, and monitoring.

## Suggested architecture for the PPT

Browser → Streamlit Community Cloud (application hosting) → SQLite file (prototype storage).

Development and validation occur in Google Colab; source code and version history are maintained in GitHub. For a production architecture, replace local SQLite with a persistent managed database and add authentication, monitoring, and backup controls.
