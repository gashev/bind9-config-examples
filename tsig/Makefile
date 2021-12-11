start:
	./create.sh
	ansible-playbook playbook.yml

stop:
	podman rm -f server-1 server-2
	podman network rm tsig
	rm -rfv server-1 server-2
test:
	python3 test.py
