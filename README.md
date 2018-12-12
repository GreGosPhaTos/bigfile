
# Bigfile

Is a cli tool that helps find huge files on your file system


## Run it ! Using python or python3

`python ./bigfile.py --help`


## Or Download the executable (Unix system)

`wget -qO- https://raw.githubusercontent.com/GreGosPhaTos/bigfile/master/archives/latest.tar.gz | tar xvz`

then

`./bigfile --help`

You can move to your executable path `sudo mv ./bigfile /usr/local/bin/` for a global use.


## How it works ?

 - scan your home folder, looking for 700 MB files and more :

 `bigfile --dir /home/me --fileSize 700`

 will give :

 ```
 /home/me/huge_movie.mp4
 /home/me/huge_file.ext
 ```

 - output the files size :

 `bigfile --dir /home/me --fileSize 700 --outputSize`

 will give :

 ```
 /home/me/huge_movie.mp4 (721 MB / 756214320 Bytes)
 /home/me/huge_file.ext (866 MB / 908960540 Bytes)
 ```
