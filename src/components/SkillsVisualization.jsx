import React from 'react'
import './SkillsVisualization.css'

const SkillsVisualization = () => {
  const skills = [
    { name: 'Java', icon: '☕' },
    { name: 'Spring Boot', icon: '🍃' },
    { name: 'React.js', icon: '⚛️' },
    { name: 'AWS', icon: '☁️' },
    { name: 'MySQL', icon: '🗄️' },
    { name: 'Docker', icon: '🐳' }
  ]

  return (
    <div className="tech-stack">
      <div className="tech-items">
        {skills.map((skill, index) => (
          <div key={skill.name} className="tech-item">
            <span className="tech-icon">{skill.icon}</span>
            <span className="tech-name">{skill.name}</span>
          </div>
        ))}
      </div>
    </div>
  )
}

export default SkillsVisualization