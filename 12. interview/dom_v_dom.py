""" The DOM (Document Object Model) and Virtual DOM (V-DOM) are concepts related to how web pages are rendered and updated, 
but they work in different ways:

DOM (Document Object Model)
What It Is: 
The DOM is a programming interface for web documents. It represents the structure of a webpage as a tree of objects, 
where each object is a part of the document (like elements, attributes, and text).
How It Works: When a web page is loaded, the browser creates the DOM from the HTML, CSS, and JavaScript. 
The DOM is live, meaning any changes to the DOM instantly affect the web page.

Performance: 
Directly manipulating the DOM can be slow and resource-intensive, 
especially if the changes are frequent or involve large portions of the page, 
because the browser has to re-render the entire page or parts of it each time.

Virtual DOM (V-DOM)
What It Is: 
The Virtual DOM is an abstraction of the DOM, used primarily in modern front-end frameworks like React. 
It is a lightweight copy of the actual DOM that exists in memory.
