# Penguin Paddle!

Hi everybody, this is the project I've been working on recently for Hackclub's Undercity. 

Penguin Paddle is my own touch-sensitive iambic morse code keyer that has multiple differrent output options, including a buzzer to make sound. It is designed with future expansion in mind with mounting holes and solder joints for potentially adding vertical pads in the future (Which will be printed as a snap-off section of my PCB), as well as a usb-c port for keyboard support. 

It uses two switches and two potentiometers to control all of the settings from on the board, so there is no challenge when trying to increase the speed of your keying or vice versa. It uses a piezo buzzer to make the sound and the volume is adjustable, and it has an overall On/Off switch. 

I decided to make it because I've ben getting into morse code, and I had an idea a while beck to create my own keyer as I don't have one, so when I realized I needed to make a project for Highway to Undercity that would have grants for my hardware I was exited to realize this was the perfect oppurtunity to create it! Hopefully it should help me do what I am trying to do with morse code; connecting and sharing stories with people across the world with my own unique twist.

Schematic Photos
![Screenshot 2025-07-03 001631](https://github.com/user-attachments/assets/96f580f6-f464-4034-bf2e-c4915ba0e847)

PCB Photos:
![Screenshot 2025-07-03 001008](https://github.com/user-attachments/assets/e82d6817-1f7a-482b-a53f-79117945ed3b)
![Screenshot 2025-07-03 000936](https://github.com/user-attachments/assets/3d44899d-3d7a-4a4d-bfef-054540377b99)
![Screenshot 2025-07-03 001031](https://github.com/user-attachments/assets/7e937ce9-1769-40c0-9ad6-2b2040b043dc)

Case Photos:
![IMG_4678](https://github.com/user-attachments/assets/60da4510-70b7-4a6a-ac78-4f1f5823caf4)
![IMG_4679](https://github.com/user-attachments/assets/fad18d87-3657-422e-8835-aa87924024c3)
![IMG_4680](https://github.com/user-attachments/assets/a42ae7c3-6c51-4c55-a932-9d31a2517aee)


# BOM

| Quantity | Part | Link | Price |
| ----------- | ----------- |----------- |----------- |
| 1 | 3.5mm Stereo Audio Jack | https://www.digikey.ca/en/products/detail/same-sky-formerly-cui-devices/SJ1-3533NG/738701 | $1.82 |
| 2 | 10k Rotatary Potentiometer | https://www.digikey.ca/en/products/detail/tt-electronics-bi/P0915N-EC15BR10K/4780755 | $6.68 |
| 1 | 12.2mm Piezo Buzzer | https://www.digikey.ca/en/products/detail/tdk-corporation/PS1240P02BT/935924 | $0.84 |
| 1 | Xiao ESP32-S3 | https://www.digikey.ca/en/products/detail/seeed-technology-co-ltd/113991114/19285530 | $11.63 |
| 2 | 30v SPDT Slide Switch | https://www.digikey.ca/en/products/detail/c-k/SS-12D07-VG-4-NS-GA-PA/2747177 | $2.73 |
| 1 | 1k Axial Resistor | https://www.digikey.ca/en/products/detail/stackpole-electronics-inc/CF14JT1K00/1741314 | $0.32 |
| 1 | 45v NPN Transistor | https://www.digikey.ca/en/products/detail/onsemi/BC550CBU/975565 | $0.45 |
| 4 (1 Set) | Rubber Non-slip Feet | https://www.aliexpress.com/item/1005006957329213.html?spm=a2g0o.productlist.main.4.7ed225d4ohj3jz&aem_p4p_detail=202507021943012590468155837960001117326&algo_pvid=f81f5567-9a14-4309-aeaf-c89860f7dd07&algo_exp_id=f81f5567-9a14-4309-aeaf-c89860f7dd07-3&pdp_ext_f=%7B%22order%22%3A%224936%22%2C%22eval%22%3A%221%22%7D&pdp_npi=4%40dis%21CAD%212.36%212.29%21%21%2112.13%2111.77%21%402101c59117515105811047138ee51d%2112000039096298486%21sea%21CA%210%21ABX&curPageLogUid=p0n3ON4NCfNg&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202507021943012590468155837960001117326_1#nav-specification |  |
| 1 | Custom PCB | For me: https://cart.jlcpcb.com/shopcart/cart | $24.92 (Or $2.84 with cheaper option, but faster wear on pads) |
