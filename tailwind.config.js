/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Include all HTML files in templates
    './static/css/*.css', // Include all CSS files in static/css
    './static/js/*.js',   // Include all JS files in static/js
    // Add other paths as necessary
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

