if [ "setup_microservice" = $1 ]; then
    echo "Running install microservice requirements"
    exec pip install -r microservice/scrapping_datbase_api/requirements.txt
    exit;
fi

if [ "setup_scrapper" = $1 ]; then
    echo "Running install scrapper requirements"
    exec pip install -r scrapper/aplication/requirements.txt
    exit;
fi

if [ "makemigrations" = $1 ]; then
    echo "Make migrations"
    exec python3 microservice/scrapping_datbase_api/manage.py makemigrations
    exit;
fi

if [ "migrate" = $1 ]; then
    echo "Migrate database configuration"
    exec python3 microservice/scrapping_datbase_api/manage.py migrate
    exit;
fi

if [ "microservice" = $1 ]; then
    echo "Running DRF microservice"
    exec python3 microservice/scrapping_datbase_api/manage.py runserver
    exit;
fi


if [ "runscrapper" = $1 ]; then
    echo "Running scrapper"
    exec python3 scrapper/aplication/main.py
    exit;
fi

echo "Error invalid argument, please README.md"
exit 5;