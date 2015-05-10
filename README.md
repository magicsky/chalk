# chalk 
> Terminal string styling for python. Native port of [chalk for nodejs](https://www.npmjs.com/package/chalk)

![preview](http://cdn-qiniu.qiniudn.com/ebe705f3.png)

## Why
* Highly performant
* Expressive API
* Auto-detects color support

## install
```
pip install chalk
```

## Usage
````
chalk = require("chalk")
print chalk.red("Hello chalk")
````

## Styles
### Modifiers
* reset
* bold
* dim
* italic (not widely supported)
* underline
* inverse
* hidden
* strikethrough (not widely supported))

### Colors
* black
* red
* green
* yellow
* blue (on Windows the bright version is used as normal blue is illegible)
* magenta
* cyan
* white
* gray

### Background colors
* bgBlack
* bgRed
* bgGreen
* bgYellow
* bgBlue
* bgMagenta
* bgCyan
* bgWhite