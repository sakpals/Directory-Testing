#!/bin/bash

clear

echo "Test ScramFS CLI save."

#create and move to testing dir
mkdir cli_test
cd cli_test

# create and activate python virtual envi
#python3.4 -m venv test
#source ./test/bin/activate

echo "========================================================================="

echo "Creating dummy files to be read as standard input."

echo "========================================================================="

echo "making dummy small (45KB,500MB) files" 
dd if=/dev/urandom bs=1024 count=45 of=dummy_45KB
dd if=/dev/urandom bs=1048576 count=500 of=dummy_500MB
echo
echo "-------------------------------------------------------------------------" 
echo "making dummy medium size (1GB, 5GB) files"
dd if=/dev/urandom bs=1073741824 count=1 of=dummy_1GB
dd if=/dev/urandom bs=1073741824 count=5 of=dummy_5GB
echo
echo "-------------------------------------------------------------------------" 
echo " making dummy large(10GB, 30GB) files"
dd if=/dev/urandom bs=1073741824 count=10 of=dummy_10GB
dd if=/dev/urandom bs=1073741824 count=30 of=dummy_30GB
echo
echo "========================================================================="
echo 
echo "TESTING: small 45KB file "
cat dummy_45KB | scramfs save save_small_45KB.txt
if diff "save_small_45KB.txt" "dummy_45KB" > /dev/null;
	then echo "PASS";
else
	echo "FAIL";
fi
echo "========================================================================="
echo 
echo "TESTING: small 500MB file "
cat dummy_500MB | scramfs save save_small_500MB.txt
if diff "save_small_500MB.txt" "dummy_500MB" > /dev/null;
	then echo "PASS";
else
	echo "FAIL";
fi
echo "========================================================================="
echo
echo "TESTING: medium 1GB file "
cat dummy_1GB | scramfs save save_med_1GB.txt
if diff "save_med_1GB.txt" "dummy_1GB" > /dev/null;
	then echo "PASS";
else
	echo "FAIL";
fi
echo "========================================================================="
echo
echo "TESTING: medium 5GB file "
cat dummy_5GB | scramfs save save_med_5GB.txt
if diff "save_med_5GB.txt" "dummy_5GB" > /dev/null;
	then echo "PASS";
else
	echo "FAIL";
fi
echo "========================================================================="
echo
echo "TESTING: large 10GB file "
cat dummy_10GB | scramfs save save_large_10GB.txt
if diff "save_large_10GB.txt" "dummy_10GB" > /dev/null;
	then echo "PASS";
else
	echo "FAIL";
fi
echo "========================================================================="
echo
echo "TESTING: large 30GB file "
cat dummy_30GB | scramfs save save_large_30GB.txt
if diff "save_large_30GB.txt" "dummy_30GB" > /dev/null;
	then echo "PASS";
else
	echo "FAIL";
fi
echo "========================================================================="
echo
echo "END"
echo "========================================================================="
