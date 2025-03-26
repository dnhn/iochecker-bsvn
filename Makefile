.DEFAULT: welcome
.PHONY: setup clean check

py = .venv/bin/python

welcome:
	@echo 'setup    -- Setup environment'
	@echo 'clean    -- Clean up environment'
	@echo 'check    -- Run the program'

setup:
	@python3 -m venv .venv
	@echo 'Virtual environment created.'
	@echo 'Run the following commands:'
	@echo '> source .venv/bin/activate'
	@echo '> pip install -r requirements.txt'
	@echo '> deactivate'

clean:
	@rm -rf .venv __pycache__
	@echo 'Cleaned up.'

check:
	@echo 'Checking…'
	@$(py) -m main
	@echo 'Checked.'
