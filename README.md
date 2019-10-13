# ExpertSystem
[![Unit][]]() [![Status][]]() [![License][]]()

[License]: https://img.shields.io/badge/License-MIT-blue
[Status]: https://img.shields.io/badge/Status-experimental-yellow
[Unit]: https://img.shields.io/badge/Unit-education-brightgreen
[jParser]: https://github.com/GeorgyFirsov/jParser

It is simple "decision-machine", that parses production rules and initial state as JSON and outputs a way of "thinking" of itself. 

I wrote it for private usage for "Intelligent systems" cource in my university. It means, that this code can be a bit bad in comparison to my other repos (but I tried to keep myself concentrated to write clean code). 

### Usage
```python
from ExpertSystem.Machine import Machine

...

machine = Machine(rules_file, initial_file)
machine.start()
```

### Dependencies

This script uses my JSON-parser - [jParser][]. It must be placed near `ExpertSystem` directory. `Utils` directories can be merged, but `settings.py` file should be taken from jParser!

### Example

Usage can be discovered on an example (`example.py` in this repo). All data you can find in `Data` directory.

Output of `example.py`:
```
Initial state: ['допуск в лабораторию', 'свободные деньги', 'список литературы', 'удобное расписане', 'свободное время', 'желание учиться', 'факультативы']

Collision of [8, 9, 10, 11] rules
Rule 10 used. Got: купить ноутбук

Collision of [4, 8, 9, 11] rules
Rule 4 used. Got: заниматься дома

Collision of [8, 9, 11] rules
Rule 9 used. Got: получить книги в библиотеке

Collision of [5, 8, 11] rules
Rule 5 used. Got: читать необходимую литературу

Collision of [2, 8, 11] rules
Rule 2 used. Got: отличная теоретичекая база

Collision of [8, 11] rules
Rule 8 used. Got: ходить в универ

Collision of [7, 11] rules
Rule 7 used. Got: выполненные лабы

Rule 11 used. Got: посещать доп занятия

Rule 6 used. Got: хорошие результаты за к/р

Rule 3 used. Got: отличная практическая база

Rule 1 used. Got: успешная сдача экзамена

Target "успешная сдача экзамена" reached
```
