NAME=chrisgute/hello_server
VERSION=$(grep "Version:" main.py | cut -d' ' -f2)

sudo docker build . -t ${NAME}:latest -t $NAME:${VERSION}
build_result=$?

if [ $build_result -ne 0 ]; then
    echo -e "\nFAILED TO BUILD ${NAME}\n"
else
    sudo docker images chrisgute/hello_server
fi