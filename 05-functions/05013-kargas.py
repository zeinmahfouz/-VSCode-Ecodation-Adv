

# region ornek_2


dilPython = {
    "programlamaDili" : "python",
    "seviye" : "yüksek",
    "interpreter" : True,
    "versiyon" : 3.64
}

dilCSharp = {
    "programlamaDili" : "c#",
    "seviye" : "yüksek",
    "interpreter": False,
    "versiyon" : 8.0
}

def dilBilgisi(dil):
    print(f"{dil['programlamaDili']}\t{dil['seviye']}\t{dil['interpreter']}\t{dil['versiyon']}")


print("Prg.Dil\tSeviye\tInterp\tVersiyon")
print("-------\t-------\t-------\t-------")

dilBilgisi(dilPython)
dilBilgisi(dilCSharp)

# endregion
