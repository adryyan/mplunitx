{{ fullname | escape | underline}}

{% block attributes %}
{% if attributes %}
.. rubric:: {{ _('Module Attributes') }}

.. autosummary::
   :toctree:
{% for item in attributes %}
   {{ module }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block functions %}
{% if functions %}
.. rubric:: {{ _('Functions') }}

.. autosummary::
   :toctree:
   :nosignatures:
{% for item in functions %}
   {{ module }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block classes %}
{% if classes %}
.. rubric:: {{ _('Classes') }}

.. autosummary::
   :toctree:
   :template: mplunitx_class.rst
   :nosignatures:
{% for item in classes %}
   {{ module }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block exceptions %}
{% if exceptions %}
.. rubric:: {{ _('Exceptions') }}

.. autosummary::
   :toctree:
{% for item in exceptions %}
   {{ module }}.{{ item }}
{%- endfor %}
{% endif %}
{% endblock %}

{% block modules %}
{% if modules %}
.. rubric:: Modules

.. autosummary::
   :toctree:
   :template: mplunitx_module.rst
   :recursive:
{% for item in modules %}
   {{ item }}
{%- endfor %}
{% endif %}
{% endblock %}
