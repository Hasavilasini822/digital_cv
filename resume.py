from fpdf import FPDF
import streamlit as st
from PIL import Image

PAGE_TITLE = "Digital Resume"
PAGE_ICON = ":star:"


def main():
    st.set_page_config(layout="centered")
    st.title("Digital Resume")

    uploaded_file = st.sidebar.file_uploader("Upload Profile Picture", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        profile_pic = uploaded_file.read()
        st.sidebar.image(profile_pic, caption='Profile Picture', use_column_width=True)

        # Personal details
        st.sidebar.subheader("Personal Details")
        Name = st.sidebar.text_input("Name")
        Email = st.sidebar.text_input("Email")
        Phone = st.sidebar.text_input("Phone")
        Linkedin = st.sidebar.text_input("linkedin")

        # Education
        st.sidebar.subheader("Education")
        College = st.sidebar.text_input("College Name")
        degree = st.sidebar.text_input("Degree")
        graduation_year = st.sidebar.text_input("Graduation Year")

         # Skills
        st.sidebar.subheader("Skills")
        skills = st.sidebar.text_area("List your skills")


        # Projects
        st.sidebar.header("Projects")
        Pname = st.sidebar.text_input("Project Name")
        description = st.sidebar.text_area("description")
        
        # Work experience
        st.sidebar.header("Work Experience")
        company = st.sidebar.text_input("Company")
        position = st.sidebar.text_area("Position")

        # Display profile picture and personal details in the main section
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(profile_pic, caption=' ', use_column_width=True)

        with col2:
            st.header("Personal Details")
            st.markdown(f" Name :     {Name}")
            st.markdown(f"Email :     {Email}")
            st.markdown(f"Phone :     {Phone}")
            st.markdown(f"Linkedin:     {Linkedin}")

        # Display education and work experience in the main section
        st.header("🖊 Education")
        st.markdown(f" College :    { College}")
        st.markdown(f" Degree :     { degree}")
        st.markdown(f" Graduation Year:       { graduation_year}")

        st.header("🔗 SKills")
        st.markdown(f" Description :    {skills}")

        st.header("🏆 Project")
        st.markdown(f" Project :    {Pname}")
        st.markdown(f" Description :    {description}")


        st.header("📝 Work Experience")
        st.markdown(f" Company :    {company}")
        st.markdown(f" Position :    {position}")
       


        st.sidebar.markdown("---")

        # Generate and download the resume file
        resume_filename = "resume.pdf"
        resume_data = generate_resume_data(Name, Email, Phone, Linkedin, College, degree, graduation_year, skills, Pname, description, company, position)

        # Create a download button
        st.sidebar.download_button(
            label="Download Resume",
            data=resume_data,
            file_name=resume_filename,
            mime="application/pdf"
        )


def generate_resume_data(Name, Email, Phone, Linkedin, College, degree, graduation_year, skills, Pname, description, company, position):
    # Generate your resume content using FPDF
    pdf = FPDF()
    pdf.add_page()

    # Add profile picture
    pdf.set_xy(10, 10)
    pdf.image("profile_picture.png", w=40, h=40)

    # Add personal details
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Name: {Name}", ln=True)
    pdf.cell(0, 10, f"Email: {Email}", ln=True)
    pdf.cell(0, 10, f"Phone: {Phone}", ln=True)
    pdf.cell(0, 10, f"Linkedin: {Linkedin}", ln=True)

    # Add education section
    pdf.set_font("Arial", "B", size=14)
    pdf.cell(0, 10, "Education", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"College: {College}", ln=True)
    pdf.cell(0, 10, f"Degree: {degree}", ln=True)
    pdf.cell(0, 10, f"Graduation Year: {graduation_year}", ln=True)


    # Add skills section
    pdf.set_font("Arial", "B", size=14)
    pdf.cell(0, 10, "Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Skills: {skills}", ln=True)
    

    # Add projects section
    pdf.set_font("Arial", "B", size=14)
    pdf.cell(0, 10, "Projects", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Project Name: {Pname}", ln=True)
    pdf.cell(0, 10, f"Description: {description}", ln=True)

    # Add work experience section
    pdf.set_font("Arial", "B", size=14)
    pdf.cell(0, 10, "Work Experience", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Company: {company}", ln=True)
    pdf.cell(0, 10, f"Position: {position}", ln=True)

    # Save the PDF to a file
    pdf.output("resume.pdf")

    with open("resume.pdf", "rb") as file:
        resume_data = file.read()

    return resume_data


if __name__ == "__main__":
    main()
