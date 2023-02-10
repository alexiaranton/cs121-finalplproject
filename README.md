# cs121-finalplproject
Sawa: A Bisaya Programming Language 

<p align="center">
  <b>Sawa is a a new programming langauge founded in Python</b>
</p>

<h2 align="center">Uwusage</h2>

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
<p align="center">Variables can be declared using the keyword <code>baryabol</code>.</p>

```py
baryabol baka = 100
baryabol awoo = "two"
baryabol chan = 25
baryabol baka = baka + 1
baryabol awoo = 500
baryabol chan = chan * 2

patik(awoo)
patik(baka)
patik(chan)
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
baryabol awoo = 501

KUNG awoo == 502 IMBIS baryabol chan = "awoo is 502!" LAINKUNG awoo == 501 IMBIS baryabol chan = "awoo is 501!" LAIN baryabol chan = "awoo is 500!"

patik(chan)
```

h4 align="left">Output</h4>

```
awoo is 501!
```

<h3 align="center">Loops</h3>

```py
PARA i = 0 SA 5 IMBIS
	patik("UwU")
HUMAN
```

<h4 align="left">Output</h4>

```
UwU
UwU
UwU
UwU
UwU
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
