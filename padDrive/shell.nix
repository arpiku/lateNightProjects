{pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs.python311Packages; 
  [
   evdev
   pyautogui
   pywayland
    ];
}

