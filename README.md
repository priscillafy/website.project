# Static Website Template

This is a static website template for priscillafy aiming to make creating standard HTML/CSS/JS based websites easy. The template also sets up a node server in your project directory so it's easy to view work in progress or deploy to Heroku.

Install the template by doing
`priscillafy install https://github.com/priscillafy/website.project.git`

Create a new project by doing
`priscillafy project website`

### Provided File Templates ###

**page**

Creates a new HTML page in _public/html/_

Example: `priscillafy create page awesomepage`, a new file called "awesomepage.html" will be created.

**script**

Creates a new JavaScript file in _public/js/_

Example: `priscillafy create script myscript`, a new file called "myscript.js" will be created.

**style**

Creates a new CSS style in _public/css/_

Example: `priscillafy create style funstyle`, a new file called "funstyle.css" will be created.

### Tasks ###

**start**

Starts the Node server. Visit localhost:3000/<pagename>.html in your browser to view your page.

Example: `priscillafy run start`

