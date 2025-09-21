import React from 'react'
import Header from './components/Header'
import Hero from './components/Hero'
import About from './components/About'
import Experience from './components/Experience'
import Projects from './components/Projects'
import Contact from './components/Contact'
import ScrollProgress from './components/ScrollProgress'
import ThemeToggle from './components/ThemeToggle'
import BackToTop from './components/BackToTop'
import ParticleBackground from './components/ParticleBackground'
import './App.css'

function App() {
  return (
    <div className="App">
      <ParticleBackground />
      <ScrollProgress />
      <ThemeToggle />
      <BackToTop />
      <Header />
      <Hero />
      <About />
      <Experience />
      <Projects />
      <Contact />
    </div>
  )
}

export default App