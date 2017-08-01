# Basic Linux Commands for Beginners

### <a name="user-content-general"></a>General

`ls` - lists files

*   **Important flags**  
    `-a` - display hidden files  
    `-R` - recursively displays files  
    `-l` - displays extra details like size, owner, group, date the file was last modified and permissions

`cd <path>` - change directory to `path`

*   Here `path` may be relative or absolute.

(`cd ..` - takes to parent directory  
`cd` - takes to `<user>` directory[denoted by `~`]  
`cd -` - takes to the previous directory you were in)

*   **Trivia:** `user` directory is present in the `home` directory which is present in the `root` directory(denoted by `/`). [`/home/<user>` in Linux and `Users/<user>` in macOS] Then there is no further upper directory after `root`.

`pwd` - print working directory. Prints absolute path to current directory.

`^` symbol is used for representing 'ctrl' ... e.g. `^C` = ctrl key + c

`touch <filename>`- creates a new file with any extension we want.

**Note:** `touch` is a much more advanced command and can be used to change the file access and modification times. For more info see `man touch`.

`rm <filename>` - removes a file.  
`rm -r <directory>` - recursively removes all files in a directory. Then removes the empty directory.  
**Note:** This command might ask you for permission for every file that it deletes. To prevent this use `-f`(force) flag.  
`mkdir <dir_name>` - makes a new directory  
`rmdir <dir_name>` - removes an **empty** directory

`cp /path/to/file /path/to/copy/to` - used to copy file.  
(Use `cp -r` to copy a directory recursively)  
`mv /old/path/to/file /new/path/to/file` - used to move file.

*   **Trivia:** `mv [old_filename] [new_filename]` is the best method to rename a file.

`grep [flag] <text to search> <files to search in>`

*   **Important flags**  
    `-i` - Performs case insensitive matching  
    `-r` - Helps to search recursively through a directory  
    `-l` - Outputs the name of the files in which the search text is present  
    `-L` - Outputs the name of the files in which the search text is not present  
    `--color=auto` - Highlights the search text in the output

`cut` - cuts out selected portions of each line from file and writes them to the standard output.  
`cut -c 2-5 file` - cut characters 2 to 5 from each line of file  
`cut -d"x" -f 1 file` - returns each part of every line before first occurrence of 'x' (-d is delimiter and -f is field)

`clear` or `^l` - scrolls down to an empty screen

`reset` - initialises terminal variables to thier default value

`passwd <username>` - Change password for a user

`find <query>` - finds files and directories with name `query` in the current directory and its subdirectories  
`find -d <query>` - looks for a directory with name `query`  
`find -f <query>` - looks for a file with name `query`

`history` - shows all typed commands history  
`history n` -shows last n commands

`sudo <command>` - Run the command as superuser(a.k.a. root)

`!<text>` - repeats a previous command in history which started with 'text'  
`!!` - repeats the previous command  
`sudo !!` - repeats the previous command as superuser

`whoami` - gives the username of the current user.  
`su <username>` - Used to switch to a different user. This prompts for the password of the user you switch to.  
`sudo -i` - Switch to `root` user. This user has complete access to all files.

**Note:** While `sudo -i` will ask you for your login password to become superuser, `su root` will ask for the root password. These are not the same. You may have to set or change the root password by running `sudo passwd root` first.

*   **Trivia:**`sudo` stands for `SUperuser DO` and `su` stands for `Substitute User`.

`man <command>` - shows manual entry for the command. Manual contains all the flags related to that command and their use.

`time <command>` - gives the time taken for the command to execute. Very useful when you want to find the execution time of your programs.

`diff [file1] [file2]` - compares the two files line by line. Usually used to compare ideal output and user-generated output.  
`diff -z [file1] [file2]` - Ignores trailing-whitespaces while comparing the two files

`.` - refers to current directory  
`..` - refers to parent directory

*   **Trivia:** Files with file names starting with `.` are hidden.

`echo "hello"` - prints hello on the terminal

`>` - used to store the output of a task in some file(overwrites if file with same name is present) rather than displaying it on the terminal.  
`>>` - same task as `>` but does not overwrites just appends to the file with the same name.

`|` - piping is used to give the output of a command as input to another command ..for e.g `history | grep "find"` will search for "find" in the output of `history`

`<command> | tee <filename>` - used to show output of `command` on terminal as well as writing the output to a file `filename`.

`cat` - used to open a file in terminal in read-only format

*   **Trivia:** Unless you have infinite scrolling turned on (available in Profile Preferences -> Scrolling tab of the terminal), there is a limit to how many lines you can see on the screen.

`<output of some command> | less` - allows the user to advance through the content by pressing SPACE, move backwards by pressing 'b' and quit using 'q'. Pressing ESC followed by SPACE allows you to scroll down one screen at a time.

Example: `cat file | less`

`<output of some command> | more` - is similar to using `less`, but allows viewing one screen at a time.

*   **Trivia:** All commands typed in the terminal are saved in `history` or the `.bash_history` file in the home directory. `history | less` or `cat ~/.bash_history` will let you scroll through previously typed commands.

* * *

### <a name="user-content-opening-files-with-common-text-editors"></a>Opening files with common Text Editors

`<vim|vi|nano|emacs> <filename>` : opens a file in the respective text editor inside the terminal.  
`gedit <filename>` : opens a file with filename in Gedit . `subl <filename>` : opens a file with filename in Sublime Text.  
`subl <foldername>`: Opens the entire folder in Sublime Text. Very helpful when you are working on projects with multiple file.

* * *

### <a name="user-content-running-scripts"></a>Running Scripts

`sh [path/to/script]` - To run a non-executable `sh` script.  
`bash [path/to/script]` - To run a non-executable `bash` script  
`./<location/of/executable>` - Just type the file location to run an executable file.

* * *

### <a name="user-content-changing-permissions"></a>Changing Permissions

`chmod a+x file` - Grants execution permission to all users of a file.  
`chmod a+w file` - Grants write permission to all users of a file.  
`chmod a+r file` - Grants read permission to all users of a file.
`chmod <number> <file-name>` - Grant permission to *file-name* on the basis of the number provided
**Important : **
*   *Explanation for permission-number :*
    *   Everyone falls into one of three categories - `user`, `group` or `others`.
    *   Each category is associated with three permission-flags : `r` for *read*, `w` for *write* and `x` for *execute* ; these flags determine what the person is capable of doing with that file/directory.
    *   The flags are in the order **rwx-rwx-rwx** for **user-group-others** respectively.
    *   Each of `r`, `w` and `x` is given a boolean value (*0 or 1, i.e. NOT_ALLOWED or ALLOWED in layman's terms*).
    *   The permission-number is obtained by joining the decimal representation of the flags' values for each category in the forementioned order.
    *   **For example :** (755)~10~ -> (7-5-5)~10~ -> (111-101-101)~2~ -> rwx-r-x-r-x permission
*   `-R` flag along with *directory-name* instead of *file-name* can be used to grant the specified permission to each item of the directory.

This are just examples. `chmod` has a lot of different configurations for different kinds of permissions. For all details see its `man` page.

`chown -R <username> path/of/file/or/directory` - Gives the ownership of the file or all files in the directory and its subdirectories to the mentioned user.

* * *


### <a name="user-content-aliases"></a>Aliases

An alias is a word assigned to a statement, and acts as a keyboard shortcut.

`alias py='python'` - would pass `python` whenever `py` is entered.

This alias lasts as long as the terminal is running. To create a permanent alias, append this line to `~/.bash_profile` or `~/.bash_aliases`.

`unalias <alias_name>` - Removes the alias. E.g. `unalias py` - After this `py` would not work as `python`.

* * *

### <a name="user-content-downloading"></a>Downloading

`Wget` and `cURL` are two great utilities for downloading stuff. They are a replacement to the Download Managers you must have used on Windows.

*   **Trivia:** `cURL` is powered by `libcurl` - a cross-platform library with a stable API that can be used by each and everyone. `Wget` on the other hand is command line only. There's no library.

`wget <url_to_download>` - Downloads the file at the specified url.  
`wget -c <url_to_download>` - Resumes an incomplete download. Very helpful when a large file download stops due to some error.  
`wget --tries=100 <url_to_download>` - Set the retry download attempts. This is very useful when the download file is large and the internet connection has problems.

*   **Trivia:** `wget` does 20 retries by default.

`wget -i <download_list_file.txt>` - For Multiple downloads. Downloads all the files/URLs mentioned in file.  
`wget --recursive --page-requisites --html-extension --convert-links --no-parent <URL>` - Use this command to download the entire website so that you can view it offline.

*   --recursive: download the entire Web site.

*   --page-requisites: get all the elements that compose the page (images, CSS and so on).

*   --html-extension: save files with the .html extension.

*   --convert-links: convert links so that they work locally, off-line.

*   --no-parent: prevents wget from downloading anything from the folders beneath the folder you want to acquire.

*   **Trivia:** `cURL` supports more protocols and authentication methdods than `Wget` and is almost always pre-installed on the OS. `Wget` on the other hand is famous because of its ability to download an entire website for offline view.

`curl -O <url_to_download>` - Downloads the file at the specified url.  
`curl -O <URL1> -O <URL2>` - Downloads files at both urls.  
`curl -C - -O <url_to_download>` - Resumes an incomplete download.

*   **Trivia:** `cURL` can also be used to upload files to `ftp` server. Use `curl -u <ftpuser>:<ftppass> -T <myfile> <ftp://ftp.testserver.com>`

* * *

### <a name="user-content-installation-commands"></a>Installation Commands

##### <a name="user-content-debian-ubuntu-and-other-debian-based-distros"></a>Debian, Ubuntu and other debian-based distros

`apt-get install <package-name>` - Installs a package

*   **Important flags**  
    `-y` - Replies **yes** to all confirmations `apt-get` asks for during install.

`apt-cache search <query>` - Searches package names and descriptions for the query string. Used to find the package-names.

`apt-get remove <package-name>` - Removes a package (but not the configuration files)

`apt-get purge <package-name>` - Removes a package (along with the configuration files)

`apt-get update` - APT keeps a local database on your hard drive with a list of all available packages and where to find them. This command explicitly updates the database.

##### <a name="user-content-fedora-red-hat-and-centos"></a>Fedora, Red Hat and CentOS

`yum install <package-name>` - Installs a package

* * *

### <a name="user-content-networking"></a>Networking

`ifconfig` - when used without any flags, used to display the status of all active network interfaces.

`iwconfig` - similar to `ifconfig`, but used for wireless network interfaces.

`ping [domain_name_or_ip_address]` - Used to ping a domain name or IP address continuously. It can be stopped by `^C`. Generally used to check if the server is up and responding.

`dig example.com` - Queries DNS servers for information. Gives back the `A` record which points the domain name to an IP address. Using the `+short` flag returns just the IP address linked to the domain name.

`+nocomments` – Turn off the comment lines  
`+noauthority` – Turn off the authority section  
`+noadditional` – Turn off the additional section  
`+nostats` – Turn off the stats section  
`+noanswer` – Turn off the answer section (Of course, you wouldn’t want to turn off the answer section)

`dig -x [IP address]` - Queries and returns a `PTR` record against the IP address queried. The PTR record helps in Reverse DNS Lookup i.e. it provides the domain name linked to an IP address. Example `dig -x 127.0.0.1 +short` returns `localhost.`.

*   **Trivia:** When you reverse lookup an IP say 1.2.3.4, the PTR record for the domain name `4.3.2.1.in-addr.arpa`, more generally `reverse_ip.in-addr.arpa`. (in-addr -> Inverse Address. arpa -> Address and Routing Parameter Area)

*   **Trivia:** The arpa top-level domain was the first domain installed in the Domain Name System (DNS).

`arp` - It manipulates or displays the kernel's _IPv4_ network neighbour cache. It can add entries to the table, delete one, or display the current content.

*   **Trivia:** ARP stands for Address Resolution Protocol.

`traceroute [IP address/ Domain name]` tracks the route packets taken from our computer on their way to a given host. It utilizes the IP protocol's **time to live** (TTL) field and attempts to elicit an `ICMP TIME_EXCEEDED` response from each gateway along the path to the host. This response contains the IP address of the gateway which are then listed as output on the terminal.  
**Note:** You might see `*`(asterisk) instead of IPs sometimes. This means that the packet was not acknowledged and no response was sent before timeout. This is generally done purposefully to hide the identity of the servers.

`whois domain_name.com` - Generates a long list of output regarding the server registration.

`netstat` - The netstat command symbolically displays the contents of various network-related data structures. It helps answer the question “What in blazes is going on on my network?”. The columns present in the output are:

*   `Proto` - tell us if the socket listed is [TCP](https://www.wikiwand.com/en/Transmission_Control_Protocol) or [UDP](https://www.wikiwand.com/en/User_Datagram_Protocol)

*   `Recv-Q` and `Send-Q` - tell us how much data is in the queue for that socket, waiting to be read (Recv-Q) or sent (Send-Q). In short: if this is 0, everything’s ok, if there are non-zero values anywhere, there may be trouble.

*   `Local Address` and `Foreign Address` - tell to which hosts and ports the listed sockets are connected. The local end is always on the computer on which you’re running netstat , and the foreign end is about the other computer (could be somewhere in the local network or somewhere on the internet).  
    **Note:** The `Foreign Address` can be `localhost` sometimes. It means the computer is talking to itself over the network, so to speak. This is also known as `loopback`.

*   `State` - tells in which state the listed sockets are. The TCP protocol defines states, including “LISTEN” (wait for some external computer to contact us) and “ESTABLISHED” (ready for communication). The stranger among these is the “CLOSE WAIT” state shown by two sockets. This means that the foreign or remote machine has already closed the connection, but that the local program somehow hasn’t followed suit. Strange states and non-empty queues(non-zero values in `Send-Q` or `Recv-Q`) often go together.

* * *

### <a name="user-content-extracting-compressed-files"></a>Extracting compressed files

`tar -xvzf <file.tar.gz>` - used to extract the .tar.gz file

* * *

### <a name="user-content-compressing-files"></a>Compressing files

`tar -cvzf <tarballname.tar.gz> <item_to_compress_1> [item_to_compress_2]` - used to compress any number of files into a .tar.gz compressed archive.

*   tarball.tar.gz: This is the name of the final compressed archive.

`-x`: tar can collect files or extract them. x does the latter.  
`-c`: Collects files to be compressed  
`-v`: makes tar talk a lot. Verbose output shows you all the files being extracted.  
`-z`: tells tar to decompress the archive using gzip  
`-f`: this must be the last flag of the command, and the tar file must be immediately after. It tells tar the name and path of the compressed file.

* * *

### <a name="user-content-process-management"></a>Process Management

`top` - displays processor activity in real time.

`ps` returns the snapshot of current processes.  
`ps -e` returns every process running on the system  
`ps -u <useraccount>` returns list of processes running on user account.  
`ps -u <useraccount> | grep <Application>` - fetches all processes of "Application"

<div id="js-repo-pjax-container" dir="ltr">

<div id="readme" dir="ltr">

The leftmost number returned by the `ps` command is called the Process ID (PID). A particular process can be terminated using `kill`

`kill <PID>` - kills the process having PID as that entered.  
`kill -9 <PID>` - performs a violent kill  
`killall <processname>` - kills all instances of processname

</div>

</div>
