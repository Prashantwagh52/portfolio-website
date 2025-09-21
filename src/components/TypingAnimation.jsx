import React, { useState, useEffect } from 'react'
import './TypingAnimation.css'

const TypingAnimation = ({ texts, speed = 100, deleteSpeed = 50, pauseTime = 2000 }) => {
  const [currentTextIndex, setCurrentTextIndex] = useState(0)
  const [currentText, setCurrentText] = useState('')
  const [isDeleting, setIsDeleting] = useState(false)

  useEffect(() => {
    const timeout = setTimeout(() => {
      const fullText = texts[currentTextIndex]
      
      if (isDeleting) {
        setCurrentText(fullText.substring(0, currentText.length - 1))
      } else {
        setCurrentText(fullText.substring(0, currentText.length + 1))
      }

      if (!isDeleting && currentText === fullText) {
        setTimeout(() => setIsDeleting(true), pauseTime)
      } else if (isDeleting && currentText === '') {
        setIsDeleting(false)
        setCurrentTextIndex((prevIndex) => (prevIndex + 1) % texts.length)
      }
    }, isDeleting ? deleteSpeed : speed)

    return () => clearTimeout(timeout)
  }, [currentText, isDeleting, currentTextIndex, texts, speed, deleteSpeed, pauseTime])

  return (
    <span className="typing-animation">
      {currentText}
      <span className="cursor">|</span>
    </span>
  )
}

export default TypingAnimation