# Book Review App - Data centric development</h1>

!Remove development server before deploying

Book Review App
 
The user is presented with a list of books, they can read and write reviews and have access to links to buy the books they may like.
 
* [Live link to site](https://book-review-kelvinhere.herokuapp.com/ 'Heroku live link to app')
* [This Repository](https://github.com/KelvinHere/book-review-app 'Github repository link')
 
## Contents
 
1. [**UX**](#ux)
   * [**Project Purpose**](#project-purpose)
   * [**Wireframe Designs**](#wireframe-designs)
   * [**User Stories**](#user-stories)
   * [**Business and Developer Goals**](#business-and-developer-goals)
   * [**Design Choices**](#design-choices)   
       * [*Colours and Fonts*](#colours-and-fonts)
2. [**Features**](#features)
   * [**Existing Features**](#existing-features)
   * [**Future Features**](#future-features)
       * [*Near Future*](#near-future)
       * [*Far Future*](#far-future)
3. * [**Changes in Development**](#changes-in-development)
4. * [**Testing**](#testing)
5. * [**Technologies Used**](#technologies-used)
6. * [**Deployment**](#deployment)
7. * [**Credits**](#credits)
       * [**Content**](#content)
       * [**Media**](#media)
       * [**Acknowledgements**](#acknowledgements)

## UX
 
#### Project Purpose

The purpose of this project is to create an application where poeple can review books they have read.

Using this app you will be able to  :-

- Create
    - A book
    - A review with a score

- Read 
    - A list of books and sort them by Title, Author and Rating
    - The average score from a book
    - A list of reviews and their scores

- Update
    - A books information

- Delete 
    - A book from the database
    - A review from a book


#### Wireframe Designs

#### User Stories

#### Business and Developer Goals

The business purpose of this app is to engage the user with a list of books they can enjoy, if a user likes a book they will be able to buy it from an affiliate link, earning the owner of the link money.

Each feature must be well programmed, function properly and be bug free.  This will display a professional use of the programming language and test suite.
 
Defensive programming must be used to avoid users destroying or corrupting the databse via bad input.

This milestone project will show an understanding of Flask, Python, MongoDB, Javascript, jQuery, HTML, CSS, the DOM and how they all interact to form a final product.
 
#### Design Choices
 
##### Colours and Fonts

## Features
 
### Existing Features

Books average score only updates when a new review for that book is added

### Future Features
 
##### Near Future

- Add sort by genre feature

##### Far Future

### Changes in Development

## Testing
 
TESTING LINK HERE

## Technologies Used

NOT YET UPDATED

- **HTML5/CSS3** - Languages
   - Industry standard web development
- [Javascript](https://www.javascript.com/) - Programming Language
   - Used to create the logic for the matching game.
- [jQuery](https://jquery.com/) - JavaScript Library
   - Used to simplify DOM traversal and manipulation
- [Jasmin](https://jasmine.github.io/) - Testing
   - A behavior-driven development framework for testing JavaScript code.
- [Gitpod](https://www.gitpod.com) - IDE
   - Used for its one stop contained development workflow via browser
- [Git](https://git-scm.com/) - Version-control system
   - Used to version control the project
- [Github](https://www.github.com) - Code hosting platform
   - Was used for its robust repository system and ability to view website through **GitHub Pages**
- [Draw.io](https://www.draw.io/) - Wireframing tool
   - Used for rapid wireframe prototyping
- [GNU Image Manipulation Program](https://www.gimp.org/) - Image editing software
   - Used to edit images for the website
 
## Deployment

### Prerequisites
`pip3 install flask`
`pip3 install flask-pymongo`
`pip3 install dnspython`

UPDATE TO HEROKU DEPLOYMENT

This project was created in Git Pod and version controlled through 'Git', the project was committed and pushed to GitHub where it is hosted through GitHub Pages.
 
The deployed version of Pairs was hosted on GitHub Pages using the following steps :-
 
1. Login to KelvinHere on [GitHub](https://github.com/).
2. Select the [Milestone-Interactive](https://github.com/KelvinHere/Milestone-Interactive) repository.
3. Select 'Settings' for this repository and scroll down to Github Pages.
4. Click 'Source' and change the source to be the master branch.
5. A link will appear this is the address of the live page, changes can take up to 5-10 minutes to appear.
 
Add this repository to your local workspace by :-
 
1. Opening the [Milestone-Interactive](https://github.com/KelvinHere/Milestone-Interactive) repository.
2. Click the green 'Code' button and then copy the 'Clone with HTTPS' URL.
3. In your local workspace open a terminal.
4. From inside the directory you want to copy the clone to, type `git clone` and paste the URL you copied from GitHub then press enter.  Example below.
 
`git clone https://github.com/KelvinHere/example.git`
 
5. Cloning will be completed when your terminal is waiting for its next command.
6. For more information or changes in the cloning procedure [>Click Here<](https://github.com/git-guides/git-clone)

Project Development :-
* This project was developed using GitPod.
* After files are created or modified they are committed to a GitHub repository by :-
    - adding the modified files locally using `git add .`
    - commiting the modified files with a message of changes using `git commit -m "changes here"`
    - pushing the new commit to the master branch on GitHub repository with `git push`

* During development a new branch on GitHub was created via pull request.  This was for a major change to the code (the game board was refactored to an object) and allowed experimentation without affecting the master branch.  This new branch worked out well and was merged into the master branch.

## Credits
### Content
 
- This project was created by KelvinHere
 
### Media

### Acknowledgements

* [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/).
* [Code Institute](https://codeinstitute.net/).
* My mentor Spencer.