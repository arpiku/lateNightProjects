## Apr 21 13:34
 - On NixOS with wayland and with wayland based desktop environment in general, pyautogui is of no use.
 - pyDirectInput is just not available on nixpkgs, which is fine, since it's not that great a piece of code anyways.
 - The tablet driver for Huion doesn't work.
 - pywayland doesn't work!
 - Haven't been able to create virtual input device to use the tablet as a mouse.
 - Haven't been able to create a vritual input device at all.

 - Looking into wayland, probably will have to write something from scratch.
