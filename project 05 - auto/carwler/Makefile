deploy: ## deploy project to scrapinghub
	shub deploy
	ls -1 | grep -x -e build -e project.egg-info -e setup.py | xargs rm -r

clean: ## remove python cache
	find . \( -name \*.pyc -or -name \*.pyo -or -name __pycache__ \) -delete
	test -d .scrapy && rm -r .scrapy

.PHONY .SILENT: clean deploy