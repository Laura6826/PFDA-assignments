# Programming for Data Analytics 24-25: 4369

## Assignments submitted as part of the module Programming for Data Analytics 24-25: 4369., Higher Diploma in Science, Data Analytics

## *Author: Laura Lyons*

***

This README file was written using the [GitHub's documentation on READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) as a guidance document
***

  &#x26a0;&#xfe0f; **DISCLAIMER**

  Microsoft Co-Pilot was used to generate ideas of the content of the following notebook. That said, the notebook is mainly my own work, as I had to re-work the code the text in generated to meet my own needs.(*The warning icon was sourced from [Stackoverflow](https://stackoverflow.com/questions/50544499/how-to-make-a-styled-markdown-admonition-box-in-a-github-gist)*)

## **Table of contents**

1. [Introduction.](#1-introduction).
1. [The purpose of this project.](#2-the-purpose-of-this-project)
1. [How to get started.](#3-how-to-get-started)
1. [How to get help.](#4-how-to-get-help)
1. [How to contribute.](#5-how-to-contribute)
1. [Weekly Assignment.](#6-weekly-assignments)

    1. [Assignment 01- Create Directory Structure](#assignment-01---create-directory-structure)
    2. [Assignment 02- Weather](#assignment-02---weather)
    3. [Assignment 03- Domains](#assignment-03---domains)
    5. [Assignment 05- Risk](#assignment-05--risk)
    6. [Assignment 06- Knock airport Weather](#assignment-06---knock-airport-weather)

## 1. Introduction

This project was created to fufill an assessment requirement of Programming for Data Analytics 24-25: 4369, as part of the H.Dip in Science in Data Analytics.

Each week, following a series of lectures, an assignment was set, to demonstrate both learning and additional reading/research on the topics discussed in the lectures.

This repository is collection of my weekly assignments, including some additional guidance and instruction in how to run each Assignment/program.

***

## 2. The purpose of this project

As noted on the [assignment instructions](https://vlegalwaymayo.atu.ie/course/view.php?id=10462#section-3),

The purpose of the assessment is to ensure students can demonstrate the following:

1. Programmatically create plots and other visual outputs from data.
1. Design computer algorithms to solve numerical problems.
1. Create software that incorporates and utilises standard numerical libraries.
1. Employ appropriate data structures when programming for data-intensive applications.

## 3. How to get started

### Necessary software

In order to run the included files, you will need to ensure that you have access to the correct softwear. I would recommend downloading the following applications (ensuring sufficent space on your hard drive prior to installation):

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) (if Anaconda is too large, miniconda would also suffice).
2. [Visual Studio Code](https://code.visualstudio.com/Download) (this is a code editor).

### **Additions to** *.gitignore*

A number of [additional files](https://github.com/github/gitignore/tree/main/Global) were added to my .gitignore prior to running the programmes:

  1. python.gitignore
  2. macOS..gitignore
  3. VisualStudioCode.gitignore
  4. Linux.gitignore
  5. TeX.gitignore
  6. Vim.gitignore
  7. Windows.gitignore

## How to run the Notebook

### Using Using Visual Studio Code & Anaconda or GitHub Codespaces

**Clone the Repository**:

```ruby
   git clone https://github.com/Laura6826/PFDA-project
```

**Install the required packages**:

For a seamless excutition, I would also recommend you have access to the below libraries prior to running the files. The libraries required to run this file (as noted below), can be installed with the following code:

```ruby
pip install -r requirements.txt
```

,or you can manually install each of the libraries below.+

```ruby
  import pandas as pd
  import numpy as np
  import matplotlib.pyplot as plt
  import seaborn as sns
  import scipy
```

***

### Open the notebook in Visual Studio Code

- Open Visual Studio Code.
- Open the `computer_infrastructure_assignments` folder.
- Open the folder associated with the assignment you wish to look at.

## 4. How to get help

I have attached below,a number of helpful links, should you wish to extrapolate on any of the methods used within this project.

1. [Anaconda](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf)
1. [Visual Studio Code](https://code.visualstudio.com/Download)
1. [w3schools](https://www.w3schools.com/)
1. [Pandas](https://pandas.pydata.org/)
1. [Numpy](https://numpy.org/)
1. [Matplotlib.py](https://matplotlib.org/)
1. [Seaborn](https://seaborn.pydata.org/)

Additionally, a number of links are embedded within the code, in areas that i found confussing/difficult, that should help should there be any difficulty.

## 5. How to contribute

As this project was created to fufill an assessment requirement of the Principles of Data Analytics, as part of the H.Dip in Science in Data Analytics, no contributions will be allowed, in order to comply with ATU Policy on [Plagiarism](https://www.atu.ie/sites/default/files/2024-02/aqae022-academic-integrity-policy-1.pdf) and the [Student Code of Conduct](https://www.atu.ie/sites/default/files/2022-08/Student%20Code_Final_August_2022.pdf).

Should you find any errors or have any recommendations , please submit a pull request on Github. or just wish to contact that author, you can do so at <maxwell6826@gmail.com>.

***

## **6. Weekly Assignments**

## **Assignment 01** - Create Directory Structure

**Assignment Instructions:**

Create a repository for this module, and upload a link to where you will put your handups.

You have a Choice of the format of your repositories, Either:

1. One repository with three folders (assignments, mywork, project). Make sure you submit a link to the appropriate folder.
1. Three separate repositories (PFDA-assignments, PFDA-mywork, PFDA-project). Make sure you submit a link to the appropriate repository

***

## **Assignment 02** - Weather

**Assignment Instructions:**

Task 1: Commit something to your assignment repository this week (anything)

Task 2: I have put a CSV file in a assignment folder in the PFDA-courseware repository

Create a jupyter notebook called `assignment2-weather.ipynb` that has a nice plot of the temperature over time

```ruby
dryBulbTemperature_Celsius
```

### Associated Code

#### Task 1

```ruby
print("Hello World!")
```

#### Task 2

The notebook created to fulfill this part of the assignment can be located [here](https://github.com/Laura6826/PFDA-assignments/blob/main/assignment02/assignment2-weather.ipynb)

**My notes:**

The data needed to be manipulated as it contained both the data and time, while we only required the time. This is the [code](https://stackoverflow.com/questions/35595710/splitting-timestamp-column-into-separate-date-and-time-columns) necessary to complete this task.

The plot was initally generated using Matplotlib and afterwards on Seaborn.

***

## **Assignment 03** - Domains

**Assignment Instructions:**

Create a notebook called `assignment03-pie.ipynb`.

The note book should have a nice pie chart of peoples email domains in the [csv file](https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download).

**My notes:**

The notebook associated with assignment 3 can be found [here](https://github.com/Laura6826/PFDA-assignments/blob/main/assignment03/assignment03-pie.ipynb), and the pie chart generated is below.

![assignment 3, pie chart](https://github.com/Laura6826/PFDA-assignments/blob/main/assignment03/images/assignment03.jpg)

***

## **Assignment 05** -Risk

**Assignment Instructions:**

### Basic

- Write a program (or notebook) called `assignment_5_risk` (.py or .ipynb).
- The program should simulates 1000 individual battle rounds in Risk (3 attacker vs 2 defender) and plots the result.
- One battle round is one shake of the attacker and defender dice.

### Extra

- A more complicated version simulates a full series of rounds for armies of arbitrary sizes, until one side is wiped out, and plots the results.

**My notes:**

- For the basic game of risk, we predefine a battle to 1000 rounds.
- For the 'extra' part of the task, the player is prompted to enter the size of the attacker army and the defenders army.
- There is a lot of comments in this assignment, as it was very difficult and it was necessary to note each step as it was complete, so it would be easier to tweek as it was developing.
- Microscoft Copilot was used during this assignment to help debg difficult parts of the code.

***

## **Assignment 06** - Knock airport Weather

**Assignment Instructions:**

- Create a python file or notebook called assignment_6_Weather (.py or .ipynb)
- Get the data from this [link](https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv).

Plot:

1. The temperature
2. The mean temperature each day
3. The mean temperature for each month
4. The Windspeed (there is data missing from this column)
5. The rolling windspeed (say over 24 hours)
6. The max windspeed for each day
7. The monthly mean of the daily max windspeeds (yer I am being nasty here)

**My notes:**

The Jupyter notebook associated with this assignment can be found [here](https://github.com/Laura6826/PFDA-assignments/blob/main/assignment06/assignment_6_weather.ipynb)

***

### End
