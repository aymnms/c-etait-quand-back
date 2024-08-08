<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">c-etait-quand-back</h3>

  <p align="center">
Api of general culture games about invention creation dates
    <br />
    <a href="https://github.com/github_username/c-etait-quand-back/wiki"><strong>🔜 <strike>Explore the docs</strike></strong></a>
    <br />
    <a href="https://github.com/github_username/c-etait-quand-front">🔜 <strike>Front side</strike></a>
    ·
    <a href="https://github.com/aymnms/c-etait-quand-back/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/aymnms/c-etait-quand-back/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a website of general culture games about invention creation dates.
Many questions will be asked about inventions: the objective is to find the closest date!
The player with the highest score wins!

This repository contain only the back of the project: the api.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url] 
* [![Flask][Flask]][Flask-url]
* [![Sqlite][Sqlite]][Sqlite-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need to install Python and pip

### Installation

1. Clone the repo
   ```sh
   $ git clone https://github.com/aymnms/c-etait-quand-back
   ```
2. Install Pip libraries
   ```sh
   $ pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Execute this command to start the api server
```sh
$ python app.py
```

Then, you can call the api like that

**Get a random question**
```sh
$ curl http://127.0.0.1:5000/question
```

_For more examples, please refer to the [Documentation](https://github.com/aymnms/cocobot/wiki)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] MVP
  - [ ] do the database
  - [ ] GET login
  - [ ] GET logout
  - [ ] GET get random question
  - [ ] GET get question's solution
  - [ ] POST send player's answer
  - [ ] GET get all players answers
  - [ ] GET increment player score
  - [ ] GET all players score
- [ ] CI/CD

See the [open issues](https://github.com/aymnms/c-etait-quand-back/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

- [@thomassg](https://www.artstation.com/thomassg) - Graphist
- [@aymnms](https://github.com/aymnms) - Dev

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/aymnms/c-etait-quand-back.svg?style=for-the-badge
[contributors-url]: https://github.com/aymnms/c-etait-quand-back/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/aymnms/c-etait-quand-back.svg?style=for-the-badge
[forks-url]: https://github.com/aymnms/c-etait-quand-back/network/members
[stars-shield]: https://img.shields.io/github/stars/aymnms/c-etait-quand-back.svg?style=for-the-badge
[stars-url]: https://github.com/aymnms/c-etait-quand-back/stargazers
[issues-shield]: https://img.shields.io/github/issues/aymnms/c-etait-quand-back.svg?style=for-the-badge
[issues-url]: https://github.com/aymnms/c-etait-quand-back/issues
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Sqlite]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[Sqlite-url]: https://www.sqlite.org/