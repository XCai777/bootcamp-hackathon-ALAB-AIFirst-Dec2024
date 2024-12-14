from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO

def generate_pdf(session_state):
    """Generate PDF from session state data"""
    
    # Create a BytesIO buffer to receive PDF data
    buffer = BytesIO()
    
    # Set up the document
    page_size = letter if session_state.doc_format == "Letter (US, Canada)" else A4
    doc = SimpleDocTemplate(
        buffer,
        pagesize=page_size,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=72
    )
    
    # Styles
    styles = getSampleStyleSheet()
    theme_color = session_state.theme_color
    
    # Custom styles
    styles.add(ParagraphStyle(
        name='CustomHeading',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor(theme_color)
    ))
    
    # Build the document content
    content = []
    
    # Personal Information
    content.append(Paragraph(session_state.name, styles['CustomHeading']))
    content.append(Spacer(1, 12))
    
    contact_info = f"{session_state.email} | {session_state.phone} | {session_state.location}"
    content.append(Paragraph(contact_info, styles['Normal']))
    content.append(Spacer(1, 20))
    
    # Objective
    if session_state.get("objective"):
        content.append(Paragraph("OBJECTIVE", styles['CustomHeading']))
        content.append(Spacer(1, 12))
        content.append(Paragraph(session_state.objective, styles['Normal']))
        content.append(Spacer(1, 20))
    
    # Work Experience
    if session_state.get('experiences'):
        content.append(Paragraph("WORK EXPERIENCE", styles['CustomHeading']))
        content.append(Spacer(1, 12))
        for exp in session_state.get('experiences', []):
            content.append(Paragraph(f"<b>{exp.get('position', '')}</b> at {exp.get('company', '')}", styles['Normal']))
            content.append(Paragraph(f"{exp.get('start_date', '')} - {exp.get('end_date', '')}", styles['Normal']))
            content.append(Paragraph(exp.get('description', ''), styles['Normal']))
            if exp.get('technologies'):
                content.append(Paragraph(f"Technologies: {exp.get('technologies')}", styles['Normal']))
            if exp.get('team_size') and exp.get('location'):
                content.append(Paragraph(f"Team Size: {exp.get('team_size')} | Work Type: {exp.get('location')}", styles['Normal']))
            content.append(Spacer(1, 12))
    
    # Education
    if session_state.get('education'):
        content.append(Paragraph("EDUCATION", styles['CustomHeading']))
        content.append(Spacer(1, 12))
        for edu in session_state.get('education', []):
            content.append(Paragraph(f"<b>{edu.get('degree', '')}</b> in {edu.get('major', '')}", styles['Normal']))
            content.append(Paragraph(f"{edu.get('school', '')} | Graduated: {edu.get('graduation_date', '')}", styles['Normal']))
            if edu.get('gpa'):
                content.append(Paragraph(f"GPA: {edu.get('gpa')}", styles['Normal']))
            if edu.get('honors'):
                content.append(Paragraph(f"Honors: {edu.get('honors')}", styles['Normal']))
            if edu.get('coursework'):
                content.append(Paragraph(f"Relevant Coursework: {edu.get('coursework')}", styles['Normal']))
            content.append(Spacer(1, 12))
    
    # Projects
    if session_state.get('projects'):
        content.append(Paragraph("PROJECTS", styles['CustomHeading']))
        content.append(Spacer(1, 12))
        for project in session_state.get('projects', []):
            content.append(Paragraph(f"<b>{project.get('name', '')}</b>", styles['Normal']))
            content.append(Paragraph(f"{project.get('start_date', '')} - {project.get('end_date', '')}", styles['Normal']))
            content.append(Paragraph(project.get('description', ''), styles['Normal']))
            if project.get('technologies'):
                content.append(Paragraph(f"Technologies: {project.get('technologies')}", styles['Normal']))
            if project.get('url'):
                content.append(Paragraph(f"URL: {project.get('url')}", styles['Normal']))
            content.append(Spacer(1, 12))
    
    # Skills
    if session_state.get('skills'):
        content.append(Paragraph("SKILLS", styles['CustomHeading']))
        content.append(Spacer(1, 12))
        for skill in session_state.get('skills', []):
            content.append(Paragraph(f"<b>{skill.get('name', '')}</b>: {skill.get('proficiency', '')}", styles['Normal']))
    
    # Build the PDF
    doc.build(content)
    
    # Get the value of the BytesIO buffer
    pdf = buffer.getvalue()
    buffer.close()
    
    return pdf
