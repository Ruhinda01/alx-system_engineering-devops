# 0x19. Postmortem: Web Stack Debugging 3

![Debugging](/alx-system_engineering-devops/0x19-postmortem/debugging-we-bare-bears.gif)

The issue within this project was based off an ongoing Apache 500 internal server error. This is a Wordpress website running on a LAMP stack.

## Issue Summary

* **Duration**: The bug was first detected at 09:00 AM (EAT) when an engineer tried to access the website and was consistently given a `HTTP/1.0 500 Internal Server Error` this error was then ratified at 13:00 AM (EAT).

* **Impact**: This made the entire website down consistently delivering a `500 internal server error` to the user. Approximately 45% of the users were affected by this major error.

* **Root Cause**: The root cause to this issue was a typo found in the settings of the WordPress html files. This was diagnosed by looking through error logs and looking at the realtime logs of the website trying to be accessed.

## Timeline

* 09:00 AM (EAT) - The issue was detected in the early morning hours after purposeful maintenance checks were done by the team the day before. A user sent in a complaint alert which reached our team.
* 10:00 AM (EAT) - An investigation was done by first looking at the server. This was done to check of the server was running and also look into the configuration files.
* 11:00 AM (EAT) - The initial check to look for the server errors in the configuration and also to see if the server was running turned out to be misleading. The path to debugging this error was then switched to looking at the WordPress html directory.
* 12:00 AM (EAT) - This debugging task was then pushed to myself to solve and get the website up and running.
* 13:00 AM (EAT) - A typo was found in the `wp-settings.php` file and this mainly affected the functionality of the website. Through use of automation, I was able to fix the bug which finally made the website fully functional.

![Finally](/alx-system_engineering-devops/0x19-postmortem/omg-hell.gif)

## Root Cause and Resolution

The issue causing the consistent "500 internal server errors" was due to a typo in the `wp-setting.php` file. This typo affected how files were accessed to ensure the proper functionality of the website. The typo was `phpp` instead of being `php`.

This issue was fixed through automation by utilising Puppet code that run a shell command `sed -i "s/phpp/php/g" /var/www/html/wp-settings.php`. This replaced all `phpp` instances in the file to `php`. Finally i was able to run this command `curl -sI 127.0.0.1` which delivered a "200 status code" and therefore successful fixing the bug.

## Corrective and Preventative Measures

Care should be taken when setting up servers, configuration files and settings of WordPress websites. Ensuring proper monitoring of the server by use of Datadog and other related software to monitor server health and performance.

List of tasks to address the issue:
* Use the `strace` command to locate the errors when running the a command like this `curl -sI 127.0.0.1` and then redirect output to a file to retain the errors even the command is not running.
* Navigate through the errors and locate any possible errors. `Hint: will have a -1 return value`
* Navigate to the `wp-settings.php` or the `wp-config` to locate any errors and fix them either through use of automation or fix it directly in the file.
