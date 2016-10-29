# Amazon Echo App: Next Meetup via Meetup.com

## The App

Ask an Amazon Echo (or Dot or Touch, aka Alexa) when the next meetup is and receive the date,
title, and description.

This was the result of a talk I gave for the
[PyStPete Python Meetup](https://www.meetup.com/Saint-Petersburg-Python-Meetup/). Hack away!

## Asking Questions

The supported pattern is something like:

```
<device greeting>, ask <app invocation> <phrase>
```

Where:
* _device greeting_ is most likely _Alexa_, but it could also be _Amazon_ or _Echo_.
* _app invocation_ is configured in the
[Amazon/Alexa dev portal](https://developer.amazon.com/edw/home.html#/skills/list).

### Supported App Invocations

* when the next meetup is
* when the next meeting is
* when the next talk is
* when the next event is
* when is the next meetup
* when is the next meeting
* when is the next talk
* when is the next event

### Examples Spoken Phrases

````
Alexa, ask Py Saint Pete when the next meetup is.
Alexa, ask Py Saint Pete when is the next meeting?
```
