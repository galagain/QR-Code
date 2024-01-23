[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

# QR-Code

This tool allows for the generation of QR Codes for any given website. It creates two images: one with a white
background and another with a transparent background.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>


<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

This project requires Python and several libraries. Install them using the following commands:

```
$ pip install qrcode[pil]
$ pip install opencv-python
$ pip install numpy
```

### Installation

1. Clone the repository:

``` bash
git clone https://github.com/galagain/QR-Code.git
```

2. Navigate to the project directory.

<!-- USAGE EXAMPLES -->

## Usage

To generate a QR Code for the URL  [https://galagain.com/cv.pdf](https://galagain.com/cv.pdf), with a specific color (
e.g., magenta, represented as "255,0,255"), follow these steps:

1. Run the script from the command line with the URL and color as arguments:

``` bash
python .\generate.py "https://galagain.com/cv.pdf" --color "255,0,255"
```

2. Retrieve the generated images:

- *qr_code_transparent.png*: <img src="images/qr_code_transparent.png" width="80" height="80">
- *qr_code_white.png*: <img src="images/qr_code_white.png" width="80" height="80">


<!-- MARKDOWN LINKS -->

[contributors-url]: https://github.com/galagain/QR-Code/graphs/contributors

[forks-url]: https://github.com/galagain/QR-Code/network/members

[stars-url]: https://github.com/galagain/QR-Code/stargazers

[issues-url]: https://github.com/galagain/QR-Code/issues

[license-url]: https://github.com/galagain/QR-Code/blob/master/LICENSE.txt

[linkedin-url]: https://www.linkedin.com/in/calvin-galagain/

[contributors-shield]: https://img.shields.io/github/contributors/galagain/QR-Code.svg?style=for-the-badge

[forks-shield]: https://img.shields.io/github/forks/galagain/QR-Code.svg?style=for-the-badge

[stars-shield]: https://img.shields.io/github/stars/galagain/QR-Code.svg?style=for-the-badge

[issues-shield]: https://img.shields.io/github/issues/galagain/QR-Code.svg?style=for-the-badge

[license-shield]: https://img.shields.io/github/license/galagain/QR-Code?label=license&style=for-the-badge

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555


<!-- MARKDOWN IMAGES -->

[white-image]: images/qr_code_white.png

[transparent-image]: images/qr_code_transparent.png
