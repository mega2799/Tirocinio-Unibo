docker-compose up >> /LOG/container.log & sleep 50 && docker exec -it mongodb sh /home/import.sh && pwd &&mongosh -u root -p pass12345 --authenticationDatabase admin -f ../scripts/makeIndex.js 
