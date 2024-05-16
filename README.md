# Toolbar image strip assembler
This python script generates a bitmap strip that can be used as a toolbar resource for windows applications.

![Toolbar](toolbar.png)

![Toolbar](samples/toolbar1.png)

![Toolbar](samples/toolbar2.png)

### Repo
https://github.com/ovidiuvio/toolbar-strip.git

### Functionality
* Loads toolbar definition from a JSON file.
* Supports processing SVG and other image formats.
* Resizes all images to 16x16.
* Combines the processed images horizontally into a single PNG image strip.

### Usage

Define toolbar items in toolbar.json:
```
[
  "images/icons8-about-16.png",
  "images/icons8-web-16.png",
  "images/icons8-settings.svg",
  "images/icons8-console-16.png",
  "images/icons8-memory-16.png",
  "images/icons8-file.svg",
  "images/icons8-save-16.png"
]
```

Assemble the toolbar strip:

```
python3 toolbar.py
```

This will combine the images listed in `toolbar.json` into a single PNG image named `toolbar.png`.

![Toolbar](toolbar.png)

Icons from https://icons8.com/

