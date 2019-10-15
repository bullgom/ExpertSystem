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
Initial state: ['Желание учиться', 'Общительность', 'Много денег', 'Много времени']

Collision of [16, 18, 14, 15] rules
Rule 16 used. Got: Подходящее окружение

Collision of [18, 14, 15] rules
Rule 18 used. Got: Много знакомых

Collision of [9, 14, 15] rules
Rule 9 used. Got: Общение с опытными людьми

Collision of [14, 15] rules
Rule 14 used. Got: Учёба в университете

Collision of [15, 7, 10] rules
Rule 15 used. Got: Саморазвитие

Collision of [8, 7, 10] rules
Rule 8 used. Got: Прохождение курсов

Collision of [7, 10] rules
Rule 7 used. Got: Чтение нужных книг

Collision of [3, 10] rules
Rule 3 used. Got: Хорошие знания теории

Rule 10 used. Got: Выполнение заданий

Rule 4 used. Got: Богатый опыт

Rule 1 used. Got: Прохождение собеседования

Target "Прохождение собеседования" reached
```
