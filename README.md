# PyCharm QML Enhancement

Enable QML (Qt Modeling Language) syntax highlight and code completion in PyCharm.

# Screenshots

**Syntax highlight**

![](.assets/image-20201127224559615.png)

**Code completion**

![](.assets/image-20201127224745541.png)

# How To Use

1. Download [pycharm-qml-keywords-highlight.md](./pycharm-qml-keywords-highlight.md)

3. Open PyCharm settings - Editor - File Types, click the 'add' button. You will see the dialog pane

   ![](.assets/image-20201127225050047.png)

4. Enable options like below

   ![](.assets/image-20201127225233543.png)

5. Open the downloaded file, copy its content, paste to PyCharm dialog pane like below

   ![](.assets/image-20201127225449503.png)

6. And add `*.qml` file types

   ![](.assets/image-20201127225527272.png)

7. Now you can see the code highlighted in .qml ^_^

# Notice

1. The source keywords are extracted from Qt 5.15. Be notice that some modules and properties are not available in Qt 6.0. You may find the difference by checking Qt offical documentation.
2. The code completion is not perfect, since it always dumps all matched keywords as you typed, regardless which module or which component you're using.

# Compile From Source

See [Developer Guide](README-dev.md).
