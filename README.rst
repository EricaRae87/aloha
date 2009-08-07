=====
aloha
=====

This package provides you with the aloha template tag that allows you
to render "Hello" in different languages. It is flickr inspired and 
you are welcome to contribute more translations.

To install, place the `aloha` directory somewhere on your python path,
then add `aloha` to `INSTALLED_APPS` in your `settings.py` file.

{% aloha %}
===========
The aloha tag generates a random greeting, renders it, and updates 
the context with additional variables containing further details
of the greeting language.
 
 Syntax::
     {% load aloha %}
     {% aloha %}
     {% aloha language as [varname] and info as [varname] %}
 
 Example usage::
 
     {% aloha language as aloha_lang and info as aloha_info %}

 Example usage::
    
     <h1>{% aloha %}!</h1>
     {% ifnotequal aloha_language "English" %}
     	<h2>{{aloha_info}}</h2>
     {% endifnotequal %}
