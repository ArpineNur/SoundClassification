# **Sound Classification**
## Description
 This project classifies sound files into 2 categories: *noisy* and *clean*.
 
 User specifies the path to the sound files (*./data* by default), then the script plays *.mp3* files one by one, asking for user input after each sound. The user should type only *n* (for *noisy*) or *c* (for *clean*). If the user input is wrong the script will keep asking for the right input, before playing the next sound. In order to replay the sound user should type *r*.
 
 When all sounds will be played the script will output a *.json* file, with sound file names with their corresponding category. User will be asked for the path and name input for the output json file, if not specified the output will be saved in the current working directory.

## Requirements
The script has been developed with **Python 3.8**.
The following library should be installed prior to use:
* [playsound](https://pypi.org/project/playsound/) - can be installed with *pip*

## Usage
After cloning the **runner.py** and **data** directory run the script:

`python runner.py`

Script will ask for user input of the directory with data.
If you want to use the default **data** directory just skip this step (by clicking *Enter*).
If you want to classify data from other directory specify the full path to that directory, i.e:

`C:/example_folder/data`

If you specify a directory that does not exist the script will throw an *Exception* and will stop execution.

After the directory is specified the script will filter *.mp3* files and start to play them.
If no *.mp3* files are found the script will stop execution.

After playing each sound the script will pause and wait for classification:
    * If you want to classify the sound as clean, type `c`
    * If you want to classify the sound as noisy, type `n`
    * If you want to replay the sound, type `r`

If you type anything else besides the above mentioned inputs, the script will continue to ask for the right input.

After playing all the files, the script will ask for output file name input.
Note that the script will force the *.json* format of the file.
If nothing is typed the default *output.json* will be saved in current directory.