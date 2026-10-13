import streamlit as st
import pandas as pd
from database import init_db, add_student, get_students, delete_student, get_student_count, validate_student

st.set_page_config(page_title="Student Management System", page_icon="🎓", layout="wide")

init_db()

st.title("🎓 Cloud-Based Student Management System")
st.caption("FT-III Cloud Computing Case Study | Streamlit · GitHub · SQLite")
st.info("Academic prototype: the app is hosted by Streamlit Community Cloud after deployment from GitHub. SQLite is used for demonstration; local-file persistence is not guaranteed on hosted platforms.")

with st.sidebar:
    st.header("Project details")
    st.write("**Development:** Google Colab")
    st.write("**Source control:** GitHub")
    st.write("**Deployment:** Streamlit Community Cloud")
    st.write("**Database:** SQLite")
    st.divider()
    st.subheader("Cloud concepts")
    st.write("- Hosted application runtime")
    st.write("- Version-controlled source code")
    st.write("- Database CRUD operations")
    st.write("- Input validation")

total = get_student_count()
c1, c2 = st.columns(2)
c1.metric("Total student records", total)
c2.metric("Application status", "Running", help="This status means the Streamlit app has loaded; it is not an external uptime guarantee.")

tab1, tab2, tab3 = st.tabs(["➕ Add Student", "📋 View Records", "🧪 Evaluation"])

with tab1:
    st.subheader("Register a student")
    with st.form("add_student_form", clear_on_submit=True):
        name = st.text_input("Student name", max_chars=100)
        email = st.text_input("Email address", max_chars=150)
        course = st.text_input("Course / department", max_chars=100)
        submitted = st.form_submit_button("Add Student", type="primary")
    if submitted:
        valid, message = validate_student(name, email, course)
        if not valid:
            st.error(message)
        else:
            try:
                add_student(name.strip(), email.strip(), course.strip())
                st.success("Student added successfully.")
                st.rerun()
            except Exception as exc:
                st.error(f"Could not save student record: {exc}")

with tab2:
    st.subheader("Student records")
    records = get_students()
    if records:
        df = pd.DataFrame(records, columns=["ID", "Name", "Email", "Course", "Created at (UTC)"])
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.download_button(
            "Download records as CSV",
            data=df.to_csv(index=False).encode("utf-8"),
            file_name="student_records.csv",
            mime="text/csv",
        )
        ids = [row[0] for row in records]
        selected_id = st.selectbox("Select student ID to delete", ids, format_func=lambda x: f"ID {x}")
        if st.button("Delete selected student", type="secondary"):
            delete_student(selected_id)
            st.success(f"Deleted student ID {selected_id}.")
            st.rerun()
    else:
        st.warning("No records yet. Add a student in the first tab.")

with tab3:
    st.subheader("Evaluation checklist")
    st.write("Use this section during your demonstration. Record real measurements in the PPT.")
    st.markdown("""
    - **Create:** Add a student and confirm the success message.
    - **Read:** Open View Records and verify the new row.
    - **Update:** This version does not implement editing; identify it as a future enhancement.
    - **Delete:** Select a record ID and delete it.
    - **Persistence:** Refresh the page and check whether the record remains during the current runtime.
    - **Performance:** Measure page/request latency using browser tools or a separate HTTP test where available.
    """)
    st.warning("Do not claim measured performance, guaranteed persistence, or zero cost unless you have tested and verified it.")
    st.markdown("**Health check:** the app's internal database health can be checked from the Colab test notebook using the database functions.")
