import asyncio
from bleak import BleakScanner, BleakClient


async def run_ble():
    print("Searching for devices...")
    devices = await BleakScanner.discover()
    if not devices: return print("No devices found.")

    for i, d in enumerate(devices):
        print(f"[{i}] {d.name or 'Unknown'} ({d.address})")

    idx = int(input("\nSelect device index: "))
    device = devices[idx]

    async with BleakClient(device.address) as client:
        print(f"Connected to {device.name or device.address}")

        # getting characteristics
        chars = []
        for service in client.services:
            for char in service.characteristics:
                chars.append(char)

        while client.is_connected:
            print("\n--- Available Characteristics ---")
            for i, c in enumerate(chars):
                # c.description — in bleak names of characteristics
                name = c.description if c.description else "Unknown Characteristic"
                print(f"[{i}] {name}")
                print(f"    UUID: {c.uuid}")
                print(f"    Rights: ({','.join(c.properties)})")

            print("\n[R] Read | [W] Write | [E] Exit")
            action = input("Action: ").upper()

            if action == "E": break
            if action not in ["R", "W"]: continue

            try:
                char_idx = int(input("Select index: "))
                selected_char = chars[char_idx]

                if action == "R":
                    if "read" in selected_char.properties:
                        val = await client.read_gatt_char(selected_char.uuid)
                        print(f"\n>>> Raw (HEX): {val.hex()}")
                        print(f">>> Text: {val.decode(errors='ignore')}")
                    else:
                        print("!! This cannot be read.")

                elif action == "W":
                    if "write" in selected_char.properties or "write-without-response" in selected_char.properties:
                        msg = input("Enter message: ")
                        await client.write_gatt_char(selected_char.uuid, msg.encode())
                        print(">>> Sent!")
                    else:
                        print("!! This cannot be written.")
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(run_ble())