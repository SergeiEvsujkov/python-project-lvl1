install:
	poetry install
	
makelint:
	poetry run flake8 brain_games

.PHONY: install makelint
