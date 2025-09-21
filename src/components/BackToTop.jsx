import React, { useState, useEffect } from 'react'
import './BackToTop.css'

const BackToTop = () => {
  const [isVisible, setIsVisible] = useState(false)

  useEffect(() => {
    const handleScroll = () => {
      setIsVisible(window.scrollY > 300)
    }

    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }

  return (
    <button 
      className={`back-to-top ${isVisible ? 'visible' : ''}`}
      onClick={scrollToTop}
    >
      <span className="arrow">↑</span>
    </button>
  )
}

export default BackToTop