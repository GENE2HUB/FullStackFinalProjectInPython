## **Full Stack Test Automation Final Project with Python, Selenium, Appium, Pytest e.t.c**
[Short Video - Demonstration]()
### **_This project created to demonstrate my knowledge and skills in Automation Testing._**
***
### _About_
The project demonstrates a smart automation infrastructure. It is built in hierarchy order of modules. 
The modules contain number of classes with methods.
There are main/common/helpers/actions/page_object modules.
In this way, the tests can be created in very simple way with a minimum lines of code.
Also the infrastructure allows to work with different kinds of applications.
**Big advantage of the infrastructure is that it can be easy maintained!**

### _Project Overview_

The project is an example of infrastructure for automation testing of different kinds of applications:
* Web based application
* Mobile application
* Web API
* Electron application
* Desktop application

***

### **_Infrastructure project includes using of:_**
* Page Object Design Pattern
* Project Layers(Extensions/Work Flows/Test Cases...)
* Support of Different Clients/Browsers
* Failure Mechanism
* Common Functionality
* External Files Support (XML,CSV)
* Reporting System (including screenshots)
* Visual Testing
* DB support
* CI support  

***

### _List of applications were used in this project:_
* Web based application: Grafana webpage
* Mobile application: Mortgage calculator
* Web API: Grafana API
* Electron application: Todolist
* Desktop application: Windows calculator

***

### _Tools & Frameworks used in the project:_
* Testing Framework: Pytest
* Listeners: interface used to generate logs and customize the Pytest reports
* MySQL Free Online DB: used for login to Grafana web page
* [Jenkins](https://www.jenkins.io/)- for tests execution trigger by schedule and job
* REST Assured: for API testing
* [Allure]() Reports - as the main reporting system

***

### Tests Execution:
> Each of the applications has a few tests for demonstration purpose.
These tests can be developed in a very simple way, due to a lot of work with the infrastructure.
[[Sanity Tests]]()

***

### _Known Issues:_
* Sometimes can be conflicts with some dependencies the applications are using.
Hence, the project is for DEMO purpose only. 
* In production it should be divided into several projects.
* The mortgage calculator app was initially tested exclusively on Android devices 
due to the need for an Apple developer license to distribute on iOS. 
However, to test the app on an iPhone within our existing infrastructure, 
simply acquire an Apple developer license and provide the device's unique identifier (UUID). 
No modifications to the app's code are required.
