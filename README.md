# Stuffs to memorize

## Simple GIT command
```
echo "# omg" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/keirace/omg.git
git push -u origin main
```

## Change Repo URL
git remote set-url origin new.git.url/here

## To Authenticate Git
```
git config --global user.email "emailaddress@yahoo.com"
git config --global user.name "username"
git config --global user.password "password"
```

## Revert most recent Commit
```
git reset HEAD~1
```
