チュートリアル
==============

アプリケーションをプロジェクトに追加する
----------------------------------------

skypehub アプリケーションをDjangoのプロジェクトに追加します。

settings.py の INSTALLED_APPS に skypehub を追加します。

DBテーブルを作成する
--------------------

manage.py の syncdb コマンドを実行して skypehub に必要なDBテーブルを作成します。

::

  python manage.py syncdb

Skypeへの接続オプションを設定する
---------------------------------

デフォルトの設定では `Transport=X11` になっています。Linuxではデフォルト設定で問題ないでしょう。

Windowsの場合、SKYPE_HOOK_OPTIONSを空にする必要があります。

settings.py に次のように追記します。

.. sourcecode:: python

  SKYPE_HOOK_OPTIONS = {}

botを起動する
-------------

skypebotを起動しましょう。Skypeを起動してから次のコマンドを実行します。

::

  python manage.py runskypebot

起動できましたか？ではbotを実際に作成してみましょう。

アプリケーションを作成する
--------------------------

`#hello` と入力されると `こんにちは(ユーザ名)さん` と返事をするbotを作成します。

manage.py の startapp コマンドでアプリケーションを作成します。

::

  python manage.py startapp hello

INSTALLED_APPSにhelloを追加します。

イベントのレシーバを記述する
----------------------------

Skype botがメッセージを受信した際に実行されるレシーバを記述します。

作成したhelloアプリケーションのディレクトリに `skypebot.py` という名前でファイルを作成します。

.. sourcecode:: python

  #coding:utf-8
  from skypehub.handlers import on_message
  
  def receiver(handler, message, status):
      # メッセージ受信したときのみ
      if status != 'RECEIVED':
          return
      body = message.Body.lower()
      if body == '#hello':
          # メッセージ送信
          message.Chat.SendMessage(u'こんにちは %s さん' % message.Sender.FullName)
  
  # レシーバを登録
  on_message.connect(receiver)

.. note::

  runskypebot コマンドは、起動時にアプリケーションディレクトリの `skypebot.py` という名前のファイルを自動的にロードします。

