if [ ! -e ".devcontainer/.env" ]; then
    cp .devcontainer/.env.template .devcontainer/.env
    echo ".env file created."
else
    echo ".env file already exists."
fi
