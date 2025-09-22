import React from 'react'
import TypingAnimation from './TypingAnimation'
import './Hero.css'

const Hero = () => {
  return (
    <section id="home" className="hero">
      <div className="container">
        <div className="hero-content">
          <div className="hero-text animate-slide-up">
            <h1 className="hero-title animate-fade-in">
              Hi, I'm <span className="name-highlight animate-glow">Prashant Wagh</span>
            </h1>
            <h2 className="hero-subtitle animate-fade-in-delay-1">
              <TypingAnimation 
                texts={[
                  'Full Stack Java Developer',
                  'Spring Boot Developer',
                  'React.js Developer',
                  'AWS Cloud Engineer',
                  'Microservices Architecture'
                ]}
                speed={100}
                deleteSpeed={50}
                pauseTime={2000}
              />
            </h2>
            <p className="hero-description animate-fade-in-delay-2">
              Results-driven Full Stack Java Developer with 2.9+ years of experience in designing, 
              developing, and deploying robust software solutions using Java, Spring Boot, React.js, and AWS. 
              Based in Hyderabad, India.
            </p>
            <div className="hero-buttons animate-fade-in-delay-3">
              <a href="#projects" className="btn btn-primary btn-hover-effect">
                View My Work
              </a>
              <a href="#contact" className="btn btn-outline btn-hover-effect">
                Get In Touch
              </a>
            </div>
          </div>
          <div className="hero-visual animate-slide-right">
            <div className="floating-card card-1 animate-float">
              <div className="card-content">
                <div className="icon animate-bounce">☕</div>
                <span>Java</span>
              </div>
            </div>
            <div className="floating-card card-2 animate-float-delay">
              <div className="card-content">
                <div className="icon animate-bounce">🍃</div>
                <span>Spring Boot</span>
              </div>
            </div>
            
            <div className="floating-card card-3 animate-float-delay-2">
              <div className="card-content">
                <div className="icon animate-bounce">☁️</div>
                <span>AWS</span>
              </div>
            </div>

            <div className="floating-card card-4 animate-float-delay">
              <div className="card-content">
                <div className="icon animate-bounce">⚛️</div>
                <span>React JS</span>
              </div>
            </div>
            <div className="hero-avatar animate-scale-in">
              <div className="avatar-placeholder animate-pulse">
                <span>👨‍💻</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div className="scroll-indicator">
        <div className="scroll-arrow"></div>
      </div>
    </section>
  )
}

export default Hero