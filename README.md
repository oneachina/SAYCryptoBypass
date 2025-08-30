# SAYCryptoBypass

<p align="center">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
    <img src="https://img.shields.io/badge/Platform-Unity-lightgrey.svg">
    <img src="https://img.shields.io/badge/Language-Python-blue.svg">
</p>

## Introduction / 介绍
A proof-of-concept analysis and bypass of a weak encryption and device binding scheme found in a Unity application. For educational purposes only.

对一个Unity应用中发现的弱加密和设备绑定方案的概念验证分析与绕过

___为了防止DMCA 本项目会进行Archive / To prevent DMCA takedowns, this project will be archived.___

## Overview / 概述
This repository contains a full breakdown of a custom encryption algorithm `SAYCrypto` and device verification scene `scnVerify` found in a compiled Unity application. The code was recovered through decompilation and serves as a perfect case study for what not to do when implementing client-side security.

本仓库包含了对一个已编译Unity应用中发现的自定义加密算法 `SAYCrypto` 和设备验证场景 `scnVerify` 的完整剖析 该代码通过反编译获得 并作为一个完美的案例研究 展示了在实现客户端安全时不应采取的做法

The original code's purpose was to bind the application to a specific device by encrypting the device's unique identifier `SystemInfo.deviceUniqueIdentifie` and storing it in local `PlayerPrefs`. This implementation is trivially bypassable.

原代码的目的是通过加密设备的唯一标识符 `SystemInfo.deviceUniqueIdentifie` 并将其存储在本地 `PlayerPrefs` 来实现应用与特定设备的绑定。该实现可被轻易绕过。

Disclaimer / 免责声明: This project is intended for educational and security research purposes only. It aims to demonstrate common vulnerabilities to help developers build more secure software. Do not use this information for malicious activities.
免责声明： 本项目仅用于教育和安全研究目的。旨在演示常见漏洞，以帮助开发者构建更安全的软件。请勿将此信息用于恶意活动。

## Based On / 基于的分析
The analysis is based on the decompiled C# code of two primary classes:

本分析基于对两个主要类的反编译C#代码：

1. SAYCrypto (Namespace: StArray)

   - A static class providing Encrypt and Decrypt methods using a custom algorithm.

   - 一个静态类，提供使用自定义算法的 Encrypt 和 Decrypt 方法。

   - Key Flaws / 关键缺陷:

      - Hard-coded default key ("SAY"). / 硬编码的默认密钥（"SAY"）。

      - Predictable key-derived parameters (shift bits, XOR keys). / 可预测的密钥派生参数（移位位数、XOR密钥）。

      - The algorithm is entirely client-side and reversible. / 算法完全在客户端且可逆。

2. scnVerify (Namespace: StArray)

    - A MonoBehaviour scene that checks for a valid device binding on start. / 一个MonoBehaviour场景，在启动时检查有效的设备绑定。

    - Key Flaws / 关键缺陷:

        - Relies on the weak SAYCrypto for validation. / 依赖脆弱的 SAYCrypto 进行验证。

        - Stores the validation state in easily modifiable PlayerPrefs. / 将验证状态存储在易于修改的 PlayerPrefs 中。

        - All verification logic is client-side. / 所有验证逻辑都在客户端。

##  Bypass Methods / 绕过方法

Since the algorithm is known and reversible, you can generate a valid code for any Device ID.
由于算法已知且可逆，您可以为任何设备ID生成有效代码。
A Python script `main.py` is provided in this repo to demonstrate this.
本仓库提供了一个Python脚本 `main.py` 来演示此方法。
```bash
python main.py you_device_id
```

## License / 许可证
This project is licensed under the MIT License - see the LICENSE file for details.
本项目基于MIT许可证 - 详见 LICENSE 文件。

## Warning / 警告
Remember: True security requires a thoughtful, layered approach and never relies on hiding information on the client.
请记住：真正的安全需要深思熟虑的分层方法，绝不能依赖于在客户端隐藏信息。
