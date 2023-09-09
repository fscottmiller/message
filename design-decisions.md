# Design Decisions

This page will discuss the design of the message service as they evolve over time.

## What is a `message`? 
The plan is to create a simple message board app. Messages should be postable by authenticated users and should be removed from the board after some amount of time. Nothing complex.

## Key objectives:
1. Create a service that enables basic CRUD operations around the data type `message` and is available over REST protocol for users
2. Create a database for this service to store messages, message versions, history, etc
3. Create an event bus to be utilized by this service in order to showcase messages as communication between other services to be added in the future
4. Keep it free, utilize SaaS where possible

Initial scope includes:
1. Service creation with basic CRUD operations (create, read (list and get), update, delete)
2. Database creation and access
3. IDE cultivation (current choice being github codespaces)
4. Event bus creation and access
5. Web hosting
6. functional testing

Out of initial scope:
1. authentication - anyone can run
2. history, message versions, complex data operations - initial configuration will simply store messages
3. multiple environments
4. load, integration, e2e testing


## Tooling Decisions
1. Service will be implemented in Python using FastAPI. That's mostly to keep development simple and easy.

https://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application