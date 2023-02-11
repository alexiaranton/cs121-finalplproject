# cs121-finalplproject
Sawa: A Bisaya Programming Language

<p align="center">
  <b>Sawa is a new programming language based on Python</b>
</p>

<h2 align="center">Usage</h2>

<h4 align="left">Himo og bagong file - <code>test.sawa</code></h4>

```py
patik("Agoy!")
```

<h4 align="left">Dagan</h4>

Either run from the interpreter directly:
```sh
python basic.py test.sawa
```

Or run in an interactive shell:
```sh
python shell.py
> dagan("test.sawa")
```

<h4 align="left">Output</h4>

```
Sige! Bidyohi ko!
```

<h2 align="center">Documentation</h2>

<h3 align="center">General</h3>

<p align="center"><code>python shell.py</code> opens the basic shell. Running <code>dagan("test.sawa")</code> from the shell execuwutes code from the file <code>test.sawa</code>.</p>

<h3 align="center">Variables</h3>
<p align="center">Variables can be declared using the keyword <code>BARYABOL</code>.</p>

```py
BARYABOL una = 100
BARYABOL ikaduha = "two"
BARYABOL ikatulo = 25
BARYABOL una = una + 1
BARYABOL ikaduha = 500
BARYABOL ikatulo = ikatulo * 2

patik(ikaduha)
patik(una)
patik(ikatulo)
```

<h4 align="left">Output</h4>

```
500
101
50
```

<h3 align="center">Conditionals</h3>
<p align="center">KUNG《condition》IMBIS《expression》LAINKUNG《condition》IMBIS《expression》</p>

```py
BARYABOL ikaduha = 501

KUNG ikaduha == 502 IMBIS BARYABOL ikatulo = "ikaduha is 502!" LAINKUNG ikaduha == 501 IMBIS BARYABOL ikatulo = "ikaduha is 501!" LAIN BARYABOL ikatulo = "ikaduha is 500!"

patik(ikatulo)
```

h4 align="left">Output</h4>

```
ikaduha is 501!
```

<h3 align="center">Loops</h3>

```py
PARA i = 0 SA 5 IMBIS
	patik("Sawa")
HUMAN
```

<h4 align="left">Output</h4>

```
Sawa
Sawa
Sawa
Sawa
Sawa
```


<h3 align="center">Functions</h3>

```py
KALIHOKAN owofy(pwefix) -> pwefix + "OwO"

patik(owofy("This is pyth"))
```

<h4 align="left">Output</h4>

```
This is Sawa
```
