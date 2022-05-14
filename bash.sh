"C:\Program Files\Docker\Docker\frontend\Docker Desktop.exe"
docker buildx
docker buildx create --name mybuilder
docker buildx use mybuilder
docker buildx build . --platform linux/arm/v7 -t niggiover9000/eaglegang:arm --push
docker buildx build . --platform linux/arm64/v8 -t niggiover9000/eaglegang:arm64 --push
docker buildx build . --platform linux/amd64 -t niggiover9000/eaglegang:amd64 --push