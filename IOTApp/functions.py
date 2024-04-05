from django.shortcuts import HttpResponse, redirect, render
import serial

pin = serial.Serial("COM7", 9600)

def unit(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor




def lighton(request):
    print("button clicked")
    pin.write(b"on13")
    return redirect("home")


def lightoff(request):
    print("button clicked")
    pin.write(b"off13")
    return redirect("home")


def relay_on_7(request):
    pin.write(b"on7")
    return redirect("home")


def relay_off_7(request):
    pin.write(b"off7")
    return redirect("home")


def relay_on_6(request):
    pin.write(b"on6")
    return redirect("home")


def relay_off_6(request):
    pin.write(b"off6")
    return redirect("home")


def relay_on_5(request):
    pin.write(b"on5")
    return redirect("home")


def relay_off_5(request):
    pin.write(b"off5")
    return redirect("home")


def relay_off_4(request):
    pin.write(b"off4")
    return redirect("home")


def relay_on_4(request):
    pin.write(b"on4")
    return redirect("home")


def homepage(request):
    return render(request, "index.html")


def turn_off_all_relay(request):
    pin.write(b"on7")
    pin.write(b"on6")
    pin.write(b"on5")
    pin.write(b"on4")
    return redirect("home")


def turn_on_all_relay(request):
    pin.write(b"off7")
    pin.write(b"off6")
    pin.write(b"off5")
    pin.write(b"off4")
    return redirect("home")