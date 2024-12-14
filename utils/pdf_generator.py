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
    
    # Build the PDF
    doc.build(content)
    
    # Get the value of the BytesIO buffer
    pdf = buffer.getvalue()
    buffer.close()
    
    return pdf