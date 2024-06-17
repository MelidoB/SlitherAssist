<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [x] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/MelidoB/SlitherAssist">
    <img src="https://github.com/MelidoB/SlitherAssist/blob/feature/integrate-dynamic-cursor/assets/Logo.webp" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">SlitherAssist</h3>

[![Download SlitherAssist v1.1.0](https://img.shields.io/badge/Download-v1.1.0-blue?style=for-the-badge&logo=github)](https://github.com/MelidoB/SlitherAssist/releases/tag/v1.1.0)]

<p></p>
  <p>
    SlitherAssist improves Slither.io control when using a controller. It keeps the cursor near your snake's head for better responsiveness. Connect your controller using tools like reWASD to map it to mouse movements.


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
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]][Python-url]
* [![PyQt5][PyQt5]][PyQt5-url]
* [![Pynput][Pynput]][Pynput-url]
* [![PyInstaller][PyInstaller]][PyInstaller-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow these steps to set up the `SlitherAssist` project locally.

### Prerequisites

Make sure you have the following installed on your system:

* [Python](https://www.python.org/downloads/) (Version 3.6 or above)
* [Git](https://git-scm.com/)

## Installation

To set up `SlitherAssist` on your local machine, follow these steps:

1. **Clone the Repository**:
   - Open a terminal or command prompt.
   - Run the following command to clone the `SlitherAssist` repository:
     ```bash
     git clone https://github.com/MelidoB/SlitherAssist.git
     ```

2. **Navigate to the Project Directory**:
   - Change into the project directory:
     ```bash
     cd SlitherAssist
     ```

3. **Create a Virtual Environment**:
   - Create a virtual environment named `env` to manage dependencies:
     ```bash
     python -m venv env
     ```

4. **Activate the Virtual Environment**:
   - Activate the virtual environment to use isolated Python packages:
     - On Windows:
       ```bash
       env\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source env/bin/activate
       ```

5. **Install Required Dependencies**:
   - Use `pip` to install all necessary packages listed in the `requirements.txt` file:
     ```bash
     pip install -r requirements.txt
     ```

6. **Run the Application**:
   - Start the `SlitherAssist` application by executing:
     ```bash
     python Gui.py
     ```


<!-- USAGE EXAMPLES -->
## Usage

Below are examples demonstrating how to use SlitherAssist effectively:

### Showing Interface Working
![SlitherAssist Interface](https://github.com/MelidoB/SlitherAssist/blob/feature/integrate-dynamic-cursor/assets/SlitherAssist_Interface.gif?raw=true)

### In-Game Usage
![SlitherAssist In Game](https://github.com/MelidoB/SlitherAssist/blob/feature/integrate-dynamic-cursor/assets/SlitherAssist_In_Game.gif?raw=true)

### Winning with SlitherAssist
![SlitherAssist Winning](https://github.com/MelidoB/SlitherAssist/blob/feature/integrate-dynamic-cursor/assets/SlitherAssist_Winning.gif?raw=true)

These GIFs show how SlitherAssist enhances your Slither.io gameplay by keeping the cursor close to the snake’s head and providing smoother control.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

### v1.0.0 - Initial Release
- [x] Integrate Dynamic Cursor functionality to keep the mouse close to the snake's head for smoother control.
- [x] Enable automatic cursor adjustments to improve gameplay responsiveness.
- [x] Implement system tray minimization to keep the desktop organized.
- [x] Provide easy setup and installation instructions.

### Planned Features
- **v1.1.0**: Customizable Cursor Images
  - Add the ability to change and customize the cursor images used in SlitherAssist.
  - Include a settings option for users to select their preferred cursor style.

See the [open issues](https://github.com/MelidoB/SlitherAssist/issues) for a full list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are welcome and appreciated! To contribute to `SlitherAssist`, follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top of the repository page.

2. **Create a Branch**: 
   ```bash
   git checkout -b feature/YourFeatureName
Make Your Changes: Implement your changes or new features.

Commit Your Changes:

bash
Copy code
git commit -m 'Add feature: YourFeatureName'
Push to Your Fork:

bash
Copy code
git push origin feature/YourFeatureName
Open a Pull Request: Go to the original repository and click "New Pull Request" to submit your changes for review.

For any suggestions or to report bugs, please open an issue with the relevant tag.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact
<p>Melido Bello - mbellon000@citymail.cuny.edu</p>

Project Link: [https://github.com/MelidoB/SlitherAssist](https://github.com/MelidoB/SlitherAssist)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

- **Team Members**: 
  - Melido Bello

- **Resources**:
  - [Python Documentation](https://docs.python.org/3/) - For comprehensive Python language documentation.
  - [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/) - For building graphical interfaces with PyQt5.
  - [Pynput Documentation](https://pynput.readthedocs.io/en/latest/) - For controlling and monitoring input devices.
  - [PyInstaller Documentation](https://pyinstaller.readthedocs.io/en/stable/) - For packaging Python applications into standalone executables.
  - [Dynamic Cursor in PyQt5 Video Tutorial](https://www.youtube.com/watch?v=-a4XPffa8Xg) - A tutorial on creating a dynamic cursor using PyQt5.

- **Tools**:
  - [Visual Studio Code](https://code.visualstudio.com/) - A powerful and versatile code editor.
  - [GitHub](https://github.com/) - For version control and project hosting.
  - [GIMP](https://www.gimp.org/) - For creating and editing images and icons.
  - [Git](https://git-scm.com/) - For tracking changes and collaborating on code.
  - [ImageTools](https://www.imagetools.org/trim) - For trimming images easily.
  - [Remove.bg](https://www.remove.bg/upload) - For removing image backgrounds quickly.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/MelidoB/SlitherAssist/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/MelidoB/SlitherAssist/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/MelidoB/SlitherAssist/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/MelidoB/SlitherAssist/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/MelidoB/SlitherAssist/blob/master/LICENSE.txt

[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[PyQt5]: https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=Qt&logoColor=white
[PyQt5-url]: https://riverbankcomputing.com/software/pyqt/intro
[Pynput]: https://img.shields.io/badge/Pynput-4C4C4C?style=for-the-badge
[Pynput-url]: https://pypi.org/project/pynput/
[PyInstaller]: https://img.shields.io/badge/PyInstaller-00C8FF?style=for-the-badge&logo=pyinstaller&logoColor=white
[PyInstaller-url]: https://www.pyinstaller.org/
