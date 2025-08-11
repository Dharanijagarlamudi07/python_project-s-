/* Project: Better Life - Multi-page Business Website Structure: /index.html /about.html /products.html /contact.html /testimonials.html /newsletter.html /css/styles.css /assets/ (images, logo) */

/* styles.css / / Save this file as /css/styles.css */

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');

{ margin: 0; padding: 0; box-sizing: border-box; } html { font-family: 'Montserrat', sans-serif; line-height: 1.6; scroll-behavior: smooth; } body { background: #fff; color: #333; } nav { background: #2C3E50; padding: 1rem; } nav ul { display: flex; list-style: none; justify-content: center; } nav ul li { margin: 0 1rem; } nav ul li a { color: #ECF0F1; text-decoration: none; font-weight: 600; } nav ul li a:hover { color: #18BC9C; } header, footer { text-align: center; padding: 2rem 1rem; } footer { background: #2C3E50; color: #ECF0F1; margin-top: 2rem; } .container { max-width: 1000px; margin: auto; padding: 2rem 1rem; } .btn { display: inline-block; background: #18BC9C; color: #fff; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 4px; font-weight: 600; transition: background 0.3s; } .btn:hover { background: #159d87; } /* Page-specific styles */ .hero { background: url('../assets/hero.jpg') center/cover no-repeat; height: 60vh; display: flex; align-items: center; justify-content: center; color: #fff; text-shadow: 1px 1px 3px rgba(0,0,0,0.7); } .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; } .card { border: 1px solid #ddd; padding: 1rem; border-radius: 4px; text-align: center; } form input, form textarea { width: 100%; padding: 0.75rem; margin-bottom: 1rem; border: 1px solid #ccc; border-radius: 4px; } form button { border: none; cursor: pointer; }


/* index.html */

<!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Better Life</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="products.html">Products</a></li>
            <li><a href="testimonials.html">Testimonials</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="newsletter.html">Newsletter</a></li>
        </ul>
    </nav>
    <header class="hero">
        <div class="container">
            <h1>Welcome to Better Life</h1>
            <p>Your source for the best Amazon products</p>
            <a href="products.html" class="btn">Shop Now</a>
        </div>
    </header>
    <footer>
        <p>&copy; 2025 Better Life. All rights reserved.</p>
    </footer>
</body>
</html><!-- about.html --><!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Us - Better Life</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>...same as index...</nav>
    <section class="container">
        <h2>About Us</h2>
        <p>Better Life is dedicated to curating high-quality products on Amazon that improve your daily life. We carefully select items in categories like home, tech, and wellness to ensure you get the best value and performance.</p>
    </section>
    <footer>...same as index...</footer>
</body>
</html><!-- products.html --><!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Products - Better Life</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>...same as index...</nav>
    <section class="container">
        <h2>Our Top Picks</h2>
        <div class="grid">
            <!-- Repeat this card structure for each product -->
            <div class="card">
                <img src="assets/product1.jpg" alt="Product 1" />
                <h3>Product 1</h3>
                <p>Short description of product 1.</p>
                <a href="#" class="btn">Buy on Amazon</a>
            </div>
            <!-- Add more cards -->
        </div>
    </section>
    <footer>...same as index...</footer>
</body>
</html><!-- testimonials.html --><!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Testimonials - Better Life</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>...same as index...</nav>
    <section class="container">
        <h2>What Our Customers Say</h2>
        <div class="grid">
            <div class="card">
                <p>“Amazing selection and fast shipping!”</p>
                <p><strong>- Jane Doe</strong></p>
            </div>
            <div class="card">
                <p>“I found exactly what I needed. Highly recommend!”</p>
                <p><strong>- John Smith</strong></p>
            </div>
        </div>
    </section>
    <footer>...same as index...</footer>
</body>
</html><!-- contact.html --><!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Better Life</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>...same as index...</nav>
    <section class="container">
        <h2>Contact Us</h2>
        <form action="#" method="post">
            <input type="text" name="name" placeholder="Your Name" required />
            <input type="email" name="email" placeholder="Your Email" required />
            <textarea name="message" rows="5" placeholder="Your Message" required></textarea>
            <button type="submit" class="btn">Send Message</button>
        </form>
    </section>
    <footer>...same as index...</footer>
</body>
</html><!-- newsletter.html --><!DOCTYPE html><html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Newsletter - Better Life</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <nav>...same as index...</nav>
    <section class="container">
        <h2>Join Our Newsletter</h2>
        <p>Stay updated on the latest product recommendations and deals.</p>
        <form action="#" method="post">
            <input type="email" name="email" placeholder="Your Email" required />
            <button type="submit" class="btn">Subscribe</button>
        </form>
    </section>
    <footer>...same as index...</footer>
</body>
</html>