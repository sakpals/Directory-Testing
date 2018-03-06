#!/bin/bash
echo '========================================================='
echo 'TESTING MKDIR COMMANDS'
echo '========================================================='

echo 'creating an alias for testing'

scramfs alias create -e enc -p ~/enc.scramfs

echo
echo '========================================================='

echo 'scramfs mkdir dir'

scramfs mkdir dir

if cd dir;
	then echo 'PASS'
else
	echo 'FAIL'
fi
echo
echo '========================================================='

cd ..

echo 'scramfs mkdir scramfs://enc/dir'

scramfs mkdir scramfs://enc/dir

if scramfs ls scramfs://enc/dir;
	then echo 'PASS'
else
	echo 'FAIL'
fi
echo
echo '========================================================='

echo 'scramfs mkdir dir1/dir2/dir3'



if [scramfs mkdir dir1/dir2/dir3 -eq 'cannot create directory'];
	then echo 'FAIL'
else
	echo 'PASS'
fi
echo
echo '========================================================='

echo 'scramfs mkdir scramfs://enc/dir1/dir2/dir3'



if [scramfs mkdir scramfs://enc/dir1/dir2/dir3 -eq 'cannot create directory'];
	then echo 'FAIL'
else
	echo 'PASS'
fi
echo
echo '========================================================='

echo 'scramfs mkdir -p dir1/dir2/dir3'

scramfs mkdir -p dir1/dir2/dir3

if cd dir1/dir2/dir3;
	then echo 'PASS'
else
	echo 'FAIL'
fi
echo
echo '========================================================='

echo 'scramfs mkdir -p scramfs://enc/dir1/dir2/dir3'

scramfs mkdir -p scramfs://enc/dir1/dir2/dir3

if scramfs ls scramfs://enc/dir1/dir2/dir3;
	then echo 'PASS'
else
	echo 'FAIL'
fi
echo
echo '========================================================='

mkdir dir1

echo 'For existing directory: scramfs mkdir dir1'


if [scramfs mkdir dir1];
	then echo 'FAIL'
else
	echo 'PASS'
fi
echo
echo '========================================================='

scramfs mkdir scramfs://enc/dir1

echo 'For existing directory: scramfs mkdir scramfs://enc/dir1'


if [scramfs mkdir scramfs://enc/dir1];
	then echo 'FAIL'
else
	echo 'PASS'
fi
echo '========================================================='
echo 'END'
echo '========================================================='






