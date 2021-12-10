start:
	ansible-playbook playbook.yml

stop:
	podman rm -f server-1 server-2
	rm -rf 1/cache 2/cache

test:
	python3 test.py
