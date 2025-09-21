import React from 'react'
import './About.css'

const About = () => {
  const skills = [
    { name: 'Java', level: 95, icon: '☕' },
    { name: 'Spring Boot', level: 90, icon: '🍃' },
    { name: 'React.js', level: 85, icon: '⚛️' },
    { name: 'AWS', level: 80, icon: '☁️' },
    { name: 'MySQL', level: 85, icon: '🗄️' },
    { name: 'Docker', level: 75, icon: '🐳' }
  ]

  return (
    <section id="about" className="section">
      <div className="container">
        <h2 className="section-title">About Me</h2>
        <div className="about-content">
          <div className="about-text fade-in-left">
            <div className="about-intro">
              <h3>Full Stack Java Developer</h3>
              <p>
                With 2.9+ years of experience in full-stack development, I specialize in building 
                robust enterprise applications using Java, Spring Boot, React.js, and AWS. 
                Currently leading development of enterprise projects at Smac-X Inno Labs, 
                reducing manual operations by 60%.
              </p>
              <p>
                I'm passionate about architecting scalable backend systems, implementing secure 
                authentication, and deploying cloud-native solutions. My expertise spans from 
                microservices architecture to real-time features using WebSocket and Spring AI integration.
              </p>
            </div>
            <div className="stats">
              {[
                { number: '40+', label: 'UI Components Built' },
                { number: '2.9+', label: 'Years Experience' },
                { number: '99.99%', label: 'System Uptime' }
              ].map((stat, index) => (
                <div key={index} className="stat-item scale-on-hover" style={{animationDelay: `${index * 0.2}s`}}>
                  <span className="stat-number">{stat.number}</span>
                  <span className="stat-label">{stat.label}</span>
                </div>
              ))}
            </div>
          </div>
          <div className="skills-section fade-in-right">
            <h3>Skills & Technologies</h3>
            <div className="skills-grid">
              {skills.map((skill, index) => (
                <div key={skill.name} className="skill-item glow-on-hover" style={{animationDelay: `${index * 0.1}s`}}>
                  <div className="skill-header">
                    <span className="skill-icon">{skill.icon}</span>
                    <span className="skill-name">{skill.name}</span>
                    <span className="skill-percentage">{skill.level}%</span>
                  </div>
                  <div className="skill-bar">
                    <div 
                      className="skill-progress" 
                      style={{ width: `${skill.level}%`, animationDelay: `${index * 0.2}s` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  )
}

export default About