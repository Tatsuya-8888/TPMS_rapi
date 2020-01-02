from bluepy import btle

scan = btle.Scanner(0)



def hex2int(_HEX):
  _BIN=bytes.fromhex(_HEX)
  _Rev=_BIN[::-1]
  _HEX=_Rev.hex()
  if _HEX == "":
    _HEX="0000"
  return int(_HEX,16)


# 83:ea:ca:40:01:33
# R.R.

# 82:ea:ca:30:02:40
# R.L.

# 81:ea:ca:20:00:44
# F.R.

# 80:ea:ca:10:07:7e
# F.L.




# 10秒スキャン
devs = scan.scan(10.0)


FR='81:ea:ca:20:00:44'
FL='80:ea:ca:10:07:7e'
RR='83:ea:ca:40:01:33'
RL='82:ea:ca:30:02:40'

for device in devs:

  # FR check

  if device.addr == FR:
    print("-------------------------")
    print(device.addr)

    for (Code,desc,value) in device.getScanData():
      Press = value[16:22]
      Temp = value[24:28]

      if Code == 255 and device.addr == FR:
        print(hex2int(Press))
        print(hex2int(Temp))
        # data
  
  # FL check

  if device.addr == FL:
    print("-------------------------")
    print(device.addr)

    for (Code,desc,value) in device.getScanData():
      Press = value[16:22]
      Temp = value[24:28]

      if Code == 255 and device.addr == FL:
        print(hex2int(Press))
        print(hex2int(Temp))
        # data

  # RR check

  if device.addr == RR:
    print("-------------------------")
    print(device.addr)

    for (Code,desc,value) in device.getScanData():
      Press = value[16:22]
      Temp = value[24:28]

      if Code == 255 and device.addr == RR:
        print(hex2int(Press))
        print(hex2int(Temp))
        # data

  # LR check

  if device.addr == LR:
    print("-------------------------")
    print(device.addr)

    for (Code,desc,value) in device.getScanData():
      Press = value[16:22]
      Temp = value[24:28]

      if Code == 255 and device.addr == LR:
        print(hex2int(Press))
        print(hex2int(Temp))
        # data



