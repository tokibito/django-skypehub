インストール
============

django-skypehub は easy_install や pip でインストールできます。
Django と Skype4Py に依存しています。

::

  easy_install django-skypehub

Mac でのインストール
--------------------

Mac OS X における Skype4Py は 32-bit モードでしか動作しません。
これは、Mac の Skype クライアントが 32-bit モードにしか対応していないことによるものです。
32-bit モードで明示的にインストールして起動しないと、 Segmentation Fault が発生します。

Skype4Py を 32-bit モードでインストールするには、django-skypehub をインストールする前に以下のコマンドを入力してください。

::

  arch -i386 pip install Skype4Py


実際に動作させる際は、必ず python を 32-bit モードで動作させてください。
32-bit モードで動作させるには arch -i386 python とします。

以下は、skypebot の起動方法の例です。

::
  
  arch -i386 python manage.py runskypebot


この影響により、Django の DB として MySQL を選択することができません。
なぜなら、mysql-python は逆に 64-bit にしか対応していないからです。
django-skypehub を使う際は MySQL 以外の DB を使用してください。

