## School Management Syatem Fast API 
where  
Teachers can perform CRUD operations on students.  
create courses with sections and content blocks in each section.  
assign courses to students.  
interact view their courses in a list.  
Students can see the sections and content blocks for individual courses that they are taking.  
Students are able to see their progress for each course.  
Running the App Locally  
Make sure Python, and Postgres are installed. Postgres must be running.  
Create a virtual environment: python -m venv venv  
Install packages: poetry install  
Run the development server: uvicorn main:app --reload  
Tech Stack  
Fast API  
Python   
Postgres  
SQL Alchemy  
Alembic  
Pydantic  
Black  
Flake8  
Pre-commit 
<b/>
### Schema  
User

email: str  
role: enum (student, teacher)  
is_active: bool  
  
Profile  

first_name: str  
last_name: str  
bio: str (TextField)  
user_id: fk  
  
Course  

title: str  
description: str (TextField)  
user_id: fk  
  
Section  

title  
description  
course_id  
  
ContentBlock  

title  
description  
type  
url  
content  
section_id  
  
StudentCourse  

This model is used for teachers to assign courses to students.
  
student_id  
course_id  
completed  
  
CompletedContentBlock  

Every time the student completes a content block, a row is created in this table. The teacher can then go and edit this information when they grade the content block and provide feedback.

student_id  
content_block_id  
url  
feedback  
grade  
