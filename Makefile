setup_env_dev:
	@echo "Setting up development environment..."
	$(shell export $$APP_ENV=dev)

setup_env_local:
	@echo "Setting up local environment..."
	$(export APP_ENV=local)
	
setup_env_prod:
	@echo "Setting up production environment..."
	$(export APP_ENV=prod)

