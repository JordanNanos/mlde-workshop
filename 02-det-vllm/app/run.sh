docker rm -f front; docker run -d --rm --name=front --network=host front:0.1b; docker logs -f front
