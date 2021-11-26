start:
	ansible-playbook playbook.yml

stop:
	podman rm -f domain a.domain b.domain c.domain
	rm -rfv domain/cache a.domain/cache b.domain/cache c.domain/cache

test:
	python3 test.py
