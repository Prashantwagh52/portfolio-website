import React, { useState } from 'react'
import './Contact.css'

const Contact = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  })

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    // Handle form submission here
    console.log('Form submitted:', formData)
    alert('Thank you for your message! I\'ll get back to you soon.')
    setFormData({ name: '', email: '', message: '' })
  }

  const contactInfo = [
    {
      icon: '📧',
      label: 'Email',
      value: 'waghprashant6563@gmail.com',
      link: 'mailto:waghprashant6563@gmail.com'
    },
    {
      icon: '📱',
      label: 'Phone',
      value: '+91-9420952286',
      link: 'tel:+919420952286'
    },
    {
      icon: '📍',
      label: 'Location',
      value: 'Hyderabad, India',
      link: '#'
    }
  ]

  const socialLinks = [
    { name: 'LinkedIn', icon: '💼', url: 'https://linkedin.com/in/prashant-wagh-sonar-1982a4214' },
    { name: 'GitHub', icon: '🐙', url: 'https://github.com/prashant-wagh' },
    { name: 'Email', icon: '📧', url: 'mailto:waghprashant6563@gmail.com' }
  ]

  return (
    <section id="contact" className="section">
      <div className="container">
        <h2 className="section-title">Get In Touch</h2>
        <div className="contact-content">
          <div className="contact-info">
            <h3>Let's Work Together</h3>
            <p>
              I'm always interested in new opportunities in Full Stack Java Development. 
              Whether you have a project idea or want to discuss technology, feel free to reach out!
            </p>
            
            <div className="contact-details">
              {contactInfo.map((info, index) => (
                <a key={index} href={info.link} className="contact-item">
                  <span className="contact-icon">{info.icon}</span>
                  <div>
                    <span className="contact-label">{info.label}</span>
                    <span className="contact-value">{info.value}</span>
                  </div>
                </a>
              ))}
            </div>

            <div className="social-links">
              <h4>Follow Me</h4>
              <div className="social-grid">
                {socialLinks.map((social, index) => (
                  <a 
                    key={index}
                    href={social.url}
                    className="social-link"
                    target="_blank"
                    rel="noopener noreferrer"
                    title={social.name}
                  >
                    <span className="social-icon">{social.icon}</span>
                    <span className="social-name">{social.name}</span>
                  </a>
                ))}
              </div>
            </div>
          </div>

          <form className="contact-form card" onSubmit={handleSubmit}>
            <h3>Send Message</h3>
            <div className="form-group">
              <input
                type="text"
                name="name"
                placeholder="Your Name"
                value={formData.name}
                onChange={handleChange}
                required
                className="form-input"
              />
            </div>
            <div className="form-group">
              <input
                type="email"
                name="email"
                placeholder="Your Email"
                value={formData.email}
                onChange={handleChange}
                required
                className="form-input"
              />
            </div>
            <div className="form-group">
              <textarea
                name="message"
                placeholder="Your Message"
                value={formData.message}
                onChange={handleChange}
                required
                rows="5"
                className="form-input"
              ></textarea>
            </div>
            <button type="submit" className="btn btn-primary submit-btn">
              Send Message
            </button>
          </form>
        </div>
      </div>
    </section>
  )
}

export default Contact