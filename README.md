# CLI-tool for encryption/decryption data

---

## Description
CLI-tool in Python for encryption/decryption of input text or text file. 
It based on AES encryption algorithm and use binary file as an encryption key.

## Installation
Make sure you have [Python](https://www.python.org) installed (this project uses python version 3.9).
From your command line:

#### Clone this repository
``` commandline
git clone https://github.com/ailored/encrypt-decrypt-cli.git
```
#### Go into the repository
```
cd encrypt-decrypt-cli
```
#### Install dependencies
```
pip install -r requirements.txt
# OR
pip3 install -r requirements.txt
```

## Usage

### 1. To read more about arguments and flags run next command:
``` commandline
python encytool.py -h
```
Or:
``` commandline
python3 encytool.py --help
```

#### Output:
``` commandline
usage: encytool.py [-h] [-e] [-d] keyfile_path

CLI encryption-decryption tool based on AES encryption algorithm

positional arguments:
  keyfile_path   specify location of the binary encryption key file

optional arguments:
  -h, --help     show this help message and exit
  -e, --encrypt  specify it if you want to encrypt the data
  -d, --decrypt  specify it if you want to decrypt the data

```

### 2. Generate binary encryption key file
Run the following command in your command line:
``` commandline
python keygen.py
OR
python3 keygen.py
```
Check for the created key file in the key folder. If it is there, then you can go on.

### 3. Select mode and run the tool
_After running in the selected mode, the tool reads data from stdin, encrypts/decrypts the text, and outputs the result to stdout._

#### Encryption
- Encrypt a file for example "user_text.txt" in folder "data". 
Or create your own file in the project data directory, fill it with text, and save it. 
Run the following example command:
 ``` commandline
 python encytool.py --encrypt key/encryption_key.bin < data/user_text.txt
 OR
 python encytool.py -e key/encryption_key.bin < data/user_text.txt
 ```
replace <data/user_text.txt> with the right path and filename.

- Encrypt the entered text. 
If you don't have a text file or just want to encrypt the plain text you enter at the command line, 
run the following command:
 ``` commandline
 python encytool.py --encrypt key/encryption_key.bin
 OR
 python encytool.py -e key/encryption_key.bin
 ```

#### Output:
```commandline
Entered text you want to encode:


```
To finish entering, press ENTER and then press CTRL+D.

_After successful encryption, the encrypted_data.bin file will appear in the data directory._

#### Decryption
To decrypt encrypted data, all you need is an encrypted file key.
 ``` commandline
 python encytool.py --decrypt key/encryption_key.bin
 OR
 python encytool.py -d key/encryption_key.bin
 ```

After that, the program will display the nonce and tag values in the command line, 
which will be the same as the nonce and tag after encryption.

#### Two modes one line
If you want to encrypt and immediately decrypt data at once, 
you may need the following command:

``` commandline
python encytool.py --encrypt key/encryption_key.bin && python encytool.py --decrypt key/encryption_key.bin
``` 
or
``` commandline
python encytool.py -e key/encryption_key.bin < data/user_text.txt && python encytool.py --d key/encryption_key.bin
```

After that, you will see the nonce and tag values in the command line after encryption and decryption, 
and you can make sure that both nonce values are the same, similarly to the tag 