# Project Statement: Simple-Diet-Tracker

## 1. Problem Statement

Many available diet tracking applications are often overly complex, rely on subscription models, or are filled with distracting features. Individuals seeking to accurately monitor their nutrition—especially those new to fitness or macro tracking—lack a *simple, open-source, and efficient* tool focused purely on *core accountability and goal tracking*. This gap results in users struggling to maintain consistent logging and frequently losing sight of their daily caloric and macronutrient targets.

## 2. Scope of the Project

The scope of the Simple-Diet-Tracker is to deliver a fully functional *Minimum Viable Product (MVP)* focusing on the core functional requirements of personalized nutrition logging and daily goal management using *Python*.

*Inclusions:*
* User data input for meals, calories, and macronutrients (Protein, Carbs, Fat).
* Data Persistence: Storage and retrieval of daily logs and user-defined goals using local file operations (e.g., JSON or CSV file I/O).
* Real-Time Calculation: Instantaneous summation and comparison of consumption against set goals.
* Basic Reporting: Displaying a summary of consumption for the current day.
* Implementation using Python's Standard Library and object-oriented programming principles.

*Exclusions:*
* Integration with external food databases (e.g., USDA API).
* Advanced user authentication or multi-user support.
* Complex visualization or prediction features.

## 3. Target Users

The primary target users for the Simple-Diet-Tracker include:

1.  *Students/Beginners:* Individuals learning about nutrition management who require a straightforward, free tool to introduce them to calorie and macronutrient tracking without unnecessary complexity.
2.  *Fitness Enthusiasts:* Users who need a quick, reliable, and non-distracting Command Line Interface (CLI) tool to ensure they meet specific, daily macronutrient targets efficiently.

## 4. High-Level Features

* *Core Logging (CRUD):* Fast, intuitive entry and retrieval of food items with customizable nutritional values.
* *Goal Visualization:* A clear dashboard showing current consumption totals versus user-defined goals.
* *Data Persistence:* Reliable storage and integrity of records using local file storage.
* *Historical Access:* Ability to view past logs to track long-term progress and patterns.
*