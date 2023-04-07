### 1. Сформулювати своє розуміння, що таке тип даних.
Тип даних означає множину припустимих значень даних та множину операцій над даними. Типи вказують програмам та програмістам на те, як слід обробляти дані. Типи надаються або значенням в пам'яті, або об'єктам, таким, як змінні. У Мові  програмування Python кожна змінна має свій тип. 
Тип необхідний для того, щоб визначити:
* які значення може приймати змінна;
* які операції можна виконувати з цією змінною;
* як зберігати значення змінної в пам'яті;

Інтерпетататор Python сам визначає тип змінної по тому значенню, яке їй присвоється.

### 2. Сформулювати своє розуміння типізацій - динамічної, статичної, сильної та слабкої.
Будь-яке значення в комп'ютері складається із множини бітів, апаратне забезпечення не розрізняє навіть адресу, коди операцій, символьні дані, цілі числа. Присвоєння типу даних (типізація) надає значення набору бітів.
**Статична типізація** — механізм, що дозволяє на етапі написання програми визначити через тип об'єкта програми множину припустимих значень та множину операцій над об'єктом так, що порушення вимог типізації буде призводити до попередження або помилки на етапі трансляції програми, а не на етапі її виконання. Тип об'єкта, встановлений при написанні програми, не може бути змінений на етапі виконання програми, але значення, яке містить об'єкт, може бути перетворене (приведене) до іншого типу.
**Динамічна типізація** мови програмування означає, що основна частина перевірок типів виконується під час виконання програми, а не під час компіляції. У динамічній типізації, значення мають типи, а змінні — ні, тому змінна може містити значення будь-якого типу.
**Сильна типізація** мови програмування має суворіші правила під час компіляції, а це означає, що помилки та відмови виникають частіше. Більшість цих правил впливає на призначення змінних, значення, що повертаються функцією, аргументи процедури та виклик функції. 
**Слабка типізація** має більш вільні правила, які можуть давати непередбачувані або навіть помилкові результати або може виконувати неявне перетворення типів під час виконання.

***Сильна типізація характеризується тим, що мова не дозволяє поєднувати у виразах різні типи та не виконує автоматичні неявні перетворення, наприклад неможна відняти з рядка множину. Мови зі слабкою типізацією виконують значну кількість неявних перетворень автоматично, навіть якщо може трапитися втрата точності або перетворення неоднозначне.***