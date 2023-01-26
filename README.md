### python-project-lvl1
### Hexlet tests and linter status:
[![Actions Status](https://github.com/Dmitry-Zhiryakov/python-project-lvl1/workflows/hexlet-check/badge.svg)](https://github.com/Dmitry-Zhiryakov/python-project-lvl1/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/edc43778536664726a54/maintainability)](https://codeclimate.com/github/Dmitry-Zhiryakov/python-project-lvl1/maintainability)
[![Github Actions](https://github.com/Dmitry-Zhiryakov/python-project-lvl1/actions/workflows/github_actions.yml/badge.svg)](https://github.com/Dmitry-Zhiryakov/python-project-lvl1/actions/workflows/github_actions.yml)

# Brain Games

"Brain Games" — a set of five console games built on the principle of popular mobile applications for brain pumping. Each game asks questions that need to be answered correctly. After three correct answers, it is considered that the game is over. Incorrect answers end the game and offer to go through it again.

## Installation:

### Using pip [(Demonstration)](https://asciinema.org/a/Mudh1GPExqwiCLLQUjIaZpGIn):

```
pip install --user git+https://github.com/Dmitry-Zhiryakov/python-project-lvl1.git
```

### Clone repository and use poetry [(Demonstration)](https://asciinema.org/a/wjU0lPlmn0aot2al5FP8gcYhX):

Clone repository:

```
git clone https://github.com/Dmitry-Zhiryakov/python-project-lvl1.git
```

Run `poetry lock --no-update` to sync dependencies at poetry.lock and pyproject.toml files:

```
poetry lock --no-update
```

Install dependencies:

```
make install
```

Build the package:

```
make build
```

Install the package:

```
make package-install
```

## Games:

1. `brain-calc` (Calculator). The player is shown a random mathematical expression, such as 35 + 16, which must be calculated and the correct answer written down. [(Demonstration)](https://asciinema.org/a/rOwFEkJsPNDsnDmvcv56nkA5L)

```
brain-calc
```

2. `brain-progression` (Progression). The player is shown a series of numbers forming an arithmetic progression. It is necessary to determine the missing number, replaced by two dots. [(Demonstration)](https://asciinema.org/a/s3EYS7RirmZ9tWOpAUjGH97eU)

```
brain-progression
```

3. `brain-even` (Definition of an even number). The player is shown a random number and needs to answer 'yes' if the number is even, or 'no' if it's odd [(Demonstration)](https://asciinema.org/a/C2RQeg5Is05d545vesH0Ua7xj)  
 
```
brain-even
```

4. `brain-gcd` (Finding the Greatest Common Divisor). The player is shown two random numbers, eg '25 50'. The player must calculate and enter the greatest common divisor of these numbers. [(Demonstration)](https://asciinema.org/a/Rgp8boeJBtOajKeXW9lTPpEmN)
 
```
brain-gcd
```

5. `brain-prime` (Definition of a prime number). The player is shown a random number and needs to answer 'yes' if the number is prime. Otherwise, 'no' should be answered. [(Demonstration)](https://asciinema.org/a/wvweybDdEblCrCRzlJ1OxRXtV)

```
brain-prime
```
