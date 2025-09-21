#!/usr/bin/env python3
"""
Professional Resume PDF Generator for Top-Tier Companies
Generates a highly professional, ATS-friendly PDF resume
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.colors import HexColor, black
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
import os

def create_professional_resume():
    # Professional color scheme
    primary_color = HexColor('#2c3e50')  # Dark blue-gray
    accent_color = HexColor('#3498db')   # Professional blue
    text_color = HexColor('#34495e')     # Dark gray
    light_gray = HexColor('#7f8c8d')     # Light gray
    
    # Create PDF document
    filename = "Prashant_Wagh_Senior_Full_Stack_Developer.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, 
                          rightMargin=0.4*inch, leftMargin=0.4*inch,
                          topMargin=0.4*inch, bottomMargin=0.4*inch)
    
    # Get styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=primary_color,
        alignment=TA_CENTER,
        spaceAfter=4,
        fontName='Helvetica-Bold',
        letterSpacing=1
    )
    
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=light_gray,
        alignment=TA_CENTER,
        spaceAfter=8,
        fontName='Helvetica'
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=text_color,
        alignment=TA_CENTER,
        spaceAfter=16,
        fontName='Helvetica'
    )
    
    section_style = ParagraphStyle(
        'SectionStyle',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=primary_color,
        fontName='Helvetica-Bold',
        spaceAfter=6,
        spaceBefore=12,
        borderWidth=2,
        borderColor=accent_color,
        borderPadding=3,
        textTransform='uppercase'
    )
    
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=text_color,
        alignment=TA_JUSTIFY,
        spaceAfter=4,
        fontName='Helvetica',
        lineHeight=12
    )
    
    job_title_style = ParagraphStyle(
        'JobTitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=primary_color,
        fontName='Helvetica-Bold',
        spaceAfter=2
    )
    
    company_style = ParagraphStyle(
        'CompanyStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=text_color,
        fontName='Helvetica-Bold',
        spaceAfter=3
    )
    
    tech_style = ParagraphStyle(
        'TechStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor=light_gray,
        fontName='Helvetica-Oblique',
        spaceAfter=6,
        backColor=HexColor('#ecf0f1'),
        borderPadding=3
    )
    
    # Build content
    content = []
    
    # Header
    content.append(Paragraph("PRASHANT WAGH", name_style))
    content.append(Paragraph("Full Stack Java Developer", title_style))
    content.append(Paragraph(
        "Email: waghprashant6563@gmail.com | Phone: +91-9420952286<br/>"
        "Location: Hyderabad, India | LinkedIn: linkedin.com/in/prashant-wagh-sonar-1982a4214", 
        contact_style
    ))
    
    # Professional Summary
    content.append(Paragraph("PROFESSIONAL SUMMARY", section_style))
    content.append(Paragraph(
        "Results-driven Full Stack Java Developer with 2.8+ years of experience in designing, developing, and "
        "deploying robust software solutions using Java, Spring Boot, React.js, and AWS. Skilled in optimizing "
        "performance, implementing efficient code, and delivering high-quality software in fast-paced environments.",
        body_style
    ))
    
    # Technical Skills
    content.append(Paragraph("CORE TECHNICAL COMPETENCIES", section_style))
    
    skills_data = [
        ["Programming Languages:", "Java 8/11/17, JavaScript ES6+, TypeScript, SQL, Python"],
        ["Backend Technologies:", "Spring Boot (Key), Microservices (Key), Spring Security, Spring Data JPA, Spring Cloud, Spring AI, Hibernate"],
        ["Frontend Technologies:", "React.js (Key), Redux, HTML5, CSS3, Bootstrap, Material-UI, JavaScript"],
        ["Cloud & DevOps:", "AWS (Key) - EC2, S3, RDS, Lambda, IAM, VPC, Docker, Kubernetes, Jenkins, CI/CD"],
        ["Databases & Storage:", "MySQL, PostgreSQL, MongoDB, Redis, MSSQL, Database Design"],
        ["Tools & Methodologies:", "Git, Maven, Gradle, Postman, JMeter, Agile/Scrum, TDD, Code Review"]
    ]
    
    skills_table = Table(skills_data, colWidths=[1.3*inch, 5.2*inch])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('TEXTCOLOR', (0, 0), (0, -1), primary_color),
        ('TEXTCOLOR', (1, 0), (1, -1), text_color),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(skills_table)
    content.append(Spacer(1, 8))
    
    # Work Experience
    content.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))
    
    # Job 1
    job1_header = Table([
        ["Full Stack Java Developer + Cloud", "November 2024 - Present"]
    ], colWidths=[4.2*inch, 2.3*inch])
    job1_header.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, 0), primary_color),
        ('TEXTCOLOR', (1, 0), (1, 0), light_gray),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(job1_header)
    
    content.append(Paragraph("Smac-X Inno Labs Pvt Ltd", company_style))

    
    job1_bullets = [
        "• Leading development of two enterprise projects from scratch—Ticketing Tool and Vendor Portal—reducing manual SAP operations by 60%",
        "• Architected secure and scalable backend systems using Spring Boot, Spring Security, and Spring Data JPA, handling over 1M database transactions monthly",
        "• Built and deployed 40+ highly responsive UI components with React.js and Redux, increasing user satisfaction scores by 30%",
        "• Managed AWS infrastructure, including EC2, S3, RDS, VPC, IAM, and Route 53, achieving 99.99% uptime and cutting deployment time by 40%",
        "• Implemented WebSocket-based real-time chat and notification features, enhancing communication efficiency by 45% within the platform",
        "• Integrated SAP services to deliver cloud-native solutions, ensuring seamless compatibility with SAP environments and improving deployment efficiency by 35%"
    ]
    
    for bullet in job1_bullets:
        content.append(Paragraph(bullet, body_style))
    

    
    # Job 2
    job2_header = Table([
        ["Full Stack Java Developer", "February 2023 - October 2024"]
    ], colWidths=[4.2*inch, 2.3*inch])
    job2_header.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, 0), primary_color),
        ('TEXTCOLOR', (1, 0), (1, 0), light_gray),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(job2_header)
    
    content.append(Paragraph("Engeniuspark Technologies, Nashik", company_style))

    
    job2_bullets = [
        "• Developed and maintained RESTful APIs and microservices using Spring Boot, Spring Cloud, Spring Data JPA, and Spring Security, improving backend reliability by 40%",
        "• Implemented JWT-based authentication and authorization, reducing unauthorized access by 90% and aligning with enterprise-grade security standards",
        "• Designed scalable and fault-tolerant microservices architecture using Spring Cloud, improving system availability to 99.9% during high-traffic events",
        "• Built real-time features like chat and notifications using WebSocket and STOMP, enhancing user engagement by 50% across core modules",
        "• Deployed Dockerized microservices to AWS EC2 with S3 and RDS integrations, achieving 100% deployment consistency and reducing infrastructure cost by 20%",
        "• Mentored 5 junior developers on Java and React.js, raising overall code quality and increasing team productivity by 25% in under six months"
    ]
    
    for bullet in job2_bullets:
        content.append(Paragraph(bullet, body_style))
    
    # Internship
    job3_header = Table([
        ["Full Stack Java Developer Intern", "January 2023 - February 2023"]
    ], colWidths=[4.2*inch, 2.3*inch])
    job3_header.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
        ('FONTNAME', (1, 0), (1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (0, 0), primary_color),
        ('TEXTCOLOR', (1, 0), (1, 0), light_gray),
        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    content.append(job3_header)
    
    content.append(Paragraph("Oasis Infobyte", company_style))
    
    job3_bullets = [
        "• Developed web applications using Java, Spring Boot, and React.js during intensive training program",
        "• Built responsive frontend components and integrated with backend APIs for seamless user experience",
        "• Gained hands-on experience with database operations using MySQL and implemented CRUD functionalities",
        "• Collaborated with development team on multiple projects and learned industry best practices"
    ]
    
    for bullet in job3_bullets:
        content.append(Paragraph(bullet, body_style))
    

    
    # Key Projects
    content.append(Paragraph("KEY TECHNICAL PROJECTS", section_style))
    
    projects = [
        {
            "title": "AI-Powered Customer Support System",
            "description": "Developed intelligent chatbot system integrating Spring AI with OpenAI API, featuring real-time WebSocket communication and natural language processing capabilities. Achieved 70% automation of customer queries and 40% reduction in support response time.",
            "tech": "Technologies: Spring Boot, Spring AI, OpenAI API, WebSocket, React.js, Natural Language Processing"
        },
        {
            "title": "GraphQL-Based Order Management System",
            "description": "Architected modern order and customer management system using GraphQL, replacing traditional REST APIs. Reduced API response complexity by 60% and improved data fetching efficiency by 45%, supporting real-time order tracking for 10,000+ daily transactions.",
            "tech": "Technologies: Spring Boot, GraphQL, MySQL, Spring Data JPA, React.js, Real-time Updates"
        },

    ]
    
    for project in projects:
        content.append(Paragraph(project["title"], job_title_style))
        content.append(Paragraph(project["description"], body_style))
        content.append(Paragraph(project["tech"], tech_style))
    
    # Education
    content.append(Paragraph("EDUCATION", section_style))
    content.append(Paragraph("B.Tech", job_title_style))
    content.append(Paragraph("Dr.Babasaheb Ambedkar Technological University", company_style))
    content.append(Paragraph("CGPA: 8.4/10 | Graduated: 2023", body_style))
    
    # Certifications
    content.append(Paragraph("CERTIFICATIONS", section_style))
    
    certifications = [
        "• Full Stack Java Development",
        "• AWS Cloud Practitioner Essentials"
    ]
    
    for cert in certifications:
        content.append(Paragraph(cert, body_style))
    
    # Build PDF
    doc.build(content)
    print(f"Professional resume PDF generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_professional_resume()