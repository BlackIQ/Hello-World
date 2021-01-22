# Contributing to Hello World project
If you want to contribute to this project:
- Fork this repo in github
- Clone your fork
- Create a branch
- Make your changes and commit
- Push your branch to your fork
- Send a pull request from your branch to this project

Some notes:
- if you are adding new example, surely test that code before commiting
- Do not change `README.md` directly, new languages will be added to the list automatically

### Adding new language
If you want to add new language to this repo, You should create a directory named name of that language capitalized. for example `Python` or `Php`.

Then, you should add your examples to that folder. for example `Python/my_example.py`

Also, add a `README.md` for that language. for example `Python/README.md`.
This file should contain a description about that language, a link to wikipedia, etc.
Don't worry, this is not required. if you don't, we do this after your PR.

Also you can put a file named `info.json` in the language folder. this file lets `gen-readme.py` script to
write name and a link about creators of that language in the `README.md` list and some other options in the future:

```json
{
	"creator": {
		"title": "Python Development Team",
		"link": "https://github.com/python"
	}
}
```

If you added this file, for add name and link of creator, you should run `python3 gen-readme.py` script.

### TODO
If you haven't any idea for contributing, but you want to contribute, you can See [TODO file](/TODO.md) and [Github Issues](https://github.com/BlackIQ/Hello-World/issues). This will help you to file a task to do.

