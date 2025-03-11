<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BlueStacks Tweaker - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #f4f4f4;
        }
        h1, h2 {
            color: #333;
        }
        code {
            background-color: #eee;
            padding: 3px 6px;
            border-radius: 4px;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 4px;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <h1>BlueStacks Tweaker</h1>
    <p><strong>Author:</strong> 4nnonyme</p>
    <p>A powerful tool to tweak and optimize BlueStacks emulator using ADB commands.</p>

    <h2>Features</h2>
    <ul>
        <li>Connect to BlueStacks emulator</li>
        <li>Change DPI settings</li>
        <li>Adjust FPS limits</li>
        <li>Install APK files</li>
        <li>Modify device model properties</li>
    </ul>

    <h2>Installation</h2>
    <p>Make sure you have <code>ADB</code> installed on your system. You can install it using:</p>
    <pre><code>sudo apt install adb  # For Linux
choco install adb    # For Windows (using Chocolatey)</code></pre>

    <h2>Usage</h2>
    <p>Run the script using Python:</p>
    <pre><code>python bluestacks_tweaker.py</code></pre>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li>ADB installed</li>
        <li>CustomTkinter library (<code>pip install customtkinter</code>)</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License.</p>
</body>
</html>
