# P1
Itter is a multipurpose platform for things 
- recording your progress
- sharing your thoughts
- moments of your journey
- and accomplishing your goals.


model of user interaction

![image](https://github.com/user-attachments/assets/c2162d75-e84a-45e1-82e4-724b76ba8563)

that should be the model1 of a high level overview on how it is going to work.
setting up techniques would mean i want to use flask application for this and then use git pages or railways for hosting.
okay lets begin then.

just set up my basic outlook the first deployment 
-using railways for development
this is how the first look of the website is
![image](https://github.com/user-attachments/assets/e8ec412c-214e-4b32-a422-f1844fcb4258)


alright now lets start editing this html file to curate it to the login page

the frame work should be something like this

![image](https://github.com/user-attachments/assets/ea015372-71fb-4fca-9e58-78add5f14c38)

and then adding an image to that it should look a bit better so 
![image](https://github.com/user-attachments/assets/3b376691-0445-4d3e-9f95-9d828b637228)

that should now let me add in fileds for user to sgin-in/log-in enter mail and password should be fine.

okay now lets begin with the next page i am thinking of a simple page with two options one would be sign-in if the user isn't identified then take user to the new login page
-user email
-password
if already known
if new 
-user email
-password
-confirm password

![image](https://github.com/user-attachments/assets/18bad464-b481-42fa-a950-6924c2e41598)
![image](https://github.com/user-attachments/assets/58de775b-4b0a-4dfc-ad75-b5e87ce50f2f)
![image](https://github.com/user-attachments/assets/ec61382e-df5c-4a1b-8b3b-2291d05994ba)
that should be my current standing now i will go to the models section to start working on the database maintainance so i can assign each user their own instance and yeah maintain overall transparacny for
-data storage
-user validation
-new registration

added a databse checks are looking good now i can go ahead to develop the application in this increment now it looks like i would have to implement user aspects and how the landing page looks like etc eeha.
still a bit rough flash images though so got to work on that gui to so.

okay the first level building is done with some rough edges though now second stage plan ahs to thought out.
![image](https://github.com/user-attachments/assets/80edf80f-f2ed-44ea-8afa-4a01b8945378)

that would be the simple model for now the functions include
- update status on goals
- add/remove goals
- record daily progress

there are few more features i want but for now it should be the core features.

![image](https://github.com/user-attachments/assets/38021bd5-d484-4cc1-8a98-759da2dcda41)

alright how its looking for now though its a dead veresion still i didn't add life to it for now i belive thats would be the over all how the strucutre will look like ofcourse theme and and one two features are to 
added here and there that would be the users default profile page. And to add life to it is the main priroity in mind right now rest of the features i will add them as the come.

![image](https://github.com/user-attachments/assets/d94e6228-2627-4537-93bf-0a4e98f36d5c)

kind of have changed a few things now umm i want to track those put on active and the reflections made.(these would be analyzed to make suggestions)
and wait i will update the heat map js

well i didn't work on heat map yet but in this increment i have put in all these things 
- each user sessions are independent now
- user name, goal, reflections are stored and shown
- gui is looking much better added in past reflections section too
have a look

![image](https://github.com/user-attachments/assets/a14262a4-b3a8-4588-b84f-be088c916630)

thats how with content its looking good i guess
things to focus on in the next increment
- heatmap js
- log out
- past reflections close and open
- detailed past reflections
- integration and analysis of gemini to suggest insights (this might be post poned to next increment.

building on this i have migrated the production development into a more sleeker and better performing website itnegarting websockets for real time cocmmuncation ebtween firedns adding progress tracking gemini integeration for personalized insghts and so on.
