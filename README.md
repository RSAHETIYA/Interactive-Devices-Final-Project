# Interactive-Devices-Final-Project


Functional Checkoff:

Project: Teaching Pianos

Project Group: Sam Willenson and Rahul Sahetiya

Description: Built a functional prototype where one piano is the dedicated student and the other is the dedicated teacher. Teacher piano is capable of playing piano notes and sending respective data to student piano. Student piano is capable of displaying the notes received on the respective LEDs. Unable to create bidirectional sending (although code is there for the function), as decoder got delayed in shipping. This created a physical constraint with respect to our GPIO pins/miniTFT covering some to power all LEDs. Finally, for the housing, vector file has been created and are planning to laser cut in the next two days to complete assembly. Decoder will also arrive tomorrow.

Video:
https://youtu.be/KECurauWU70

Final Submission:

Project plan: Big idea, timeline, parts needed, fall-back plan.

2. Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

3. Documentation of design process

First we had to design our Piano Box, laser cut it, and glue it together.
![emptyBox](https://user-images.githubusercontent.com/112603386/207697881-3df0dcbc-65dd-4b0e-9f24-cb697f526d99.jpeg)


We had an idea for how to make the keys 3 dimensional, but after hitting a few roadblocks and time constraints, we chose to pivot to a 2-dimensional key implementation.

Next we had to add all of our LEDs to the product. The goal was to have a dedicated LED for each of the 12 keys in a musical octave, however due to the lack of available GPIO pins on each of our Raspberry Pis we ran into an issue. Our TFT screens were taking up some of these GPIO pins so we were left with only 9 per Raspberry Pi. To fix this issue we planned on implementing a multiplexor to split the logic from some of these GPIO pins to make the voltage levels control multiple LEDs.

Here are images of us soldering the multiplexor into the design:
![rahulSolder](https://user-images.githubusercontent.com/112603386/207697928-e46965c9-dac7-4272-afa0-d3eaf6409a40.jpeg)
![rahulSolder2](https://user-images.githubusercontent.com/112603386/207697944-68baeb96-61be-4764-ab2a-2d3b2b9b1086.jpeg)
![solderCloseup](https://user-images.githubusercontent.com/112603386/207697970-42d0a780-90ec-462d-a4c4-4adda17cc601.jpeg)

We are both eperienced at soldering, but we made one mistake - assuming the Maker Lab had Lead solder. Because of the lack of Lead solder, this whole process proved to be more time consuming and difficult than originally expected. When our first board was finished, we tested the device to see if each LED can be powered on individually. Unfortunately, something unexpected was happening and we were getting unexpected LEDs turning on: for example LED 5 powering on when we want LED 2 on, and multiple LEDs powering on at the same time. 

To fix this issue we brainstormed how we might be able to pivot to not using the multiplexor. How could we best represent each of the 12 keys with only 9 available GPIO pins. We came up with an idea that would be symmetrical and evenly distributed across the board. Instead of having each note be represented by it's own individual LED, we will have only the white keys with LEDs housed above them. This way when a user hits a black key, this can be represented by the surrounding white keys to the left and right of this black key light up. Now single LEDs represent white keys, and double LEDs represent black keys (in the middle of the 2 LEDs).

After we figured this out we cut a hole in the back of our piano boxes to be able to snake out the power cord and webcam cables out of the back.

Now we attached the LEDs on the protoboards to the inside of the front face of our board, taped them down to be secure, and fit in the Raspberry Pi with all the alligator clips attached to a MFR capacitive touch sensor board. 


![bothNoTop](https://user-images.githubusercontent.com/112603386/207701128-3e72a2a3-2f06-410e-983f-fbf2c40d9311.jpeg)

With all the alligator clips attached to our copper 2D piano keys, we are ready to test.


https://user-images.githubusercontent.com/112603386/207701316-f26428f6-9e98-4399-bb6e-1b2f7bd7c155.mp4

We can see above that the design is working properly. The LEDs all work and when a black key is pressed the 2 surrounding LEDs light up at the same time.

4. Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

All code can be found in the Github files listed at the top of this repository. PianoTutor is the code that makes the pianos make sounrs. Tramsmitter and Receiver is the code that allows the pianos to talk to one another so they can control each others LEDs remotely. 

5. Video of someone using your project
  
  We have had many people test our product, and should have filmed more of them! We did capture two encounters however.
  
Below is a test with one user where the video unfortunately starts after I tought our user the C Blues scale using the LEDs and him not looking at my fingers. While this part of the interaction was not captured, the second half of our interaction was captured where we are still both interacting with each piano and I am showing him more functionality of how the piano can arpeggiate notes in a fun way.
  

https://user-images.githubusercontent.com/112603386/207703890-32ca8f64-c52b-4e9d-b117-49368c32c527.mov


Here is another user test where the user was unfortunately filming with a very low quality camera. However the interaction can still be seen:



https://user-images.githubusercontent.com/112603386/207704002-e08ac922-6cd1-4f9e-933d-ad9c8a11f371.mp4



6. Reflections on process (What have you learned or wish you knew at the start?)
 We wish we had known that the multiplexor implementation would prove to be so difficult to get working correctly. If we had known this we would have spent that time improving the keys and making them 3D rather than 2D. While the 2D implementation works the same way in terms of functionality, we believe 3D keys would be more fun for our users.
 
 We learned that sometimes people get excited about unintended outcomes of a project. Because the musical library we used to form the synth sounds did not play multiple notes at once, we used a while loop to loop through sounds when a user plays a chord. This made an arpeggiated chord instead of a continuous one. This was a workaround for us to be able to play all the notes someone presses as long as they hold the chord out long enough for the code to loop through each held note. However, we learned when user testing that this was often a favorite feature of our users. It made them feel more talented at piano because of how fast the notes were playing. One lesson learned here is how important user testing is; what was a side feature to us the designers was a showcase feature to the users themselves.

7. Group work distribution questionnaire
 Both of us, Sam and Rahul, shared the work fairly well on all aspects of the project. We both talked about the idea behind the product, we both talked about what parts to order, we both worked on the code, we both worked on the housing, we both worked on the soldering, we both worked on the spacing of the LEDs, we both worked on the actual taping of the copper tape to the piano keys, and we both tested with users seperately. We communicated early and often and overall the team was a success.
