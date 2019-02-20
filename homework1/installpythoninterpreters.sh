#!/bin/bash
function pyenvadd(){
	if pyenv versions | grep py$1
	then
		echo py$1 ALREADY EXISTS
	else
		pyenv local $1
		pyenv virtualenv py$1
	fi
}

if  pyenv versions | grep 2.7.6
then
echo "PYTHON 2.7.6 	ALREADY INSTALLED"
pyenvadd "2.7.6"
else
echo "INSTALLING PYTHON 2.7.6 "
pyenv install 2.7.6
pyenvadd "2.7.6"
fi

if  pyenv versions | grep 3.7.1
then
echo "PYTHON 3.7.1	ALREADY INSTALLED"
pyenvadd "3.7.1"
else
echo "INSTALLING PYTHON 3.7.1 "
pyenv install 3.7.1
pyenvadd "3.7.1"
fi
