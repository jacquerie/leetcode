# -*- coding: utf-8 -*-


def Settings(**kwargs):
    if kwargs["language"] == "cfamily":
        return {
            "flags": [
                "--std=c++11",
                "-Wall",
                "-Wextra",
                "-Werror",
                "-Wno-return-type",
                "-Wno-sign-compare",
                "-Wno-unused-but-set-variable",
            ],
        }
    return {}
