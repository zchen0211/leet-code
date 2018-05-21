# Homebrew

## Install
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
- See version
```
brew -v
```

## Update
- Update self:
```
brew update
```
- See outdated packages
```
brew outdated
```
- Upgrade all outdated packages
```
brew upgrade
```

## Pause and Resume Installation
- Pause
```
brew pin $FORMULA
```
- Resume
```
brew unpin $FORMULA
```

## Remove Packages
- Clean up a specific package
```
brew cleanup $FORMULA
```
- Clean up all
```
brew cleanup
```
- Check clean up packages
```
brew cleanup -n
```
- Just remove, no upgrade
```
brew uninstall formula_name --force
```