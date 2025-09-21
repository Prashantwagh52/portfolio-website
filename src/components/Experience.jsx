import React from 'react'
import './Experience.css'

const Experience = () => {
  const experiences = [
    {
      title: 'Full Stack Java Developer + Cloud',
      company: 'Smac-X Inno Labs Pvt Ltd',
      period: 'November 2024 - Present',
      description: 'Leading development of enterprise projects from scratch—Ticketing Tool and Vendor Portal—reducing manual SAP operations by 60%. Architected secure backend systems handling 1M+ monthly transactions and managed AWS infrastructure achieving 99.99% uptime.',
      technologies: ['Spring Boot', 'React.js', 'AWS', 'Spring Security', 'WebSocket', 'SAP']
    },
    {
      title: 'Full Stack Java Developer',
      company: 'Engeniuspark Technologies',
      period: 'February 2023 - October 2024',
      description: 'Developed RESTful APIs and microservices using Spring Boot, improving backend reliability by 40%. Implemented JWT authentication reducing unauthorized access by 90% and deployed Dockerized services to AWS, cutting infrastructure costs by 20%.',
      technologies: ['Spring Boot', 'Spring Cloud', 'Docker', 'AWS EC2', 'MySQL', 'JWT']
    }
  ]

  return (
    <section id="experience" className="section">
      <div className="container">
        <h2 className="section-title">Experience</h2>
        <div className="timeline">
          {experiences.map((exp, index) => (
            <div key={index} className="timeline-item">
              <div className="timeline-marker"></div>
              <div className="timeline-content card">
                <div className="experience-header">
                  <h3 className="job-title">{exp.title}</h3>
                  <span className="period">{exp.period}</span>
                </div>
                <h4 className="company">{exp.company}</h4>
                <p className="description">{exp.description}</p>
                <div className="technologies">
                  {exp.technologies.map((tech, techIndex) => (
                    <span key={techIndex} className="tech-tag">
                      {tech}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Experience