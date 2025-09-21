import React from 'react'
import './Projects.css'

const Projects = () => {
  const projects = [
    {
      title: 'Spring AI Chatbot',
      description: 'Integrated Spring AI into a Spring Boot application to enable real-time chat using OpenAI, enhancing user interaction and automating 70% of customer queries.',
      image: '🤖',
      technologies: ['Spring Boot', 'Spring AI', 'OpenAI API', 'WebSocket'],
      liveUrl: '#',
      githubUrl: '#'
    },
    {
      title: 'Order & Customer Service',
      description: 'Designed Order and Customer services using GraphQL in Spring Boot, reducing API response complexity by 60% compared to traditional REST.',
      image: '📦',
      technologies: ['Spring Boot', 'GraphQL', 'MySQL', 'Spring Data JPA'],
      liveUrl: '#',
      githubUrl: '#'
    },
    {
      title: 'Enterprise Ticketing Tool',
      description: 'Leading development of enterprise ticketing system from scratch, reducing manual SAP operations by 60% with secure backend architecture.',
      image: '🎫',
      technologies: ['Spring Boot', 'React.js', 'Spring Security', 'AWS', 'SAP'],
      liveUrl: '#',
      githubUrl: '#'
    },
    {
      title: 'Vendor Portal System',
      description: 'Built scalable vendor management portal with real-time features, handling 1M+ database transactions monthly with 99.99% uptime.',
      image: '🏢',
      technologies: ['Spring Boot', 'React.js', 'Redux', 'AWS RDS', 'WebSocket'],
      liveUrl: '#',
      githubUrl: '#'
    }
  ]

  return (
    <section id="projects" className="section">
      <div className="container">
        <h2 className="section-title">Featured Projects</h2>
        <div className="projects-grid grid grid-3">
          {projects.map((project, index) => (
            <div key={index} className={`project-card card fade-in-up`} style={{animationDelay: `${index * 0.2}s`}}>
              <div className="project-image">
                <span className="project-emoji">{project.image}</span>
              </div>
              <div className="project-content">
                <h3 className="project-title">{project.title}</h3>
                <p className="project-description">{project.description}</p>
                <div className="project-technologies">
                  {project.technologies.map((tech, techIndex) => (
                    <span key={techIndex} className="tech-tag">
                      {tech}
                    </span>
                  ))}
                </div>
                <div className="project-links">
                  <a href={project.liveUrl} className="btn btn-primary btn-hover-effect" target="_blank" rel="noopener noreferrer">
                    Live Demo
                  </a>
                  <a href={project.githubUrl} className="btn btn-outline btn-hover-effect" target="_blank" rel="noopener noreferrer">
                    GitHub
                  </a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

export default Projects