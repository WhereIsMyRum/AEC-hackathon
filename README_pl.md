<html>
<body>
<h1 class="title">AEC Hackathon</h1>
<h3 class="why">Powód</h3>
<p class="why">Podczas hackathonu AEC współpracowałem z wieloma osobami związanymi z różnymi aspektami architektury i konstrukcji. W trakcie hackathonu narodził się pomysł na stworzenie aplikacji, która umożliwiałaby śledzenie transportu materiałów budowlanych, od miejsca produkcji aż do placu konstrukcyjnego. Niespodziewane opóźnienia w transporcie materiałów  powodują opóźnienia w budowie, które mogą powodować znaczne straty finansowe. Umożliwenie architektom przewidywania takich sytuacji daje im szansę na odpowiednie zmodyfikowanie harmonogramu prac i tym samym zminimalizowanie wpływu opóźnienia na całokształ procesu budowy.</p>
<h3 class="what">Cel</h3>
<p class="what">Nie jest to w żadnym razie nowy pomysł - aplikacja powinna przypominać standardową opcję śledzenia przesyłek, dostępną u wielu firm kurierskich, z tą różnicą, że będzie umożliwaić śledzenie tylko i wyłącznie materiałów budowlanych. Na każdym etapie transportu, materiały są skanowane i ich aktualne położenie oraz estymowany czas dostawy jest rejestrowany na serwerze. Dane te można przeglądać za pośrednictwem aplikacji webowej i na ich podstawie podejmowac odpowiednie kroki. Niestety, z powodu tego, że ostateczny pomysł wyklaryfikował się dość późno, oraz byłem jedyną osobą techniczną w zespole, stworzona została zaledwie 'makieta' tego, jak w zamyśle miałoby to funkcjonować.</p>
<h3 class="how">Wykonanie</h3>
<p class="how">Powstała prosta strona internetowa wykorzystująca zmodyfikowany template HTML i Django na backendzie. Strona prezentuje tabele w której znajdują  się wszystki materiały, które oczekiwane są na placu konstrukcyjnym. Backend posiada pojedynczy endpoint. Wysłanie GET request na ten endpoint powoduje zmianę statusu jednego z materiałów wyszczególnionych w tabeli. Zostało to wykorzystane podczas prezentacji, gdzie w trakcie opisywania pomysłu, jeden z członków drużyny skanował kod QR umieszczony na jednym z oczekiwanych materiałów konstrukcyjnych, symulując jego dostawę i zmieniając jego status na 'dotarł do miejsca konstrukcji'. Zakres projektu był niestety wybitnie ograniczony ze względu na zbyt małą ilość czasu jak i osób zdolnych do pracy nad jego stroną techniczną.</p>
<h3 class="technologies">Zastosowane technologie</h3>
<ul class="technologies">
  <li class="technologies" hover="Python">Python</li>
  <li class="technologies" hover="Python">Django</li>
  <li class="technologies" hover="Python">HTML</li>
  <li class="technologies" hover="Python">CSS</li>
  <li class="technologies" hover="Python">JS</li>
</ul>
<hr>
<small class="created">Data powstania: September 2019</small>
</body>
</html>
