# Guilty Pad XX Λ Core Plus R

This is a pretty simple TKL keyboard with backlighting, an OLED, and a rotary encoder. The fancy trick is that it's designed to work with the [GUILTY PAD -GAY-](https://github.com/askiiart/guilty-pad-gay), so you can do whatever you want with it via Bluetooth. Connect them together and use the hackpad as macro key combos or something, literally anything!

![A screenshot of the schematic](/readme-images/schematic.png)

![A screenshot of the PCB](/readme-images/pcb.png)

![A screenshot of the 3D rendering of the PCB with all components](/readme-images/pcb-3d-model.png)

---

The woke left made me add yuri (I actually haven't added any yet, busy doing actually useful stuff)

## Bill of Materials

| Name                                                                       | Link                                                                       | Unit price | Quantity needed | MOQ | Multiple | Total per item |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------- | --------------- | --- | -------- | -------------- |
| XIAO nrf52840                                                              | <https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html>          | 8.99       | 1               | 1   | 1        | 8.99           |
| 0402 4.7k resistors (GR0402J4K7TAG00)                                      | <https://www.lcsc.com/product-detail/C49656853.html>                       | 0          | 2               | 100 | 100      | 0.04           |
| Rotary encoder w/ switch (EC11E18244A5)                                    | <https://www.lcsc.com/product-detail/C255515.html>                         | 2.05       | 1               | 1   | 1        | 2.05           |
| 0402 806k resistor (SCR0402F806K)                                          | <https://www.lcsc.com/product-detail/C3016043.html>                        | 0          | 1               | 100 | 100      | 0.05           |
| 0402 2M resistor (GR0402J2MTAG00)                                          | <https://www.lcsc.com/product-detail/C49653113.html>                       | 0          | 1               | 100 | 100      | 0.04           |
| 0603 10uF capacitor (CL10A106MQ8NNNC)                                      | <https://www.lcsc.com/product-detail/C1691.html>                           | 0          | 1               | 50  | 50       | 0.24           |
| 60x Mill-Max hotswap sockets                                               | <https://keeb.io/products/mill-max-hotswap-sockets?variant=32377167511646> | 7.99       | 3               | 1   | 1        | 23.97          |
| 20x SK6803MINI-E (LEDs)                                                    | <https://www.aliexpress.us/item/3256807898532204.html>                     | 31.16      | 5               | 1   | 1        | 24.7           |
| 22 AWG wires w/ JST XH connectors                                          | <https://www.aliexpress.us/item/3256803495901819.html>                     | 0.99       | 1               | 1   | 1        | 0.99           |
| Complimentary P/N channel MOSFETs (G1NP02ELL)                              | <https://www.lcsc.com/product-detail/C840056.html>                         | 0.03       | 1               | 20  | 20       | 0.66           |
| 15 uH Inductor (SLW4030S150MST)                                            | <https://www.lcsc.com/product-detail/C206361.html>                         | 0.07       | 1               | 10  | 10       | 0.69           |
| 5V boost converter (H8118A40PR)                                            | <https://www.lcsc.com/product-detail/C410998.html>                         | 0.13       | 1               | 5   | 5        | 0.66           |
| Diodes (1N4001)                                                            | <https://www.lcsc.com/product-detail/C2909965.html>                        | 0          | 89              | 50  | 50       | 0.41           |
| Level shifter (74LV1T08GW-TP)                                              | <https://www.lcsc.com/product-detail/C42460230.html>                       | 0.06       | 1               | 10  | 10       | 0.57           |
| 90x MX switches (Holy Panda 55g)                                           | <https://www.aliexpress.us/item/3256805924985540.html>                     | 5.49       | 1               | 1   | 1        | 5.49           |
| IO expander (AW9523BTQR)                                                   | <https://www.lcsc.com/product-detail/C148077.html>                         | 0.35       | 1               | 1   | 1        | 0.35           |
| Keycaps                                                                    | <https://www.aliexpress.us/item/3256809006592332.html>                     | 0.99       | 1               | 1   | 1        | 0.99           |
| 5000mAh 307090 lipo                                                        | <https://www.aliexpress.us/item/3256809787664995.html>                     | $5.18      | 1               | 1   | 1        | 4.18           |
| M2 screws and heat-set inserts (10x M2x3 inserts, 6x M2x4 (5?), 4x M2xTBD) | <https://www.aliexpress.us/item/3256807644176828.html>                     | 0.99       | 1               | 1   | 0.99     | 0.99           |
| 0.91" 128x32 OLED                                                          | <https://www.aliexpress.us/item/3256804386173217.html>                     | 0.99       | 1               | 1   | 0.99     | 0.99           |
|                                                                            |                                                                            |            |                 |     |          |                |
| Component Total                                                            |                                                                            |            |                 |     |          | 78.05          |
|                                                                            |                                                                            |            |                 |     |          |                |
| PCB total                                                                  |                                                                            |            |                 |     |          | 29.74          |
| Seeed studio shipping                                                      |                                                                            |            |                 |     |          | 5.46           |
| keeb.io shipping                                                           |                                                                            |            |                 |     |          | 6.37           |
| SK6803MINI-E shipping                                                      |                                                                            |            |                 |     |          | 6.52           |
| 5000mAh lipo shipping                                                      |                                                                            |            |                 |     |          | 5.41           |
| LCSC shipping & handling                                                   |                                                                            |            |                 |     |          | 11.71          |
|                                                                            |                                                                            |            |                 |     |          |                |
| Subtotal                                                                   |                                                                            |            |                 |     |          | 143.25         |
| Without mill-max sockets                                                   |                                                                            |            |                 |     |          | 112.91         |
|                                                                            |                                                                            |            |                 |     |          |                |
| Total                                                                      |                                                                            |            |                 |     |          | 155.07         |
| **Without mill-max sockets**                                               |                                                                            |            |                 |     |          | 122.23         |
