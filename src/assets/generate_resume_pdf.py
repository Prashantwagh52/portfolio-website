#!/usr/bin/env python3
"""
Resume PDF Generator
Generates a professional ATS-friendly PDF resume for Prashant Wagh
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.pdfgen import canvas
import os

def create_resume_pdf():
    # Define colors
    primary_color = HexColor('#1a5f3f')
    text_color = HexColor('#333333')
    gray_color = HexColor('#666666')
    
    # Create PDF document
    filename = "Prashant_Wagh_Full_Stack_Java_Developer_ATS.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, 
                          rightMargin=0.5*inch, leftMargin=0.5*inch,
                          topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=primary_color,
        alignment=TA_CENTER,
        spaceAfter=6,
        fontName='Helvetica-Bold'
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=gray_color,
        alignment=TA_CENTER,
        spaceAfter=12,
        fontName='Helvetica'
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=text_color,
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName='Helvetica'
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=primary_color,
        fontName='Helvetica-Bold',
        spaceAfter=8,
        spaceBefore=16,
        borderWidth=1,
        borderColor=gray_color,
        borderPadding=2
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=text_color,
        alignment=TA_JUSTIFY,
        spaceAfter=6,
        fontName='Helvetica'
    )
    
    job_title_style = ParagraphStyle(
        'JobTitleStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=primary_color,
        fontName='Helvetica-Bold',
        spaceAfter=2
    )
    
    company_style = ParagraphStyle(
        'CompanyStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=text_color,
        fontName='Helvetica-Bold',
        spaceAfter=4
    )
    
    tech_style = ParagraphStyle(
        'TechStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=gray_color,
        fontName='Helvetica-Oblique',
        spaceAfter=8
    )
    
    # Build content
    content = []
    
    # Header
    content.append(Paragraph("PRASHANT WAGH", name_style))
    content.append(Paragraph("Full Stack Java Developer", title_style))
    content.append(Paragraph(
        "Email: waghprashant6563@gmail.com | Phone: +91-9420952286 | Location: Hyderabad, India<br/>"
        "LinkedIn: linkedin.com/in/prashant-wagh-sonar-1982a4214", 
        contact_style
    ))
    
    # Professional Summary
    content.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    content.append(Paragraph(
        "Results-driven Full Stack Java Developer with 2.6+ years of experience in designing, developing, "
        "and deploying robust enterprise applications using Java, Spring Boot, React.js, and AWS. "
        "Proven track record of reducing manual operations by 60%, improving system reliability by 40%, "
        "and achieving 99.99% uptime. Expertise in microservices architecture, cloud-native solutions, "
        "and real-time features implementation. Strong problem-solving skills with experience in Agile "
        "methodologies and team collaboration.",
        body_style
    ))
    
    # Technical Skills
    content.append(Paragraph("TECHNICAL SKILLS", section_style))
    
    skills_data = [
        ["Programming Languages:", "Java, JavaScript, SQL, HTML, CSS"],
        ["Frameworks & Libraries:", "Spring Boot, Spring Security, Spring Data JPA, Spring Cloud, Spring AI, React.js, Redux"],
        ["Cloud Technologies:", "AWS (EC2, S3, RDS, IAM, VPC), Docker, Kubernetes"],
        ["Databases:", "MySQL, MSSQL, Redis, PostgreSQL"],
        ["Tools & Technologies:", "Git, Jenkins, Postman, JMeter, Maven, Gradle, WebSocket, GraphQL"],
        ["Methodologies:", "Agile, Scrum, Microservices Architecture, RESTful APIs, CI/CD, Unit Testing, Code Review"]
    ]
    
    skills_table = Table(skills_data, colWidths=[1.5*inch, 5*inch])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, -1), primary_color),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(skills_table)
    content.append(Spacer(1, 12))
    
    # Work Experience
    content.append(Paragraph("WORK EXPERIENCE", section_style))
    
    # Job 1
    job1_header = Table([
        ["Full Stack Java Developer + Cloud", "November 2024 - Present"]
    ], colWidths=[4*inch, 2.5*inch])
    job1_header.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, 0), primary_color),
        ('TEXTCOLOR', (1, 0), (1, 0), gray_color),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(job1_header)
    
    content.append(Paragraph("Smac-X Inno Labs Pvt Ltd, Hyderabad", company_style))
    content.append(Paragraph(
        "Leading development of enterprise projects from scratch—Ticketing Tool and Vendor Portal—reducing "
        "manual SAP operations by 60%. Architected secure backend systems handling 1M+ monthly transactions "
        "and managed AWS infrastructure achieving 99.99% uptime.",
        body_style
    ))
    
    job1_bullets = [
        "• Developed enterprise ticketing system with Spring Boot and React.js, improving operational efficiency",
        "• Implemented Spring Security with JWT authentication, reducing unauthorized access by 90%",
        "• Integrated WebSocket for real-time features and Spring AI for automated customer query handling",
        "• Managed AWS cloud infrastructure with EC2, RDS, and S3 for scalable deployment"
    ]
    
    for bullet in job1_bullets:
        content.append(Paragraph(bullet, body_style))
    
    content.append(Paragraph(
        "Technologies: Spring Boot, React.js, AWS, Spring Security, WebSocket, Spring AI, SAP Integration",
        tech_style
    ))
    
    # Job 2
    job2_header = Table([
        ["Full Stack Java Developer", "February 2023 - October 2024"]
    ], colWidths=[4*inch, 2.5*inch])
    job2_header.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, 0), primary_color),
        ('TEXTCOLOR', (1, 0), (1, 0), gray_color),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(job2_header)
    
    content.append(Paragraph("Engeniuspark Technologies, Hyderabad", company_style))
    content.append(Paragraph(
        "Developed RESTful APIs and microservices using Spring Boot, improving backend reliability by 40%. "
        "Implemented JWT authentication and deployed Dockerized services to AWS, cutting infrastructure costs by 20%.",
        body_style
    ))
    
    job2_bullets = [
        "• Built scalable microservices architecture using Spring Boot and Spring Cloud",
        "• Developed responsive web applications with React.js and Redux for state management",
        "• Implemented CI/CD pipelines using Jenkins and Docker for automated deployment",
        "• Optimized database queries and implemented caching strategies with Redis",
        "• Collaborated with cross-functional teams using Agile methodology and code review practices"
    ]
    
    for bullet in job2_bullets:
        content.append(Paragraph(bullet, body_style))
    
    content.append(Paragraph(
        "Technologies: Spring Boot, Spring Cloud, React.js, Docker, AWS EC2, MySQL, JWT, Redis",
        tech_style
    ))
    
    # Key Projects
    content.append(Paragraph("KEY PROJECTS", section_style))
    
    projects = [
        {
            "title": "Spring AI Chatbot Integration",
            "description": "Integrated Spring AI into Spring Boot application enabling real-time chat using OpenAI API, automating 70% of customer queries and enhancing user interaction through WebSocket implementation.",
            "tech": "Technologies: Spring Boot, Spring AI, OpenAI API, WebSocket, React.js"
        },
        {
            "title": "GraphQL Order & Customer Service",
            "description": "Designed Order and Customer services using GraphQL in Spring Boot, reducing API response complexity by 60% compared to traditional REST APIs and improving data fetching efficiency.",
            "tech": "Technologies: Spring Boot, GraphQL, MySQL, Spring Data JPA, React.js"
        },
        {
            "title": "Enterprise Vendor Portal System",
            "description": "Built scalable vendor management portal with real-time features, handling 1M+ database transactions monthly with 99.99% uptime and secure authentication system.",
            "tech": "Technologies: Spring Boot, React.js, Redux, AWS RDS, WebSocket, Spring Security"
        }
    ]
    
    for project in projects:
        content.append(Paragraph(project["title"], job_title_style))
        content.append(Paragraph(project["description"], body_style))
        content.append(Paragraph(project["tech"], tech_style))
    
    # Education
    content.append(Paragraph("EDUCATION", section_style))
    content.append(Paragraph("Bachelor of Engineering in Computer Science", job_title_style))
    content.append(Paragraph("Pune University, Maharashtra", company_style))
    content.append(Paragraph("CGPA: 8.2/10 | Merit Scholarship Recipient | Coding Competition Winner | Graduated: 2022", body_style))
    
    # Certifications
    content.append(Paragraph("CERTIFICATIONS & ACHIEVEMENTS", section_style))
    
    certifications = [
        "• AWS Certified Solutions Architect Associate (In Progress)",
        "• Oracle Certified Professional Java SE Developer",
        "• Spring Boot Microservices Certification",
        "• Merit Scholarship for Academic Excellence",
        "• Winner - College Level Coding Competition"
    ]
    
    for cert in certifications:
        content.append(Paragraph(cert, body_style))
    
    # Build PDF
    doc.build(content)
    print(f"Resume PDF generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_resume_pdf()