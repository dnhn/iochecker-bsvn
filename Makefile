.DEFAULT: welcome
.PHONY: setup clean check

py = .venv/bin/python

welcome:
	@echo 'setup    -- Setup environment'
	@echo 'clean    -- Clean up environment'
	@echo 'check    -- Run program'

setup:
	@python3 -m venv .venv
	@cp .env.sample .env
	@echo 'Virtual environment created.'
	@echo 'Run the following commands:'
	@echo '> source .venv/bin/activate'
	@echo '> pip install -r requirements.txt'
	@echo '> deactivate'

clean:
	@rm -rf .venv __pycache__
	@echo 'Cleaned up.'

check:
	@$(py) -m main
