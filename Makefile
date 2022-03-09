install_dev:
	@echo "instalando pacote com flag -e"
	@pip install -e .

install_final:
	@echo "instalando pacote sem flag -e"
	@pip install .
