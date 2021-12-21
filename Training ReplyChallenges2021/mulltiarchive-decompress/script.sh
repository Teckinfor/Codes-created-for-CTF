#!/bin/bash
cd run;
echo "script running";
while [[ $? == *"0"* ]]; do 
	string=$(file save);
	if [[ $string == *"gzip"* ]]; then
		echo "gzip";
		mv save save.gz;
		gzip -d save.gz > /dev/null;
	fi	
	if [[ $string == *"7-zip"* ]]; then
		echo "7zip";
		7z e save > /dev/null;
		rm save;
		mv * save;
	fi
	if [[ $string == *"Zip archive"* ]]; then
		echo "Zip archive";
		unzip save > /dev/null;
		rm save;
		mv * save;
	fi
	if [[ $string == *"directory"* ]]; then
		echo "Directory";
		cp -r save/* ./
		rm -r save;
		mv * save;
	fi
	if [[ $string == *"bzip2"* ]]; then
		echo "Bzip2";
		bzip2 -d save > /dev/null;
		mv * save;
	fi
done
