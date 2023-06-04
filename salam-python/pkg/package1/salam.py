#!/usr/bin/env python3


def get_salam():
    return "Salam Python!"


x = 1

__all__ = ["get_salam"]

if __name__ == "__main__":
    print(get_salam())
