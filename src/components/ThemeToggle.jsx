import React, { useState, useEffect } from 'react'
import './ThemeToggle.css'

const ThemeToggle = () => {
  const [isDark, setIsDark] = useState(false)

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme')
    if (savedTheme === 'dark') {
      setIsDark(true)
      document.body.classList.add('dark-theme')
    }
  }, [])

  const toggleTheme = () => {
    setIsDark(!isDark)
    if (!isDark) {
      document.body.classList.add('dark-theme')
      localStorage.setItem('theme', 'dark')
    } else {
      document.body.classList.remove('dark-theme')
      localStorage.setItem('theme', 'light')
    }
  }

  return (
    <button className="theme-toggle" onClick={toggleTheme}>
      <div className={`toggle-slider ${isDark ? 'dark' : ''}`}>
        <span className="toggle-icon">
          {isDark ? '🌙' : '☀️'}
        </span>
      </div>
    </button>
  )
}

export default ThemeToggle