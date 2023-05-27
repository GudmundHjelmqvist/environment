# Commands to run the application
run:
	streamlit run app.py

fix_dns:
	echo -e "[network]\ngenerateResolvConf = false" | sudo tee -a /etc/wsl.conf
	sudo unlink /etc/resolv.conf
	echo nameserver 1.1.1.1 | sudo tee /etc/resolv.conf

install:
	sudo apt-get install python3 python3-venv python3-pip libpq-dev apt-transport-https gnupg2
	python3 -m venv .venv

install_dependencies:
	#source .venv/bin/activate
	pip3 install -r requirements.txt
		
	