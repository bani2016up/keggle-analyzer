echo "RUNNING poetry lock"

cd backend
poetry lock
cd ../
cd kaggle-api
poetry lock
cd ../

echo "RUNNING docker compose"
docker compose up
