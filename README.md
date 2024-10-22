## **_Final Project of the 2024 Full Stack Test Automation Course, utilizing:_**
* Python
* Selenium
* Appium
* Pytest, etc.

[Short Video - Demonstration](https://drive.google.com/file/d/1X5k3uUw-s3gFtWCgLTit5sq33SU3n2K6/view?usp=sharing)
### **_This project was created to showcase my knowledge and skills in automation testing._**
***
### _About_
The project showcases a smart automation infrastructure designed with a modular hierarchy. 
It is organized into various modules, each containing multiple classes with relevant methods. 
Key modules include main, common, helpers, actions, and page_object, which work together 
to create a streamlined testing process.

This structure allows tests to be written with minimal lines of code, making the process straightforward and efficient. 
Additionally, the infrastructure supports integration with different types of applications, providing flexibility across various testing scenarios.
**A significant advantage of this design is its ease of maintenance, ensuring long-term scalability and adaptability!**

### _Project Overview_
The project is an example of infrastructure for automation testing of different kinds of applications:
* Desktop application
* Electron application
* Mobile application
* Web API
* Web based application
* Web DB

***

### **_Infrastructure project includes using of:_**
* Page Object Design Pattern
* Project Layers(Extensions/Work Flows/Test Cases/Configuration/DDT/Utilities...)
* Support of Different Clients/Browsers
* Failure Mechanism
* Common Functionality
* External Files Support (XML,CSV,JSON)
* Reporting System (including screenshots)
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

### _Tests Execution:_
> Each of the applications has a few tests for demonstration purpose.
These tests can be developed in a very simple way, due to a lot of work with the infrastructure.
[[Sanity Tests]]()

***

### _Known Issues:_
### _1.Mobile application testing:_
>Testing the Mortgage Calculator App:
Initially, the mortgage calculator app was tested exclusively on Android devices due to the requirement 
for an Apple developer license to distribute the app on iOS. To facilitate testing on an iPhone within our 
existing infrastructure, an Apple developer license needs to be acquired, and the device's unique identifier (UUID) 
must be provided. No changes to the app's code are necessary for this process.

### _2. Resolving Conflicts Between Applications Under Test (AUT)::_
>Occasionally, conflicts arise when applications share the same dependencies, such as using identical ports. For instance, 
both a mobile application and a desktop application might be set to use port 4723. To resolve this conflict, 
the mobile application's port was changed to 4724, eliminating the dependency issue.