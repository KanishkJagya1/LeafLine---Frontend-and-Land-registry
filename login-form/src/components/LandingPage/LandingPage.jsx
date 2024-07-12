import React from 'react';
import './LandingPage.css';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <header className="header">
        <nav className="navbar">
          <a href="#home" className="logo">Greenify</a>
          <ul className="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#products">Products</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
        <div className="header-content">
          <h1>Welcome to Greenify</h1>
          <p>Your Sustainable Shopping Destination</p>
          <a href="#products" className="btn">Shop Now</a>
        </div>
      </header>

      <section className="features" id="features">
        <h2>Why Choose Greenify?</h2>
        <div className="feature-cards">
          <div className="feature-card">
            <i className="feature-icon"></i>
            <h3>Sustainable Products</h3>
            <p>Eco-friendly and sustainably sourced products.</p>
          </div>
          <div className="feature-card">
            <i className="feature-icon"></i>
            <h3>High Quality</h3>
            <p>Products that meet high-quality standards.</p>
          </div>
          <div className="feature-card">
            <i className="feature-icon"></i>
            <h3>Customer Support</h3>
            <p>Reliable and friendly customer service.</p>
          </div>
        </div>
      </section>

      <section className="products" id="products">
        <h2>Our Best-Selling Sustainable Products</h2>
        <div className="product-cards">
          <div className="product-card">
            <img src="product1.jpg" alt="Product 1" />
            <h3>Organic Cotton Tote Bag</h3>
            <p>$25.00</p>
          </div>
          <div className="product-card">
            <img src="product2.jpg" alt="Product 2" />
            <h3>Hemp Backpack</h3>
            <p>$45.00</p>
          </div>
          <div className="product-card">
            <img src="product3.jpg" alt="Product 3" />
            <h3>Bamboo Utensil Set</h3>
            <p>$15.00</p>
          </div>
        </div>
      </section>

      <section className="reviews" id="reviews">
        <h2>Customer Reviews</h2>
        <div className="review-cards">
          <div className="review-card">
            <p>"Excellent products and customer service!"</p>
            <h3>Sarah Johnson</h3>
          </div>
          <div className="review-card">
            <p>"I love their sustainable approach."</p>
            <h3>Mike Anderson</h3>
          </div>
          <div className="review-card">
            <p>"Highly recommend Greenify!"</p>
            <h3>Laura Lee</h3>
          </div>
        </div>
      </section>

      <section className="blog" id="blog">
        <h2>Latest Blog Posts</h2>
        <div className="blog-cards">
          <div className="blog-card">
            <img src="blog1.jpg" alt="Blog 1" />
            <h3>Eco-Friendly Living Tips</h3>
            <p>Learn how to live a more sustainable life.</p>
          </div>
          <div className="blog-card">
            <img src="blog2.jpg" alt="Blog 2" />
            <h3>Guide to Sustainable Shopping</h3>
            <p>Discover the best eco-friendly products.</p>
          </div>
          <div className="blog-card">
            <img src="blog3.jpg" alt="Blog 3" />
            <h3>Recycling Tips and Tricks</h3>
            <p>Improve your recycling habits with these tips.</p>
          </div>
        </div>
      </section>

      <footer className="footer" id="contact">
        <div className="footer-content">
          <h3>Subscribe to our Newsletter</h3>
          <form className="newsletter-form">
            <input type="email" placeholder="Enter your email" />
            <button type="submit" className="btn">Subscribe</button>
          </form>
          <p>Contact us: info@greenify.com | +1 234 567 890</p>
          <p>&copy; 2024 Greenify. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default LandingPage;