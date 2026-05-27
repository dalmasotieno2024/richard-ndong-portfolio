<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Richard Owino Ndong | General Contractor</title>
    <style>
        /* Modern, Clean Construction Theme Styling */
        :root {
            --primary: #d97706; /* Construction Amber */
            --dark: #1e293b;
            --light: #f8fafc;
            --gray: #64748b;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }

        /* Header & Navigation */
        header {
            background-color: var(--dark);
            color: white;
            padding: 1.5rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }

        .nav-container {
            max-width: 1100px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }

        .logo h1 {
            font-size: 1.5rem;
            color: white;
        }
        .logo span {
            color: var(--primary);
        }

        /* Hero Section */
        .hero {
            background: linear-gradient(rgba(30, 41, 59, 0.85), rgba(30, 41, 59, 0.9)), Helvetica, Arial, sans-serif;
            color: white;
            padding: 5rem 1.5rem;
            text-align: center;
        }

        .hero-content {
            max-width: 800px;
            margin: 0 auto;
        }

        .hero h2 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            color: #cbd5e1;
            margin-bottom: 1.5rem;
        }

        .badge {
            background-color: var(--primary);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            display: inline-block;
            font-weight: bold;
        }

        /* Main Content Container */
        .container {
            max-width: 1100px;
            margin: 3rem auto;
            padding: 0 1.5rem;
        }

        .section-title {
            text-align: center;
            margin-bottom: 2rem;
            position: relative;
            padding-bottom: 0.5rem;
        }

        .section-title::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 60px;
            height: 4px;
            background-color: var(--primary);
            border-radius: 2px;
        }

        /* Project Grid (Responsive) */
        .project-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .card {
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            border-top: 4px solid var(--primary);
            transition: transform 0.2s;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        .card-body {
            padding: 1.5rem;
        }

        .card-category {
            font-size: 0.8rem;
            text-transform: uppercase;
            font-weight: bold;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }

        .card-title {
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }

        .card-location {
            font-size: 0.9rem;
            color: var(--gray);
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
        }

        /* Contact Section */
        .contact-section {
            background-color: #e2e8f0;
            padding: 3rem 1.5rem;
            text-align: center;
            border-radius: 8px;
            margin-top: 4rem;
        }

        .contact-btn {
            display: inline-block;
            background-color: var(--dark);
            color: white;
            padding: 0.75rem 2rem;
            text-decoration: none;
            border-radius: 4px;
            font-weight: bold;
            margin-top: 1rem;
            transition: background 0.2s;
        }

        .contact-btn:hover {
            background-color: var(--primary);
        }

        /* Footer */
        footer {
            background-color: var(--dark);
            color: #94a3b8;
            text-align: center;
            padding: 2rem;
            margin-top: 4rem;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

    <header>
        <div class="nav-container">
            <div class="logo">
                <h1>Mr. Richard <span>Owino Ndong</span></h1>
            </div>
            <div class="badge">General Contractor</div>
        </div>
    </header>

    <section class="hero">
        <div class="hero-content">
            <h2>Reliable Construction & Infrastructure Services</h2>
            <p>Based in Homa Bay County, delivering quality classrooms, sanitation structures, and security fencing across Homa Bay and Migori Counties.</p>
        </div>
    </section>

    <main class="container">
        <h2 class="section-title">Completed Work & Projects</h2>
        <div class="project-grid" id="project-container">
            <p style="text-align: center; grid-column: 1/-1;">Loading expert projects...</p>
        </div>

        <section class="contact-section">
            <h2>Have a Project in South Nyanza?</h2>
            <p>Reach out to Mr. Richard Owino Ndong for top-quality construction work, extensions, or structural fencing.</p>
            <a href="tel:+254700000000" class="contact-btn">Call to Discuss Project</a>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 Mr. Richard Owino Ndong. All Rights Reserved. Built for Homa Bay & Migori Contracting.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // Fetch the external CSV file
            fetch('projects.csv')
                .then(response => {
                    if (!response.ok) {
                        throw new Error("Could not find projects.csv file");
                    }
                    return response.text();
                })
                .then(csvText => {
                    parseAndDisplayCSV(csvText);
                })
                .catch(error => {
                    console.error("Error loading CSV:", error);
                    document.getElementById('project-container').innerHTML = 
                        `<p style="color: red; text-align: center; grid-column: 1/-1;">Error loading data file. Please ensure projects.csv is uploaded.</p>`;
                });
        });

        function parseAndDisplayCSV(text) {
            const lines = text.split('\n').map(line => line.trim()).filter(line => line.length > 0);
            const container = document.getElementById('project-container');
            container.innerHTML = ''; // Clear loading message

            // Skip headers loop through the rest
            for (let i = 1; i < lines.length; i++) {
                // Quick CSV row parser that respects quotation marks for commas
                const row = parseCSVRow(lines[i]);
                
                if (row.length >= 4) {
                    const [title, location, category, description] = row;

                    // Create the HTML structural element for the project card
                    const card = document.createElement('div');
                    card.className = 'card';
                    card.innerHTML = `
                        <div class="card-body">
                            <div class="card-category">${escapeHTML(category)}</div>
                            <h3 class="card-title">${escapeHTML(title)}</h3>
                            <div class="card-location">📍 ${escapeHTML(location)}</div>
                            <p class="card-text">${escapeHTML(description)}</p>
                        </div>
                    `;
                    container.appendChild(card);
                }
            }
        }

        // Helper function to handle standard CSV split nuances safely
        function parseCSVRow(text) {
            let p = '', r = [];
            let q = false;
            for (let i = 0; i < text.length; i++) {
                let c = text[i];
                if (c === '"') { q = !q; }
                else if (c === ',' && !q) { r.push(p); p = ''; }
                else { p += c; }
            }
            r.push(p);
            return r;
        }

        // Helper to prevent script injection vulnerabilities
        function escapeHTML(str) {
            return str.replace(/[&<>'"]/g, 
                tag => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;' }[tag] || tag)
            );
        }
    </script>
</body>
</html>