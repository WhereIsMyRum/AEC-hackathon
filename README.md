<html>
<body>
<h1 class="title">AEC Hackathon</h1>
<h3 class="why">Why</h3>
<p class="why">During the AEC hackathon I was cooperating with lots of people from the field of architecture. During the hackathon an idea came to life - creating a service that allows monitoring the transport of various building materials, from the producer's all the way to the construction site. The unexpected delay in transport of construction materials causes delay in the building process, which in turn can cause huge financial loss. Being able to at least foresee and prepare for such events, gives the architect opportunity to adjust the schedule and lower the impact it causes on the whole construction schedule.</p>
<h3 class="what">What</h3>
<p class="what">The idea is not so new - in theory the service should resemble the one that is already available for a regular package tracking, but be exclusive only to construction materials. At every stage of delivery all the constructions materials are scanned and in the system it is registered what is their current location and what is the approximate time of delivery. Then all the data can be viewed in a web application, and suitable steps can be taken. As I was the only technical person in our team, and the actual idea clarified itself rather late, we decided to create a rather limited proof of concept.</p>
<h3 class="how">How</h3>
<p class="how">A simple website was created using customized HTML template, using Django on the backend. The site presents a table with all the materials that are awaited at the construction site. The site has a single API endpoint, hitting which causes one of the material's state to update. This was used for the presentation purposes, where during the idea presentation someone would scan a QR code on the construction material that 'just arrived', and the status would be updated to 'on site'. The whole project's scope was very limited due to the limited amount of time and number of people able to work on it.</p>
<h3 class="technologies">Technologies used</h3>
<ul class="technologies">
  <li class="technologies" hover="Python">Python</li>
  <li class="technologies" hover="Python">Django</li>
  <li class="technologies" hover="Python">HTML</li>
  <li class="technologies" hover="Python">CSS</li>
  <li class="technologies" hover="Python">JS</li>
</ul>
<hr>
<small class="created">Created: September 2019</small>
</body>
</html>
